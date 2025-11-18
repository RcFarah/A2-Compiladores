# src/ast_builder.py

"""
Implementa o Visitor que constrói a AST.
Herda de MiniLangVisitor (gerado pelo ANTLR).

Cada nó da AST criado armazena
informações de linha e coluna para relatórios de erro.
"""

from src.generated.MiniLangParser import MiniLangParser
from src.generated.MiniLangVisitor import MiniLangVisitor
from src import ast_nodes as ast

class AstBuilderVisitor(MiniLangVisitor):

    # --- Visitantes de Regras Principais ---

    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        """program: statement* EOF;"""
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return ast.Program(statements, line=ctx.start.line, column=ctx.start.column)

    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        """block: LBRACE statement* RBRACE;"""
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return ast.Block(statements, line=ctx.start.line, column=ctx.start.column)

    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        """statement: (block | declaration | ... | expression SEMIC);"""
        child = ctx.getChild(0)
        if child:
            return self.visit(child)
        # Retorna um nó vazio se houver erro de sintaxe
        return ast.Empty(line=ctx.start.line, column=ctx.start.column) 

    # --- Visitantes de Statements ---

    def visitIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        """if_stmt: IF LPAREN expression RPAREN statement (ELSE statement)?;"""
        condition = self.visit(ctx.expression())
        if_block = self.visit(ctx.statement(0))
        
        else_block = None
        if ctx.ELSE():
            else_block = self.visit(ctx.statement(1))
            
        token = ctx.IF().symbol # Pega o token 'if'
        return ast.IfStatement(condition, if_block, else_block, line=token.line, column=token.column)

    def visitWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        """while_stmt: WHILE LPAREN expression RPAREN statement;"""
        condition = self.visit(ctx.expression())
        block = self.visit(ctx.statement())
        token = ctx.WHILE().symbol
        return ast.WhileStatement(condition, block, line=token.line, column=token.column)

    def visitDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        """do_while_stmt: DO statement WHILE LPAREN expression RPAREN SEMIC;"""
        block = self.visit(ctx.statement())
        condition = self.visit(ctx.expression())
        token = ctx.DO().symbol
        return ast.DoWhileStatement(block, condition, line=token.line, column=token.column)

    def visitFor_stmt(self, ctx:MiniLangParser.For_stmtContext):
        """for_stmt: FOR LPAREN for_initializer? SEMIC expression? SEMIC for_iterator? RPAREN statement;"""
        initializer = self.visit(ctx.for_initializer()) if ctx.for_initializer() else ast.Empty()
        # O 'for' (clássico) só tem uma 'expression'
        condition = self.visit(ctx.expression()) if ctx.expression() else ast.Empty()
        iterator = self.visit(ctx.for_iterator()) if ctx.for_iterator() else ast.Empty()
        block = self.visit(ctx.statement())
        
        token = ctx.FOR().symbol
        return ast.ForStatement(initializer, condition, iterator, block, line=token.line, column=token.column)

    def visitFor_each_stmt(self, ctx:MiniLangParser.For_each_stmtContext):
        """for_each_stmt: FOR EACH LPAREN type ID COLON ID RPAREN statement;"""
        var_type = ctx.type_().getText()
        var_id = ctx.ID(0).getText()
        iterable_id = ctx.ID(1).getText()
        block = self.visit(ctx.statement())
        
        token = ctx.FOR().symbol
        return ast.ForEachStatement(var_type, var_id, iterable_id, block, line=token.line, column=token.column)

    def visitFor_initializer(self, ctx:MiniLangParser.For_initializerContext):
        """for_initializer: (declaration | expression_list);"""
        return self.visit(ctx.getChild(0))

    def visitFor_iterator(self, ctx:MiniLangParser.For_iteratorContext):
        """for_iterator: expression_list;"""
        return self.visit(ctx.expression_list())

    def visitPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        """print_stmt: PRINT LPAREN expression_list? RPAREN SEMIC;"""
        expressions = []
        if ctx.expression_list():
            expressions = self.visit(ctx.expression_list())
        
        token = ctx.PRINT().symbol
        return ast.PrintStatement(expressions, line=token.line, column=token.column)

    def visitExpression_list(self, ctx:MiniLangParser.Expression_listContext):
        """expression_list: expression (COMMA expression)*;"""
        return [self.visit(expr) for expr in ctx.expression()]

    def visitDeclaration(self, ctx:MiniLangParser.DeclarationContext):
        """declaration: CONST? type (LBRACK RBRACK)? ID (ASSIGN expression)? SEMIC;"""
        is_const = ctx.CONST() is not None
        var_type = ctx.type_().getText()
        is_array = ctx.LBRACK() is not None
        var_id_token = ctx.ID().symbol # Pega o token do ID
        var_id = var_id_token.text
        
        expression = None
        if ctx.expression():
            # 'declaration' só tem uma 'expression'
            expression = self.visit(ctx.expression())
            
        return ast.Declaration(is_const, var_type, is_array, var_id, expression, 
                               line=var_id_token.line, column=var_id_token.column)

    def visitType(self, ctx:MiniLangParser.TypeContext):
        """type: INT | FLOAT | STRING | BOOL;"""
        return ctx.getText()

    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        """assignment: ID (LBRACK expression RBRACK)? ASSIGN expression SEMIC;"""
        var_id_token = ctx.ID().symbol
        var_name = var_id_token.text
        index_expr = None
        value_expr = None
        
        if ctx.LBRACK():
            # 'assignment' com array tem 2 'expression',
            # Elas estão em ordem. expression(0) é o índice, expression(1) é o valor.
            index_expr = self.visit(ctx.expression(0))
            value_expr = self.visit(ctx.expression(1))
        else:
            # 'assignment' normal só tem uma 'expression'
            value_expr = self.visit(ctx.expression(0))
            
        return ast.Assignment(var_name, index_expr, value_expr,
                              line=var_id_token.line, column=var_id_token.column)

    # --- Visitantes de Expressão (Precedência) ---

    def _visit_binary_op(self, ctx, operator_texts):
        """Função auxiliar para operações binárias."""
        left = self.visit(ctx.getChild(0))
        
        if ctx.getChildCount() == 1:
            return left
        
        op_index = 1
        child_index = 2
        while child_index < ctx.getChildCount():
            operator = ctx.getChild(op_index).getText()
            
            if operator in operator_texts:
                right = self.visit(ctx.getChild(child_index))
                
                op_token = ctx.getChild(op_index).symbol
                left = ast.BinaryOp(left, operator, right, 
                                    line=op_token.line, column=op_token.column)
            
            op_index += 2
            child_index += 2
            
        return left

    def visitExpression(self, ctx:MiniLangParser.ExpressionContext):
        """expression: logical_or;"""
        return self.visit(ctx.logical_or())

    def visitLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        """logical_or: logical_and (OR logical_and)*;"""
        return self._visit_binary_op(ctx, ['||'])

    def visitLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        """logical_and: equality (AND equality)*;"""
        return self._visit_binary_op(ctx, ['&&'])

    def visitEquality(self, ctx:MiniLangParser.EqualityContext):
        """equality: comparison ((EQ | NEQ) comparison)*;"""
        return self._visit_binary_op(ctx, ['==', '!='])

    def visitComparison(self, ctx:MiniLangParser.ComparisonContext):
        """comparison: arithmetic ((LT | LTE | GT | GTE) arithmetic)*;"""
        return self._visit_binary_op(ctx, ['<', '<=', '>', '>='])

    def visitArithmetic(self, ctx:MiniLangParser.ArithmeticContext):
        """arithmetic: term ((PLUS | MINUS) term)*;"""
        return self._visit_binary_op(ctx, ['+', '-'])

    def visitTerm(self, ctx:MiniLangParser.TermContext):
        """term: unary ((MULT | DIV | MOD) unary)*;"""
        return self._visit_binary_op(ctx, ['*', '/', '%'])

    def visitUnary(self, ctx:MiniLangParser.UnaryContext):
        """unary: (NOT | MINUS) unary | factor;"""
        if ctx.factor():
            return self.visit(ctx.factor())
        
        op_token = ctx.getChild(0).symbol
        operator = op_token.text
        operand = self.visit(ctx.unary())
        return ast.UnaryOp(operator, operand, line=op_token.line, column=op_token.column)

    # --- Visitantes de Fatores (Átomos) ---

    def visitFactor(self, ctx:MiniLangParser.FactorContext):
        """
        factor: LPAREN expression RPAREN
              | NEW type LBRACK expression RBRACK
              | ID (DOT ID)?
              | ID LBRACK expression RBRACK
              | literal;
        """
        if ctx.LPAREN():
            # ( expression )
            return self.visit(ctx.expression())
        
        if ctx.NEW():
            # new type [ expression ]
            array_type = ctx.type_().getText()
            # O 'new' só tem uma 'expression'
            size_expr = self.visit(ctx.expression())
            token = ctx.NEW().symbol
            return ast.NewArray(array_type, size_expr, line=token.line, column=token.column)
            
        if ctx.literal():
            return self.visit(ctx.literal())
            
        if ctx.ID():
            id_token = ctx.ID(0).symbol
            if ctx.LBRACK():
                # Array Access: ID [ expression ]
                array_id_node = ast.Id(id_token.text, line=id_token.line, column=id_token.column)
                # O 'array access' só tem uma 'expression'
                index_expr = self.visit(ctx.expression())
                return ast.ArrayAccess(array_id_node, index_expr, line=id_token.line, column=id_token.column)
                
            if ctx.DOT():
                # Dot Access: ID . ID
                left_id_node = ast.Id(id_token.text, line=id_token.line, column=id_token.column)
                right_id_str = ctx.ID(1).getText()
                dot_token = ctx.DOT().symbol
                return ast.DotAccess(left_id_node, right_id_str, line=dot_token.line, column=dot_token.column)
                
            # Apenas ID
            return ast.Id(id_token.text, line=id_token.line, column=id_token.column)

    def visitLiteral(self, ctx:MiniLangParser.LiteralContext):
        """
        literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE;
        """
        if ctx.INT_LIT():
            token = ctx.INT_LIT().symbol
            return ast.IntLiteral(int(token.text), line=token.line, column=token.column)
            
        if ctx.FLOAT_LIT():
            token = ctx.FLOAT_LIT().symbol
            return ast.FloatLiteral(float(token.text), line=token.line, column=token.column)
            
        if ctx.STRING_LIT():
            token = ctx.STRING_LIT().symbol
            raw_string = token.text
            return ast.StringLiteral(raw_string[1:-1], line=token.line, column=token.column)
            
        if ctx.TRUE():
            token = ctx.TRUE().symbol
            return ast.BoolLiteral(True, line=token.line, column=token.column)
            
        if ctx.FALSE():
            token = ctx.FALSE().symbol

            return ast.BoolLiteral(False, line=token.line, column=token.column)
