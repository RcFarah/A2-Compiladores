# src/error_listener.py

"""
Define um Error Listener customizado para o ANTLR.

Em vez de apenas imprimir o erro no console e continuar (o padrão),
este listener levanta uma exceção 'SyntaxError', que podemos
capturar no cli.py para parar a compilação.
"""

from antlr4.error.ErrorListener import ErrorListener

class MiniLangErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Este método é chamado pelo ANTLR sempre que um erro de sintaxe é encontrado.
        """
        # Formata a mensagem de erro
        error_message = f"Erro de Sintaxe na linha {line}:{column} - {msg}"
        
        # Levanta uma exceção padrão do Python, que interromperá o parse
        raise SyntaxError(error_message)