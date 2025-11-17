# src/cli.py

import sys
import os
from antlr4 import *

# Definições de Cor ANSI
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# INÍCIO DA CORREÇÃO DE PATH 
# Isso força o Python a entender a estrutura do seu projeto,
# adicionando a pasta raiz (A2 Compiladores) ao seu caminho de busca.
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)
# FIM DA CORREÇÃO DE PATH


# Imports
from src.generated.MiniLangLexer import MiniLangLexer
from src.generated.MiniLangParser import MiniLangParser
from src.ast_builder import AstBuilderVisitor
from src.pretty import print_ast_ascii
from src.sema import SemanticAnalyzer, SemanticError
from src.error_listener import MiniLangErrorListener
from src.interp import Interpreter, RuntimeErrorLang
from src.codegen import CodeGenVisitor 

def main(argv):
    """Função principal que executa o pipeline."""
    
    if len(argv) < 2:
        print("Uso: python src/cli.py <arquivo_de_teste.min>")
        print("Exemplo: python src/cli.py tests/ok_simple.min")
        sys.exit(1)
        
    input_file = argv[1]
    
    try:
        input_stream = FileStream(input_file, encoding='utf-8')

        # 1. Lexer, 2. Parser
        lexer = MiniLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MiniLangErrorListener())
        stream = CommonTokenStream(lexer)
        parser = MiniLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MiniLangErrorListener())
        
        # 3. Parse Tree
        print(f"--- Fazendo parse de: {input_file} ---")
        parse_tree = parser.program()

        # 4. AST
        print("\n--- Construindo AST ---")
        visitor = AstBuilderVisitor()
        ast_tree = visitor.visit(parse_tree)
        
        # 5. Pretty Print AST
        print("\n--- Árvore Sintática Abstrata (ASCII) ---")
        print_ast_ascii(ast_tree)
        
        # 6. Análise Semântica
        print("\n--- Análise Semântica ---")
        sema_analyzer = SemanticAnalyzer()
        sema_analyzer.visit(ast_tree)
        
        # (MODIFICADO) Adiciona cor verde
        print(f"{Colors.GREEN}Análise semântica concluída com sucesso!{Colors.RESET}")

        # 7. Tabela de Símbolos
        print("\n" + sema_analyzer.symtab.get_debug_output())

        # 8. Execução (Intérprete)
        print("\n" + "="*30)
        print(f"--- Fase de Execução ({Colors.CYAN}Intérprete{Colors.RESET}) ---")
        interpreter = Interpreter()
        interpreter.visit(ast_tree) # Inicia a execução
        print("="*30)
        
        # 9. Geração de Código
        print("\n" + "="*30)
        print(f"--- Fase de Geração de Código ({Colors.CYAN}Python{Colors.RESET}) ---")
        codegen = CodeGenVisitor()
        python_code = codegen.visit(ast_tree)
        print(python_code)
        print("="*30)
        
        # 10. Execução do Código Gerado
        print("\n" + "="*30)
        print(f"--- Executando Código ({Colors.CYAN}Python Gerado{Colors.RESET}) ---")
        exec(python_code, globals()) # Executa o código gerado
        print("="*30)


    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {input_file}")
        sys.exit(1)
    
    # (MODIFICADO) Adiciona cores de erro
    except SyntaxError as e:
        print(f"\n{Colors.RED}{Colors.BOLD}!!!!!! ERRO DE SINTAXE !!!!!!{Colors.RESET}")
        print(f"{Colors.YELLOW}{e}{Colors.RESET}")
        sys.exit(1)

    # (MODIFICADO) Adiciona cores de erro
    except SemanticError as e:
        print(f"\n{Colors.RED}{Colors.BOLD}!!!!!! ERRO SEMÂNTICO !!!!!!{Colors.RESET}")
        print(f"{Colors.YELLOW}{e}{Colors.RESET}")
        sys.exit(1)
    
    # (MODIFICADO) Adiciona cores de erro
    except RuntimeErrorLang as e:
        print(f"\n{Colors.RED}{Colors.BOLD}!!!!!! ERRO DE EXECUÇÃO (INTÉRPRETE) !!!!!!{Colors.RESET}")
        print(f"{Colors.YELLOW}{e}{Colors.RESET}")
        sys.exit(1)
        
    except Exception as e:
        print(f"Ocorreu um erro durante a compilação: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)