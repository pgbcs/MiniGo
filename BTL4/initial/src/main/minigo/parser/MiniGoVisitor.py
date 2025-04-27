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


    # Visit a parse tree produced by MiniGoParser#decllist.
    def visitDecllist(self, ctx:MiniGoParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#normal_vardecl.
    def visitNormal_vardecl(self, ctx:MiniGoParser.Normal_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#normal_vardecl_without_init.
    def visitNormal_vardecl_without_init(self, ctx:MiniGoParser.Normal_vardecl_without_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#normal_vardecl_with_init.
    def visitNormal_vardecl_with_init(self, ctx:MiniGoParser.Normal_vardecl_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_vardecl.
    def visitArr_vardecl(self, ctx:MiniGoParser.Arr_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_vardecl_with_init.
    def visitArr_vardecl_with_init(self, ctx:MiniGoParser.Arr_vardecl_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_vardecl_without_init.
    def visitArr_vardecl_without_init(self, ctx:MiniGoParser.Arr_vardecl_without_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrdimlist.
    def visitArrdimlist(self, ctx:MiniGoParser.ArrdimlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrdim.
    def visitArrdim(self, ctx:MiniGoParser.ArrdimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrliteral.
    def visitArrliteral(self, ctx:MiniGoParser.ArrliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrlistvalue.
    def visitArrlistvalue(self, ctx:MiniGoParser.ArrlistvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listvalue.
    def visitListvalue(self, ctx:MiniGoParser.ListvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value_for_arr.
    def visitValue_for_arr(self, ctx:MiniGoParser.Value_for_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalvalue_for_arr.
    def visitLiteralvalue_for_arr(self, ctx:MiniGoParser.Literalvalue_for_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structbody.
    def visitStructbody(self, ctx:MiniGoParser.StructbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#fieldlist.
    def visitFieldlist(self, ctx:MiniGoParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst.
    def visitStructinst(self, ctx:MiniGoParser.StructinstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst_body.
    def visitStructinst_body(self, ctx:MiniGoParser.Structinst_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst_fieldlist.
    def visitStructinst_fieldlist(self, ctx:MiniGoParser.Structinst_fieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst_fieldprime.
    def visitStructinst_fieldprime(self, ctx:MiniGoParser.Structinst_fieldprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structinst_field.
    def visitStructinst_field(self, ctx:MiniGoParser.Structinst_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacebody.
    def visitInterfacebody(self, ctx:MiniGoParser.InterfacebodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodlist.
    def visitMethodlist(self, ctx:MiniGoParser.MethodlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_group_prime.
    def visitParam_group_prime(self, ctx:MiniGoParser.Param_group_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_group.
    def visitParam_group(self, ctx:MiniGoParser.Param_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_mem_list.
    def visitParam_mem_list(self, ctx:MiniGoParser.Param_mem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcbody.
    def visitFuncbody(self, ctx:MiniGoParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmtlist.
    def visitStmtlist(self, ctx:MiniGoParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returntype.
    def visitReturntype(self, ctx:MiniGoParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodimple.
    def visitMethodimple(self, ctx:MiniGoParser.MethodimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodimple_body.
    def visitMethodimple_body(self, ctx:MiniGoParser.Methodimple_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr0.
    def visitExpr0(self, ctx:MiniGoParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrdimlist_expr.
    def visitArrdimlist_expr(self, ctx:MiniGoParser.Arrdimlist_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrdim_expr.
    def visitArrdim_expr(self, ctx:MiniGoParser.Arrdim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#value.
    def visitValue(self, ctx:MiniGoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#subexpr.
    def visitSubexpr(self, ctx:MiniGoParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalvalue.
    def visitLiteralvalue(self, ctx:MiniGoParser.LiteralvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall.
    def visitFunccall(self, ctx:MiniGoParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arglist.
    def visitArglist(self, ctx:MiniGoParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argprime.
    def visitArgprime(self, ctx:MiniGoParser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcallbody.
    def visitMethodcallbody(self, ctx:MiniGoParser.MethodcallbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcalltail.
    def visitMethodcalltail(self, ctx:MiniGoParser.MethodcalltailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#accesslist.
    def visitAccesslist(self, ctx:MiniGoParser.AccesslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#otherassignop.
    def visitOtherassignop(self, ctx:MiniGoParser.OtherassignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callstmt.
    def visitCallstmt(self, ctx:MiniGoParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#firstifstmt.
    def visitFirstifstmt(self, ctx:MiniGoParser.FirstifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmtbody.
    def visitIfstmtbody(self, ctx:MiniGoParser.IfstmtbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseifstmtlist.
    def visitElseifstmtlist(self, ctx:MiniGoParser.ElseifstmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elseifstmt.
    def visitElseifstmt(self, ctx:MiniGoParser.ElseifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elsestmt.
    def visitElsestmt(self, ctx:MiniGoParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicforstmt.
    def visitBasicforstmt(self, ctx:MiniGoParser.BasicforstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmtbody.
    def visitForstmtbody(self, ctx:MiniGoParser.ForstmtbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_cond_update_forstmt.
    def visitInit_cond_update_forstmt(self, ctx:MiniGoParser.Init_cond_update_forstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_for.
    def visitInit_for(self, ctx:MiniGoParser.Init_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign.
    def visitAssign(self, ctx:MiniGoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rangeforstmt.
    def visitRangeforstmt(self, ctx:MiniGoParser.RangeforstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)



del MiniGoParser