from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    #program: decllist EOF
    def visitProgram(self,ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))  
    
    #decllist: decl decllist | decl
    def visitDecllist(self,ctx:MiniGoParser.DecllistContext):
        if(ctx.getChildCount() == 1):
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        
    def visitDecl(self,ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitVardecl(self,ctx:MiniGoParser.VardeclContext):
        return self.visit(ctx.getChild(0))
    
    def visitNormal_vardecl(self,ctx:MiniGoParser.Normal_vardeclContext):
        return self.visit(ctx.getChild(0))
    
    def visitNormal_vardecl_without_init(self,ctx:MiniGoParser.Normal_vardecl_without_initContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.typedecl()),None)
    
    def visitNormal_vardecl_with_init(self,ctx:MiniGoParser.Normal_vardecl_with_initContext):
        if(ctx.getChildCount() == 6):
            return VarDecl(ctx.ID().getText(),self.visit(ctx.typedecl()),self.visit(ctx.exp()))
        else:
            return VarDecl(ctx.ID().getText(),None,self.visit(ctx.exp()))
        
    def visitTypedecl(self,ctx:MiniGoParser.TypedeclContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        
    def visitArr_vardecl(self,ctx:MiniGoParser.Arr_vardeclContext):
        return self.visit(ctx.getChild(0))
    
    def visitArr_vardecl_with_init(self,ctx:MiniGoParser.Arr_vardecl_with_initContext):
        if(ctx.getChildCount() == 7):
            return VarDecl(ctx.ID().getText(), ArrayType(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl())), self.visit(ctx.arrliteral()))
        else:
            return VarDecl(ctx.ID().getText(), None, self.visit(ctx.arrliteral()))
    
    def visitArr_vardecl_without_init(self,ctx:MiniGoParser.Arr_vardecl_without_initContext):
        return VarDecl(ctx.ID().getText(),  ArrayType(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl())), None)
    
    def visitArrdimlist(self,ctx:MiniGoParser.ArrdimlistContext):
        return [self.visit(ctx.arrdim())] + self.visit(ctx.arrdimlist()) if ctx.arrdimlist() else [self.visit(ctx.arrdim())]

    def visitArrdim(self,ctx:MiniGoParser.ArrdimContext):
        return IntLiteral(int(ctx.DEC_LIT().getText())) if ctx.DEC_LIT() else Id(ctx.ID().getText())
    
    def visitArrliteral(self, ctx:MiniGoParser.ArrliteralContext):
        return ArrayLiteral(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl()), self.visit(ctx.arrlistvalue()))

    def visitArrlistvalue(self, ctx:MiniGoParser.ArrlistvalueContext):
        return self.visit(ctx.listvalue())
    
    def visitListvalue(self, ctx:MiniGoParser.ListvalueContext):
        return [self.visit(ctx.value_for_arr())] + self.visit(ctx.listvalue()) if ctx.listvalue() else [self.visit(ctx.value_for_arr())]
    
    def visitValue_for_arr(self, ctx:MiniGoParser.Value_for_arrContext):
        return self.visit(ctx.getChild(0))
    
    def visitLiteralvalue_for_arr(self, ctx:MiniGoParser.Literalvalue_for_arrContext):
        if ctx.DEC_LIT():
            return IntLiteral(int(ctx.DEC_LIT().getText()))
        elif ctx.BIN_LIT():
            return IntLiteral(int(ctx.BIN_LIT().getText()[2:],2))
        elif ctx.OCT_LIT():
            return IntLiteral(int(ctx.OCT_LIT().getText()[2:],8))
        elif ctx.HEX_LIT():
            return IntLiteral(int(ctx.HEX_LIT().getText()[2:],16))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.structinst():
            return self.visit(ctx.structinst())

    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))
    
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.structbody()))

    def visitStructbody(self, ctx:MiniGoParser.StructbodyContext):
        return self.visit(ctx.fieldlist())

    def visitFieldlist(self, ctx:MiniGoParser.FieldlistContext):
        return [self.visit(ctx.field())] + self.visit(ctx.fieldlist()) if ctx.fieldlist() else []

    def visitField(self, ctx:MiniGoParser.FieldContext):
        if ctx.arrdimlist():
            return VarDecl(ctx.ID().getText(), ArrayType(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl())), None)
        else: return (ctx.ID().getText(), self.visit(ctx.typedecl()))
    
    def visitStructinst(self, ctx:MiniGoParser.StructinstContext):
        return StructLiteral(ctx.ID().getText(), self.visit(ctx.structinst_body()))
    
    def visitStructinst_body(self, ctx:MiniGoParser.Structinst_bodyContext):
        return self.visit(ctx.structinst_fieldlist())

    def visitStructinst_fieldlist(self, ctx:MiniGoParser.Structinst_fieldlistContext):
        return self.visit(ctx.structinst_fieldprime()) if ctx.getChildCount() == 1 else []

    def visitStructinst_fieldprime(self, ctx:MiniGoParser.Structinst_fieldprimeContext):
        return [self.visit(ctx.structinst_field())] + self.visit(ctx.structinst_fieldprime()) if ctx.structinst_fieldprime() else [self.visit(ctx.structinst_field())]

    def visitStructinst_field(self, ctx:MiniGoParser.Structinst_fieldContext):
        return (ctx.ID().getText(), self.visit(ctx.expr()))

    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.interfacebody()))

    def visitInterfacebody(self, ctx:MiniGoParser.InterfacebodyContext):
        return self.visit(ctx.methodlist())

    def visitMethodlist(self, ctx:MiniGoParser.MethodlistContext):
        return [self.visit(ctx.method())] + self.visit(ctx.methodlist()) if ctx.methodlist() else []

    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        flatten_paramlist = [x.varType for x in self.visit(ctx.paramlist())]
        return Prototype(ctx.ID().getText(), flatten_paramlist, self.visit(ctx.returntype())) if ctx.returntype() else Prototype(ctx.ID().getText(), flatten_paramlist, VoidType())

    def visitFundecl(self, ctx:MiniGoParser.FuncdeclContext):
        flatten_paramlist = self.visit(ctx.paramlist())
        if ctx.returntype():
            return FuncDecl(ctx.ID().getText(), flatten_paramlist, self.visit(ctx.returntype()), self.visit(ctx.funcbody()))
        else:
            return FuncDecl(ctx.ID().getText(), flatten_paramlist, VoidType(), self.visit(ctx.funcbody()))

    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        paramlist = self.visit(ctx.param_group_prime()) if ctx.param_group_prime() else []
        return [param for sublist in paramlist for param in sublist]

    
    def visitParam_group_prime(self, ctx:MiniGoParser.Param_group_primeContext):
        return [self.visit(ctx.param_group())] + self.visit(ctx.param_group_prime()) if ctx.param_group_prime() else [self.visit(ctx.param_group())]

    def visitParam_group(self, ctx:MiniGoParser.Param_groupContext):
        if ctx.arrdimlist():
            varList = self.visit(ctx.param_mem_list())
            return [VarDecl(var, ArrayType(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl())), None) for var in varList]
        else:
            return [VarDecl(var, self.visit(ctx.typedecl()), None) for var in varList]

    def visitParam_mem_list(self, ctx:MiniGoParser.Param_mem_listContext):
        return [ctx.ID().getText()] + self.visit(ctx.param_mem_list()) if ctx.param_mem_list() else [ctx.ID().getText()]

    def visitFuncbody(self, ctx:MiniGoParser.FuncbodyContext):
        return Block(self.visit(ctx.stmtlist()))
    
    def visitStmtlist(self, ctx:MiniGoParser.StmtlistContext):
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist()) if ctx.stmtlist() else []
    
    def visitReturntype(self, ctx:MiniGoParser.ReturntypeContext):
        if ctx.arrdimlist():
            return ArrayType(self.visit(ctx.arrdimlist()), self.visit(ctx.typedecl()))
        else: return self.visit(ctx.typedecl())

    def visitMethodimple(self, ctx:MiniGoParser.MethodimpleContext):
        paramlist = self.visit(ctx.paramlist())
        fundecl = FuncDecl(
            ctx.ID(2).getText(),
            paramlist,
            self.visit(ctx.returntype()) if ctx.returntype() else VoidType(),
            self.visit(ctx.methodimple_body())
        )
        return MethodDecl(ctx.ID(0).getText(),StructType(ctx.ID(1).getText()) ,fundecl)
    
    def visitMethodimple_body(self, ctx):
        return self.visit(ctx.stmtlist())
    
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expr()), self.visit(ctx.expr0()))
        
    def visitExpr0(self, ctx:MiniGoParser.Expr0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expr0()), self.visit(ctx.expr1()))

    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr4()))
    
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount()==3:
            return FieldAccess(self.visit(ctx.expr5()), ctx.ID().getText())
        elif ctx.getChildCount()==4:
            return ArrayCell(self.visit(ctx.expr5()), self.visit(ctx.expr()))
        




    # def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
    #     if ctx.getChildCount() == 1:
    #         return self.visit(ctx.getChild(0))
    #     else:
    #         return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr5()), self.visit(ctx.expr6()))




#need check:
# method in struct???
#need check interface decl 
#recType???
#method call and field access and array cell nested

