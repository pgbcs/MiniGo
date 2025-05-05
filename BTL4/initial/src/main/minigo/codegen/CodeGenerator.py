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
        elif type(typ) is ArrayType:
            return ArrayType(typ.dimens, self.getType(typ.eleType))
        return typ

    def getLiteralValue(self, initExpr):
        if type(initExpr) in self.initType:
            if type(initExpr) is BooleanLiteral:
                return "1" if initExpr.value else "0"
            return str(initExpr.value)
        return None

    def generateAllIndices(self, shape):
        result = []

        def backtrack(current: List):
            if len(current) == len(shape):
                result.append(current[:])
                return
            for i in range(shape[len(current)].value):
                current.append(i)
                backtrack(current)
                current.pop()

        backtrack([])
        return result

        

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

    # def emitObjectInit(self, env):
    #     for key in self.emit.keys():
    #         if key in list(map(lambda x: x[0], env['struct'])) or key ==self.className:
    #             frame = Frame("<init>", VoidType())  
    #             self.emit[key].printout(self.emit[key].emitMETHOD("<init>", MType([], VoidType()), False))  # Bắt đầu định nghĩa phương thức <init>
    #             frame.enterScope(True)  
    #             self.emit[key].printout(self.emit[key].emitVAR(frame.getNewIndex(), "this", ClassType(key), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
                
    #             self.emit[key].printout(self.emit[key].emitLABEL(frame.getStartLabel(), frame))
    #             self.emit[key].printout(self.emit[key].emitREADVAR("this", ClassType(key), 0, frame))  
    #             self.emit[key].printout(self.emit[key].emitINVOKESPECIAL(frame))  
            
                
    #             self.emit[key].printout(self.emit[key].emitLABEL(frame.getEndLabel(), frame))
    #             self.emit[key].printout(self.emit[key].emitRETURN(VoidType(), frame))  
    #             self.emit[key].printout(self.emit[key].emitENDMETHOD(frame))  
    #             frame.exitScope() 
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit[self.className].printout(self.emit[self.className].emitMETHOD("<init>", MType([], VoidType()), False))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit[self.className].printout(self.emit[self.className].emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit[self.className].printout(self.emit[self.className].emitLABEL(frame.getStartLabel(), frame))
        self.emit[self.className].printout(self.emit[self.className].emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit[self.className].printout(self.emit[self.className].emitINVOKESPECIAL(frame))  
    
        
        self.emit[self.className].printout(self.emit[self.className].emitLABEL(frame.getEndLabel(), frame))
        self.emit[self.className].printout(self.emit[self.className].emitRETURN(VoidType(), frame))  
        self.emit[self.className].printout(self.emit[self.className].emitENDMETHOD(frame))  
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

        self.emitObjectInit()
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
            # env['inFunc'] = True
            self.visit(ast.body,env)
            self.emit[o['className']].printout(self.emit[o['className']].emitNOP())
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
        if varType is None:
            env = o.copy()
            env['onlyType'] = True
            varType = self.visit(ast.varInit, env)
        if o['turn'] == 2:
            if 'frame' not in o: # global var
                o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
                self.emit[o['className']].printout(self.emit[o['className']].emitATTRIBUTE(ast.varName, varType, True, False, self.getLiteralValue(ast.varInit)))
                if not ast.varInit or not type(ast.varInit) in self.initType: o['globalInit'] = True
            else:
                frame: Frame = o['frame']
                index = frame.getNewIndex()
                o['env'][0].append(Symbol(ast.varName, varType, Index(index)))
                self.emit[o['className']].printout(self.emit[o['className']].emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
                if type(varType) is ArrayType and not ast.varInit:
                    self.emit[o['className']].printout(self.emit[o['className']].emitARRAY(varType.dimens, varType.eleType, frame))
                if ast.varInit:
                    # self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame)) --original code
                    newO = o.copy()
                    newO['isLeft'] = False
                    initCode,initType = self.visit(ast.varInit, newO)
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
                    varInitCode,_ = self.visit(ast.varInit, newO)
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

            #<init>
            frame = Frame("<init>", VoidType())
            self.emit[ast.name].printout(self.emit[ast.name].emitMETHOD("<init>", MType([], VoidType()), False))  # Bắt đầu định nghĩa phương thức <init>
            frame.enterScope(True)  
            self.emit[ast.name].printout(self.emit[ast.name].emitVAR(frame.getNewIndex(), "this", ClassType(ast.name), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
            
            self.emit[ast.name].printout(self.emit[ast.name].emitLABEL(frame.getStartLabel(), frame))
            self.emit[ast.name].printout(self.emit[ast.name].emitREADVAR("this", ClassType(ast.name), 0, frame))  
            self.emit[ast.name].printout(self.emit[ast.name].emitINVOKESPECIAL(frame))  

            # for e in ast.elements:
            #     if 
            
            self.emit[ast.name].printout(self.emit[ast.name].emitLABEL(frame.getEndLabel(), frame))
            self.emit[ast.name].printout(self.emit[ast.name].emitRETURN(VoidType(), frame))  
            self.emit[ast.name].printout(self.emit[ast.name].emitENDMETHOD(frame))  
            frame.exitScope()  


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

    def visitIf(self, ast: If, o):

        frame: Frame = o['frame']
        className = o['className']

        elseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        
        endFlag = True
        env = o.copy()
        env['isLeft'] = False
        self.emit[className].printout(self.visit(ast.expr, env)[0])
        self.emit[className].printout(self.emit[className].emitIFFALSE(elseLabel, frame))
        if not ast.thenStmt is None:
            # if 'inFunc' in o and o['inFunc']:
            #     returnStmt = next(filter(lambda x: type(x) is Return, ast.thenStmt.member), None)
            #     if not returnStmt is None: endFlag = False
            self.visit(ast.thenStmt, o)
        if endFlag: self.emit[className].printout(self.emit[className].emitGOTO(endLabel, frame))
        self.emit[className].printout(self.emit[className].emitLABEL(elseLabel, frame))
        if not ast.elseStmt is None:
            self.visit(ast.elseStmt, o)
        self.emit[className].printout(self.emit[className].emitLABEL(endLabel, frame))
        
        return o

    def visitForBasic(self, ast: ForBasic, o):
        pass
    

    #TODO: what case it is not stmt but still need pop???
    def visitFuncCall(self, ast: FuncCall, o):#TODO: if it is stmt ???
        sym:Symbol = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        if 'onlyType' in o and o['onlyType']: return sym.mtype.rettype
        env = o.copy()
        env['isLeft'] = False
        paramCode = "".join([self.visit(x, env)[0] for x in ast.args])

        funcCallCode = self.emit[o['className']].emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
            
        if 'isLeft' in o and o['isLeft'] ==False:
            return paramCode + funcCallCode, sym.mtype.rettype
        else:
            popCode = self.emit[o['className']].emitPOP(o['frame']) if not type(sym.mtype.rettype) is VoidType else ""
            self.emit[o['className']].printout(paramCode+funcCallCode+popCode)
            return o
    
    def visitMethCall(self, ast: MethCall, o):
        env = o.copy()
        env['isLeft'] = False
        recCode, recType = self.visit(ast.receiver, env)

        thisType = next(filter(lambda x: x[0] == recType.name, o['struct'] + o['interface']), None)
        if len(thisType) == 2: #it is interface
            sym: Symbol = next(filter(lambda x: x.name == ast.metName, thisType[1]),None)
        else:
            sym: Symbol = next(filter(lambda x: x.name == ast.metName, thisType[2]),None)

        if 'onlyType' in o and o['onlyType']: return sym.mtype.rettype

        paramCode = "".join([self.visit(x, env)[0] for x in ast.args])
        methCallCode = self.emit[o['className']].emitINVOKEVIRTUAL(f"{sym.value.value}/{ast.metName}",sym.mtype, o['frame'])

        if 'isLeft' in o and o['isLeft'] ==False:
            return recCode + paramCode + methCallCode, sym.mtype.rettype
        else:
            popCode = self.emit[o['className']].emitPOP(o['frame']) if not type(sym.mtype.rettype) is VoidType else ""
            self.emit[o['className']].printout(recCode + paramCode+methCallCode+popCode)
            return o

    def visitFieldAccess(self, ast: FieldAccess, o):
        env = o.copy()
        env['isLeft'] = False
        recCode,recType = self.visit(ast.receiver, env)

        className = recType.name
        thisStruct = next(filter(lambda x: x[0] == recType.name, o['struct']),None)
        field: Symbol = next(filter(lambda x: x.name == ast.field, thisStruct[1]), None)
        if o['isLeft']:
            return recCode, (field, className)
        else:
            fieldAccessCode =recCode + self.emit[o['className']].emitGETFIELD(
                className+"/"+ast.field,
                field.mtype,
                o['frame'] 
            )
            return fieldAccessCode, field.mtype

    def visitArrayCell(self, ast: ArrayCell, o):
        env = o.copy()
        env['isLeft'] = False

        arrCode, arrType= self.visit(ast.arr, env)

        className = o['className']

        if len(arrType.dimens)>len(ast.idx):
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
        else:
            retType = arrType.eleType
        if 'onlyType' in o and o['onlyType']: return retType
        indexCode = ""
        for index, value in enumerate(ast.idx):
            indexCode+=self.visit(value, env)[0]
            if index != len(ast.idx)-1:
                indexCode+=self.emit[className].emitALOAD(ArrayType(None, None), o['frame']) #only need ArrayType                

        # indexCode = reduce(lambda x,y: x+self.visit(x, env)[0], ast.idx, "")


        if o['isLeft']==True:
            return arrCode+indexCode, retType
        else:
            arrCellCode = self.emit[className].emitREADVAR2(retType, o['frame'])
            return arrCode+indexCode+arrCellCode, retType

    def visitAssign(self, ast: Assign, o):
        env = o.copy() 
        # if type(lhsCode) is tuple:
        #     self.emit[o['className']].printout(lhsCode[0] +rhsCode + lhsCode[1])
        if type(ast.lhs) is FieldAccess:    
            env['isLeft'] = True
            lhsCode, optVal = self.visit(ast.lhs, env)
            env['isLeft'] = False 
            rhsCode, rhsType = self.visit(ast.rhs, env)
            finCode = self.emit[o['className']].emitPUTFIELD(
                optVal[1] + '/'+ optVal[0].name,
                optVal[0].mtype,
                env['frame']
            )
            self.emit[o['className']].printout(lhsCode+rhsCode+finCode)
        elif type(ast.lhs) is ArrayCell:
            env['isLeft'] = True
            lhsCode, optVal = self.visit(ast.lhs, env)
            env['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, env)
            finCode = self.emit[o['className']].emitASTORE(optVal, o['frame'])
            self.emit[o['className']].printout(lhsCode+rhsCode+finCode)
        else:            
            env['isLeft'] = False 
            rhsCode, rhsType = self.visit(ast.rhs, env)
            env['isLeft'] = True
            lhsCode, optVal = self.visit(ast.lhs, env)
            self.emit[o['className']].printout(rhsCode+lhsCode)
        return o

    def visitBinaryOp(self, ast: BinaryOp, o):
        env = o.copy()
        env['isLeft'] = False
        
        className = o['className']
        frame: Frame = o['frame']
        retType =None
        #have many circuit ???
        if ast.op == "&&":
            retType =  BoolType()
            if 'onlyType' in o and o['onlyType']: return retType
            tempFlag = None
            if 'isFirstSCO' in o:
                tempFlag = o['isFirstSCO']
                trueLabel = o['trueLabelO']
                o['isFirstSCO'] = True
            
            if 'isFirstSCA' in o and o['isFirstSCA'] == False:
                falseLabel = o['falseLabelA']
                
                if type(ast.left) is BinaryOp:
                    leftCode = self.visit(ast.left, o.copy())[0]
                else:
                    leftCode = self.visit(ast.left, o.copy())[0]
                    leftCode += self.emit[className].emitIFFALSE(falseLabel, frame)
                
                if type(ast.right) is BinaryOp:
                    rightCode = self.visit(ast.right, o.copy())[0]
                else:
                    rightCode = self.visit(ast.right, o.copy())[0]
                    rightCode += self.emit[className].emitIFFALSE(falseLabel, frame)
            else:
                falseLabel = frame.getNewLabel()
                endLabel = frame.getNewLabel()

                envSC = o.copy()
                envSC['isLeft'] = False
                envSC['isFirstSCA'] = False
                envSC['falseLabelA'] = falseLabel

                if type(ast.left) is BinaryOp:
                    leftCode = self.visit(ast.left, envSC)[0]
                else:
                    envLeft = o.copy()
                    envLeft['isLeft'] = False
                    leftCode = self.visit(ast.left, envLeft)[0]
                    leftCode += self.emit[className].emitIFFALSE(falseLabel, frame)
                
                if type(ast.right) is BinaryOp:
                    #must assign again due to left hand can turn off it
                    envSC['isLeft'] = False
                    envSC['isFirstSCA'] = False
                    envSC['falseLabelA'] = falseLabel
                    rightCode = self.visit(ast.right, envSC)[0]
                else:
                    envRight = o.copy()
                    envRight['isLeft'] = False
                    rightCode = self.visit(ast.right, envRight)[0]
                    rightCode += self.emit[className].emitIFFALSE(falseLabel, frame)

                if tempFlag == False:
                    rightCode+=self.emit[className].emitGOTO(trueLabel, frame)
                    rightCode+=self.emit[className].emitLABEL(falseLabel, frame)
                else:
                    rightCode+=self.emit[className].emitPUSHCONST(1, IntType(), frame)
                    rightCode+=self.emit[className].emitGOTO(endLabel, frame)
                    rightCode+=self.emit[className].emitLABEL(falseLabel, frame)
                    rightCode+=self.emit[className].emitPUSHCONST(0, IntType(), frame)
                    rightCode+=self.emit[className].emitLABEL(endLabel, frame)
        elif ast.op == '||':
            tempFlag = None
            if 'isFirstSCA' in o:
                tempFlag = o['isFirstSCA']
                falseLabel = o['falseLabelA']
                o['isFirstSCA'] = True
            retType =  BoolType()
            if 'onlyType' in o and o['onlyType']: return retType
            if 'isFirstSCO' in o and o['isFirstSCO'] == False:
                trueLabel = o['trueLabelO']
                
                if type(ast.left) is BinaryOp:
                    leftCode = self.visit(ast.left, o.copy())[0]
                else:
                    leftCode = self.visit(ast.left, o.copy())[0]
                    leftCode += self.emit[className].emitIFTRUE(trueLabel, frame)
                
                if type(ast.right) is BinaryOp:
                    rightCode = self.visit(ast.right, o.copy())[0]
                else:
                    rightCode = self.visit(ast.right, o.copy())[0]
                    rightCode += self.emit[className].emitIFTRUE(trueLabel, frame)
            else:
                trueLabel = frame.getNewLabel()
                endLabel = frame.getNewLabel()

                envSC = o.copy()
                envSC['isLeft'] = False
                envSC['isFirstSCO'] = False
                envSC['trueLabelO'] = trueLabel

                if type(ast.left) is BinaryOp:
                    leftCode = self.visit(ast.left, envSC)[0]
                else:
                    envLeft = o.copy()
                    envLeft['isLeft'] = False
                    leftCode = self.visit(ast.left, envLeft)[0]
                    leftCode += self.emit[className].emitIFTRUE(trueLabel, frame)
                
                if type(ast.right) is BinaryOp:
                    envSC['isLeft'] = False
                    envSC['isFirstSCO'] = False
                    envSC['trueLabelO'] = trueLabel
                    rightCode = self.visit(ast.right, envSC)[0]
                else:
                    envRight = o.copy()
                    envRight['isLeft'] = False
                    rightCode = self.visit(ast.right, envRight)[0]
                    rightCode += self.emit[className].emitIFTRUE(trueLabel, frame)
                if tempFlag == False:
                    rightCode+=self.emit[className].emitGOTO(falseLabel , frame)
                    rightCode+=self.emit[className].emitLABEL(trueLabel, frame)
                else:
                    rightCode+=self.emit[className].emitPUSHCONST(0, IntType(), frame)
                    rightCode+=self.emit[className].emitGOTO(endLabel , frame)
                    rightCode+=self.emit[className].emitLABEL(trueLabel, frame)
                    rightCode+=self.emit[className].emitPUSHCONST(1, IntType(), frame)
                    rightCode+=self.emit[className].emitLABEL(endLabel, frame)
        else:
            env['onlyType'] = True
            leftType = self.visit(ast.left, env)
            rightType = self.visit(ast.right, env)

            #need compute retType first
            if ast.op == "+":
                if type(leftType) is type(rightType) and type(leftType) in [StringType, IntType, FloatType]:
                    retType = leftType
                elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                    retType = FloatType()
            elif ast.op in ["-", "*", "/"]:
                if type(leftType) is type(rightType) and type(leftType) in [FloatType, IntType]:
                    retType = leftType
                elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                    retType = FloatType()
            elif ast.op == "%": 
                retType = IntType()
            elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                retType = BoolType()

            if 'onlyType' in o and o['onlyType']: return retType
            env['onlyType'] = False
            if type(leftType) is type(rightType) and type(leftType) is StringType:
                if ast.op == "+":
                    leftCode = self.emit[className].emitSTRINGBUILDER(frame)
                    leftCode += self.emit[className].emitDUP(frame)
                    leftCode += self.visit(ast.left, env)[0]
                    leftCode += self.emit[className].emitINVOKEVIRTUAL("java/lang/StringBuilder/append", MType([StringType()], ClassType("java/lang/StringBuilder")), frame)
                    leftCode += self.emit[className].emitDUP(frame)
                    rightCode = self.visit(ast.right, env)[0]
                    rightCode += self.emit[className].emitINVOKEVIRTUAL("java/lang/StringBuilder/append", MType([StringType()], ClassType("java/lang/StringBuilder")), frame)
                    rightCode += self.emit[className].emitINVOKEVIRTUAL("java/lang/StringBuilder/toString", MType([],  StringType()), frame )
                elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                    leftCode, leftType = self.visit(ast.left, env)
                    rightCode, rightType =self.visit(ast.right, env)
                    if 'isFirstSCA' in o and o['isFirstSCA'] == False:
                        rightCode+=self.emit[className].emitRELOPSTRING1(ast.op, o['falseLabelA'], frame)
                    elif 'isFirstSCO' in o and o['isFirstSCO'] == False:
                        rightCode+=self.emit[className].emitRELOPSTRING2(ast.op, o['trueLabelO'], frame)
                    else: rightCode+=self.emit[className].emitREOPSTRING(ast.op, frame)
            else:
                leftCode, leftType = self.visit(ast.left, env)
                rightCode, rightType =self.visit(ast.right, env)

                if ast.op == "+":
                    if type(leftType) is type(rightType) and type(leftType) in [StringType, IntType, FloatType]:
                        rightCode+=self.emit[className].emitADDOP(ast.op, leftType, frame)
                    elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                        if(type(leftType) is IntType):
                            leftCode+=self.emit[className].emitI2F(frame)
                        else:
                            rightCode+=self.emit[className].emitI2F(frame)
                        rightCode+=self.emit[className].emitADDOP(ast.op, leftType, frame)
                elif ast.op in ["-", "*", "/"]:
                    if type(leftType) is type(rightType) and type(leftType) in [FloatType, IntType]:
                        rightCode+= self.emit[className].emitMULOP(ast.op, leftType, frame)
                    elif not type(leftType) is type(rightType) and type(leftType) in [IntType, FloatType] and type(rightType) in [IntType, FloatType] :
                        if(type(leftType) is IntType):
                            leftCode+=self.emit[className].emitI2F(frame)
                        else:
                            rightCode+=self.emit[className].emitI2F(frame)
                        rightCode+= self.emit[className].emitMULOP(ast.op, leftType, frame)
                elif ast.op == "%": 
                    rightCode+=self.emit[className].emitMOD(frame)
                elif ast.op in ["==", "!=", "<", ">", "<=", ">="]:
                    if 'isFirstSCA' in o and o['isFirstSCA'] == False:
                        rightCode+=self.emit[className].emitRELOP1(ast.op, o['falseLabelA'], frame)
                    elif 'isFirstSCO' in o and o['isFirstSCO'] == False:
                        rightCode+=self.emit[className].emitRELOP2(ast.op, o['trueLabelO'], frame)
                    else: rightCode+=self.emit[className].emitREOP(ast.op, frame)

        return leftCode+rightCode, retType

    def visitUnaryOp(self, ast: UnaryOp, o):
        env = o.copy()
        env['isLeft'] = False
        className = o['className']
        bodyCode, bodyType = self.visit(ast.body, env)

        if 'onlyType' in o and o['onlyType']:
            return bodyType        

        retCode =bodyCode

        if ast.op == "!":
            retCode+=self.emit[className].emitNOT(bodyType, o['frame'])
        elif ast.op =="-":
            retCode+= self.emit[className].emitNEGOP(bodyType)
        
        return retCode, bodyType

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
        env = o.copy()
        env['isLeft'] = False
        retCode = ""
        if ast.expr: retCode, retType = self.visit(ast.expr, env)
        else: retType = VoidType()
        self.emit[o['className']].printout(retCode+self.emit[o['className']].emitRETURN(retType, o['frame']))
        return o
        
    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        eleType = self.getType(ast.eleType)
        retType = ArrayType(ast.dimens, eleType)
        if 'onlyType' in o and o['onlyType']:
            return retType
        className = o['className']
        frame = o['frame']
        
        retCode = self.emit[className].emitARRAY(ast.dimens, eleType, frame)
        indexList = self.generateAllIndices(ast.dimens)
        for index in indexList:
            retCode+= self.emit[className].emitDUP(frame)
            retCode+= self.emit[className].emitWRITEVAR2(index, eleType, frame)
            
            element = reduce(lambda x,y: x[y], index, ast.value)
            env = o.copy()
            env['isLeft'] = False
            valCode, valType = self.visit(element, env)
            retCode+=valCode
            retCode+= self.emit[className].emitASTORE(valType, frame)
        return retCode, retType

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
        
    def visitStructLiteral(self, ast: StructLiteral, o):
        if 'onlyType' in o and o['onlyType']: 
            return ClassType(ast.name)
        className = ast.name
        frame = o['frame']
        insCode =  self.emit[className].emitINSTANCE(ast.name, MType([], VoidType()),o['frame'])
        thisStruct = next(filter(lambda x: x[0] == ast.name, o['struct']),None)
        iniFieldCode = ""
        for e in ast.elements:
            field: Symbol = next(filter(lambda x: x.name == e[0], thisStruct[1]), None)
            iniFieldCode += self.emit[className].emitDUP(frame)
            env = o.copy()
            env['isLeft'] = False
            iniFieldCode += self.visit(e[1], env)[0]
            iniFieldCode += self.emit[className].emitPUTFIELD(className + "/" + e[0], field.mtype, frame)
        return insCode + iniFieldCode, ClassType(ast.name)

    def visitIntLiteral(self, ast: IntLiteral, o):
        if 'onlyType' in o and o['onlyType']: return IntType()
        return self.emit[o['className']].emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        if 'onlyType' in o and o['onlyType']: return FloatType()
        return self.emit[o['className']].emitPUSHCONST(str(ast.value), FloatType(), o['frame']), FloatType()

    def visitStringLiteral(self, ast: StringLiteral, o):
        if 'onlyType' in o and o['onlyType']: return StringType()
        return self.emit[o['className']].emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        if 'onlyType' in o and o['onlyType']: return BoolType()
        return self.emit[o['className']].emitPUSHCONST(str(ast.value).lower(), BoolType(), o['frame']), BoolType()

    def visitNilLiteral(self, ast: NilLiteral, o):
        pass
