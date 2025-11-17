# Generated from grammar/MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#statement.
    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniLangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#while_stmt.
    def visitWhile_stmt(self, ctx:MiniLangParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MiniLangParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniLangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#for_each_stmt.
    def visitFor_each_stmt(self, ctx:MiniLangParser.For_each_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#for_initializer.
    def visitFor_initializer(self, ctx:MiniLangParser.For_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#for_iterator.
    def visitFor_iterator(self, ctx:MiniLangParser.For_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#print_stmt.
    def visitPrint_stmt(self, ctx:MiniLangParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expression_list.
    def visitExpression_list(self, ctx:MiniLangParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#declaration.
    def visitDeclaration(self, ctx:MiniLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#type.
    def visitType(self, ctx:MiniLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignment.
    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expression.
    def visitExpression(self, ctx:MiniLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#logical_or.
    def visitLogical_or(self, ctx:MiniLangParser.Logical_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#logical_and.
    def visitLogical_and(self, ctx:MiniLangParser.Logical_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#equality.
    def visitEquality(self, ctx:MiniLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#comparison.
    def visitComparison(self, ctx:MiniLangParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#arithmetic.
    def visitArithmetic(self, ctx:MiniLangParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#term.
    def visitTerm(self, ctx:MiniLangParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#unary.
    def visitUnary(self, ctx:MiniLangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#factor.
    def visitFactor(self, ctx:MiniLangParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#literal.
    def visitLiteral(self, ctx:MiniLangParser.LiteralContext):
        return self.visitChildren(ctx)



del MiniLangParser