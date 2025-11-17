# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,261,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,5,1,61,8,1,10,1,12,1,64,9,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,80,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,108,8,6,1,6,1,6,3,6,112,
        8,6,1,6,1,6,3,6,116,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,3,8,133,8,8,1,9,1,9,1,10,1,10,1,10,3,10,140,
        8,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,148,8,11,10,11,12,11,151,
        9,11,1,12,3,12,154,8,12,1,12,1,12,1,12,3,12,159,8,12,1,12,1,12,1,
        12,3,12,164,8,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,
        14,175,8,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,5,16,186,
        8,16,10,16,12,16,189,9,16,1,17,1,17,1,17,5,17,194,8,17,10,17,12,
        17,197,9,17,1,18,1,18,1,18,5,18,202,8,18,10,18,12,18,205,9,18,1,
        19,1,19,1,19,5,19,210,8,19,10,19,12,19,213,9,19,1,20,1,20,1,20,5,
        20,218,8,20,10,20,12,20,221,9,20,1,21,1,21,1,21,5,21,226,8,21,10,
        21,12,21,229,9,21,1,22,1,22,1,22,3,22,234,8,22,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,249,8,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,257,8,23,1,24,1,24,1,24,0,0,25,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,0,7,2,0,10,12,14,14,1,0,24,25,1,0,26,29,1,0,30,31,1,0,32,34,
        2,0,31,31,35,35,1,0,17,21,269,0,53,1,0,0,0,2,58,1,0,0,0,4,79,1,0,
        0,0,6,81,1,0,0,0,8,90,1,0,0,0,10,96,1,0,0,0,12,104,1,0,0,0,14,120,
        1,0,0,0,16,132,1,0,0,0,18,134,1,0,0,0,20,136,1,0,0,0,22,144,1,0,
        0,0,24,153,1,0,0,0,26,167,1,0,0,0,28,169,1,0,0,0,30,180,1,0,0,0,
        32,182,1,0,0,0,34,190,1,0,0,0,36,198,1,0,0,0,38,206,1,0,0,0,40,214,
        1,0,0,0,42,222,1,0,0,0,44,233,1,0,0,0,46,256,1,0,0,0,48,258,1,0,
        0,0,50,52,3,4,2,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,0,0,1,57,1,1,0,0,0,58,
        62,5,40,0,0,59,61,3,4,2,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,
        0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,41,0,0,66,
        3,1,0,0,0,67,80,3,2,1,0,68,80,3,24,12,0,69,80,3,28,14,0,70,80,3,
        6,3,0,71,80,3,8,4,0,72,80,3,10,5,0,73,80,3,12,6,0,74,80,3,14,7,0,
        75,80,3,20,10,0,76,77,3,30,15,0,77,78,5,42,0,0,78,80,1,0,0,0,79,
        67,1,0,0,0,79,68,1,0,0,0,79,69,1,0,0,0,79,70,1,0,0,0,79,71,1,0,0,
        0,79,72,1,0,0,0,79,73,1,0,0,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,
        1,0,0,0,80,5,1,0,0,0,81,82,5,6,0,0,82,83,5,38,0,0,83,84,3,30,15,
        0,84,85,5,39,0,0,85,88,3,4,2,0,86,87,5,7,0,0,87,89,3,4,2,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,7,1,0,0,0,90,91,5,8,0,0,91,92,5,38,0,0,
        92,93,3,30,15,0,93,94,5,39,0,0,94,95,3,4,2,0,95,9,1,0,0,0,96,97,
        5,16,0,0,97,98,3,4,2,0,98,99,5,8,0,0,99,100,5,38,0,0,100,101,3,30,
        15,0,101,102,5,39,0,0,102,103,5,42,0,0,103,11,1,0,0,0,104,105,5,
        4,0,0,105,107,5,38,0,0,106,108,3,16,8,0,107,106,1,0,0,0,107,108,
        1,0,0,0,108,109,1,0,0,0,109,111,5,42,0,0,110,112,3,30,15,0,111,110,
        1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,115,5,42,0,0,114,116,
        3,18,9,0,115,114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,
        5,39,0,0,118,119,3,4,2,0,119,13,1,0,0,0,120,121,5,4,0,0,121,122,
        5,5,0,0,122,123,5,38,0,0,123,124,3,26,13,0,124,125,5,22,0,0,125,
        126,5,44,0,0,126,127,5,22,0,0,127,128,5,39,0,0,128,129,3,4,2,0,129,
        15,1,0,0,0,130,133,3,24,12,0,131,133,3,22,11,0,132,130,1,0,0,0,132,
        131,1,0,0,0,133,17,1,0,0,0,134,135,3,22,11,0,135,19,1,0,0,0,136,
        137,5,9,0,0,137,139,5,38,0,0,138,140,3,22,11,0,139,138,1,0,0,0,139,
        140,1,0,0,0,140,141,1,0,0,0,141,142,5,39,0,0,142,143,5,42,0,0,143,
        21,1,0,0,0,144,149,3,30,15,0,145,146,5,43,0,0,146,148,3,30,15,0,
        147,145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,
        150,23,1,0,0,0,151,149,1,0,0,0,152,154,5,13,0,0,153,152,1,0,0,0,
        153,154,1,0,0,0,154,155,1,0,0,0,155,158,3,26,13,0,156,157,5,46,0,
        0,157,159,5,47,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,
        0,160,163,5,22,0,0,161,162,5,23,0,0,162,164,3,30,15,0,163,161,1,
        0,0,0,163,164,1,0,0,0,164,165,1,0,0,0,165,166,5,42,0,0,166,25,1,
        0,0,0,167,168,7,0,0,0,168,27,1,0,0,0,169,174,5,22,0,0,170,171,5,
        46,0,0,171,172,3,30,15,0,172,173,5,47,0,0,173,175,1,0,0,0,174,170,
        1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,5,23,0,0,177,178,
        3,30,15,0,178,179,5,42,0,0,179,29,1,0,0,0,180,181,3,32,16,0,181,
        31,1,0,0,0,182,187,3,34,17,0,183,184,5,37,0,0,184,186,3,34,17,0,
        185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,
        188,33,1,0,0,0,189,187,1,0,0,0,190,195,3,36,18,0,191,192,5,36,0,
        0,192,194,3,36,18,0,193,191,1,0,0,0,194,197,1,0,0,0,195,193,1,0,
        0,0,195,196,1,0,0,0,196,35,1,0,0,0,197,195,1,0,0,0,198,203,3,38,
        19,0,199,200,7,1,0,0,200,202,3,38,19,0,201,199,1,0,0,0,202,205,1,
        0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,37,1,0,0,0,205,203,1,0,
        0,0,206,211,3,40,20,0,207,208,7,2,0,0,208,210,3,40,20,0,209,207,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,39,1,
        0,0,0,213,211,1,0,0,0,214,219,3,42,21,0,215,216,7,3,0,0,216,218,
        3,42,21,0,217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,
        1,0,0,0,220,41,1,0,0,0,221,219,1,0,0,0,222,227,3,44,22,0,223,224,
        7,4,0,0,224,226,3,44,22,0,225,223,1,0,0,0,226,229,1,0,0,0,227,225,
        1,0,0,0,227,228,1,0,0,0,228,43,1,0,0,0,229,227,1,0,0,0,230,231,7,
        5,0,0,231,234,3,44,22,0,232,234,3,46,23,0,233,230,1,0,0,0,233,232,
        1,0,0,0,234,45,1,0,0,0,235,236,5,38,0,0,236,237,3,30,15,0,237,238,
        5,39,0,0,238,257,1,0,0,0,239,240,5,15,0,0,240,241,3,26,13,0,241,
        242,5,46,0,0,242,243,3,30,15,0,243,244,5,47,0,0,244,257,1,0,0,0,
        245,248,5,22,0,0,246,247,5,45,0,0,247,249,5,22,0,0,248,246,1,0,0,
        0,248,249,1,0,0,0,249,257,1,0,0,0,250,251,5,22,0,0,251,252,5,46,
        0,0,252,253,3,30,15,0,253,254,5,47,0,0,254,257,1,0,0,0,255,257,3,
        48,24,0,256,235,1,0,0,0,256,239,1,0,0,0,256,245,1,0,0,0,256,250,
        1,0,0,0,256,255,1,0,0,0,257,47,1,0,0,0,258,259,7,6,0,0,259,49,1,
        0,0,0,23,53,62,79,88,107,111,115,132,139,149,153,158,163,174,187,
        195,203,211,219,227,233,248,256
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'for'", "'each'", "'if'", "'else'", "'while'", "'print'", 
                     "'int'", "'float'", "'string'", "'const'", "'bool'", 
                     "'new'", "'do'", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "':'", "'.'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "ML_COMMENT", "WS", "FOR", 
                      "EACH", "IF", "ELSE", "WHILE", "PRINT", "INT", "FLOAT", 
                      "STRING", "CONST", "BOOL", "NEW", "DO", "TRUE", "FALSE", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID", "ASSIGN", 
                      "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "NOT", "AND", "OR", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "SEMIC", "COMMA", "COLON", 
                      "DOT", "LBRACK", "RBRACK" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_if_stmt = 3
    RULE_while_stmt = 4
    RULE_do_while_stmt = 5
    RULE_for_stmt = 6
    RULE_for_each_stmt = 7
    RULE_for_initializer = 8
    RULE_for_iterator = 9
    RULE_print_stmt = 10
    RULE_expression_list = 11
    RULE_declaration = 12
    RULE_type = 13
    RULE_assignment = 14
    RULE_expression = 15
    RULE_logical_or = 16
    RULE_logical_and = 17
    RULE_equality = 18
    RULE_comparison = 19
    RULE_arithmetic = 20
    RULE_term = 21
    RULE_unary = 22
    RULE_factor = 23
    RULE_literal = 24

    ruleNames =  [ "program", "block", "statement", "if_stmt", "while_stmt", 
                   "do_while_stmt", "for_stmt", "for_each_stmt", "for_initializer", 
                   "for_iterator", "print_stmt", "expression_list", "declaration", 
                   "type", "assignment", "expression", "logical_or", "logical_and", 
                   "equality", "comparison", "arithmetic", "term", "unary", 
                   "factor", "literal" ]

    EOF = Token.EOF
    COMMENT=1
    ML_COMMENT=2
    WS=3
    FOR=4
    EACH=5
    IF=6
    ELSE=7
    WHILE=8
    PRINT=9
    INT=10
    FLOAT=11
    STRING=12
    CONST=13
    BOOL=14
    NEW=15
    DO=16
    TRUE=17
    FALSE=18
    INT_LIT=19
    FLOAT_LIT=20
    STRING_LIT=21
    ID=22
    ASSIGN=23
    EQ=24
    NEQ=25
    LT=26
    LTE=27
    GT=28
    GTE=29
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    MOD=34
    NOT=35
    AND=36
    OR=37
    LPAREN=38
    RPAREN=39
    LBRACE=40
    RBRACE=41
    SEMIC=42
    COMMA=43
    COLON=44
    DOT=45
    LBRACK=46
    RBRACK=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1410905145168) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MiniLangParser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1410905145168) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(MiniLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MiniLangParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniLangParser.AssignmentContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.Do_while_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.For_stmtContext,0)


        def for_each_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.For_each_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MiniLangParser.Print_stmtContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def SEMIC(self):
            return self.getToken(MiniLangParser.SEMIC, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 72
                self.do_while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 73
                self.for_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 74
                self.for_each_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 75
                self.print_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 76
                self.expression()
                self.state = 77
                self.match(MiniLangParser.SEMIC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MiniLangParser.IF)
            self.state = 82
            self.match(MiniLangParser.LPAREN)
            self.state = 83
            self.expression()
            self.state = 84
            self.match(MiniLangParser.RPAREN)
            self.state = 85
            self.statement()
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(MiniLangParser.ELSE)
                self.state = 87
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MiniLangParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MiniLangParser.WHILE)
            self.state = 91
            self.match(MiniLangParser.LPAREN)
            self.state = 92
            self.expression()
            self.state = 93
            self.match(MiniLangParser.RPAREN)
            self.state = 94
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MiniLangParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def SEMIC(self):
            return self.getToken(MiniLangParser.SEMIC, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_do_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while_stmt" ):
                listener.enterDo_while_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while_stmt" ):
                listener.exitDo_while_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MiniLangParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MiniLangParser.DO)
            self.state = 97
            self.statement()
            self.state = 98
            self.match(MiniLangParser.WHILE)
            self.state = 99
            self.match(MiniLangParser.LPAREN)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(MiniLangParser.RPAREN)
            self.state = 102
            self.match(MiniLangParser.SEMIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def SEMIC(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.SEMIC)
            else:
                return self.getToken(MiniLangParser.SEMIC, i)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def for_initializer(self):
            return self.getTypedRuleContext(MiniLangParser.For_initializerContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def for_iterator(self):
            return self.getTypedRuleContext(MiniLangParser.For_iteratorContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniLangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MiniLangParser.FOR)
            self.state = 105
            self.match(MiniLangParser.LPAREN)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 311393451008) != 0):
                self.state = 106
                self.for_initializer()


            self.state = 109
            self.match(MiniLangParser.SEMIC)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 311393419264) != 0):
                self.state = 110
                self.expression()


            self.state = 113
            self.match(MiniLangParser.SEMIC)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 311393419264) != 0):
                self.state = 114
                self.for_iterator()


            self.state = 117
            self.match(MiniLangParser.RPAREN)
            self.state = 118
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_each_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniLangParser.FOR, 0)

        def EACH(self):
            return self.getToken(MiniLangParser.EACH, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def COLON(self):
            return self.getToken(MiniLangParser.COLON, 0)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_for_each_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_each_stmt" ):
                listener.enterFor_each_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_each_stmt" ):
                listener.exitFor_each_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each_stmt" ):
                return visitor.visitFor_each_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_each_stmt(self):

        localctx = MiniLangParser.For_each_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for_each_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MiniLangParser.FOR)
            self.state = 121
            self.match(MiniLangParser.EACH)
            self.state = 122
            self.match(MiniLangParser.LPAREN)
            self.state = 123
            self.type_()
            self.state = 124
            self.match(MiniLangParser.ID)
            self.state = 125
            self.match(MiniLangParser.COLON)
            self.state = 126
            self.match(MiniLangParser.ID)
            self.state = 127
            self.match(MiniLangParser.RPAREN)
            self.state = 128
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniLangParser.DeclarationContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(MiniLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_for_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_initializer" ):
                listener.enterFor_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_initializer" ):
                listener.exitFor_initializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_initializer" ):
                return visitor.visitFor_initializer(self)
            else:
                return visitor.visitChildren(self)




    def for_initializer(self):

        localctx = MiniLangParser.For_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_initializer)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.declaration()
                pass
            elif token in [15, 17, 18, 19, 20, 21, 22, 31, 35, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.expression_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_iteratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(MiniLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_for_iterator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_iterator" ):
                listener.enterFor_iterator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_iterator" ):
                listener.exitFor_iterator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_iterator" ):
                return visitor.visitFor_iterator(self)
            else:
                return visitor.visitChildren(self)




    def for_iterator(self):

        localctx = MiniLangParser.For_iteratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_iterator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expression_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniLangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def SEMIC(self):
            return self.getToken(MiniLangParser.SEMIC, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MiniLangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stmt" ):
                return visitor.visitPrint_stmt(self)
            else:
                return visitor.visitChildren(self)




    def print_stmt(self):

        localctx = MiniLangParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiniLangParser.PRINT)
            self.state = 137
            self.match(MiniLangParser.LPAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 311393419264) != 0):
                self.state = 138
                self.expression_list()


            self.state = 141
            self.match(MiniLangParser.RPAREN)
            self.state = 142
            self.match(MiniLangParser.SEMIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = MiniLangParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expression()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 145
                self.match(MiniLangParser.COMMA)
                self.state = 146
                self.expression()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def SEMIC(self):
            return self.getToken(MiniLangParser.SEMIC, 0)

        def CONST(self):
            return self.getToken(MiniLangParser.CONST, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 152
                self.match(MiniLangParser.CONST)


            self.state = 155
            self.type_()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 156
                self.match(MiniLangParser.LBRACK)
                self.state = 157
                self.match(MiniLangParser.RBRACK)


            self.state = 160
            self.match(MiniLangParser.ID)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 161
                self.match(MiniLangParser.ASSIGN)
                self.state = 162
                self.expression()


            self.state = 165
            self.match(MiniLangParser.SEMIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniLangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def BOOL(self):
            return self.getToken(MiniLangParser.BOOL, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 23552) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def SEMIC(self):
            return self.getToken(MiniLangParser.SEMIC, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniLangParser.ID)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 170
                self.match(MiniLangParser.LBRACK)
                self.state = 171
                self.expression()
                self.state = 172
                self.match(MiniLangParser.RBRACK)


            self.state = 176
            self.match(MiniLangParser.ASSIGN)
            self.state = 177
            self.expression()
            self.state = 178
            self.match(MiniLangParser.SEMIC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_or(self):
            return self.getTypedRuleContext(MiniLangParser.Logical_orContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.logical_or()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.Logical_andContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.Logical_andContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.OR)
            else:
                return self.getToken(MiniLangParser.OR, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_logical_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_or" ):
                listener.enterLogical_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_or" ):
                listener.exitLogical_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_or" ):
                return visitor.visitLogical_or(self)
            else:
                return visitor.visitChildren(self)




    def logical_or(self):

        localctx = MiniLangParser.Logical_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logical_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.logical_and()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 183
                self.match(MiniLangParser.OR)
                self.state = 184
                self.logical_and()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.EqualityContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.AND)
            else:
                return self.getToken(MiniLangParser.AND, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_logical_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_and" ):
                listener.enterLogical_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_and" ):
                listener.exitLogical_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and" ):
                return visitor.visitLogical_and(self)
            else:
                return visitor.visitChildren(self)




    def logical_and(self):

        localctx = MiniLangParser.Logical_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logical_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.equality()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 191
                self.match(MiniLangParser.AND)
                self.state = 192
                self.equality()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ComparisonContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.EQ)
            else:
                return self.getToken(MiniLangParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEQ)
            else:
                return self.getToken(MiniLangParser.NEQ, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = MiniLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.comparison()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.comparison()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ArithmeticContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LT)
            else:
                return self.getToken(MiniLangParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LTE)
            else:
                return self.getToken(MiniLangParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.GT)
            else:
                return self.getToken(MiniLangParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.GTE)
            else:
                return self.getToken(MiniLangParser.GTE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = MiniLangParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.arithmetic()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.arithmetic()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.TermContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.PLUS)
            else:
                return self.getToken(MiniLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MINUS)
            else:
                return self.getToken(MiniLangParser.MINUS, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic(self):

        localctx = MiniLangParser.ArithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arithmetic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.term()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self.term()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.UnaryContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.UnaryContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MULT)
            else:
                return self.getToken(MiniLangParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.DIV)
            else:
                return self.getToken(MiniLangParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MOD)
            else:
                return self.getToken(MiniLangParser.MOD, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniLangParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.unary()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0):
                self.state = 223
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.unary()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MiniLangParser.UnaryContext,0)


        def NOT(self):
            return self.getToken(MiniLangParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniLangParser.MINUS, 0)

        def factor(self):
            return self.getTypedRuleContext(MiniLangParser.FactorContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniLangParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                _la = self._input.LA(1)
                if not(_la==31 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                self.unary()
                pass
            elif token in [15, 17, 18, 19, 20, 21, 22, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def NEW(self):
            return self.getToken(MiniLangParser.NEW, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)

        def DOT(self):
            return self.getToken(MiniLangParser.DOT, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniLangParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MiniLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MiniLangParser.LPAREN)
                self.state = 236
                self.expression()
                self.state = 237
                self.match(MiniLangParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(MiniLangParser.NEW)
                self.state = 240
                self.type_()
                self.state = 241
                self.match(MiniLangParser.LBRACK)
                self.state = 242
                self.expression()
                self.state = 243
                self.match(MiniLangParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(MiniLangParser.ID)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 246
                    self.match(MiniLangParser.DOT)
                    self.state = 247
                    self.match(MiniLangParser.ID)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.match(MiniLangParser.ID)
                self.state = 251
                self.match(MiniLangParser.LBRACK)
                self.state = 252
                self.expression()
                self.state = 253
                self.match(MiniLangParser.RBRACK)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniLangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniLangParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniLangParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniLangParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4063232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





