# src/ast_nodes.py

"""
Define todas as classes de nós para a Árvore Sintática Abstrata (AST).
Cada classe agora armazena 'line' e 'column' para relatórios de erro detalhados.
"""

class Node:
    """Classe base para todos os nós da AST."""
    def __init__(self, line=None, column=None):
        self.line = line
        self.column = column

    def __repr__(self):
        """Um __repr__ genérico que ignora line/column para clareza."""
        attrs = {k: v for k, v in self.__dict__.items() if k not in ('line', 'column')}
        return f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in attrs.items())})"

# --- Nós Contêineres ---

class Program(Node):
    """Nó raiz da AST. Contém uma lista de statements."""
    def __init__(self, statements, line=None, column=None):
        super().__init__(line, column)
        self.statements = statements

class Block(Node):
    """Representa um bloco de código, ex: { ... }."""
    def __init__(self, statements, line=None, column=None):
        super().__init__(line, column)
        self.statements = statements

class Empty(Node):
    """Representa um nó vazio, útil para partes opcionais (ex: 'for')."""
    def __init__(self, line=None, column=None):
        super().__init__(line, column)

# --- Nós de Statements ---

class Declaration(Node):
    """Declaração de variável (ex: const int[] a = 1;)."""
    def __init__(self, is_const, var_type, is_array, var_id, expression, line=None, column=None):
        super().__init__(line, column)
        self.is_const = is_const
        self.var_type = var_type
        self.is_array = is_array
        self.var_id = var_id
        self.expression = expression  # Pode ser None

class Assignment(Node):
    """Atribuição (ex: a = 1; ou a[0] = 1;)."""
    def __init__(self, var_name, index_expr, expression, line=None, column=None):
        super().__init__(line, column)
        self.var_name = var_name
        self.index_expr = index_expr  # Nó de expressão (se for array) ou None
        self.expression = expression

class IfStatement(Node):
    """Statement 'if' (ex: if (cond) ... else ...)."""
    def __init__(self, condition, if_block, else_block, line=None, column=None):
        super().__init__(line, column)
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block  # Pode ser None ou outro IfStatement

class WhileStatement(Node):
    """Statement 'while'."""
    def __init__(self, condition, block, line=None, column=None):
        super().__init__(line, column)
        self.condition = condition
        self.block = block

class DoWhileStatement(Node):
    """Statement 'do-while'."""
    def __init__(self, block, condition, line=None, column=None):
        super().__init__(line, column)
        self.block = block
        self.condition = condition

class ForStatement(Node):
    """'for' clássico (ex: for (int i = 0; i < 10; i = i + 1) ...)."""
    def __init__(self, initializer, condition, iterator, block, line=None, column=None):
        super().__init__(line, column)
        self.initializer = initializer # Pode ser Declaration, Assignment ou Empty
        self.condition = condition   # Pode ser Expression ou Empty
        self.iterator = iterator     # Pode ser Expression ou Empty
        self.block = block

class ForEachStatement(Node):
    """'for each' (ex: for each (int item : array) ...)."""
    def __init__(self, var_type, var_id, iterable_id, block, line=None, column=None):
        super().__init__(line, column)
        self.var_type = var_type
        self.var_id = var_id
        self.iterable_id = iterable_id
        self.block = block

class PrintStatement(Node):
    """Statement 'print' (ex: print(a, b);)."""
    def __init__(self, expressions, line=None, column=None):
        super().__init__(line, column)
        self.expressions = expressions  # Lista de nós de expressão

# --- Nós de Expressão ---

class BinaryOp(Node):
    """Operação binária (ex: a + b, a && b)."""
    def __init__(self, left, operator, right, line=None, column=None):
        super().__init__(line, column)
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOp(Node):
    """Operação unária (ex: !a, -a)."""
    def __init__(self, operator, operand, line=None, column=None):
        super().__init__(line, column)
        self.operator = operator
        self.operand = operand

# --- Nós Atômicos (Fatores) ---

class Id(Node):
    """Identificador (variável)."""
    def __init__(self, name, line=None, column=None):
        super().__init__(line, column)
        self.name = name

class DotAccess(Node):
    """Acesso a propriedade (ex: obj.prop)."""
    def __init__(self, left_id, right_id, line=None, column=None):
        super().__init__(line, column)
        self.left_id = left_id
        self.right_id = right_id

class ArrayAccess(Node):
    """Acesso a índice de array (ex: arr[i])."""
    def __init__(self, array_id_node, index_expr, line=None, column=None):
        super().__init__(line, column)
        self.array_id_node = array_id_node
        self.index_expr = index_expr

class NewArray(Node):
    """Criação de array (ex: new int[10])."""
    def __init__(self, array_type, size_expr, line=None, column=None):
        super().__init__(line, column)
        self.array_type = array_type
        self.size_expr = size_expr

# --- Nós Literais ---

class IntLiteral(Node):
    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value

class FloatLiteral(Node):
    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value

class StringLiteral(Node):
    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value

class BoolLiteral(Node):
    def __init__(self, value, line=None, column=None):
        super().__init__(line, column)
        self.value = value