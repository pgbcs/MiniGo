from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import JasminCode
from CodeGenError import *


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.jvm = JasminCode()
        self.interface = []

    def getJVMType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "I"
        elif typeIn is FloatType:
            return "F"
        elif typeIn is BoolType:
            return "Z"
        elif typeIn is StringType:
            return "Ljava/lang/String;"
        elif typeIn is VoidType:
            return "V"
        elif typeIn is ArrayType:
            return "["*len(inType.dimens) + self.getJVMType(inType.eleType)
        elif typeIn is MType:
            return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
        elif typeIn is cgen.ClassType or typeIn in [Id, StructType]:
            return "L" + inType.name + ";"
        else:
            return str(typeIn)

    def getFullType(self, inType):
        typeIn = type(inType)
        if typeIn is IntType:
            return "int"
        elif typeIn is FloatType:
            return "float"
        elif typeIn is BoolType:
            return "boolean"
        elif typeIn is cgen.StringType:
            return "java/lang/String"
        elif typeIn in [cgen.ClassType, StructType, Id]:
            return inType.name
        elif typeIn is VoidType:
            return "void"

    def emitPUSHICONST(self, in_, frame):
        #in: Int or Sring
        #frame: Frame
        
        if type(in_) is int:
            frame.push()
            i = in_
            if i >= -1 and i <=5:
                return self.jvm.emitICONST(i)
            elif i >= -128 and i <= 127:
                return self.jvm.emitBIPUSH(i)
            elif i >= -32768 and i <= 32767:
                return self.jvm.emitSIPUSH(i)
        elif type(in_) is str:
            if in_ == "true":
                return self.emitPUSHICONST(1, frame)
            elif in_ == "false":
                return self.emitPUSHICONST(0, frame)
            else:
                return self.emitPUSHICONST(int(in_), frame)

    def emitPUSHFCONST(self, in_, frame):
        #in_: String
        #frame: Frame
        
        f = float(in_)
        frame.push()
        rst = "{0:.4f}".format(f)
        if rst == "0.0" or rst == "1.0" or rst == "2.0":
            return self.jvm.emitFCONST(rst)
        else:
            return self.jvm.emitLDC(in_)           

    ''' 
    *    generate code to push a constant onto the operand stack.
    *    @param in the lexeme of the constant
    *    @param typ the type of the constant
    '''
    def emitPUSHCONST(self, in_, typ, frame):
        #in_: String
        #typ: Type
        #frame: Frame
        
        if type(typ) in [IntType, BoolType]:
            return self.emitPUSHICONST(in_, frame)
        elif type(typ) is StringType:
            frame.push()
            return self.jvm.emitLDC(in_)
        elif type(typ) is FloatType:
            return self.emitPUSHFCONST(in_, frame)
        else:
            raise IllegalOperandException(in_)

    ##############################################################

    def emitALOAD(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()#????
        if type(in_) is IntType:
            return self.jvm.emitIALOAD()
        elif type(in_) is FloatType:
            return self.jvm.emitFALOAD()
        elif type(in_) is BoolType:
            return self.jvm.emitBALOAD()
        elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
            return self.jvm.emitAALOAD()
        else:
            raise IllegalOperandException(str(in_))

    def emitASTORE(self, in_, frame):
        #in_: Type
        #frame: Frame
        #..., arrayref, index, value -> ...
        
        frame.pop()
        frame.pop()
        frame.pop()
        if type(in_) is IntType:
            return self.jvm.emitIASTORE()
        elif type(in_) is FloatType:
            return self.jvm.emitFASTORE()
        elif type(in_) is BoolType:
            return self.jvm.emitBASTORE()
        elif type(in_) is cgen.ArrayType or type(in_) is cgen.ClassType or type(in_) is StringType:
            return self.jvm.emitAASTORE()
        else:
            raise IllegalOperandException(str(in_))

    '''    generate the var directive for a local variable.
    *   @param in the index of the local variable.
    *   @param varName the name of the local variable.
    *   @param inType the type of the local variable.
    *   @param fromLabel the starting label of the scope where the variable is active.
    *   @param toLabel the ending label  of the scope where the variable is active.
    '''
    def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
        #in_: Int
        #varName: String
        #inType: Type
        #fromLabel: Int
        #toLabel: Int
        #frame: Frame
        
        return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

    def emitREADVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #... -> ..., value
        
        frame.push()
        if type(inType) in [IntType, BoolType]:
            return self.jvm.emitILOAD(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFLOAD(index)
        elif type(inType) is cgen.ArrayType or type(inType) is cgen.ClassType or type(inType) is StringType:
            return self.jvm.emitALOAD(index)
        else:
            # print(inType)
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *
    '''
    def emitREADVAR2(self, typ, frame):
        #name: String
        #typ: Type
        #frame: Frame
        #... -> ..., value

        # frame.pop()
        return self.emitALOAD(typ, frame)


    '''
    *   generate code to pop a value on top of the operand stack and store it to a block-scoped variable.
    *   @param name the symbol entry of the variable.
    '''
    def emitWRITEVAR(self, name, inType, index, frame):
        #name: String
        #inType: Type
        #index: Int
        #frame: Frame
        #..., value -> ...
        
        frame.pop()

        if type(inType) in [IntType, BoolType]:
            return self.jvm.emitISTORE(index)
        elif type(inType) is FloatType:
            return self.jvm.emitFSTORE(index)
        elif type(inType) is cgen.ArrayType or type(inType) is cgen.ClassType or type(inType) is StringType:
            return self.jvm.emitASTORE(index)
        else:
            raise IllegalOperandException(name)

    ''' generate the second instruction for array cell access
    *   indices is tuple store index list: [1,2,3]->(1, 2, 3)
    '''
    def emitWRITEVAR2(self, indices, typ, frame): #old version: emitWRITEVAR2(self, name, indices, typ, frame)
        #name: String
        #typ: Type
        #frame: Frame
        #..., value -> ...

        result= ""

        for index, value in enumerate(indices):
            if index == len(indices)-1:
                result+=self.emitPUSHCONST(value, IntType(), frame)
            else:
                result+=self.emitPUSHCONST(value, IntType(), frame)
                result+=self.emitALOAD(ArrayType(None, None), frame)
        
        return result

        #frame.push()
        # raise IllegalOperandException(name)

    ''' generate the field (static) directive for a class mutable or immutable attribute.
    *   @param lexeme the name of the attribute.
    *   @param in the type of the attribute.
    *   @param isFinal true in case of constant; false otherwise
    '''
    def emitATTRIBUTE(self, lexeme, in_, isStatic, isFinal, value):
        #lexeme: String
        #in_: Type
        #isFinal: Boolean
        #value: String
        if isStatic:
            return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), isFinal, value)
        else:
            return self.jvm.emitINSTANCEFIELD(lexeme, self.getJVMType(in_), isFinal, value)

    def emitGETSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.push()
        return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

    def emitPUTSTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        
        frame.pop()
        return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

    def emitGETFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

    def emitPUTFIELD(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        frame.pop()
        frame.pop()
        return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a static method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESTATIC(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        if not type(typ.rettype) is VoidType:
            frame.push()
        return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

    ''' generate code to invoke a special method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name)
    *   @param in the type descriptor of the method.
    '''
    def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
        #lexeme: String
        #in_: Type
        #frame: Frame

        if not lexeme is None and not in_ is None:
            typ = in_
            list(map(lambda x: frame.pop(), typ.partype))
            frame.pop()
            if not type(typ.rettype) is VoidType:
                frame.push()
            return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
        elif lexeme is None and in_ is None:
            frame.pop()
            return self.jvm.emitINVOKESPECIAL()

    ''' generate code to invoke a virtual method
    * @param lexeme the qualified name of the method(i.e., class-name/method-name)
    * @param in the type descriptor of the method.
    '''
    def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))

    '''
    *   generate ineg, fneg.
    *   @param in the type of the operands.
    '''
    def emitNEGOP(self, in_):
        #in_: Type
        #frame: Frame
        #..., value -> ..., result

        if type(in_) is IntType:
            return self.jvm.emitINEG()
        else:
            return self.jvm.emitFNEG()

    def emitNOT(self, in_, frame):
        #in_: Type
        #frame: Frame

        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        result = list()
        result.append(self.emitIFTRUE(label1, frame))
        result.append(self.emitPUSHCONST("true", in_, frame))
        result.append(self.emitGOTO(label2, frame))
        result.append(self.emitLABEL(label1, frame))
        result.append(self.emitPUSHCONST("false", in_, frame))
        result.append(self.emitLABEL(label2, frame))
        return ''.join(result)

    '''
    *   generate iadd, isub, fadd or fsub.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''
    def emitADDOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "+":
            if type(in_) is IntType:
                return self.jvm.emitIADD()
            else:
                return self.jvm.emitFADD()
        else:
            if type(in_) is IntType:
                return self.jvm.emitISUB()
            else:
                return self.jvm.emitFSUB()

    '''
    *   generate imul, idiv, fmul or fdiv.
    *   @param lexeme the lexeme of the operator.
    *   @param in the type of the operands.
    '''

    def emitMULOP(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        frame.pop()
        if lexeme == "*":
            if type(in_) is IntType:
                return self.jvm.emitIMUL()
            else:
                return self.jvm.emitFMUL()
        else:
            if type(in_) is IntType:
                return self.jvm.emitIDIV()
            else:
                return self.jvm.emitFDIV()

    def emitDIV(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIDIV()

    def emitMOD(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIREM()

    '''
    *   generate iand
    '''

    def emitANDOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIAND()

    '''
    *   generate ior
    '''
    def emitOROP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitIOR()

    def emitREOP(self, op, frame):
        #op: String
        #in_: Type
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(labelF))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(labelF))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(labelF))
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)

    def emitRELOP1(self, op, falseLabel, frame):
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPLE(falseLabel))
            # result.append(self.emitGOTO(trueLabel, frame))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPNE(falseLabel))
        # if trueLabel: result.append(self.jvm.emitGOTO(trueLabel, frame))
        return ''.join(result)
    
    def emitRELOP2(self, op, trueLabel, frame):
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()

        frame.pop()
        frame.pop()
        if op == ">":
            result.append(self.jvm.emitIFICMPGT(trueLabel))
            # result.append(self.emitGOTO(trueLabel, frame))
        elif op == ">=":
            result.append(self.jvm.emitIFICMPGE(trueLabel))
        elif op == "<":
            result.append(self.jvm.emitIFICMPLT(trueLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFICMPLE(trueLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFICMPNE(trueLabel))
        elif op == "==":
            result.append(self.jvm.emitIFICMPEQ(trueLabel))
        # if trueLabel: result.append(self.jvm.emitGOTO(trueLabel, frame))
        return ''.join(result)
    '''   generate the method directive for a function.
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''

    def emitREOPSTRING(self, op, frame):
        result = list()
        labelF = frame.getNewLabel()
        labelO = frame.getNewLabel()

        result.append(self.emitINVOKEVIRTUAL("java/lang/String.compareTo", MType([StringType()], IntType()), frame))
        if op == ">":
            # result.append(self.emitINVOKEVIRTUAL("java/lang/String.equals", MType([cgen.ClassType("java/lang/Object")], BoolType())))
            result.append(self.jvm.emitIFLE(labelF))
        elif op == ">=":
            
            result.append(self.jvm.emitIFLT(labelF))
        elif op == "<":
            result.append(self.jvm.emitIFGE(labelF))
        elif op == "<=":
            result.append(self.jvm.emitIFGT(labelF))
        elif op == "!=":
            result.append(self.jvm.emitIFEQ(labelF))
        elif op == "==":
            result.append(self.jvm.emitIFNE(labelF))
        result.append(self.emitPUSHCONST("1", IntType(), frame))
        frame.pop()
        result.append(self.emitGOTO(labelO, frame))
        result.append(self.emitLABEL(labelF, frame))
        result.append(self.emitPUSHCONST("0", IntType(), frame))
        result.append(self.emitLABEL(labelO, frame))
        return ''.join(result)


    def emitRELOPSTRING1(self, op, falseLabel, frame):
        result = list()

        result.append(self.emitINVOKEVIRTUAL("java/lang/String.compareTo", MType([StringType()], IntType()), frame))
        if op == ">":
            result.append(self.jvm.emitIFLE(falseLabel))
            # result.append(self.emitGOTO(trueLabel, frame))
        elif op == ">=":
            result.append(self.jvm.emitIFLT(falseLabel))
        elif op == "<":
            result.append(self.jvm.emitIFGE(falseLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFGT(falseLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFEQ(falseLabel))
        elif op == "==":
            result.append(self.jvm.emitIFNE(falseLabel))
        return ''.join(result)

    def emitRELOPSTRING2(self, op, trueLabel, frame):
        #op: String
        #in_: Type
        #trueLabel: Int
        #falseLabel: Int
        #frame: Frame
        #..., value1, value2 -> ..., result

        result = list()

        result.append(self.emitINVOKEVIRTUAL("java/lang/String.compareTo", MType([StringType()], IntType()), frame))
        if op == ">":
            result.append(self.jvm.emitIFGT(trueLabel))
            # result.append(self.emitGOTO(trueLabel, frame))
        elif op == ">=":
            result.append(self.jvm.emitIFGE(trueLabel))
        elif op == "<":
            result.append(self.jvm.emitIFLT(trueLabel))
        elif op == "<=":
            result.append(self.jvm.emitIFLE(trueLabel))
        elif op == "!=":
            result.append(self.jvm.emitIFNE(trueLabel))
        elif op == "==":
            result.append(self.jvm.emitIFEQ(trueLabel))
        # if trueLabel: result.append(self.jvm.emitGOTO(trueLabel, frame))
        return ''.join(result)

    def emitMETHOD(self, lexeme, in_, isStatic):
        #lexeme: String
        #in_: Type
        #isStatic: Boolean
        #frame: Frame

        return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

    '''   generate the end directive for a function.
    '''
    def emitENDMETHOD(self, frame):
        #frame: Frame

        buffer = list()
        buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
        buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
        buffer.append(self.jvm.emitENDMETHOD())
        return ''.join(buffer)

    def getConst(self, ast):
        #ast: Literal
        if type(ast) is IntLiteral:
            return (str(ast.value), IntType())

    '''   generate code to initialize a local array variable.<p>
    *   @param index the index of the local variable.
    *   @param in the type of the local array variable.
    '''

    '''   generate code to initialize local array variables.
    *   @param in the list of symbol entries corresponding to local array variable.    
    '''

    '''   generate code to jump to label if the value on top of operand stack is true.<p>
    *   ifgt label
    *   @param label the label where the execution continues if the value on top of stack is true.
    '''
    def emitIFTRUE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFGT(label)

    '''
    *   generate code to jump to label if the value on top of operand stack is false.<p>
    *   ifle label
    *   @param label the label where the execution continues if the value on top of stack is false.
    '''
    def emitIFFALSE(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFLE(label)

    def emitIFICMPGT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPGT(label)

    def emitIFICMPLT(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.emitIFICMPLT(label)    

    '''   generate code to duplicate the value on the top of the operand stack.<p>
    *   Stack:<p>
    *   Before: ...,value1<p>
    *   After:  ...,value1,value1<p>
    '''
    def emitDUP(self, frame):
        #frame: Frame

        frame.push()
        return self.jvm.emitDUP()

    def emitPOP(self, frame):
        #frame: Frame

        frame.pop()
        return self.jvm.emitPOP()

    '''   generate code to exchange an integer on top of stack to a floating-point number.
    '''
    def emitI2F(self, frame):
        #frame: Frame

        return self.jvm.emitI2F()

    ''' generate code to return.
    *   <ul>
    *   <li>ireturn if the type is IntegerType or BooleanType
    *   <li>freturn if the type is RealType
    *   <li>return if the type is null
    *   </ul>
    *   @param in the type of the returned expression.
    '''

    def emitRETURN(self, in_, frame):
        #in_: Type
        #frame: Frame

        if type(in_) is IntType:
            frame.pop()
            return self.jvm.emitIRETURN()
        elif type(in_) is FloatType:
            frame.pop()
            return self.jvm.emitFRETURN()
        elif type(in_) is cgen.ClassType or type(in_) is StringType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is ArrayType:
            frame.pop()
            return self.jvm.emitARETURN()
        elif type(in_) is BoolType:
            frame.pop()
            return self.jvm.emitIRETURN()
        
        elif type(in_) is VoidType:
            return self.jvm.emitRETURN()

    ''' generate code that represents a label	
    *   @param label the label
    *   @return code Label<label>:
    '''
    def emitLABEL(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitLABEL(label)

    ''' generate code to jump to a label	
    *   @param label the label
    *   @return code goto Label<label>
    '''
    def emitGOTO(self, label, frame):
        #label: Int
        #frame: Frame

        return self.jvm.emitGOTO(label)

    ''' generate some starting directives for a class.<p>
    *   .source MPC.CLASSNAME.java<p>
    *   .class public MPC.CLASSNAME<p>
    *   .super java/lang/Object<p>
    '''
    def emitPROLOG(self, name, parent):
        #name: String
        #parent: String

        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(self.jvm.emitCLASS("public " + name))
        result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
        return ''.join(result)

    def emitLIMITSTACK(self, num):
        #num: Int

        return self.jvm.emitLIMITSTACK(num)

    def emitLIMITLOCAL(self, num):
        #num: Int

        return self.jvm.emitLIMITLOCAL(num)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        #in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

    #write more
    def emitINTERFACE(self, name, parent=""):
        result = list()
        result.append(self.jvm.emitSOURCE(name + ".java"))
        result.append(".interface public " + name + JasminCode.END)
        result.append(self.jvm.emitSUPER("java/lang/Object" if parent == "" else parent))
        return ''.join(result)
    '''
        use for emit abstract method
    *   @param lexeme the qualified name of the method(i.e., class-name/method-name).
    *   @param in the type descriptor of the method.
    *   @param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
    '''
    def emitAMETHOD(self, lexeme, in_):
        return JasminCode.END + ".method public abstract " + lexeme + self.getJVMType(in_) + JasminCode.END + self.jvm.emitENDMETHOD()
        
    def emitINSTANCE(self, lexeme, in_, frame):
        result=""
        frame.push()
        result+=self.jvm.emitNEW(lexeme)
        result+=self.emitDUP(frame)
        result+=self.emitINVOKESPECIAL(frame, lexeme+"/<init>", in_)
        return result


    def emitARRAY(self, dimens, eleType, frame):
        result = ""
        if len(dimens) == 1:
            inType = type(eleType)
            result+=self.emitPUSHCONST(dimens[0].value, IntType(), frame)
            if inType in [IntType, FloatType, BoolType]:
                result+=self.jvm.emitNEWARRAY(self.getFullType(eleType))
            else:
                result+=self.jvm.emitANEWARRAY(self.getFullType(eleType))
        else:
            result += reduce(lambda x,y: x + self.emitPUSHCONST(y.value, IntType(), frame), dimens, '')
            result+=self.jvm.emitMULTIANEWARRAY(self.getJVMType(ArrayType(dimens, eleType)), str(len(dimens)))
        return result
    
    def emitNOP(self):
        return self.jvm.INDENT + "nop" + self.jvm.END
    # def emitARRAYLITERAL(self, dimens, eleType, values, frame, isFirst=True, currentAccess=None):
    #     result=""
    #     if isFirst: result += self.emitARRAY(dimens, eleType, frame)
    #     if len(dimens)== 1:
    #         if type(eleType) in [IntType, FloatType, BoolType]:
    #             result+=emit

    def emitSTRINGBUILDER(self, frame):
        frame.push()
        result = self.jvm.emitNEW("java/lang/StringBuilder")
        result += self.emitDUP(frame)
        result += self.emitINVOKESPECIAL(frame, "java/lang/StringBuilder/<init>", MType([], VoidType())) 
        return result
    
    def emitPUSHNULL(self, frame):
        frame.push()
        return self.jvm.emitPUSHNULL()
    
    def emitINVOKEINTERFACE(self, lexeme, in_, frame):
        #lexeme: String
        #in_: Type
        #frame: Frame

        typ = in_
        list(map(lambda x: frame.pop(), typ.partype))
        frame.pop()
        if not type(typ) is VoidType:
            frame.push()
        return self.jvm.emitINVOKEINTERFACE(lexeme, self.getJVMType(in_), len(typ.partype)+1)
    

    def emitIMPLEMENT(self, lexeme):
        if lexeme in self.interface:
            return 
        className = self.filename[self.filename.rindex('/')+1:self.filename.rindex('.j')]
        for i, v in enumerate(self.buff):
            if v == f'.source {className}.java\n.class public {className}\n.super java.lang.Object\n':
                self.buff.insert(i+1, self.jvm.emitIMPLEMENTS(lexeme))
                self.interface.append(lexeme)
                break
        return 
    
    def emitIFNULL(self, label, frame):
        #label: Int
        #frame: Frame

        frame.pop()
        return self.jvm.INDENT + "ifnull Label" + str(label) + self.jvm.END