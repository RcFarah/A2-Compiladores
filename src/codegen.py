"""
Implementa a Fase 5: Geração de Código (Codegen).
(Corrigido) Agora inclui uma Tabela de Símbolos interna para
renomear (mangle) variáveis e simular o escopo de bloco.
"""

from src import ast_nodes as ast
import sys

# --- Tabela de Símbolos para o CodeGen ---

class CodeGenSymbolTable:
    """Gerencia o renomeamento (mangling) de nomes de variáveis."""
    
    def __init__(self):
        # Pilha de escopos. Cada escopo é um dict { "var_minilang": "var_python" }
        self.scopes = [{}]
        self.scope_level_counter = 0 # Contador para nomes únicos

    def enter_scope(self):
        """Entra em um novo escopo."""
        self.scopes.append({})
        self.scope_level_counter += 1

    def leave_scope(self):
        """Sai do escopo atual."""
        if len(self.scopes) > 1:
            self.scopes.pop()
        # Não podemos sair do escopo global

    def declare(self, name):
        """Declara uma nova variável no escopo ATUAL."""
        current_scope = self.scopes[-1]
        # Cria um nome único em Python (ex: "x__1", "x__2")
        mangled_name = f"{name}__{self.scope_level_counter}"
        current_scope[name] = mangled_name
        return mangled_name

    def lookup(self, name):
        """Procura o nome Python de uma variável, do escopo interno para o externo."""
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        
        # Isso não deve acontecer se a semântica passou
        raise Exception(f"Erro de Codegen: Variável '{name}' não encontrada.")

# --- O Gerador de Código (Visitor da AST) ---

class CodeGenVisitor:
    
    def __init__(self):
        self.output = []
        self.indent_level = 0
        self.symtab = CodeGenSymbolTable() 

    def _indent(self):
        return "    " * self.indent_level

    def _emit(self, line):
        self.output.append(f"{self._indent()}{line}")

    def visit(self, node):
        if node is None:
            return ""
            
        method_name = f'visit_{node.__class__.__name__}'
        visitor_method = getattr(self, method_name, self.generic_visit)
        return visitor_method(node)

    def generic_visit(self, node):
        if node is None or isinstance(node, ast.Empty):
            return ""
        raise NotImplementedError(f"Método 'visit_{node.__class__.__name__}' não implementado.")

    # --- Visitantes de Nós Contêineres ---

    def visit_Program(self, node: ast.Program):
        self._emit("# --- Código Python Gerado ---")
        self._emit("import sys # Adicionado para compatibilidade")
        
        # Helper de print
        self._emit("\ndef _minilang_print(*args):")
        self.indent_level += 1
        self._emit("output = []")
        self._emit("for arg in args:")
        self.indent_level += 1
        self._emit("if isinstance(arg, bool):") # Checagem explícita de bool
        self.indent_level += 1
        self._emit("output.append('true' if arg else 'false')")
        self.indent_level -= 1
        self._emit("elif arg is None:")
        self.indent_level += 1
        self._emit("output.append('null')")
        self.indent_level -= 1
        self._emit("else:")
        self.indent_level += 1
        self._emit("output.append(str(arg))")
        self.indent_level -= 1
        self.indent_level -= 1
        self._emit("print(' '.join(output))")
        self.indent_level -= 1
        self._emit("\n# --- Início do Código do Usuário ---")
        
        for stmt in node.statements:
            self.visit(stmt)
            
        self._emit("# --- Fim do Código do Usuário ---")
        return "\n".join(self.output)

    
    def visit_Block(self, node: ast.Block):
        # Um bloco (mesmo standalone) deve criar um novo escopo de variável
        self.symtab.enter_scope()
        
        if not node.statements:
            self._emit("pass")
            self.symtab.leave_scope() # Sai do escopo
            return

        for stmt in node.statements:
            self.visit(stmt)
        
        self.symtab.leave_scope() # Sai do escopo

    # --- Visitantes de Statements ---

    
    def visit_Declaration(self, node: ast.Declaration):
        # 1. Declara na Tabela de Símbolos do Codegen e pega o nome Python
        mangled_name = self.symtab.declare(node.var_id)
        
        if node.is_const:
            self._emit(f"# Declaração de constante (tratada como variável em Python)")
        
        if node.expression:
            expr_code = self.visit(node.expression)
            self._emit(f"{mangled_name} = {expr_code}")
        else:
            self._emit(f"{mangled_name} = None")

    
    def visit_Assignment(self, node: ast.Assignment):
        # 1. Busca o nome Python correto da variável
        mangled_name = self.symtab.lookup(node.var_name)
        value_code = self.visit(node.expression)
        
        if node.index_expr:
            index_code = self.visit(node.index_expr)
            self._emit(f"{mangled_name}[{index_code}] = {value_code}")
        else:
            self._emit(f"{mangled_name} = {value_code}")

    def visit_IfStatement(self, node: ast.IfStatement):
        cond_code = self.visit(node.condition)
        self._emit(f"if {cond_code}:")
        
        self.indent_level += 1
        self.visit(node.if_block) # visit_Block irá cuidar do escopo
        self.indent_level -= 1
        
        current_else_node = node.else_block
        
        while isinstance(current_else_node, ast.IfStatement):
            elif_node = current_else_node
            elif_cond_code = self.visit(elif_node.condition)
            
            self._emit(f"elif {elif_cond_code}:")
            self.indent_level += 1
            self.visit(elif_node.if_block) # visit_Block irá cuidar do escopo
            self.indent_level -= 1
            
            current_else_node = elif_node.else_block
        
        if current_else_node is not None:
            self._emit("else:")
            self.indent_level += 1
            self.visit(current_else_node) # visit_Block irá cuidar do escopo
            self.indent_level -= 1

    def visit_WhileStatement(self, node: ast.WhileStatement):
        cond_code = self.visit(node.condition)
        self._emit(f"while {cond_code}:")
        self.indent_level += 1
        self.visit(node.block) # visit_Block irá cuidar do escopo
        self.indent_level -= 1

    def visit_DoWhileStatement(self, node: ast.DoWhileStatement):
        self._emit("while True:")
        self.indent_level += 1
        
        # 'do-while' cria um escopo para o bloco
        self.symtab.enter_scope()
        if isinstance(node.block, ast.Block):
            for stmt in node.block.statements:
                self.visit(stmt)
        else:
            self.visit(node.block)
        
        cond_code = self.visit(node.condition)
        self._emit(f"if not ({cond_code}):")
        self.indent_level += 1
        self._emit("break")
        self.indent_level -= 1
        
        self.symtab.leave_scope() # Sai do escopo do 'do'
        self.indent_level -= 1

    def visit_ForStatement(self, node: ast.ForStatement):
        self._emit("# Início do 'for' C-style (traduzido para 'while')")
        # 'for' cria seu próprio escopo
        self.symtab.enter_scope()
        
        if not isinstance(node.initializer, ast.Empty):
            self.visit(node.initializer)
        
        cond_code = self.visit(node.condition) if not isinstance(node.condition, ast.Empty) else "True"
        self._emit(f"while {cond_code}:")
        
        self.indent_level += 1
        if isinstance(node.block, ast.Block):
             for stmt in node.block.statements:
                self.visit(stmt)
        else:
             self.visit(node.block)
        
        if not isinstance(node.iterator, ast.Empty):
            iter_code = self.visit(node.iterator)
            self._emit(iter_code)
            
        self.indent_level -= 1
        self.symtab.leave_scope() # Sai do escopo do 'for'
        self._emit("# Fim do 'for' C-style")

    
    def visit_ForEachStatement(self, node: ast.ForEachStatement):
        # 1. Busca o nome Python do iterável
        iterable_mangled_name = self.symtab.lookup(node.iterable_id)
        
        self._emit(f"# 'for each' cria um escopo interno")
        self.symtab.enter_scope()
        
        # 2. Declara a nova variável de loop (ex: 'num__X')
        loop_var_mangled = self.symtab.declare(node.var_id)
        
        self._emit(f"for {loop_var_mangled} in {iterable_mangled_name}:")
        self.indent_level += 1
        self.visit(node.block) # visit_Block criará *outro* escopo (correto)
        self.indent_level -= 1
        
        self.symtab.leave_scope()

    def visit_PrintStatement(self, node: ast.PrintStatement):
        expr_codes = [self.visit(expr) for expr in node.expressions]
        self._emit(f"_minilang_print({', '.join(expr_codes)})")

    # --- Visitantes de Expressões (Retornam strings) ---

    def visit_BinaryOp(self, node: ast.BinaryOp):
        left_code = self.visit(node.left)
        right_code = self.visit(node.right)
        
        op_map = {'&&': 'and', '||': 'or'}
        op = op_map.get(node.operator, node.operator)
        
        return f"({left_code} {op} {right_code})"

    def visit_UnaryOp(self, node: ast.UnaryOp):
        operand_code = self.visit(node.operand)
        op_map = {'!': 'not'}
        op = op_map.get(node.operator, node.operator)
        
        return f"({op} {operand_code})"

    # --- Visitantes de Fatores (Retornam strings) ---

    
    def visit_Id(self, node: ast.Id):
        # Busca o nome Python correto (ex: 'x__0')
        return self.symtab.lookup(node.name)
        
    def visit_ArrayAccess(self, node: ast.ArrayAccess):
        array_code = self.visit(node.array_id_node)
        index_code = self.visit(node.index_expr)
        return f"{array_code}[{index_code}]"

    def visit_NewArray(self, node: ast.NewArray):
        size_code = self.visit(node.size_expr)
        return f"([None] * {size_code})"

    def visit_DotAccess(self, node: ast.DotAccess):
        left_code = self.visit(node.left)
        right_code = node.right_id
        return f"{left_code}.{right_code}"

    # --- Visitantes de Literais (Retornam strings) ---
    
    def visit_IntLiteral(self, node: ast.IntLiteral):
        return str(node.value)

    def visit_FloatLiteral(self, node: ast.FloatLiteral):
        return str(node.value)
        
    def visit_StringLiteral(self, node: ast.StringLiteral):
        return repr(node.value)
        
    def visit_BoolLiteral(self, node: ast.BoolLiteral):

        return "True" if node.value else "False"
