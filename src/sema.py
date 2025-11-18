"""
Implementa a Fase 3: Análise Semântica.
(Corrigido para lidar corretamente com declarações de array)
"""

from src import ast_nodes as ast
import sys

# --- 1. Classe de Erro Semântico ---

class SemanticError(Exception):
    """Exceção customizada para erros semânticos."""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)

    def __str__(self):
        # Formata a mensagem de erro com localização, se disponível
        if self.line is not None and self.column is not None:
            return f"[Linha {self.line}:{self.column}] Erro Semântico: {self.message}"
        return f"Erro Semântico: {self.message}"

# --- 2. Classes de Símbolo e Tabela ---

class Symbol:
    """Armazena informações sobre um identificador (variável)."""
    def __init__(self, name, var_type, is_const=False, is_array=False):
        self.name = name
        self.type = var_type
        self.is_const = is_const
        self.is_array = is_array
        self.is_initialized = False

    def __repr__(self):
        props = [self.type]
        if self.is_const: props.append("const")
        if self.is_array: props.append("array")
        if self.is_initialized: props.append("init")
        return f"<{self.name}: {', '.join(props)}>"

class SymbolTable:
    """Gerencia uma pilha de escopos."""
    
    def __init__(self):
        self.scopes = [{}]
        self.current_scope_level = 0
        self.debug_output = []

    def enter_scope(self):
        """Entra em um novo escopo (ex: ao entrar em um 'block')."""
        self.scopes.append({})
        self.current_scope_level += 1
        self.debug_output.append(f"-> Enter Scope (Lvl {self.current_scope_level})")

    def leave_scope(self):
        """Sai do escopo atual."""
        if self.current_scope_level > 0:
            self.scopes.pop()
            self.current_scope_level -= 1
            self.debug_output.append(f"<- Leave Scope (Lvl {self.current_scope_level})")
        else:
            raise SemanticError("Erro Interno: Tentando sair do escopo global.")

    def declare(self, symbol, node: ast.Node):
        """Declara um novo símbolo no escopo ATUAL."""
        current_scope = self.scopes[-1]
        if symbol.name in current_scope:
            # Erro: Variável já declarada neste escopo
            raise SemanticError(f"Variável '{symbol.name}' já declarada neste escopo.",
                                line=node.line, column=node.column)
        
        current_scope[symbol.name] = symbol
        self.debug_output.append(f"   Declare: {symbol} (Lvl {self.current_scope_level})")

    def lookup(self, name, node: ast.Node):
        """Procura por um símbolo do escopo atual para fora."""
        for i in range(self.current_scope_level, -1, -1):
            scope = self.scopes[i]
            if name in scope:
                return scope[name]
        
        # Não encontrou
        raise SemanticError(f"Variável '{name}' não declarada.",
                            line=node.line, column=node.column)

    def set_initialized(self, name, node: ast.Node):
        """Marca uma variável como inicializada."""
        symbol = self.lookup(name, node) # 'lookup' fará a checagem de existência
        symbol.is_initialized = True
        self.debug_output.append(f"   Initialize: {symbol.name}")

    def get_debug_output(self):
        """Retorna o log de escopos para impressão."""
        return "\n".join(self.debug_output)

# --- 3. O Analisador Semântico (Visitor da AST) ---

class SemanticAnalyzer:
    """
    Visitor que caminha pela AST (criada pelo AstBuilderVisitor)
    e realiza a análise semântica.
    """
    
    def __init__(self):
        self.symtab = SymbolTable()

    def visit(self, node):
        method_name = f'visit_{node.__class__.__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)

    def generic_visit(self, node):
        if node is None or isinstance(node, ast.Empty):
            return
        raise NotImplementedError(f"Método 'visit_{node.__class__.__name__}' não implementado.")

    # --- Visitantes de Nós Contêineres ---

    def visit_Program(self, node: ast.Program):
        self.symtab.debug_output = ["--- Tabela de Símbolos (Log) ---"]
        for stmt in node.statements:
            self.visit(stmt)
        self.symtab.debug_output.append("--- Fim da Análise ---")

    def visit_Block(self, node: ast.Block):
        self.symtab.enter_scope()
        for stmt in node.statements:
            self.visit(stmt)
        self.symtab.leave_scope()

    # --- Visitantes de Statements ---

    def visit_Declaration(self, node: ast.Declaration):
        # (INÍCIO DA CORREÇÃO)
        # 1. Cria o símbolo primeiro, com seu tipo declarado
        symbol = Symbol(node.var_id, node.var_type, node.is_const, node.is_array)
        
        # 2. Checa a expressão de inicialização (se existir)
        if node.expression:
            init_type = self.visit(node.expression) # ex: "int[]" ou "int"
            
            # Constrói o tipo completo declarado (ex: "int[]")
            full_declared_type = symbol.type
            if symbol.is_array:
                full_declared_type += "[]"
                
            # Compara o tipo da expressão com o tipo declarado
            if init_type != full_declared_type:
                # Checa se os tipos base são diferentes (ex: int[] = new bool[10])
                init_base_type = init_type.replace("[]", "")
                if symbol.type != init_base_type:
                     raise SemanticError(f"Não pode atribuir tipo '{init_type}' à variável '{symbol.name}' do tipo '{full_declared_type}'.",
                                        line=node.expression.line, column=node.expression.column)

                # Checa se a "array-zicidade" bate (ex: int[] a = 10)
                is_init_array = init_type.endswith("[]")
                if symbol.is_array != is_init_array:
                     raise SemanticError(f"Incompatibilidade de array: Não pode atribuir '{init_type}' para '{full_declared_type}'.",
                                        line=node.expression.line, column=node.expression.column)

        # 3. Declara o símbolo na tabela
        self.symtab.declare(symbol, node=node)
        
        # 4. Marca como inicializado se tiver expressão
        if node.expression:
            symbol.is_initialized = True
        # (FIM DA CORREÇÃO)

    def visit_Assignment(self, node: ast.Assignment):
        # 1. Verifica se a variável existe
        symbol = self.symtab.lookup(node.var_name, node=node)
        
        # 2. Verifica se é 'const'
        if symbol.is_const:
            raise SemanticError(f"Não pode atribuir a variável constante '{node.var_name}'.",
                                line=node.line, column=node.column)

        # 3. Visita a expressão da direita para saber seu tipo
        expr_type = self.visit(node.expression)

        # 4. Checagem de tipos
        if node.index_expr:
            # A. É uma atribuição de array (ex: a[i] = 10)
            if not symbol.is_array:
                raise SemanticError(f"Variável '{node.var_name}' não é um array e não pode ser indexada.",
                                    line=node.line, column=node.column)
            
            index_type = self.visit(node.index_expr)
            if index_type != 'int':
                raise SemanticError(f"Índice de array para '{node.var_name}' deve ser 'int', mas foi '{index_type}'.",
                                    line=node.index_expr.line, column=node.index_expr.column)
                
            if symbol.type != expr_type:
                raise SemanticError(f"Não pode atribuir tipo '{expr_type}' a um elemento do array '{node.var_name}' do tipo '{symbol.type}'.",
                                    line=node.expression.line, column=node.expression.column)
        
        else:
            # B. É uma atribuição normal (ex: a = 10)
            if symbol.is_array:
                 raise SemanticError(f"Não pode atribuir um valor a um array inteiro '{node.var_name}'.",
                                     line=node.line, column=node.column)
            
            if symbol.type != expr_type:
                raise SemanticError(f"Não pode atribuir tipo '{expr_type}' à variável '{node.var_name}' do tipo '{symbol.type}'.",
                                    line=node.expression.line, column=node.expression.column)

        # 5. Marca como inicializada
        self.symtab.set_initialized(symbol.name, node=node)

    def visit_IfStatement(self, node: ast.IfStatement):
        cond_type = self.visit(node.condition)
        if cond_type != 'bool':
            raise SemanticError(f"Condição do 'if' deve ser 'bool', mas foi '{cond_type}'.",
                                line=node.condition.line, column=node.condition.column)
        
        self.visit(node.if_block)
        
        if node.else_block:
            self.visit(node.else_block)

    def visit_WhileStatement(self, node: ast.WhileStatement):
        cond_type = self.visit(node.condition)
        if cond_type != 'bool':
            raise SemanticError(f"Condição do 'while' deve ser 'bool', mas foi '{cond_type}'.",
                                line=node.condition.line, column=node.condition.column)
        self.visit(node.block)

    def visit_DoWhileStatement(self, node: ast.DoWhileStatement):
        self.visit(node.block)
        cond_type = self.visit(node.condition)
        if cond_type != 'bool':
            raise SemanticError(f"Condição do 'do-while' deve ser 'bool', mas foi '{cond_type}'.",
                                line=node.condition.line, column=node.condition.column)

    def visit_ForStatement(self, node: ast.ForStatement):
        self.symtab.enter_scope()
        self.visit(node.initializer)
        
        if not isinstance(node.condition, ast.Empty):
            cond_type = self.visit(node.condition)
            if cond_type != 'bool':
                raise SemanticError(f"Condição do 'for' deve ser 'bool', mas foi '{cond_type}'.",
                                    line=node.condition.line, column=node.condition.column)
        
        self.visit(node.iterator)
        self.visit(node.block)
        self.symtab.leave_scope()

    def visit_ForEachStatement(self, node: ast.ForEachStatement):
        iterable_sym = self.symtab.lookup(node.iterable_id, node=node)
        if not iterable_sym.is_array:
            raise SemanticError(f"'{node.iterable_id}' não é um array (usado em 'for each').",
                                line=node.line, column=node.column)
            
        if node.var_type != iterable_sym.type:
             raise SemanticError(f"Tipo da variável '{node.var_type} {node.var_id}' não bate com o tipo do array '{iterable_sym.type}[]'.",
                                 line=node.line, column=node.column)
             
        self.symtab.enter_scope()
        
        item_sym = Symbol(node.var_id, node.var_type, is_const=True, is_array=False)
        self.symtab.declare(item_sym, node=node) # Usa a linha do 'for each'
        item_sym.is_initialized = True
        
        self.visit(node.block)
        self.symtab.leave_scope()

    def visit_PrintStatement(self, node: ast.PrintStatement):
        for expr in node.expressions:
            self.visit(expr)

    # --- Visitantes de Expressões (Retornam o tipo) ---

    def visit_BinaryOp(self, node: ast.BinaryOp):
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        op = node.operator

        if op in ('&&', '||'):
            if left_type != 'bool' or right_type != 'bool':
                raise SemanticError(f"Operador '{op}' exige operandos 'bool', mas recebeu '{left_type}' e '{right_type}'.",
                                    line=node.line, column=node.column)
            return 'bool'
            
        if op in ('>', '<', '>=', '<=', '==', '!='):
            if left_type != right_type:
                 raise SemanticError(f"Operador '{op}' não pode comparar tipos diferentes '{left_type}' e '{right_type}'.",
                                     line=node.line, column=node.column)
            return 'bool'

        if op in ('+', '-', '*', '/', '%'):
            if (left_type not in ('int', 'float')) or (right_type not in ('int', 'float')):
                 raise SemanticError(f"Operador '{op}' exige operandos numéricos ('int' ou 'float'), mas recebeu '{left_type}' e '{right_type}'.",
                                     line=node.line, column=node.column)
            
            if left_type == 'float' or right_type == 'float':
                return 'float'
            return 'int'
            
        raise SemanticError(f"Operador binário desconhecido: {op}", line=node.line, column=node.column)

    def visit_UnaryOp(self, node: ast.UnaryOp):
        op_type = self.visit(node.operand)
        op = node.operator

        if op == '!':
            if op_type != 'bool':
                raise SemanticError(f"Operador '!' exige operando 'bool', mas recebeu '{op_type}'.",
                                    line=node.line, column=node.column)
            return 'bool'
            
        if op == '-':
            if op_type not in ('int', 'float'):
                raise SemanticError(f"Operador '-' (negação) exige operando numérico, mas recebeu '{op_type}'.",
                                    line=node.line, column=node.column)
            return op_type
            
        raise SemanticError(f"Operador unário desconhecido: {op}", line=node.line, column=node.column)

    # --- Visitantes de Fatores (Retornam o tipo) ---

    def visit_Id(self, node: ast.Id):
        symbol = self.symtab.lookup(node.name, node=node)
        if not symbol.is_initialized:
             raise SemanticError(f"Variável '{node.name}' usada antes de ser inicializada.",
                                 line=node.line, column=node.column)
        return symbol.type
        
    def visit_ArrayAccess(self, node: ast.ArrayAccess):
        array_type = self.visit(node.array_id_node)
        symbol = self.symtab.lookup(node.array_id_node.name, node=node.array_id_node)
        
        if not symbol.is_array:
             raise SemanticError(f"Tentando indexar '{symbol.name}', que não é um array.",
                                 line=node.line, column=node.column)
             
        index_type = self.visit(node.index_expr)
        if index_type != 'int':
            raise SemanticError(f"Índice de array para '{symbol.name}' deve ser 'int', mas foi '{index_type}'.",
                                line=node.index_expr.line, column=node.index_expr.column)
            
        return symbol.type

    def visit_NewArray(self, node: ast.NewArray):
        size_type = self.visit(node.size_expr)
        if size_type != 'int':
            raise SemanticError(f"Tamanho do 'new {node.array_type}[]' deve ser 'int', mas foi '{size_type}'.",
                                line=node.size_expr.line, column=node.size_expr.column)
        
        return f"{node.array_type}[]" # Retorna o tipo do array

    def visit_DotAccess(self, node: ast.DotAccess):
        raise SemanticError("Acesso com '.' (DotAccess) não é suportado.",
                            line=node.line, column=node.column)

    # --- Visitantes de Literais (Retornam o tipo) ---
    
    def visit_IntLiteral(self, node: ast.IntLiteral):
        return 'int'

    def visit_FloatLiteral(self, node: ast.FloatLiteral):
        return 'float'
        
    def visit_StringLiteral(self, node: ast.StringLiteral):
        return 'string'
        
    def visit_BoolLiteral(self, node: ast.BoolLiteral):

        return 'bool'
