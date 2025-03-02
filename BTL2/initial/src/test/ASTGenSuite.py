import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() {};"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """var x int ;"""
        expect = str(Program([VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """func main () {}; var x int ;"""
        expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_scalar_variable_declare1(self):
        input = """var i int;"""
        expect = str(Program([VarDecl("i",IntType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_scalar_variable_declare2(self):
        input = """var i boolean;"""
        expect = str(Program([VarDecl("i",BoolType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    
    def test_scalar_variable_declare3(self):
        input = """var i float;"""
        expect = str(Program([VarDecl("i",FloatType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_scalar_variable_declare4(self):
        input = """var i string;"""
        expect = str(Program([VarDecl("i",StringType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_scalar_variable_declare_with_struct_type(self):
        input = """var i PPL;"""
        expect = str(Program([VarDecl("i",Id("PPL"),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_variable_with_init1(self):
        input = """var i int = 1;"""
        expect = str(Program([VarDecl("i",IntType(),IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_variable_with_init2(self):
        input = """var i boolean = true;"""
        expect = str(Program([VarDecl("i",BoolType(),BooleanLiteral(True))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_variable_with_init3(self):
        input = """var i float = 1.0;"""
        expect = str(Program([VarDecl("i",FloatType(),FloatLiteral(1.0))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_variable_with_init4(self):
        input = """var i string = "hello";"""
        expect = str(Program([VarDecl("i",StringType(),StringLiteral("\"hello\""))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_variable_with_init5(self):
        input = """var i PPL = 1;"""
        expect = str(Program([VarDecl("i",Id("PPL"),IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_variable_with_bin_init(self):
        input = """var i int = 0b1010;"""
        expect = str(Program(
            [
                VarDecl("i",IntType(),IntLiteral(10))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_variable_with_oct_init(self):
        input = """var i int = 0o123;"""
        expect = str(Program(
            [
                VarDecl("i",IntType(),IntLiteral(83))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_variable_with_hex_init(self):
        input = """var i int = 0x123;"""
        expect = str(Program(
            [
                VarDecl("i",IntType(),IntLiteral(291))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_variable_init_without_type(self):
        input = """var i = 1;"""
        expect = str(Program(
            [
                VarDecl("i",None,IntLiteral(1))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_constant_declare1(self):
        input = """const Pi = 1;"""
        expect = str(Program(
            [
                ConstDecl("Pi",None,IntLiteral(1))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_constant_declare2(self):
        input = """const flag = true;"""
        expect = str(Program(
            [
                ConstDecl("flag",None,BooleanLiteral(True))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_constant_declare3(self):
        input = """const Pi = 3 + 14;"""
        expect = str(Program(
            [
                ConstDecl("Pi",None,BinaryOp("+",IntLiteral(3),IntLiteral(14)))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_constant_declare4(self):
        input = """const a = b;"""
        expect = str(Program(
            [
                ConstDecl("a",None,Id("b"))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_array_declare_without_init(self):
        input = """var a[5] int;"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5)],IntType()),None)
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_array_declare_with_many_dim(self):
        input = """var a[5][4][3][2][1] string;"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(1)],StringType()),None)
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_array_declare_with_init(self):
        input = """var a[5] int = [5] int {1,2,3,4,5};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_array_declare_with_init_and_many_dim(self):
        input = """var a [5][5][5] int = [5][5][5]int{
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}      },
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },
        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        },        {
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0},
            {0, 0, 0, 0, 0}        }};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5),IntLiteral(5),IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5),IntLiteral(5),IntLiteral(5)],IntType(),
                [
                    [
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)]
                    ],
                    [
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)]
                    ],
                    [
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)]
                    ],
                    [
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)]
                    ],
                    [
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)],
                        [IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0),IntLiteral(0)]
                    ]
                ]
                ))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_array_declare_with_init_not_enough_element(self):
        input = """var a [5] int = [5] int{1,2,3,4};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_array_declare_with_init_too_much_element(self):
        input = """var a [5] int = [5] int{1,2,3,4,5,6};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(5)],IntType()),ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6)]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    
    def test_array_declare_with_not_match_dim(self):
        input = """var a [1][2] int = [2][1]int{{1},{2}};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(1),IntLiteral(2)],IntType()),ArrayLiteral([IntLiteral(2),IntLiteral(1)],IntType(),[[IntLiteral(1)],[IntLiteral(2)]]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_array_declare_with_enough_dim(self):
        input = """var a [1][2] int = [1]int{1};"""
        expect = str(Program(
            [
                VarDecl("a",ArrayType([IntLiteral(1),IntLiteral(2)],IntType()),ArrayLiteral([IntLiteral(1)],IntType(),[IntLiteral(1)]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_struct_declare(self):
        input = """type PPL struct{
            requisite string;
            min int;
            max int;
            avg float;
            passed boolean;
        };"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType()),
                        ("min",IntType()),
                        ("max",IntType()),
                        ("avg",FloatType()),
                        ("passed",BoolType())
                    ],
                    []
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    # def 
    def test_use_instance_of_struct(self):
        input = """type PPL struct{
            requisite string;
            min int;
            avg float;
            passed boolean;
        };
        var a PPL = PPL{requisite: "Math", min: 5, max: 7.5,passed: true};"""
        expect =str(
            Program(
                [
                    StructType("PPL",
                        [
                            ("requisite",StringType()),
                            ("min",IntType()),
                            ("avg",FloatType()),
                            ("passed",BoolType())
                        ],
                        []
                    ),
                    VarDecl("a",Id("PPL"),StructLiteral("PPL",
                        [
                            ("requisite",StringLiteral("\"Math\"")),
                            ("min",IntLiteral(5)),
                            ("max",FloatLiteral(7.5)),
                            ("passed",BooleanLiteral(True))
                        ]
                    ))
                ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
        
    def test_declare_struct_method(self):
        input = """type PPL struct{
            requisite string;
        };
        func (p PPL) getRequisite() string{
            return p.requisite;
        };"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType())
                    ],[]),
                MethodDecl(
                    "p",
                    Id("PPL"),
                    FuncDecl(
                        "getRequisite",
                        [],
                        StringType(),
                        Block(
                            [
                                Return(FieldAccess(Id("p"),"requisite"))
                            ]
                        )
                    )
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_struct_method_with_param(self):
        input = """type PPL struct{
            requisite string;
        };
        func (p PPL) setRequisite(req, abc string, xyz int){
            return;
        };"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType())
                    ],[]),
                MethodDecl(
                    "p",
                    Id("PPL"),
                    FuncDecl(
                        "setRequisite",
                        [ParamDecl("req",StringType()),ParamDecl("abc",StringType()),ParamDecl("xyz",IntType())],
                        VoidType(),
                        Block(
                            [
                                Return(None)
                            ]
                        )
                    )
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # def test_
    # def test_array_and_struct_access(self):
    #     input = """func main(){
    #         a[0][2].c[3]:=1;
    #     };"""
    #     expect = str(Program(
    #         [
    #             FuncDecl("main",[],VoidType(),Block(
    #                 [
    #                     Assign(ArrayCell(FieldAccess(ArrayCell(Id("a"),[IntLiteral(0), IntLiteral(2)]),"c"),[IntLiteral(3)]),IntLiteral(1))
    #                 ]
    #             ))
    #         ]
    #         ))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))
