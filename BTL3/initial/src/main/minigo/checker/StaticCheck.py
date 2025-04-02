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

class DefType:
    __metaclass__= ABCMeta
    pass

class StructType(DefType):
    def __init__(self, name, fields=[],mtypes=[]):    
        self.name: str=name
        self.fields: List[Symbol]=fields
        self.mtypes: List[Symbol]=mtypes    

class InterfaceType(DefType):
    def __init__(self, name, mtypes=[]):
        self.name: str = name
        self.mtypes: List[Symbol]=mtypes

class Props:
    def __init__(self, scope=[], env=[], typ_env=[], turn=1):
        self.scope: List[Symbol] = scope
        self.env: List[Symbol]= env
        self.typ_env: List[DefType] = typ_env
        self.turn: int= turn

class StaticChecker(BaseVisitor,Utils):
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]
        self.prim_type=["IntType", 
                        "FloatType", 
                        "BoolType", 
                        "StringType", 
                        "VoidType", 
                        "ArrayType", 
                        "StructType", 
                        "InterfaceType"]
    
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

    def reducer(self, acc: Props, ele):#chưa có xử lý cập nhật type mới
        visited = self.visit(ele, acc)
        if visited is None: return acc #đảm bảo cho các turn không cần giá trị đó
        if isinstance(ele, MethodDecl):
            return Props(acc.scope,acc.env, [x if x.name != ele.recType 
                     else DefType(x.name, x.fields, x.mtypes+[visited]) 
                     for x in acc.typ_env])
        else: return Props(acc.scope+[visited], acc.env+[visited])

    def visitProgram(self,ast: Program, c: Props):
        #lambda acc,ele: acc[0] + [self.visit(ele,acc)]
        #need 3 turn 
        #turn 1: check global type
        #turn 2: check global func
        #turn 3: check in block
        firstTurn = reduce(self.reducer, ast.decl,Props())
        #reset global variable


        return reduce(self.reducer, ast.decl,Props())

    def visitVarDecl(self, ast: VarDecl, c: Props):
        #turn 1 và turn 2 chỉ quan tâm đến name:
        res = self.lookup(ast.varName,c.scope , lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if c.turn == 1:
            return Symbol(ast.varName, ast.varType)
        #check kiểu khai báo của biến có tồn tại không
        #cần xảy ra ở cả turn 2 và turn 3 (do turn 3 có thể xảy ra trong block)
        res = self.lookup(type(ast.varType), c.typ_env, lambda x: x.name)
        if res is None and type(ast.varType) not in self.prim_type: 
            varcheck = self.lookup(type(ast.varType), c.env, lambda x: x.name)
            if not varcheck is None: raise TypeMismatch(ast)
            raise Undeclared(Identifier(), type(ast.varType))
        if c.turn == 2: 
            return Symbol(ast.varName, ast.varType)
        else:
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
        if c.turn == 3:
            if ast.conType is None:
                conType = self.visit(ast.iniExpr,c.env)
            return Symbol(ast.conName, ast.conType)
        else: return Symbol(ast.conName, ast.conType)

    def visitFuncDecl(self,ast: FuncDecl, c: Props):
        #check funcname in its scope
        res = self.lookup(ast.name, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        if c.turn==1:
            return Symbol(ast.name, MType(None, None))
        #check kiểu trả về của hàm có hợp lệ không (do ko có trường hợp func trong block nên ko check turn 3)
        if c.turn==2:
            #check kiểu trả về có hợp lệ không
            res = self.lookup(type(ast.retType), c.typ_env, lambda x: x.name)
            if res is None and type(ast.retType) not in self.prim_type: 
                varcheck = self.lookup(type(ast.varType), c.env, lambda x: x.name)
                if not varcheck is None: raise TypeMismatch(ast)
                raise Undeclared(Identifier(), type(ast.retType))
            #check kiểu dùng trong param hợp lệ không
            params: Props = reduce(self.reducer, ast.params, Props([],[],c.typ_env))
            parType = [x.mtype for x in params.env]
            return Symbol(ast.name, MType(parType, ast.retType))
        else:
            thisFunc: Symbol = self.lookup(ast.name, c.env, lambda x: x.name) #lấy hàm để truy xuất bộ param thêm vào env
            #ghép type của param với name đã scan ở turn 2 để nhét vào env
            mp = zip(map(lambda x: x.parName,ast.params), thisFunc.mtype.parType)
            params = reduce(lambda x,y: x + [Symbol(y[0], y[1])], mp, [])
            local_env = c + params #check param scope
            
            #should split c to 2 part: current scope, env
            reduce(self.reducer, ast.body, Props([], local_env))

            return None#không cần trả về symbol ở turn 3 do đã có ở turn 2 


    def visitParamDecl(self, ast: ParamDecl, c: Props):
        #check xem có trùng tên không
        #check các kiểu dùng hợp lệ không
        #ok thì trả về danh sách kiểu
        res = self.lookup(ast.parName, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        res = self.lookup(type(ast.parType), c.typ_env, lambda x: x.name)
        if res is None and type(ast.parType) not in self.prim_type: 
            varcheck = self.lookup(type(ast.parType), c.env, lambda x: x.name)
            if not varcheck is None: raise TypeMismatch(ast)
            raise Undeclared(Identifier(), type(ast.parType))
        return Symbol(ast.parName, ast.parType)   



        return Symbol(ast.parName, ast.parType)

    def visitMethodDecl(self, ast: MethodDecl, c: Props):
        #Về Undeclared, cần check xem recType đã tồn tại chưa
        
        #Về Redeclared, cần check xem method này đã được thực hiện chưa
        res = self.checkExist(ast.recType, c.typ_env, lambda x: x.mtypes) 
        if not res is None:
            raise Redeclared(Method(), ast.fun.name)
        
        method = self.visit(ast.fun,Props([], c.env + [] )) #check method body

        #Thêm method này vào danh sách method của kiểu tương ứng
        # c.typ_env = [x if x.name != ast.recType 
        #             else DefType(x.name, x.fields, x.mtypes+[method]) 
        #             for x in c.typ_env]
        return method

    def visitStructType(self, ast: StructType, c: Props):
        #check redeclare name in its scope
        res = self.lookup(ast.name, c.scope, lambda x: x.name)
        


    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    


    def visitId(self,ast,c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
