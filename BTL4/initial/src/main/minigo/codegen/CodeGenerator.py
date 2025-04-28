'''
 *   @author Pham Gia Bao
 *   @version 1.0
 *   28/4/2025
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.initType = [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral]

    def getType(self, typ: Type):
        if type(typ) is Id:
            return ClassType(typ.name)
        return typ

    def getLiteralValue(self, initExpr):
        if type(initExpr) in self.initType:
            if type(initExpr) is BooleanLiteral:
                return "1" if initExpr.value else "0"
            return str(initExpr.value)
        return None


    #dont have to use it because in this case jasmin already have default value
    def genDefaultValue(self, name, typ, o, isGlobal, **kwargs):
        defaultVal = None
        if type(typ) in [IntType, BoolType]:
            defaultVal = "0"
        elif type(typ) is FloatType:
            defaultVal = "0.0"            

        if defaultVal:
            self.emit.printout(self.emit.emitPUSHCONST(defaultVal, typ, o['frame']))
        else:
            return


        if isGlobal:
            self.emit.printout(self.emit.emitPUTSTATIC(kwargs['className'] + '/' + name, typ, o['frame']))
        else:
            self.emit.printout(self.emit.emitWRITEVAR(name, typ, kwargs['index'],  o['frame']))
    # def emitInitValueLocal(self, initExpr, o):
    #     if type()

    #need add more built-in function
    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()),CName("io",True)),
            Symbol("putIntLn", MType([IntType()], VoidType()),CName("io",True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True))
            ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)        

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast: Program, c):
        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        #need divide round
        #round1: fill env with global func
        env['turn'] = 1
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        finalTurnEnv = env.copy()
        #round2: gen code in block
        env['turn'] = 2
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)

        #handle init value global variable
        if 'globalInit' in env:
            if env['globalInit']:
                frame = Frame("<clinit>", VoidType())
                finalTurnEnv['frame'] = frame
                finalTurnEnv['turn'] = 3
                self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
                frame.enterScope(True)
                self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
                reduce(lambda a,x: self.visit(x,a), ast.decl, finalTurnEnv)
                self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
                self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
                self.emit.printout(self.emit.emitENDMETHOD(frame))  
                frame.exitScope()

        self.emitObjectInit()
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitFuncDecl(self, ast: FuncDecl, o):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        if o['turn'] == 1:
            o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
            return o
        if o['turn'] == 2:
            env = o.copy()
            env['frame'] = frame
            self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
            frame.enterScope(True)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            env['env'] = [[]] + env['env']
            if isMain:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            else:
                env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
            self.visit(ast.body,env)
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            if type(ast.retType) is VoidType:
                self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()
            return o
        return o
    
    def visitParamDecl(self, ast: ParamDecl, o):
        frame: Frame = o['frame']
        index = frame.getNewIndex()
        parType = self.getType(ast.parType)
        paramCode = self.emit.emitVAR(
            index,
            ast.parName,
            parType,
            frame.getStartLabel(),
            frame.getEndLabel(),
            frame
        )
        o['env'][0].append(
            Symbol(ast.parName, parType, Index(index))
        )
        self.emit.printout(paramCode)
        return o

    def visitVarDecl(self, ast: VarDecl, o):#need modify value init
        varType = self.getType(ast.varType)
        if o['turn'] == 2:
            if 'frame' not in o: # global var
                o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
                self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, self.getLiteralValue(ast.varInit)))
                if not ast.varInit or not type(ast.varInit) in self.initType: o['globalInit'] = True
            else:
                frame: Frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
                if ast.varInit:
                    # self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame)) --original code
                    newO = o.copy()
                    newO['isLeft'] = False
                    initCode,_ = self.visit(ast.varInit, newO)
                    self.emit.printout(initCode)
                    self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index,  frame))
                else:
                    self.genDefaultValue(ast.varName, ast.varType, o, False, index=index)

        if o['turn'] == 3:
            frame: Frame = o['frame']
            if ast.varInit:
                if not type(ast.varInit) in self.initType:
                    newO = o.copy()
                    newO['isLeft'] = False #not change directly due to can affect on higher layer?!
                    varInitCode, varType = self.visit(ast.varInit, newO)
                    self.emit.printout(varInitCode)
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + '/' + ast.varName, varType, frame))
            else:
                self.genDefaultValue(ast.varName, ast.varType, o, True, className=self.className)

        return o
    
    def visitConstDecl(self, ast: ConstDecl, o):
        if o['turn'] == 1: return o
        env = o.copy()
        env['isLeft'] = False
        env['onlyType'] = True
        conType = self.visit(ast.iniExpr, env)#need field to compute constant value
        conType = self.getType(conType)
        env['onlyType'] = False
        if o['turn'] == 2:
        #need inference conType
            if 'frame' not in o: #global constant
                o['env'][0].append(Symbol(ast.conName, conType, CName(self.className)))
                self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, 
                                                           conType, 
                                                           True, 
                                                           True, 
                                                           self.getLiteralValue(ast.iniExpr)))
                if not type(ast.iniExpr) in self.initType: o['globalInit'] = True
            else:
                frame: Frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.conName, ast.conType, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, ast.conName, conType, frame.getStartLabel(), frame.getEndLabel(), frame))
                initCode,_ = self.visit(ast.iniExpr, frame)
                self.emit.printout(initCode)
                self.emit.printout(self.emit.emitWRITEVAR(ast.conName, conType, index,  frame))
        elif o['turn'] == 3:
            frame: Frame = o['frame']
            if not type(ast.iniExpr) in self.initType:
                constInitCode, _ = self.visit(ast.iniExpr, env)
                self.emit.printout(constInitCode)
                self.emit.printout(self.emit.emitPUTSTATIC(self.className + '/' + ast.conName, conType, frame))
        return o

    def visitMethodDecl(self, ast: MethodDecl, o):
        pass

    def visitStructType(self, ast: StructType, o):
        pass

    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        env = o.copy()
        env['isLeft'] = False
        [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        return o
    
    def visitBlock(self, ast, o):
        # print("env in visit Block: ",o)
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitReturn(self, ast: Return, o):
        pass

    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']),sym.mtype
        else:         
            return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']),sym.mtype
        
    def visitIntLiteral(self, ast: IntLiteral, o):
        if 'onlyType' in o and o['onlyType']: return IntType()
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        if 'onlyType' in o and o['onlyType']: return FloatType()
        return self.emit.emitPUSHCONST(str(ast.value), FloatType(), o['frame']), FloatType()

    def visitStringLiteral(self, ast: StringLiteral, o):
        if 'onlyType' in o and o['onlyType']: return StringType()
        return self.emit.emitPUSHCONST(ast.value, o['frame']), StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        if 'onlyType' in o and o['onlyType']: return BoolType()
        return self.emit.emitPUSHCONST(str(ast.value).lower(), BoolType(), o['frame']), BoolType()

    def visitNilLiteral(self, ast: NilLiteral, o):
        pass
