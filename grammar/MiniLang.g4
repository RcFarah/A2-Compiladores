// Define que este é um arquivo de gramática ANTLR4 chamado MiniLang
grammar MiniLang;
/*
 * =============================================================================
 * REGRAS DE PARSER (SINTAXE)
 * =============================================================================
 */

// Ponto de entrada: um programa é zero ou mais statements
program: statement* EOF;
// Bloco de código: usado por if/while/do/for
block: LBRACE statement* RBRACE;
// Um statement pode ser várias coisas
statement
    : block                         // Bloco
    |
declaration                   // Declaração com const, tipos e arrays
    |
assignment                    // Atribuição a var ou array
    |
if_stmt                       // if/else
    |
while_stmt                    // while
    |
do_while_stmt                 // do-while
    |
for_stmt                      // for
    |
for_each_stmt                 // for each
    |
print_stmt                    // print com múltiplos args
    |
expression SEMIC              // ex: func_call();
    ;
/*
 * =============================================================================
 * STATEMENTS DE CONTROLE
 * =============================================================================
 */

if_stmt
    : IF LPAREN expression RPAREN statement (ELSE statement)?
;

while_stmt
    : WHILE LPAREN expression RPAREN statement
    ;
do_while_stmt
    : DO statement WHILE LPAREN expression RPAREN SEMIC
    ;
// 'for' clássico
for_stmt
    : FOR LPAREN for_initializer? SEMIC expression? SEMIC for_iterator? RPAREN statement
    ;
// 'for each'
for_each_stmt
    : FOR EACH LPAREN type ID COLON ID RPAREN statement
    ;
// Elementos do 'for'
for_initializer
    : declaration                   // Permite declarar 'int i = 0'
    |
expression_list               // Permite 'i = 0, j = 1'
    ;
for_iterator
    : expression_list               // Permite 'i++, j++'
    ;
// 'print' com múltiplos argumentos 
print_stmt
    : PRINT LPAREN expression_list? RPAREN SEMIC
    ;
expression_list
    : expression (COMMA expression)*
    ;
/*
 * =============================================================================
 * DECLARAÇÃO E ATRIBUIÇÃO
 * =============================================================================
 */

// Adiciona 'const?' e '[]?'
declaration
    : CONST?
type (LBRACK RBRACK)? ID (ASSIGN expression)? SEMIC
    ;

// Tipos
type: INT | FLOAT | STRING | BOOL;
// Permite atribuição a ID normal ou a índice de array
assignment
    : ID (LBRACK expression RBRACK)?
ASSIGN expression SEMIC
    ;


/*
 * =============================================================================
 * PRECEDÊNCIA DE EXPRESSÕES
 * =============================================================================
 */

// Nível 1: Ou Lógico
expression
    : logical_or
    ;
// Nível 2: E Lógico
logical_or
    : logical_and (OR logical_and)*
    ;
// Nível 3: Igualdade
logical_and
    : equality (AND equality)*
    ;
// Nível 4: Relacional
equality
    : comparison ((EQ | NEQ) comparison)*
    ;
// Nível 5: Adição / Subtração
comparison
    : arithmetic ((LT | LTE | GT | GTE) arithmetic)*
    ;
// Nível 6: Multiplicação / Divisão / Módulo
arithmetic
    : term ((PLUS | MINUS) term)*
    ;
// Nível 7: Operadores Unários (Not e Negação)
term
    : unary ((MULT | DIV | MOD) unary)* ;
// Nível 8: Fatores (Átomos)
unary
    : (NOT | MINUS) unary
    |
factor
    ;

factor
    : LPAREN expression RPAREN            // ( expressão )
    |
NEW type LBRACK expression RBRACK   // new int[10]
    | ID (DOT ID)?
// var ou var.prop
    | ID LBRACK expression RBRACK         // var[i]
    |
literal                           // 123, 1.23, "oi", true, false
    ;
// Literais
literal
    : INT_LIT
    | FLOAT_LIT
    |
STRING_LIT
    | TRUE
    | FALSE
    ;
/*
 * =============================================================================
 * REGRAS DE LEXER (TOKENS)
 * =============================================================================
 */

// Comentário de linha única agora é '#'
COMMENT
    : '#' ~[\r\n]* -> channel(HIDDEN) // Tem que estar assim!
    ;

ML_COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

// Ignorar Espaços em Branco
WS: [ \t\r\n]+ -> skip;


// Palavras-chave
FOR   : 'for';
EACH  : 'each';
IF    : 'if';
ELSE  : 'else';
WHILE : 'while';
PRINT : 'print';
INT   : 'int';
FLOAT : 'float';
STRING: 'string';
CONST : 'const';
BOOL  : 'bool';
NEW   : 'new';
DO    : 'do';
TRUE  : 'true';
FALSE : 'false';
// Literais
INT_LIT   : [0-9]+;
FLOAT_LIT : [0-9]+ '.' [0-9]+;
STRING_LIT: '"' (~["\r\n\\] | '\\' .)*?
'"'; // String com escapes

// Identificador
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

// Operadores
ASSIGN: '=';
EQ    : '==';
NEQ   : '!=';
LT    : '<';
LTE   : '<=';
GT    : '>';
GTE   : '>=';
PLUS  : '+';
MINUS : '-';
MULT  : '*';
DIV   : '/';
MOD   : '%'; 
NOT   : '!';
AND   : '&&';
OR    : '||';

// Delimitadores
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMIC : ';';
COMMA : ',';
COLON : ':';
DOT   : '.';
LBRACK: '[';
RBRACK: ']';