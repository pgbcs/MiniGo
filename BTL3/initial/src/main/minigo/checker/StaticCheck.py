"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

@dataclass
class DefType:
    name: str
    fields: List[Symbol]=[]
    mtypes: List[Symbol]=[]

@dataclass
class Props:
    scope: List[Symbol]=[]
    env: List[Symbol]=[]
    typ_env: List[DefType] = []

class StaticChecker(BaseVisitor,Utils):
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]
    
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def checkExist(self, obj, lst, func):
        for x in lst:
            if obj in func(x):
                return obj
        return None


    def check(self):
        return self.visit(self.ast,self.global_envi)

    def reducer(self, acc: Props, ele):
        visited = self.visit(ele, acc)
        visited = [] if visited is None else visited  
        return Props(acc.scope+[visited], acc.env+[visited])

    def visitProgram(self,ast: Program, c: Props):
        #lambda acc,ele: acc[0] + [self.visit(ele,acc)]
        return reduce(self.reducer, ast.decl,Props())

    def visitVarDecl(self, ast: VarDecl, c: Props):
        res = self.lookup(ast.varName,c.scope , lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if ast.varInit:
            initType = self.visit(ast.varInit, c.env)
            if ast.varType is None:
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType,None)

    def visitConstDecl(self, ast: ConstDecl, c: Props):
        res = self.lookup(ast.conName, c.scope,lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        if ast.conType is None:
            conType = self.visit(ast.iniExpr,c.env)
        return Symbol(ast.conName, ast.conType)

    def visitFuncDecl(self,ast: FuncDecl, c: Props):
        #check funcname in its scope
        res = self.lookup(ast.name, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        local_env = c + [ast.name] + reduce(self.reducer, ast.params, Props())#check param scope
        
        #should split c to 2 part: current scope, env
        reduce(self.reducer, ast.body, Props([], local_env))

        return Symbol(ast.name, MType([], ast.retType))

    def visitParamDecl(self, ast: ParamDecl, c: Props):
        res = self.lookup(ast.parName, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType)

    def visitMethodDecl(self, ast: MethodDecl, c: Props):
        #Về Undeclared, cần check xem recType đã tồn tại chưa
        
        #Về Redeclared, cần check xem method này đã được thực hiện chưa
        res = self.checkExist(ast.recType, c.typ_env, lambda x: x.mtypes) 
        if not res is None:
            raise Redeclared(Method(), ast.fun.name)
        
        method = self.visit(ast.fun) #check method body

        #Thêm method này vào danh sách method của kiểu tương ứng
        c.typ_env = [x if x.name != ast.recType 
                    else DefType(x.name, x.fields, x.mtypes+[method]) 
                    for x in c.typ_env]
        return None


    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitId(self,ast,c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
