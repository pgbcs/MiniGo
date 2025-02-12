# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#normal_vardecl_non_init.
    def visitNormal_vardecl_non_init(self, ctx:MiniGoParser.Normal_vardecl_non_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#normal_vardecl_init.
    def visitNormal_vardecl_init(self, ctx:MiniGoParser.Normal_vardecl_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_vardecl.
    def visitArr_vardecl(self, ctx:MiniGoParser.Arr_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_value.
    def visitList_value(self, ctx:MiniGoParser.List_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fielddecl.
    def visitFielddecl(self, ctx:MiniGoParser.FielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst.
    def visitStructinst(self, ctx:MiniGoParser.StructinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldinstlist.
    def visitFieldinstlist(self, ctx:MiniGoParser.FieldinstlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldinst.
    def visitFieldinst(self, ctx:MiniGoParser.FieldinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methoddecl.
    def visitMethoddecl(self, ctx:MiniGoParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodimple.
    def visitMethodimple(self, ctx:MiniGoParser.MethodimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_list.
    def visitParam_list(self, ctx:MiniGoParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall.
    def visitFunccall(self, ctx:MiniGoParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#actualparam.
    def visitActualparam(self, ctx:MiniGoParser.ActualparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor1.
    def visitFactor1(self, ctx:MiniGoParser.Factor1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor2.
    def visitFactor2(self, ctx:MiniGoParser.Factor2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor3.
    def visitFactor3(self, ctx:MiniGoParser.Factor3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor4.
    def visitFactor4(self, ctx:MiniGoParser.Factor4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor5.
    def visitFactor5(self, ctx:MiniGoParser.Factor5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#factor6.
    def visitFactor6(self, ctx:MiniGoParser.Factor6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var.
    def visitVar(self, ctx:MiniGoParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_dim_acc.
    def visitArr_dim_acc(self, ctx:MiniGoParser.Arr_dim_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_dim.
    def visitArr_dim(self, ctx:MiniGoParser.Arr_dimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#endstmt.
    def visitEndstmt(self, ctx:MiniGoParser.EndstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callstmt.
    def visitCallstmt(self, ctx:MiniGoParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)



del MiniGoParser