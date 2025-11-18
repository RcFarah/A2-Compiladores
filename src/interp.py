"""
Implementa a Fase 4: Execução (Intérprete).
(Corrigido para imprimir '1' em vez de 'true')
"""

from src import ast_nodes as ast
import sys

# --- 1. Classe de Erro de Execução ---

class RuntimeErrorLang(Exception):
    """Exceção customizada para erros em tempo de execução."""
    pass

# --- 2. Classe de Ambiente (Memória) ---

class Environment:
    
    def __init__(self):
        self.scopes = [{}]
        self.current_scope_level = 0

    def enter_scope(self):
        self.scopes.append({})
        self.current_scope_level += 1

    def leave_scope(self):
        if self.current_scope_level > 0:
            self.scopes.pop()
            self.current_scope_level -= 1

    def declare(self, name, value):
        current_scope = self.scopes[-1]
        current_scope[name] = value

    def assign(self, name, value):
        for i in range(self.current_scope_level, -1, -1):
            scope = self.scopes[i]
            if name in scope:
                scope[name] = value
                return
        
        raise RuntimeErrorLang(f"Erro de Execução: Variável '{name}' não declarada.")

    def get(self, name):
        for i in range(self.current_scope_level, -1, -1):
            scope = self.scopes[i]
            if name in scope:
                return scope[name]
        
        raise RuntimeErrorLang(f"Erro de Execução: Variável '{name}' não declarada.")

# --- 3. O Intérprete (Visitor da AST) ---

class Interpreter:
    
    def __init__(self):
        self.env = Environment()

    def visit(self, node):
        if node is None:
            return
            
        method_name = f'visit_{node.__class__.__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)

    def generic_visit(self, node):
        if node is None or isinstance(node, ast.Empty):
            return
        raise NotImplementedError(f"Método 'visit_{node.__class__.__name__}' não implementado.")

    # --- Visitantes de Nós Contêineres ---

    def visit_Program(self, node: ast.Program):
        print("--- Executando Código ---")
        try:
            for stmt in node.statements:
                self.visit(stmt)
        except RuntimeErrorLang as e:
            print(f"\n!!!!!! ERRO DE EXECUÇÃO !!!!!!")
            print(e)
            sys.exit(1)
        print("--- Execução Concluída ---")


    def visit_Block(self, node: ast.Block):
        self.env.enter_scope()
        for stmt in node.statements:
            self.visit(stmt)
        self.env.leave_scope()

    # --- Visitantes de Statements ---

    def visit_Declaration(self, node: ast.Declaration):
        value = None
        if node.expression:
            value = self.visit(node.expression)
        
        self.env.declare(node.var_id, value)

    def visit_Assignment(self, node: ast.Assignment):
        value = self.visit(node.expression)
        
        if node.index_expr:
            array = self.env.get(node.var_name)
            index = self.visit(node.index_expr)
            
            if not isinstance(index, int) or index < 0 or index >= len(array):
                raise RuntimeErrorLang(f"Erro de Execução: Índice de array '{index}' fora dos limites para '{node.var_name}'.")
            
            array[index] = value
        else:
            self.env.assign(node.var_name, value)

    def visit_IfStatement(self, node: ast.IfStatement):
        condition = self.visit(node.condition)
        if condition:
            self.visit(node.if_block)
        elif node.else_block:
            self.visit(node.else_block)

    def visit_WhileStatement(self, node: ast.WhileStatement):
        while self.visit(node.condition):
            self.visit(node.block)

    def visit_DoWhileStatement(self, node: ast.DoWhileStatement):
        self.visit(node.block)
        while self.visit(node.condition):
            self.visit(node.block)

    def visit_ForStatement(self, node: ast.ForStatement):
        self.env.enter_scope()
        self.visit(node.initializer)
        
        while True:
            condition = True
            if not isinstance(node.condition, ast.Empty):
                condition = self.visit(node.condition)
            
            if not condition:
                break
                
            self.visit(node.block)
            self.visit(node.iterator)
            
        self.env.leave_scope()

    def visit_ForEachStatement(self, node: ast.ForEachStatement):
        iterable = self.env.get(node.iterable_id)
        
        for item in iterable:
            self.env.enter_scope()
            self.env.declare(node.var_id, item)
            self.visit(node.block)
            self.env.leave_scope()

    # (INÍCIO DA CORREÇÃO)
    def visit_PrintStatement(self, node: ast.PrintStatement):
        values = [self.visit(expr) for expr in node.expressions]
        
        output_values = []
        for v in values:
            # Checa o tipo *exato* de bool, senão '1' vira 'true'
            if isinstance(v, bool):
                output_values.append('true' if v else 'false')
            elif v is None:
                output_values.append('null')
            else:
                output_values.append(str(v))
            
        print(" ".join(output_values))
    # (FIM DA CORREÇÃO)

    # --- Visitantes de Expressões (Retornam o VALOR) ---

    def visit_BinaryOp(self, node: ast.BinaryOp):
        left = self.visit(node.left)
        
        if node.operator == '&&':
            if not left: return False
            return self.visit(node.right)
        
        if node.operator == '||':
            if left: return True
            return self.visit(node.right)

        right = self.visit(node.right)
        op = node.operator

        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/':
            if right == 0:
                raise RuntimeErrorLang("Erro de Execução: Divisão por zero.")
            return left / right
        if op == '%': return left % right
        
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right
        if op == '==': return left == right
        if op == '!=': return left != right
            
        raise RuntimeErrorLang(f"Operador binário desconhecido: {op}")

    def visit_UnaryOp(self, node: ast.UnaryOp):
        operand = self.visit(node.operand)
        op = node.operator

        if op == '!': return not operand
        if op == '-': return -operand
            
        raise RuntimeErrorLang(f"Operador unário desconhecido: {op}")

    # --- Visitantes de Fatores (Retornam o VALOR) ---

    def visit_Id(self, node: ast.Id):
        return self.env.get(node.name)
        
    def visit_ArrayAccess(self, node: ast.ArrayAccess):
        array = self.visit(node.array_id_node)
        index = self.visit(node.index_expr)
        
        if not isinstance(index, int) or index < 0 or index >= len(array):
            raise RuntimeErrorLang(f"Erro de Execução: Índice de array '{index}' fora dos limites.")
            
        return array[index]

    def visit_NewArray(self, node: ast.NewArray):
        size = self.visit(node.size_expr)
        if not isinstance(size, int) or size < 0:
            raise RuntimeErrorLang(f"Erro de Execução: Tamanho de array inválido '{size}'.")
        
        return [None] * size

    def visit_DotAccess(self, node: ast.DotAccess):
        raise RuntimeErrorLang("Erro de Execução: Acesso com '.' (DotAccess) não é suportado.")

    # --- Visitantes de Literais (Retornam o VALOR) ---
    
    def visit_IntLiteral(self, node: ast.IntLiteral):
        return node.value

    def visit_FloatLiteral(self, node: ast.FloatLiteral):
        return node.value
        
    def visit_StringLiteral(self, node: ast.StringLiteral):
        return node.value
        
    def visit_BoolLiteral(self, node: ast.BoolLiteral):

        return node.value
