"""
 * @author pgbao
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

class StructTyp(DefType):
    def __init__(self, name, fields=[],mtypes=[]):    
        self.name: str=name
        self.fields: List[Symbol]=fields
        self.mtypes: List[Symbol]=mtypes    
    def __str__(self):
        return f"name: {self.name}  fields: {[str(x) for x in self.fields]} mtypes: {[str(x) for x in self.mtypes]}"
class InterfaceTyp(DefType):
    def __init__(self, name, mtypes=[]):
        self.name: str = name
        self.mtypes: List[Symbol] = mtypes

class Props:
    def __init__(self, scope=[], env=[], typ_env=[], turn=1, initflag = {
        "isMethod": False,
        "isCallStmt": False,
        "isConst": False
    }):
        flag = ["isMethod", "isCallStmt", "isConst", "isArrayDim"]
        self.scope: List[Symbol] = scope
        self.env: List[Symbol]= env
        self.typ_env: List[DefType] = typ_env
        self.turn: int= turn
        self.flag = {x: True if initflag.get(x) == True else False for x in flag}
        

class StaticChecker(BaseVisitor,Utils):
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]
        self.prim_type=[IntType, 
                        FloatType, 
                        BoolType, 
                        StringType, 
                        VoidType, 
                        ArrayType, 
                        StructType, 
                        InterfaceType]
        
    def flatten(self, lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(self.flatten(item))
            else:
                flat_list.append(item)
        return flat_list    

    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def checkExist(self, obj, lst, func):
        for x in lst:
            if obj in func(x):
                return x
        return None

    def checkEqualFunc(self, sym1: Symbol, sym2: Symbol):
        if sym1.name != sym2.name:
            return False
        parCmp = zip(sym1.mtype.partype, sym2.mtype.partype)
        return reduce(lambda x,y: x and type(y[0]) is type(y[1]), parCmp, True)

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def reducer(self, acc: Props, ele):#chưa có xử lý cập nhật type mới
        visited = self.visit(ele, acc)
        if visited is None: return acc #đảm bảo cho các turn không cần giá trị đó
        if isinstance(ele, MethodDecl):
            return Props(acc.scope, acc.env, [x if x.name != ele.recType.name
                     else StructTyp(x.name, x.fields, x.mtypes+[visited]) 
                     for x in acc.typ_env],acc.turn)
        elif isinstance(ele, StructType) or isinstance(ele, InterfaceType):
            if isinstance(ele, StructType) and acc.turn == 2:
                return Props(acc.scope, 
                             acc.env,
                             [x if x.name != ele.name 
                              else StructTyp(x.name, visited)
                              for x in acc.typ_env], acc.turn)
            elif isinstance(ele, InterfaceType) and acc.turn ==2:
                return Props(
                    acc.scope, 
                    acc.env,
                    [
                        x if x.name != ele.name
                        else InterfaceTyp(x.name, visited)
                        for x in acc.typ_env
                    ],
                    acc.turn
                )
            return Props(acc.scope, acc.env, acc.typ_env + [visited], acc.turn)

        #Đã đảo ngược env để khi duyệt lấy đúng thứ tự từ trong ra ngoài
        else: return Props([visited]+ acc.scope,[visited]+ acc.env, acc.typ_env,acc.turn)

    def visitProgram(self,ast: Program, c: Props):
        #lambda acc,ele: acc[0] + [self.visit(ele,acc)]
        #need 3 turn 
        #turn 1: check global type_but_not_checkField
        #turn 2: check field in type
        #turn 3: check global func and checkField in struct
        #turn 4: check in block
        firstTurn = reduce(self.reducer, ast.decl,Props())
        #reset global variable
        secondTurn = reduce(self.reducer, ast.decl, Props([],[],firstTurn.typ_env,2))
        thirdTurn =  reduce(self.reducer, ast.decl, Props([],[],secondTurn.typ_env,3))
        global_func = filter(lambda x: type(x.mtype) is MType, thirdTurn.scope)

        fourthTurn = reduce(self.reducer, ast.decl,Props([], list(global_func), thirdTurn.typ_env,4))
        return fourthTurn
    
    def visitVarDecl(self, ast: VarDecl, c: Props):
        #turn 1 và turn 2 chỉ quan tâm đến name:
        res = self.lookup(ast.varName,c.scope + c.typ_env if c.turn != 4 else c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if c.turn == 1:
            return Symbol(ast.varName, ast.varType)
        #check kiểu khai báo của biến có tồn tại không
        #cần xảy ra ở cả turn 2 và turn 3 (do turn 3 có thể xảy ra trong block)
        if type(ast.varType) not in self.prim_type and ast.varType != None:
            res = self.lookup(ast.varType.name, c.typ_env, lambda x: x.name)
            if res is None: 
                # varcheck = self.lookup(type(ast.varType), c.env, lambda x: x.name)
                # if not varcheck is None: raise TypeMismatch(ast)
                raise Undeclared(Identifier(), ast.varType.name)
        if c.turn == 2 or c.turn == 3: 
            return Symbol(ast.varName, ast.varType)
        else:
            if ast.varInit:
                initType = self.visit(ast.varInit, c)
                if ast.varType is None:
                    if type(initType) is VoidType:
                        raise TypeMismatch(ast)
                    ast.varType = initType
                if not type(ast.varType) is type(initType):
                    raise TypeMismatch(ast)
            return Symbol(ast.varName, ast.varType,None)

    def visitConstDecl(self, ast: ConstDecl, c: Props):
        res = self.lookup(ast.conName, c.scope + c.typ_env if c.turn != 4 else c.scope,lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        if c.turn ==4:
            if ast.conType is None:
                (conType, initValue) = self.visit(ast.iniExpr,Props(c.scope, c.env, c.typ_env, c.turn,{"isConst": True}))
            return Symbol(ast.conName, conType, initValue)
        else: return Symbol(ast.conName, ast.conType)

    def visitFuncDecl(self,ast: FuncDecl, c: Props):
        
        #check funcname in its scope
        if c.turn != 4:
            res = self.lookup(ast.name, c.scope if c.flag["isMethod"] else c.scope + c.typ_env , lambda x: x.name)
            if not res is None:
                raise Redeclared(Function(), ast.name)
        if c.turn==1 or c.turn == 2:
            return Symbol(ast.name, MType(None, None))
        #check kiểu trả về của hàm có hợp lệ không (do ko có trường hợp func trong block nên ko check turn 3)
        if c.turn==3:
            #check kiểu trả về có hợp lệ không
            if type(ast.retType) not in self.prim_type+[VoidType]:
                res = self.lookup(ast.retType.name, c.typ_env, lambda x: x.name)
                if res is None: 
                    # varcheck = self.lookup(type(ast.varType), c.env, lambda x: x.name)
                    # if not varcheck is None: raise TypeMismatch(ast)
                    raise Undeclared(Identifier(), ast.retType.name)
            #check kiểu dùng trong param hợp lệ không
            params: Props = reduce(self.reducer, ast.params, Props([],[],c.typ_env))
            parType = [x.mtype for x in params.env]

            return Symbol(ast.name, MType(parType, ast.retType))
        else:
            params = []
            if not c.flag["isMethod"]: 
                thisFunc: Symbol = self.lookup(ast.name, c.env, lambda x: x.name) #lấy hàm để truy xuất bộ param thêm vào env
                #ghép type của param với name đã scan ở turn 2 để nhét vào env
                mp = zip(map(lambda x: x.parName,ast.params), thisFunc.mtype.partype)

                params = reduce(lambda x,y: x + [Symbol(y[0], y[1])], mp, [])
            else:
                p: Props = reduce(self.reducer, ast.params, Props([],[],c.typ_env))
                params = p.scope
            local_env = c.env + params #check param scope
            
            # for l in local_env:
            #     print(str(l))
            #should split c to 2 part: current scope, env
            # print(str(ast))
            # for m in ast.body.member:
            #     print(str(m))
            # print(ast.body.member)
            reduce(self.reducer, ast.body.member, Props([], local_env, c.typ_env, 4))

            returnStmt = next(filter(lambda x: isinstance(x, Return), ast.body.member), None)
            #Lấy hết các return ở trong func (bao gồm cả block) khác
            returnList = ([self.visit(returnStmt, c)] if returnStmt else [])+ [self.visit(x, Props([], local_env, c.typ_env, c.turn, c.flag) ) for x in ast.body.member if type(x) in [If,ForBasic,ForEach,ForStep]]
            returnList = self.flatten(returnList)
            # print(returnList)
            # for r in returnList:
            #     print(r)
            
            if len(returnList) != 0:
                checkSameType = all(type(x) is type(returnList[0]) for x in returnList)
                if not checkSameType: raise TypeMismatch(ast)
                retType = returnList[0]
            else:
                retType = VoidType()
            
            if  not type(retType) is type(ast.retType):
                if type(retType) is StructType and ast.retType is InterfaceType:
                    thisStruct = self.lookup(retType.name, c.typ_env, lambda x: x.name)
                    thisInterface= self.lookup(ast.retType.name, c.typ_env, lambda x: x.name)
                    #kiểm tra số method đã imple đủ chưa
                    if len(thisStruct.mtypes) < len(thisInterface.mtypes):
                        raise TypeMismatch(ast)
                    methCmp = zip(thisStruct.mtypes, thisInterface.mtypes)
                    #kiểm tra đã imple đủ method chưa
                    if not reduce(lambda x,y: x and self.checkEqualFunc(y[0], y[1]), methCmp, True):
                        raise TypeMismatch(ast)
                else: raise TypeMismatch(ast)

                if not (type(retType) is IntType and type(ast.retType) is FloatType):
                    raise TypeMismatch(ast)

            else:
                if type(retType) is StructType and type(ast.retType) is StructType:
                    if retType.name != ast.retType.name:
                        raise TypeMismatch(ast)

            return None#không cần trả về symbol ở turn 3 do đã có ở turn 2 


    def visitParamDecl(self, ast: ParamDecl, c: Props):
        #check xem có trùng tên không
        #check các kiểu dùng hợp lệ không
        #ok thì trả về danh sách kiểu
        res = self.lookup(ast.parName, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        if type(ast.parType) not in self.prim_type:
            res = self.lookup(ast.parType.name, c.typ_env, lambda x: x.name)
            if res is None: 
                # varcheck = self.lookup(type(ast.parType), c.env, lambda x: x.name)
                # if not varcheck is None: raise TypeMismatch(ast)
                raise Undeclared(Identifier(), ast.parType.name)
        return Symbol(ast.parName, ast.parType)   

    def visitMethodDecl(self, ast: MethodDecl, c: Props):
        #turn 1 không đụng
        #turn 2 nạp vào kiểu tương ứng
        #Về Undeclared, cần check xem recType đã tồn tại chưa
        
        #Về Redeclared, cần check xem method này đã được thực hiện chưa, không check trùng tên với những cái khác
        #Theo forum thì receiver khác scope với method nên tên còn thể che được
        if c.turn == 3:
            res = self.lookup(ast.recType.name, c.typ_env, lambda x: x.name)
            if res is None or not type(res) is StructTyp:
                # varcheck = self.lookup(ast.recType, c.env, lambda x: x.name)
                # if not varcheck is None: raise TypeMismatch(ast)
                raise Undeclared(Identifier(), ast.recType.name)
            if type(res) is StructTyp:
                preMethod = self.lookup(ast.fun.name, res.mtypes, lambda x: x.name)
                if not preMethod is None: raise Redeclared(Method(), ast.fun.name)

                checkField = self.lookup(ast.fun.name, res.fields,lambda x: x.name)
                if not checkField is None:
                    raise Redeclared(Method(), ast.fun.name)

            method = self.visit(ast.fun,Props([], c.env, c.typ_env, 3, {
                "isMethod": True
            }))
            return method
        elif c.turn == 4:
            #ở chỗ env cần thêm receiver vào
            method = self.visit(ast.fun,Props([], c.env + [Symbol(ast.receiver, ast.recType)], c.typ_env,4, {
                "isMethod": True
            }))
            return None


    def visitStructType(self, ast: StructType, c: Props):
        #check redeclare name in its scope
        #turn 1 check name và ghi lại,
        #turn 2 check field và bổ sung vào 
        if c.turn==1:
            res = self.lookup(ast.name, c.scope + c.typ_env, lambda x: x.name) #cần check ở cả các type đã khai báo trước đó
            if not res is None:
                raise Redeclared(Type(), ast.name)
            return StructTyp(ast.name)
        elif c.turn == 2:
            #check các field có bị redeclared không
            local_scope = []
            fields = []
            for e in ast.elements:
                fieldname = e[0]
                if fieldname in local_scope: raise Redeclared(Field(),e[0])
                if type(e[1]) not in self.prim_type:
                    res = self.lookup(e[1].name, c.typ_env, lambda x: x.name)
                    if res is None:
                        # if type(e[1]) in local_scope: raise TypeMismatch(ast)
                        raise Undeclared(Identifier(), e[1].name)
                local_scope+=[fieldname]

                fields += [Symbol(fieldname, e[1])]
            
            return fields
        else: return None

    def visitInterfaceType(self, ast: InterfaceType, c: Props):
        #tương tự struct chỉ hoạt động ở turn 1 và 2
        if c.turn==1:
            res = self.lookup(ast.name, c.scope + c.typ_env, lambda x: x.name) #cần check ở cả các type đã khai báo trước đó
            if not res is None:
                raise Redeclared(Type(), ast.name)
            
            return InterfaceTyp(ast.name)
        elif c.turn == 2:
            prototypes = reduce(self.reducer, ast.methods, Props([],[],c.typ_env))
            
            return prototypes.scope
        else: return None

    def visitPrototype(self, ast: Prototype, c: Props):
        res = self.lookup(ast.name, c.scope, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        #kiểm tra kiểu param hợp lý chưa
        for p in ast.params:
            if type(p) not in self.prim_type:
                res = self.lookup(p.name, c.typ_env, lambda x: x.name)
                if res is None:
                    raise Undeclared(Identifier(), p.name)
        
        #kiểm tra kiểu trả về hợp lý chưa
        if type(ast.retType) not in self.prim_type+[VoidType]:
            res = self.lookup(ast.retType.name, c.typ_env, lambda x: x.name)
            if res is None:
                raise Undeclared(Identifier(), ast.retType.name)
        return Symbol(ast.name, ast.params)

    def visitIntLiteral(self,ast: IntLiteral, c: Props):
        if c.flag["isConst"]:
            return IntType(), ast.value
        return IntType()
    
    def visitFloatLiteral(self,ast: FloatLiteral, c: Props):
        if c.flag["isConst"]:
            return FloatType(), ast.value
        return FloatType()
    
    def visitStringLiteral(self, ast: StringLiteral, c: Props):
        if c.flag["isConst"]:
            return StringType(), ast.value
        return StringType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, c: Props):
        if c.flag["isConst"]:
            return BoolType(), ast.value
        return BoolType()
    
    def visitStructLiteral(self, ast: StructLiteral, c: Props):
        #check redeclared in field
        fieldnames = list(map(lambda x: x[0], ast.elements))
        # if len(fieldnames)>0:
        #     checkSameName = all(x != fieldnames[0] for x in fieldnames)
        #     if not checkSameName:
        #         raise TypeMismatch(ast)
        thisStruct: StructTyp = self.lookup(ast.name, c.typ_env, lambda x: x.name)
        if thisStruct is None:
            raise Undeclared(Identifier(), ast.name)
        fieldThisStruct = map(lambda x: x.name, thisStruct.fields)
        
        for f in fieldnames:
            if f not in fieldThisStruct:
                raise TypeMismatch(ast)
        
        if c.flag["isConst"]:
            return StructType(
                ast.name,
                thisStruct.fields
            ), ast.elements

        return StructType(
            ast.name,
            thisStruct.fields
        )

    def visitArrayLiteral(self, ast: ArrayLiteral, c: Props):
        # dimenList = [self.visit(x) for x in ast.dimens]
        #need check id in dimen is const
        if c.flag["isConst"]:
            return ArrayType(
                ast.dimens,
                ast.eleType            
            ), ast.value
        return ArrayType(
                ast.dimens,
                ast.eleType            
            )
    
    def visitFuncCall(self, ast: FuncCall, c:Props):
        paramType = reduce(lambda x,y: x + [self.visit(y)], ast.args, [])
        func:Symbol = self.lookup(ast.funName, c.env, lambda x: x.name if isinstance(x.mtype, MType) else None)
        if func is None:
            raise Undeclared(Function(), ast.funName)
        if len(ast.args)!= len(func.mtype.partype):
            raise TypeMismatch(ast)

        if not c.flag["isCallStmt"]:
            if not isinstance(func.mtype.rettype, VoidType):  raise TypeMismatch(ast)     
        else:
            if isinstance(func.mtype.rettype, VoidType):  raise TypeMismatch(ast)

        paramCmp = zip(paramType, func.mtype.partype)
        if(not reduce(lambda x,y: x and type(y[0]) == type(y[1]) ,paramCmp, True)):
            raise TypeMismatch(ast)
        
        return func.mtype.rettype

    def visitMethodCall(self, ast: MethCall, c: Props):
        #cần check receiver trả về kiểu đúng là struct ko
        #rồi sau đó check kiểu struct đó có tồn tại không
        #rồi check có method dó trong struct đó không
        receiver = self.visit(ast.receiver)
        if not (isinstance(receiver, StructType) or isinstance(receiver, InterfaceType)):
            raise TypeMismatch(ast) 
        
        res = self.lookup(receiver.name, c.typ_env, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), receiver.name)

        methCheck = self.lookup(ast.metName, res.mtypes, lambda x: x.name)
        if methCheck is None:
            raise Undeclared(Method(), ast.metName)
        if len(methCheck.partype)!= len(ast.args):
            raise TypeMismatch(ast)
        
        if not c.flag["isCallStmt"]:
            if not isinstance(methCheck.mtype.rettype, VoidType):  raise TypeMismatch(ast)     
        else:
            if isinstance(methCheck.mtype.rettype, VoidType):  raise TypeMismatch(ast)

        paramType = reduce(lambda x,y: x + [self.visit(y)], ast.args, [])
        paramCmp = zip(paramType, methCheck.mtype.partype)
        if(not reduce(lambda x,y: x and type(y[0]) == type(y[1]) ,paramCmp, True)):
            raise TypeMismatch(ast)
        return methCheck.mtype.rettype
    
    def visitFieldAccess(self, ast: FieldAccess, c: Props):
        #check kiểu của receiver
        receiver = self.visit(ast.receiver)
        if not isinstance(receiver, StructType):
            raise TypeMismatch(ast) 
        
        res = self.lookup(receiver.name, c.typ_env, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), receiver.name)
        
        field = self.lookup(ast.field, res.fields, lambda x: x.name)

        if field is None: 
            raise Undeclared(Field(), ast.field)
        
        return field.mtype


    def visitReturn(self, ast: Return, c: Props):
        if c.turn ==4: return self.visit(ast.expr, Props(
            c.scope,
            c.env,
            c.typ_env,
            c.turn,
            {
                "isCallStmt": True
        }
        )) if ast.expr else VoidType() 
        else: return None 


    def visitAssign(self, ast: Assign, c: Props):
        rhsType = self.visit(ast.rhs, Props(
            c.scope,
            c.env,
            c.typ_env,
            c.turn,
            {
                "isCallStmt": True
        }))
        if isinstance(ast.lhs, Id):
            try: 
                lhsType = self.visit(ast.lhs, c)
            except Undeclared as e:
                if not isinstance(ast.rhs, BinaryOp):
                    return Symbol(ast.lhs.name, rhsType)
                else: raise e
        else: lhsType = self.visit(ast.lhs, c)

        if type(lhsType) is MType or type(rhsType) is MType:
            raise TypeMismatch(ast)
        
        if not type(lhsType) is type(rhsType):
            if (not type(lhsType) is FloatType) and (not type(rhsType) is IntType()):
                if type(lhsType) is InterfaceType and type(rhsType) is StructType:
                    thisStruct = self.lookup(rhsType.name, c.typ_env, lambda x: x.name)
                    thisInterface= self.lookup(lhsType.name, c.typ_env, lambda x: x.name)
                    #kiểm tra số method đã imple đủ chưa
                    if len(thisStruct.mtypes) < len(thisInterface.mtypes):
                        raise TypeMismatch(ast)
                    methCmp = zip(thisStruct.mtypes, thisInterface.mtypes)
                    #kiểm tra đã imple đủ method chưa
                    if not reduce(lambda x,y: x and self.checkEqualFunc(y[0], y[1]), methCmp, True):
                        raise TypeMismatch(ast)
                else: raise TypeMismatch(ast)
            
        else:
            if type(lhsType) is ArrayType:
                if not type(lhsType.eleType) is type(rhsType.eleType): 
                    if (not type(lhsType) is FloatType) and (not type(rhsType) is IntType()):
                        raise TypeMismatch(ast)
                else:
                    if type(lhsType.eleType) is StructType:
                        if lhsType.eleType.name != rhsType.eleType.name: raise TypeMismatch(ast)
                        #TODO:có mảng interface??? có vẻ là không do ko có interface instance
                lhsDim = list(map(lambda x: self.visit(x, Props(c.scope, c.env, c.typ_env, c.turn, {"isConstant": True})), lhsType.dimens))    
                rhsDim = list(map(lambda x: self.visit(x, Props(c.scope, c.env, c.typ_env, c.turn, {"isConstant": True})), rhsType.dimens))
                dimCmp = zip(lhsDim, rhsDim)
                if not (reduce(lambda x,y: x and y[0]==y[1], dimCmp, True)):
                    raise TypeMismatch(ast)
            elif type(lhsType) is StructType:
                if not lhsType.name != rhsType.name:
                    raise TypeMismatch(ast)
        return None


    def visitArrayCell(self, ast: ArrayCell,c: Props):
        arrType: ArrayType = self.visit(ast.arr)
        if not type(arrType) is ArrayType:
            raise TypeMismatch(ast)
        idx = [self.visit(i, Props(
            c.scope,
            c.env,
            c.typ_env,
            c.turn,
            {
                "isCallStmt": True
        })) for i in ast.idx]

        intCheck = reduce(lambda x,y: x and type(y) is IntType(), idx, True)
        if not intCheck:
            raise TypeMismatch(ast)
        
        if len(ast.idx) == len(arrType.dimens): 
            return arrType.eleType
        else: return ArrayType(
            arrType.dimens[len(arrType.dimens)-len(ast.idx):],
            arrType.eleType
        )

    def visitIf(self, ast: If, c: Props):
        if c.turn == 3:
            returnStmt = next(filter(lambda x: isinstance(x, Return), ast.thenStmt.member), None)
            return ([self.visit(returnStmt, c)] if returnStmt else []) + [self.visit(x, Props([], c.env, c.typ_env, c.turn, c.flag)) for x in ast.thenStmt.member if type(x) in [If,ForBasic,ForEach,ForStep]]
        elif c.turn == 4:
            cond = self.visit(ast.expr,c)
            if(not isinstance(cond,BoolType)):
                raise TypeMismatch(ast)
            [self.visit(x,c) for x in ast.thenStmt.member]
            if ast.elseStmt: self.visit(ast.elseStmt, c)

    def visitForBasic(self, ast: ForBasic, c: Props):
        pass

    def visitForEach(self, ast: ForEach, c: Props):
        pass

    def visitForStep(self, ast: ForStep, c: Props):
        pass

    def visitBinaryOp(self, ast: BinaryOp, c: Props):
        pass
    
    def visitUnaryOp(self, ast: UnaryOp, c: Props):
        pass


    def visitId(self,ast: Id,c: Props):
        res = self.lookup(ast.name, c.env, lambda x: x.name)
        if res is None:
            if c.flag["isConst"]: raise Undeclared(Constant(), ast.name)
            raise Undeclared(Identifier(), ast.name)
        if c.flag["isConst"]: return res.value
        return res.mtype
#TODO: khi nào check đến expr thì phải bật meth hay funcall lên
#TODO: thứ tự dùng env có cần theo thứ tự scope không