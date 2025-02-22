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
        
    # def visitTypedecl(self,ctx:MiniGoParser.TypedeclContext):
    #     return self.visit(ctx.getChild(0))
    
    # def visitFuncdecl(self,ctx:MiniGoParser.FuncdeclContext):
    #     return FuncDecl(ctx.ID().getText(),[],VoidType(),Block([]))
    	

    

