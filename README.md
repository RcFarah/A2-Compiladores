
# 🧑‍💻MiniLang Compiler

*Trabalho A2 da disciplina de Compiladores*

Este projeto é um compilador completo para uma linguagem de *script* personalizada (chamada **"MiniLang"**), construído em *Python*. Ele implementa todo o *pipeline* de compilação, desde a análise de texto até a execução.

O *front-end* (analisador léxico e sintático) foi gerado automaticamente usando o *ANTLR4*, e o *back-end* (análise semântica, intérprete e gerador de código) foi implementado manualmente em *Python*.

## 👥 Integrantes e Divisão de Tarefas
* **Rodrigo Corrêa de Sá Farah - Matrícula: 1220301863**
    * Responsável por: Estruturação do README.md e TutorialANTLR.md; Auxílio na programação do compilador; Gravação do Tutorial; Gravação da Demonstração.

* **Theo Christiano da Silva Odawara - Matrícula: 1250108456**
    * Responsável por: Auxílio na programação do compilador por completo; Auxílio na criação do Tutorial e README.md;

* **Vinicius Larsen Santos - Matrícula: 1230116152**
    * Responsável por: Auxílio na programação do compilador por completo; Auxílio na criação do Tutorial e README.md;

## 🪄Funcionalidades

### 🔤Linguagem
* Tipos de Dados: `int`, `float`, `bool`, `string`.
* Controle de Fluxo: `if/else` (com `elif`), `while`, `do-while`.
* Arrays: Suporte para declaração (`int[] a`), criação (`new int[10]`) e acesso (`a[i]`).
* Loops: Suporte a `for each` (`int item : array`).
* Constantes: Suporte à palavra-chave `const`.
* Comentários: Suporte a comentários de linha (`# ...`) e de bloco (`/* ... */`).

### 🧑‍💻Compilador

O *pipeline* do compilador inclui as seguintes fases:

1.  **Análise Léxica**: Converte o código-fonte em uma sequência de tokens.
2.  **Análise Sintática**: Verifica se a sequência de tokens segue a gramática da linguagem e constrói uma Parse Tree.
3.  **Construção da AST**: Converte a Parse Tree em uma Árvore Sintática Abstrata (AST) mais limpa.
4.  **Análise Semântica**: Percorre a AST para verificar erros de tipo, declarações de variáveis, etc., e constrói uma Tabela de Símbolos.
5.  **Geração de Código**: Gera código Python equivalente a partir da AST.
7.  **Execução Dupla:** O código pode ser executado de duas formas:
    * Intérprete: A AST é executada diretamente.
    * Gerador de Código (Codegen): A AST é traduzida para código Python (com renomeamento de variáveis para simular escopo de bloco) e depois executada.
8.  **Relatório de Erros Detalhado (Bônus):**
    * Erros Léxicos: Captura caracteres inválidos.
    * Erros Sintáticos: Captura sintaxe malformada (`ex: if (x > 5 { ...`) e para a compilação.
    * Erros Semânticos: Captura erros de tipo, escopo (variável não declarada), uso de *const*, etc., reportando a linha e coluna exatas do erro.


## 🏗️Estrutura do Projeto
```
A2 Compiladores/
│
├── grammar/
│   └── MiniLang.g4         # A gramática ANTLR4
│
├── src/
│   ├── generated/          # Código gerado pelo ANTLR (Lexer, Parser, Visitor)
│   ├── ast_nodes.py        # Definição das classes da nossa AST
│   ├── ast_builder.py      # Visitor que constrói nossa AST a partir do ANTLR
│   ├── cli.py              # O "driver" principal do compilador
│   ├── codegen.py          # Visitor que gera código Python
│   ├── error_listener.py   # Listener customizado para erros de sintaxe
│   ├── interp.py           # Visitor que executa a AST (Intérprete)
│   ├── pretty.py           # Visitor que imprime a AST em formato ASCII
│   └── sema.py             # Visitor que faz a Análise Semântica
│
├── tests/
│   ├── ok_geral.min        # Teste complexo de sucesso (FizzBuzz)
│   ├── err_sema_type.min   # Teste de erro semântico
│   └── ...                 # (Outros 13+ arquivos de teste)
│
├── antlr-4.13.2-complete.jar # Ferramenta ANTLR
├── README.md               # Este arquivo
└── TutorialANTLR.md        # Tutorial de Instalação e da Opção 2
```
## 🔤Gramática (EBNF)

A gramática da *MiniLang* está definida em `grammar/MiniLang.g4`. Aqui está uma visão geral em formato EBNF:
<details> <summary style="color:#e30bc6;font-weight:bold">Clique para ver a gramática EBNF completa da MiniLang</summary>

```ebnf
program         : statement* EOF;
block           : '{' statement* '}';
statement       : block
                | declaration
                | assignment
                | if_stmt
                | while_stmt
                | do_while_stmt
                | for_stmt
                | for_each_stmt
                | print_stmt
                | expression ';';

if_stmt         : 'if' '(' expression ')' statement ('else' statement)?;
while_stmt      : 'while' '(' expression ')' statement;
do_while_stmt   : 'do' statement 'while' '(' expression ')' ';';
for_stmt        : 'for' '(' for_initializer? ';' expression? ';' for_iterator? ')' statement;
for_each_stmt   : 'for' 'each' '(' type ID ':' ID ')' statement;
print_stmt      : 'print' '(' expression_list? ')' ';';

declaration     : 'const'? type ('[' ']')? ID ('=' expression)? ';';
assignment      : ID ('[' expression ']')? '=' expression ';';
type            : 'int' | 'float' | 'string' | 'bool';

expression      : logical_or;
logical_or      : logical_and ('||' logical_and)*;
logical_and     : equality ('&&' equality)*;
equality        : comparison (('==' | '!=') comparison)*;
comparison      : arithmetic (('<' | '<=' | '>' | '>=') arithmetic)*;
arithmetic      : term (('+' | '-') term)*;
term            : unary (('*' | '/' | '%') unary)*;
unary           : ('!' | '-') unary | factor;
factor          : '(' expression ')'
                | 'new' type '[' expression ']'
                | ID ('.' ID)?
                | ID '[' expression ']'
                | literal;
literal         : INT_LIT | FLOAT_LIT | STRING_LIT | 'true' | 'false';
```
</details>

## Como Rodar
➡️ **[Instruções de instalação em TutorialANTLR.md](TutorialANTLR.md)**

O `cli.py` é o ponto de entrada principal. Ele recebe o caminho para um arquivo `.min` como argumento.

### ✅Testando um Arquivo de Sucesso (ok_*.min)
O compilador executará todas as fases e mostrará a saída do Intérprete e do Codegen.

```Bash
python src/cli.py tests/ok_geral.min
```
### 1. Árvore Sintática Abstrata (AST)
A *AST* é uma representação hierárquica do código. Para o arquivo `ok_geral.min`, a saída da *AST* será parecida com esta:
<details> <summary style="color:#add8e6;font-weight:bold">Clique para ver a AST do arquivo ok_geral.min completa</summary>

```
Program
├── Declaration(id='arr', type='int[]')
│   └── NewArray(type='int')
│       └── IntLiteral(value=20)
├── Assignment(target='arr')
│   ├── IntLiteral(value=0)
│   └── IntLiteral(value=0)
├── Assignment(target='arr')
│   ├── IntLiteral(value=1)
│   └── IntLiteral(value=1)
├── Declaration(id='i', type='int')
│   └── IntLiteral(value=2)
├── While
│   ├── BinaryOp(op='<')
│   │   ├── Id(name='i')
│   │   └── IntLiteral(value=20)
│   └── Block
│       ├── Assignment(target='arr')
│       │   ├── Id(name='i')
│       │   └── BinaryOp(op='+')
│       │       ├── ArrayAccess
│       │       │   ├── Id(name='arr')
│       │       │   └── BinaryOp(op='-')
│       │       │       ├── Id(name='i')
│       │       │       └── IntLiteral(value=1)
│       │       └── ArrayAccess
│       │           ├── Id(name='arr')
│       │           └── BinaryOp(op='-')
│       │               ├── Id(name='i')
│       │               └── IntLiteral(value=2)
│       └── Assignment(target='i')
│           └── BinaryOp(op='+')
│               ├── Id(name='i')
│               └── IntLiteral(value=1)
└── ForEach(var='int num', iterable='arr')
    └── Block
        └── If
            ├── BinaryOp(op='==')
            │   ├── BinaryOp(op='%')
            │   │   ├── Id(name='num')
            │   │   └── IntLiteral(value=15)
            │   └── IntLiteral(value=0)
            ├── Block
            │   └── PrintStatement
            │       └── StringLiteral(value='FizzBuzz')
            └── If
                ├── BinaryOp(op='==')
                │   ├── BinaryOp(op='%')
                │   │   ├── Id(name='num')
                │   │   └── IntLiteral(value=3)
                │   └── IntLiteral(value=0)
                ├── Block
                │   └── PrintStatement
                │       └── StringLiteral(value='Fizz')
                └── If
                    ├── BinaryOp(op='==')
                    │   ├── BinaryOp(op='%')
                    │   │   ├── Id(name='num')
                    │   │   └── IntLiteral(value=5)
                    │   └── IntLiteral(value=0)
                    ├── Block
                    │   └── PrintStatement
                    │       └── StringLiteral(value='Buzz')
                    └── Block
                        └── PrintStatement
                            └── Id(name='num')
```
</details>


### 2. Tabela de Símbolos

A análise semântica constrói uma tabela de símbolos para rastrear variáveis, tipos e escopos.
<details> <summary style="color:#add8e6;font-weight:bold">Clique para ver a Tabela de Símbolos do arquivo ok_geral.min completa</summary>

```
--- Tabela de Símbolos (Log) ---
   Declare: <arr: int, array> (Lvl 0)
   Initialize: arr
   Initialize: arr
   Declare: <i: int> (Lvl 0)
-> Enter Scope (Lvl 1)
   Initialize: arr
   Initialize: i
<- Leave Scope (Lvl 0)
-> Enter Scope (Lvl 1)
   Declare: <num: int, const> (Lvl 1)
-> Enter Scope (Lvl 2)
-> Enter Scope (Lvl 3)
<- Leave Scope (Lvl 2)
-> Enter Scope (Lvl 3)
<- Leave Scope (Lvl 2)
-> Enter Scope (Lvl 3)
<- Leave Scope (Lvl 2)
-> Enter Scope (Lvl 3)
<- Leave Scope (Lvl 2)
<- Leave Scope (Lvl 1)
<- Leave Scope (Lvl 0)
--- Fim da Análise ---
```
</details>

### 3. Execução (Intérprete e Código Gerado)

O programa é executado tanto pelo intérprete quanto pelo código *Python* gerado, produzindo a mesma saída.

**Saída do Intérprete:**
<details> <summary style="color:#add8e6;font-weight:bold">Clique para ver a Saída do Intérprete do arquivo `ok_geral.min`</summary>

```
--- Fase de Execução (Intérprete) ---
--- Executando Código ---
FizzBuzz
1
1
2
Fizz
Buzz
8
13
Fizz
34
Buzz
89
Fizz
233
377
Buzz
Fizz
1597
2584
4181
--- Execução Concluída ---
```
</details>

**Código Python Gerado:**
<details> <summary style="color:#add8e6;font-weight:bold">Clique para ver o código Python gerado do arquivo `ok_geral.min`</summary>

```python
--- Fase de Geração de Código (Python) ---
# --- Código Python Gerado ---
import sys # Adicionado para compatibilidade

def _minilang_print(*args):
    output = []
    for arg in args:
        if isinstance(arg, bool):
            output.append('true' if arg else 'false')
        elif arg is None:
            output.append('null')
        else:
            output.append(str(arg))
    print(' '.join(output))

# --- Início do Código do Usuário ---
arr__0 = ([None] * 20)
arr__0[0] = 0
arr__0[1] = 1
i__0 = 2
while (i__0 < 20):
    arr__0[i__0] = (arr__0[(i__0 - 1)] + arr__0[(i__0 - 2)])
    i__0 = (i__0 + 1)
# 'for each' cria um escopo interno
for num__2 in arr__0:
    if ((num__2 % 15) == 0):
        _minilang_print('FizzBuzz')
    elif ((num__2 % 3) == 0):
        _minilang_print('Fizz')
    elif ((num__2 % 5) == 0):
        _minilang_print('Buzz')
    else:
        _minilang_print(num__2)
# --- Fim do Código do Usuário ---
```
</details>

**Saída do Código Gerado:**
<details> <summary style="color:#add8e6;font-weight:bold">Clique para ver a Saída do Código Python gerado do arquivo `ok_geral.min`</summary>

```
--- Executando Código Python Gerado ---
FizzBuzz
1
1
2
Fizz
Buzz
8
13
Fizz
34
Buzz
89
Fizz
233
377
Buzz
Fizz
1597
2584
4181
==============================
```
</details>

## Links para Vídeos de Apoio

### [Tutorial de Instalação do ANTLR](https://youtu.be/HfD-jGZRuyE)
### [Tutorial de Visão Geral do Projeto](https://youtu.be/Fx_QvF6PQ9U)
### [Realização de todos os Testes do Projeto](https://youtu.be/44EVGlfBY8c)