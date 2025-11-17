# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#while_stmt.
    def enterWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#while_stmt.
    def exitWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#for_stmt.
    def enterFor_stmt(self, ctx:MiniLangParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#for_stmt.
    def exitFor_stmt(self, ctx:MiniLangParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#for_each_stmt.
    def enterFor_each_stmt(self, ctx:MiniLangParser.For_each_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#for_each_stmt.
    def exitFor_each_stmt(self, ctx:MiniLangParser.For_each_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#for_initializer.
    def enterFor_initializer(self, ctx:MiniLangParser.For_initializerContext):
        pass

    # Exit a parse tree produced by MiniLangParser#for_initializer.
    def exitFor_initializer(self, ctx:MiniLangParser.For_initializerContext):
        pass


    # Enter a parse tree produced by MiniLangParser#for_iterator.
    def enterFor_iterator(self, ctx:MiniLangParser.For_iteratorContext):
        pass

    # Exit a parse tree produced by MiniLangParser#for_iterator.
    def exitFor_iterator(self, ctx:MiniLangParser.For_iteratorContext):
        pass


    # Enter a parse tree produced by MiniLangParser#print_stmt.
    def enterPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#print_stmt.
    def exitPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expression_list.
    def enterExpression_list(self, ctx:MiniLangParser.Expression_listContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expression_list.
    def exitExpression_list(self, ctx:MiniLangParser.Expression_listContext):
        pass


    # Enter a parse tree produced by MiniLangParser#declaration.
    def enterDeclaration(self, ctx:MiniLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniLangParser#declaration.
    def exitDeclaration(self, ctx:MiniLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type.
    def enterType(self, ctx:MiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type.
    def exitType(self, ctx:MiniLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assignment.
    def enterAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assignment.
    def exitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expression.
    def enterExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expression.
    def exitExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#logical_or.
    def enterLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        pass

    # Exit a parse tree produced by MiniLangParser#logical_or.
    def exitLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        pass


    # Enter a parse tree produced by MiniLangParser#logical_and.
    def enterLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        pass

    # Exit a parse tree produced by MiniLangParser#logical_and.
    def exitLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        pass


    # Enter a parse tree produced by MiniLangParser#equality.
    def enterEquality(self, ctx:MiniLangParser.EqualityContext):
        pass

    # Exit a parse tree produced by MiniLangParser#equality.
    def exitEquality(self, ctx:MiniLangParser.EqualityContext):
        pass


    # Enter a parse tree produced by MiniLangParser#comparison.
    def enterComparison(self, ctx:MiniLangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MiniLangParser#comparison.
    def exitComparison(self, ctx:MiniLangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MiniLangParser#arithmetic.
    def enterArithmetic(self, ctx:MiniLangParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by MiniLangParser#arithmetic.
    def exitArithmetic(self, ctx:MiniLangParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by MiniLangParser#term.
    def enterTerm(self, ctx:MiniLangParser.TermContext):
        pass

    # Exit a parse tree produced by MiniLangParser#term.
    def exitTerm(self, ctx:MiniLangParser.TermContext):
        pass


    # Enter a parse tree produced by MiniLangParser#unary.
    def enterUnary(self, ctx:MiniLangParser.UnaryContext):
        pass

    # Exit a parse tree produced by MiniLangParser#unary.
    def exitUnary(self, ctx:MiniLangParser.UnaryContext):
        pass


    # Enter a parse tree produced by MiniLangParser#factor.
    def enterFactor(self, ctx:MiniLangParser.FactorContext):
        pass

    # Exit a parse tree produced by MiniLangParser#factor.
    def exitFactor(self, ctx:MiniLangParser.FactorContext):
        pass


    # Enter a parse tree produced by MiniLangParser#literal.
    def enterLiteral(self, ctx:MiniLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniLangParser#literal.
    def exitLiteral(self, ctx:MiniLangParser.LiteralContext):
        pass



del MiniLangParser