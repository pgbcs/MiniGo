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
        self.emit: dict[str, Emitter] = {} #use for main class
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
            self.emit[o['className']].printout(self.emit[o['className']].emitPUSHCONST(defaultVal, typ, o['frame']))
        else:
            return


        if isGlobal:
            self.emit[o['className']].printout(self.emit[o['className']].emitPUTSTATIC(kwargs['className'] + '/' + name, typ, o['frame']))
        else:
            self.emit[o['className']].printout(self.emit[o['className']].emitWRITEVAR(name, typ, kwargs['index'],  o['frame']))
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
        self.emit[self.className] = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)        

    def emitObjectInit(self, env):
        for key in self.emit.keys():
            if key in list(map(lambda x: x[0], env['struct'])) or key ==self.className:
                frame = Frame("<init>", VoidType())  
                self.emit[key].printout(self.emit[key].emitMETHOD("<init>", MType([], VoidType()), False))  # Bắt đầu định nghĩa phương thức <init>
                frame.enterScope(True)  
                self.emit[key].printout(self.emit[key].emitVAR(frame.getNewIndex(), "this", ClassType(key), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
                
                self.emit[key].printout(self.emit[key].emitLABEL(frame.getStartLabel(), frame))
                self.emit[key].printout(self.emit[key].emitREADVAR("this", ClassType(key), 0, frame))  
                self.emit[key].printout(self.emit[key].emitINVOKESPECIAL(frame))  
            
                
                self.emit[key].printout(self.emit[key].emitLABEL(frame.getEndLabel(), frame))
                self.emit[key].printout(self.emit[key].emitRETURN(VoidType(), frame))  
                self.emit[key].printout(self.emit[key].emitENDMETHOD(frame))  
                frame.exitScope() 

    # def emitAllPROLOG(self):
    #     for key, value in self.emit.items():
    #         value.printout(value.emitPROLOG(key, "java.lang.Object"))

    def emitAllEPILOG(self):
        # try:
            for key, value in self.emit.items():
                value.printout(value.emitEPILOG())
        # except TypeError as R:
        #     for key, value in self.emit.items():
        #         print(f"{key},{value.buff}")
    def visitProgram(self, ast: Program, c):
        env ={}
        env['env'] = [c]
        env['struct'] = []
        env['interface'] = []
        env['className'] = self.className
        self.emit[self.className].printout(self.emit[self.className].emitPROLOG(self.className, "java.lang.Object"))
        # self.emitAllPROLOG()

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
                self.emit[self.className].printout(self.emit[self.className].emitMETHOD("<clinit>", MType([], VoidType()), True))
                frame.enterScope(True)
                self.emit[self.className].printout(self.emit[self.className].emitLABEL(frame.getStartLabel(), frame))
                reduce(lambda a,x: self.visit(x,a), ast.decl, finalTurnEnv)
                self.emit[self.className].printout(self.emit[self.className].emitLABEL(frame.getEndLabel(), frame))
                self.emit[self.className].printout(self.emit[self.className].emitRETURN(VoidType(), frame))  
                self.emit[self.className].printout(self.emit[self.className].emitENDMETHOD(frame))  
                frame.exitScope()

        self.emitObjectInit(env)
        # self.emit[self.className].printout(self.emit[self.className].emitEPILOG())
        self.emitAllEPILOG()
        return env

    def visitFuncDecl(self, ast: FuncDecl, o):
        frame = Frame(o['className'] + "/" + ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: self.getType(x.parType), ast.params)), ast.retType)
        if o['turn'] == 1:
            o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
            return o
        if o['turn'] == 2:
            env = o.copy()
            env['frame'] = frame

            self.emit[o['className']].printout(self.emit[o['className']].emitMETHOD(ast.name, mtype, o['className']==self.className))
            frame.enterScope(True)

           
            env['env'] = [[]] + env['env']
            if isMain and o['className'] == self.className:
                self.emit[o['className']].printout(self.emit[o['className']].emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            else:
                #load this if it is instance method
                if o['className'] != self.className:
                    self.emit[o['className']].printout(self.emit[o['className']].emitVAR(frame.getNewIndex(), "this", ClassType(o['className']), frame.getStartLabel(), frame.getEndLabel(), frame))
                    # self.emit[o['className']].printout(self.emit[o['className']].emitLABEL(frame.getStartLabel(), frame))
                env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
            
            self.emit[o['className']].printout(self.emit[o['className']].emitLABEL(frame.getStartLabel(), frame))
            # if 'isMethod' in env and env['isMethod']:
            #     print(env['frame'])
            self.visit(ast.body,env)
            self.emit[o['className']].printout(self.emit[o['className']].emitLABEL(frame.getEndLabel(), frame))
            if type(ast.retType) is VoidType:
                self.emit[o['className']].printout(self.emit[o['className']].emitRETURN(VoidType(), frame)) 
            self.emit[o['className']].printout(self.emit[o['className']].emitENDMETHOD(frame))
            frame.exitScope()
            return o
        return o
    
    def visitParamDecl(self, ast: ParamDecl, o):
        frame: Frame = o['frame']
        index = frame.getNewIndex()
        parType = self.getType(ast.parType)
        paramCode = self.emit[o['className']].emitVAR(
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
        self.emit[o['className']].printout(paramCode)
        return o

    def visitVarDecl(self, ast: VarDecl, o):#need modify value init
        varType = self.getType(ast.varType)
        if o['turn'] == 2:
            if 'frame' not in o: # global var
                o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
                self.emit[o['className']].printout(self.emit[o['className']].emitATTRIBUTE(ast.varName, varType, True, False, self.getLiteralValue(ast.varInit)))
                if not ast.varInit or not type(ast.varInit) in self.initType: o['globalInit'] = True
            else:
                frame: Frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
                self.emit[o['className']].printout(self.emit[o['className']].emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
                if ast.varInit:
                    # self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame)) --original code
                    newO = o.copy()
                    newO['isLeft'] = False
                    initCode,_ = self.visit(ast.varInit, newO)
                    self.emit[o['className']].printout(initCode)
                    self.emit[o['className']].printout(self.emit[o['className']].emitWRITEVAR(ast.varName, varType, index,  frame))
                else:
                    self.genDefaultValue(ast.varName, ast.varType, o, False, index=index)

        if o['turn'] == 3:
            frame: Frame = o['frame']
            if ast.varInit:
                if not type(ast.varInit) in self.initType:
                    newO = o.copy()
                    newO['isLeft'] = False #not change directly due to can affect on higher layer?!
                    varInitCode, varType = self.visit(ast.varInit, newO)
                    self.emit[o['className']].printout(varInitCode)
                    self.emit[o['className']].printout(self.emit[o['className']].emitPUTSTATIC(self.className + '/' + ast.varName, varType, frame))
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
                self.emit[o['className']].printout(self.emit[o['className']].emitATTRIBUTE(ast.conName, 
                                                           conType, 
                                                           True, 
                                                           True, 
                                                           self.getLiteralValue(ast.iniExpr)))
                if not type(ast.iniExpr) in self.initType: o['globalInit'] = True
            else:
                frame: Frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.conName, ast.conType, Index(index)))
                self.emit[o['className']].printout(self.emit[o['className']].emitVAR(index, ast.conName, conType, frame.getStartLabel(), frame.getEndLabel(), frame))
                initCode,_ = self.visit(ast.iniExpr, frame)
                self.emit[o['className']].printout(initCode)
                self.emit[o['className']].printout(self.emit[o['className']].emitWRITEVAR(ast.conName, conType, index,  frame))
        elif o['turn'] == 3:
            frame: Frame = o['frame']
            if not type(ast.iniExpr) in self.initType:
                constInitCode, _ = self.visit(ast.iniExpr, env)
                self.emit[o['className']].printout(constInitCode)
                self.emit[o['className']].printout(self.emit[o['className']].emitPUTSTATIC(self.className + '/' + ast.conName, conType, frame))
        return o

    def visitMethodDecl(self, ast: MethodDecl, o):
        if o['turn'] == 1:
            mtype = MType(list(map(lambda x: self.getType(x.parType), ast.fun.params)), ast.fun.retType)
            thisStruct = next(filter(lambda x: x[0] == ast.recType.name, o['struct']) ,None)
            thisStruct[2]+=[Symbol(ast.fun.name, mtype, CName(ast.recType.name))]
            return o
        elif o['turn'] == 2:
            env = o.copy()
            env['className'] = ast.recType.name
            env['isMethod'] = True
            env['receiver'] = ast.receiver
            env['env']= [[Symbol(ast.receiver, ClassType(ast.recType.name), Index(0))]]+ env['env']
            self.visit(ast.fun, env)
            return o
        return o

    def visitStructType(self, ast: StructType, o):
        if o['turn'] == 1:
            o['struct'].append([ast.name,[
                Symbol(e[0], self.getType(e[1]), None) for e in ast.elements 
            ],[]])
            self.emit[ast.name] = Emitter(self.path + "/" + ast.name + ".j")
            self.emit[ast.name].printout(self.emit[ast.name].emitPROLOG(ast.name, "java.lang.Object"))
            fieldCode = reduce(
                lambda x, y: x + self.emit[ast.name].emitATTRIBUTE(y[0], self.getType(y[1]), False, False, None),
                ast.elements,"")
            
            self.emit[ast.name].printout(fieldCode)
        return o
    
    def visitInterfaceType(self, ast: InterfaceType, o):
        if o['turn'] == 1:
            self.emit[ast.name] = Emitter(self.path + "/" + ast.name + ".j")
            self.emit[ast.name].printout(self.emit[ast.name].emitINTERFACE(ast.name))
            env = o.copy()
            env['className'] = ast.name
            res = reduce(
                lambda x,y: x +[self.visit(y, env)],
                ast.methods,
                []
            )
            prototypeCode = reduce(lambda x,y: x+y, map(lambda x: x[0], res))
            methodList = list(map(lambda x: x[1], res))
            o['interface'].append([ast.name, methodList])
            self.emit[ast.name].printout(prototypeCode)
        return o

    def visitPrototype(self, ast: Prototype, o):
        mtype = MType(list(map(lambda x: self.getType(x), ast.params)), ast.retType)
        return self.emit[o['className']].emitAMETHOD(ast.name, mtype), Symbol(ast.name, mtype)
        
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        env = o.copy()
        env['isLeft'] = False
        [self.emit[o['className']].printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit[o['className']].printout(self.emit[o['className']].emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        return o
    
    def visitMethCall(self, ast: MethCall, o):
        pass

    def visitFieldAccess(self, ast: FieldAccess, o):
        env = o.copy()
        env['isLeft'] = False
        recCode,recType = self.visit(ast.receiver, env)
        thisStruct = next(filter(lambda x: x[0] == recType.name, o['struct']),None)
        field: Symbol = next(filter(lambda x: x.name == ast.field, thisStruct[1]), None)
        if o['isLeft']:
            fieldAccessCode = recCode + self.emit[o['className']].emitPUTFIELD(
                o['className'] + "/" + ast.field,
                field.mtype,
                o['frame']       
            )
        else:
            fieldAccessCode =recCode + self.emit[o['className']].emitGETFIELD(
                o['className']+"/"+ast.field,
                field.mtype,
                o['frame'] 
            )
        return fieldAccessCode, field.mtype

    def visitAssign(self, ast: Assign, o):
        env = o.copy()
        env['isLeft'] = False
        rhsCode, rhsType = self.visit(ast.rhs, env) 
        env['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, env)
        self.emit[o['className']].printout(rhsCode+lhsCode)
        return o

    def visitBinaryOp(self, ast: BinaryOp, o):
        env = o.copy()
        env['isLeft'] = False
        className = o['className']
        leftCode, leftType = self.visit(ast.left, env)
        rightCode, rightType =self.visit(ast.right, env)

        if ast.op == "+":
            if type(leftType) is type(rightType) and type(leftType) in [StringType, IntType, FloatType]:
                retType = leftType
                rightCode+=self.emit[className].emitADDOP(ast.op, leftType, o['frame'])
            elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                retType = FloatType()
                if(type(leftType) is IntType):
                    leftCode+=self.emit[className].emitI2F(o['frame'])
                else:
                    rightCode+=self.emit[className].emitI2F(o['frame'])
        elif ast.op in ["-", "*", "/"]:
            if type(leftType) is type(rightType) and type(leftType) in [FloatType, IntType]:
                retType = leftType
            elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                retType = FloatType()
        elif ast.op == "%": retType = IntType()
        elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
           retType = BoolType()
        elif ast.op in ["&&", "||"]:
            retType =  BoolType()

        if 'onlyType' in o and o['onlyType']: return retType
        return leftCode+rightCode, retType

    def visitBlock(self, ast, o):
        # print("env in visit Block: ",o)
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit[o['className']].printout(self.emit[o['className']].emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit[o['className']].printout(self.emit[o['className']].emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitReturn(self, ast: Return, o):
        pass

    def visitId(self, ast: Id, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if type(sym.value) is Index:
            if 'receiver' in o and o['receiver'] == sym.name:
                # if o['className'] != self.className:
                #     resCode = self.emit[o['className']].emitREADVAR("this", ClassType(o['className']), 0, o['frame'])
                
                return self.emit[o['className']].emitREADVAR("this", sym.mtype, 0, o['frame']), sym.mtype
            else:
                if o['isLeft']:
                    resCode = self.emit[o['className']].emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']) 
                else:
                    resCode = self.emit[o['className']].emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']) 
                return resCode,sym.mtype
        else:
            if o['isLeft']:
                resCode = self.emit[o['className']].emitPUTSTATIC(f"{o['className']}/{sym.name}", sym.mtype, o['frame'])
            else:
                resCode = self.emit[o['className']].emitGETSTATIC(f"{o['className']}/{sym.name}",sym.mtype,o['frame'])
            return resCode,sym.mtype
            # return self.emit[o['className']].emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']),sym.mtype
        
    def visitIntLiteral(self, ast: IntLiteral, o):
        if 'onlyType' in o and o['onlyType']: return IntType()
        return self.emit[o['className']].emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        if 'onlyType' in o and o['onlyType']: return FloatType()
        return self.emit[o['className']].emitPUSHCONST(str(ast.value), FloatType(), o['frame']), FloatType()

    def visitStringLiteral(self, ast: StringLiteral, o):
        if 'onlyType' in o and o['onlyType']: return StringType()
        return self.emit[o['className']].emitPUSHCONST(ast.value, o['frame']), StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        if 'onlyType' in o and o['onlyType']: return BoolType()
        return self.emit[o['className']].emitPUSHCONST(str(ast.value).lower(), BoolType(), o['frame']), BoolType()

    def visitNilLiteral(self, ast: NilLiteral, o):
        pass
