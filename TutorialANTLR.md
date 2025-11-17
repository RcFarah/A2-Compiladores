# 📖 Tutorial da Opção 2: Construindo o Compilador com ANTLR4
Este documento detalha como o projeto foi configurado (Etapa 1) e como o *ANTLR4* foi usado para construir o *front-end* do compilador (Etapa 2 em diante).

## 🛠️ Instalação e Configuração (Local e Remota)
Para executar este projeto, é necessário configurar o ambiente de *Python* e *Java*.

### 1. Ambiente Local (Recomendado)
**Passo 1: Pré-requisitos (*Java*)**

É necessário ter o *Java* instalado para executar o *ANTLR*.
* O que é necessário: Embora apenas o JRE (Java Runtime Environment) seja estritamente necessário para executar o .jar do ANTLR (java -jar ...), a instalação do JDK (Java Development Kit) completo é recomendada.

* Instalação: [Link para instalação do JDK 8 (utilizado no projeto)](https://www.oracle.com/java/technologies/javase/jdk23-archive-downloads.html)

**Passo 2: Instalar Dependências *Python***

O projeto precisa da biblioteca *runtime* do *ANTLR* para *Python*.

```Bash
# O '3' representa a versão do Python 3.
pip install antlr4-python3-runtime
```

**Passo 3: Gerar os Ficheiros do Parser** *(Este passo só é necessário se você modificar a gramática grammar/MiniLang.g4)*

A ferramenta *ANTLR* (antlr-4.13.2-complete.jar) já está incluída no projeto. Execute o seguinte comando para gerar o código do *lexer* e *parser*:

```Bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

### 2. Ambiente Remoto (Google Colab)
Para rodar no *Google Colab*:

1.  **Crie um novo notebook no Google Colab.**

2.  **Faça o upload da estrutura** de pastas do projeto (as pastas *src*, *grammar* e *tests*) para o ambiente do *Colab*.

3.  **Instale as dependências na célula do notebook:**

    ```Python
    !pip install antlr4-python3-runtime
    ```

4.  **Execute o compilador numa célula** (após gerar os ficheiros do *parser*, se necessário):
    ```Python
    !python src/cli.py tests/ok_geral.min
    ```

## ⚙️ Como o ANTLR foi Usado (O Processo)
### Etapa 1: A Gramática (grammar/MiniLang.g4)
O "cérebro" do *front-end* é o arquivo de gramática. Ele define tanto o Analisador Léxico (*tokens*) quanto o Sintático (regras) em um só lugar.

Regras de *Lexer* (*Tokens*): Definidas com nomes em MAIÚSCULAS (ex: *INT*, *ID*, *WHILE*). Elas definem como o texto é dividido em "palavras".

Regras de *Parser* (Sintaxe): Definidas com nomes em minúsculas (ex: *program*, *statement*, *expression*). Elas definem a estrutura da linguagem.

Nós também implementamos bônus aqui, como mover os comentários (# e /*...*) para um *channel(HIDDEN)* para que o *parser* os ignorasse.

### Etapa 2: Geração do Código (O "Milagre" do *ANTLR*)
Uma vez que a gramática `MiniLang.g4` estava escrita, usamos o *ANTLR* para gerar automaticamente os ficheiros *Python* que compõem o *parser* (como visto no Passo 3 da instalação):

```Bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/generated grammar/MiniLang.g4
```

* -Dlanguage=Python3: Diz ao ANTLR para gerar código Python.
* -visitor: Gera a classe MiniLangVisitor.py, essencial para a próxima etapa.
* -o src/generated: O diretório de saída.

Isso criou `MiniLangLexer.py`, `MiniLangParser.py` e `MiniLangVisitor.py`.

### Etapa 3: Construindo nossa Própria *AST* (O "Visitor")
O *ANTLR* cria uma Árvore de *Parse* (concreta), mas o trabalho pedia uma Árvore Sintática Abstrata (*AST*). Para fazer essa tradução, nós criámos:

`src/ast_nodes.py`: Um ficheiro com classes *Python* simples (ex: *Program*, *IfStatement*, *BinaryOp*) que definem os nossos nós da árvore.

`src/ast_builder.py`: A classe principal desta etapa. Ela herda do `MiniLangVisitor.py` gerado. Nós sobrescrevemos os métodos *visit...()* (ex: *visitIf_stmt*) para que, ao caminhar pela árvore do *ANTLR*, ela retorne as instâncias das nossas classes de `ast_nodes.py`.

### Etapa 4: O *Pipeline* (`cli.py`)
O `cli.py` é o "motor" que conecta tudo. Ele segue este fluxo:

```Python
# 1. Lê o ficheiro-fonte
input_stream = FileStream("meu_codigo.min")

# 2. Cria o Lexer
lexer = MiniLangLexer(input_stream)

# 3. Cria o Parser
stream = CommonTokenStream(lexer)
parser = MiniLangParser(stream)

# 4. (Bónus) Adiciona o nosso listener de erro customizado
parser.removeErrorListeners()
parser.addErrorListener(MiniLangErrorListener())

# 5. Gera a Árvore de Parse (Concreta)
parse_tree = parser.program()

# 6. Constrói a nossa AST (Abstrata)
visitor = AstBuilderVisitor()
ast_tree = visitor.visit(parse_tree)

# 7. Passa a AST para as próximas fases...
sema = SemanticAnalyzer()
sema.visit(ast_tree)

interpreter = Interpreter()
interpreter.visit(ast_tree)
```

### Etapa 5: As Fases Seguintes
Após a Etapa 4, o trabalho do *ANTLR* está concluído. A *ast_tree* (a nossa *AST* limpa) é entregue para as outras fases do compilador (`sema.py`, `interp.py`, `codegen.py`), que foram implementadas manualmente como *Visitors* da nossa *AST*.

⬆️[Voltar para o README.md](README.md)