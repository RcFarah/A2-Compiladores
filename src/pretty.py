"""
Implementa o Pretty Printer para a AST.
...
"""

from src import ast_nodes as ast

# Caracteres para desenhar a árvore
PREFIX_BRANCH = "├── "
PREFIX_LAST_BRANCH = "└── "
PREFIX_CHILD_INDENT = "│   " # Indentação para filhos (se não for o último)
PREFIX_EMPTY_INDENT = "    " # Indentação para filhos (se for o último)

class AstPrettyPrinter:

    def __init__(self):
        self.output = []

    def _visit(self, node, node_prefix="", child_indent=""):
        """
        Visita um nó e o imprime, depois visita recursivamente os filhos.
        :param node: O nó atual da AST.
        :param node_prefix: O prefixo da linha ATUAL (ex: "├── ").
        :param child_indent: O prefixo de indentação para os FILHOS (ex: "│   ").
        """
        
        # 1. Pega a representação em string do nó atual
        method_name = f'visit_{node.__class__.__name__}'
        visitor_method = getattr(self, method_name, self._generic_visit)
        node_repr = visitor_method(node) # Não precisa mais do prefixo
        
        # 2. Imprime o nó atual com seu prefixo de linha
        if node_repr:
            self.output.append(f"{node_prefix}{node_repr}")
            
        # 3. Prepara para visitar os filhos
        children = self._get_children(node)
        
        # 4. Itera sobre os filhos e imprime-os recursivamente
        for i, child in enumerate(children):
            is_last = (i == len(children) - 1)
            
            if is_last:
                # O prefixo da linha do filho é "└── "
                next_node_prefix = child_indent + PREFIX_LAST_BRANCH
                # A indentação para os netos é "    "
                next_child_indent = child_indent + PREFIX_EMPTY_INDENT
            else:
                # O prefixo da linha do filho é "├── "
                next_node_prefix = child_indent + PREFIX_BRANCH
                # A indentação para os netos é "│   "
                next_child_indent = child_indent + PREFIX_CHILD_INDENT
            
            # 5. Chama recursivamente para o filho
            if isinstance(child, ast.Node):
                self._visit(child, next_node_prefix, next_child_indent)
            elif child is not None:
                # Para valores literais que não são nós (ex: 'var_id')
                self.output.append(f"{next_node_prefix}{repr(child)}")

    def _get_children(self, node):
        """(CORRIGIDO) Retorna os filhos de um nó que também são Nós da AST."""
        children = []
        if isinstance(node, (ast.Program, ast.Block)):
            children.extend(node.statements)
        elif isinstance(node, ast.Declaration):
            if node.expression:
                children.append(node.expression)
        elif isinstance(node, ast.Assignment):
            if node.index_expr: # Filho 1: índice do array
                children.append(node.index_expr)
            if node.expression: # Filho 2: valor
                children.append(node.expression)
        elif isinstance(node, ast.IfStatement):
            children.append(node.condition)
            children.append(node.if_block)
            if node.else_block:
                children.append(node.else_block)
        elif isinstance(node, (ast.WhileStatement, ast.DoWhileStatement)):
            children.append(node.condition)
            children.append(node.block)
        elif isinstance(node, ast.ForStatement):
            children.append(node.initializer)
            children.append(node.condition)
            children.append(node.iterator)
            children.append(node.block)
        elif isinstance(node, ast.ForEachStatement):
            children.append(node.block) # Outros são valores
        elif isinstance(node, ast.PrintStatement):
            children.extend(node.expressions)
        elif isinstance(node, (ast.BinaryOp, ast.DotAccess)):
            children.append(node.left)
            children.append(node.right)
        elif isinstance(node, ast.UnaryOp):
            children.append(node.operand)
        elif isinstance(node, ast.ArrayAccess):
            children.append(node.array_id_node)
            children.append(node.index_expr)
        elif isinstance(node, ast.NewArray):
            children.append(node.size_expr)
        # Literais (Int, Float, etc.) e Id/Empty não têm filhos
        
        return children

    def _generic_visit(self, node):
        """Visitante genérico para nós que não têm um método 'visit_' customizado."""
        return f"{node.__class__.__name__}"

    # --- Visitantes Customizados (para impressão mais bonita) ---
    
    def visit_Declaration(self, node):
        const = "const " if node.is_const else ""
        array = "[]" if node.is_array else ""
        return f"Declaration(id='{node.var_id}', type='{const}{node.var_type}{array}')"

    def visit_Assignment(self, node):
        # Os filhos (index_expr? e expression) serão impressos automaticamente
        return f"Assignment(target='{node.var_name}')"
            
    def visit_IfStatement(self, node):
        return "If" # Filhos: condition, if_block, else_block?

    def visit_WhileStatement(self, node):
        return "While" # Filhos: condition, block

    def visit_DoWhileStatement(self, node):
        return "DoWhile" # Filhos: block, condition
        
    def visit_ForStatement(self, node):
        return "For" # Filhos: init, cond, iter, block
        
    def visit_ForEachStatement(self, node):
        return f"ForEach(var='{node.var_type} {node.var_id}', iterable='{node.iterable_id}')"
        
    def visit_BinaryOp(self, node):
        return f"BinaryOp(op='{node.operator}')"
        
    def visit_UnaryOp(self, node):
        return f"UnaryOp(op='{node.operator}')"
    
    def visit_Id(self, node):
        return f"Id(name='{node.name}')"

    def visit_DotAccess(self, node):
        return "DotAccess" # Filhos: left, right

    def visit_ArrayAccess(self, node):
        return "ArrayAccess" # Filhos: array_id_node, index_expr
        
    def visit_NewArray(self, node):
        return f"NewArray(type='{node.array_type}')" # Filhos: size_expr

    def visit_IntLiteral(self, node):
        return f"IntLiteral(value={node.value})"
        
    def visit_FloatLiteral(self, node):
        return f"FloatLiteral(value={node.value})"
        
    def visit_StringLiteral(self, node):
        return f"StringLiteral(value='{node.value}')"
        
    def visit_BoolLiteral(self, node):
        return f"BoolLiteral(value={node.value})"

    # --- Métodos Públicos ---

    def print_tree(self, node):
        """Limpa a saída e começa a impressão a partir do nó raiz."""
        self.output = []
        self._visit(node, node_prefix="", child_indent="") # Inicia a recursão
        return "\n".join(self.output)

def print_ast_ascii(ast_root_node):
    """Função pública para criar e usar o printer."""
    printer = AstPrettyPrinter()

    print(printer.print_tree(ast_root_node))
