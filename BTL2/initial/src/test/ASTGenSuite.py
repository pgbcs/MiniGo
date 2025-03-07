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
                VarDecl("i",IntType(),IntLiteral("0b1010"))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_variable_with_oct_init(self):
        input = """var i int = 0o123;"""
        expect = str(Program(
            [
                VarDecl("i",IntType(),IntLiteral("0o123"))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_variable_with_hex_init(self):
        input = """var i int = 0x123;"""
        expect = str(Program(
            [
                VarDecl("i",IntType(),IntLiteral("0x123"))
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

    def test_call_method_of_struct(self):
        input= """type PPL struct{
            requisite string;
        };
        func (p PPL) getRequisite() string{
            return p.requisite;
        };
        func main(){
            var a PPL = PPL{requisite: "Math"};
            a.getRequisite();
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
                ),
                FuncDecl("main",[],VoidType(),Block(
                    [
                        VarDecl("a",Id("PPL"),StructLiteral("PPL",[("requisite",StringLiteral("\"Math\""))])),
                        MethCall(Id("a"),"getRequisite",[])
                    ]
                ))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_struct_declare_with_array_field(self):
        input = """type PPL struct{
            requisite string;
            min [5] int;
            max [5][5] float;
            passed boolean;
        };"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType()),
                        ("min",ArrayType([IntLiteral(5)],IntType())),
                        ("max",ArrayType([IntLiteral(5),IntLiteral(5)],FloatType())),
                        ("passed",BoolType())
                    ],[]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_struct_literal_with_array(self):
        input = """type PPL struct{
            requisite string;
            min [5] int;
            max [5][5] float;
            passed boolean;
        };
        var a PPL = PPL{requisite: "Math", min: [5] int{1,2,3,4,5}, max: [5][5] float{{1.0, 2.0, 3.0, 4.0, 5.0},{6.0, 7.0, 8.0, 9.0, 10.0},{11.0, 12.0, 13.0, 14.0, 15.0},{16.0, 17.0, 18.0, 19.0, 20.0},{21.0, 22.0, 23.0, 24.0, 25.0}}, passed: true};"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType()),
                        ("min",ArrayType([IntLiteral(5)],IntType())),
                        ("max",ArrayType([IntLiteral(5),IntLiteral(5)],FloatType())),
                        ("passed",BoolType())
                    ],[]
                ),
                VarDecl("a",Id("PPL"),StructLiteral("PPL",
                    [
                        ("requisite",StringLiteral("\"Math\"")),
                        ("min",ArrayLiteral([IntLiteral(5)],IntType(),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),
                        ("max",ArrayLiteral([IntLiteral(5),IntLiteral(5)],FloatType(),[[FloatLiteral(1.0),FloatLiteral(2.0),FloatLiteral(3.0),FloatLiteral(4.0),FloatLiteral(5.0)],[FloatLiteral(6.0),FloatLiteral(7.0),FloatLiteral(8.0),FloatLiteral(9.0),FloatLiteral(10.0)],[FloatLiteral(11.0),FloatLiteral(12.0),FloatLiteral(13.0),FloatLiteral(14.0),FloatLiteral(15.0)],[FloatLiteral(16.0),FloatLiteral(17.0),FloatLiteral(18.0),FloatLiteral(19.0),FloatLiteral(20.0)],[FloatLiteral(21.0),FloatLiteral(22.0),FloatLiteral(23.0),FloatLiteral(24.0),FloatLiteral(25.0)]])),
                        ("passed",BooleanLiteral(True))
                    ]
                ))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_struct_declare_with_struct_field(self):
        input = """type PPL struct{
            requisite string;
            min [5] int;
            max [5][5] float;
            passed boolean;
            student Student;
        };
        type Student struct{
            name string;
            age int;
            gpa float;
        };"""
        expect = str(Program(
            [
                StructType("PPL",
                    [
                        ("requisite",StringType()),
                        ("min",ArrayType([IntLiteral(5)],IntType())),
                        ("max",ArrayType([IntLiteral(5),IntLiteral(5)],FloatType())),
                        ("passed",BoolType()),
                        ("student",Id("Student"))
                    ],[]
                ),
                StructType("Student",
                    [
                        ("name",StringType()),
                        ("age",IntType()),
                        ("gpa",FloatType())
                    ],[]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_interface_declare(self):
        input = """type PPL interface{
            getRequisite() string;
            setRequisite(req string);
        };"""
        expect = str(Program(
            [
                InterfaceType("PPL",
                    [
                        Prototype("getRequisite",[],StringType()),
                        Prototype("setRequisite",[StringType()],VoidType())
                    ]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_interface_decl1(self):
        input = """type Calculator interface {
Add(x, y int) int;
Subtract(a, b float, c int) float;
Reset()
SayHello(name string)
};"""
        expect = str(Program(
            [
                InterfaceType("Calculator",
                    [
                        Prototype("Add",[IntType(),IntType()],IntType()),
                        Prototype("Subtract",[FloatType(),FloatType(),IntType()],FloatType()),
                        Prototype("Reset",[],VoidType()),
                        Prototype("SayHello",[StringType()],VoidType())
                    ]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_interface_decl_with_more_return_type(self):
        input = """type Cool interface {
            a(b,c,d,e boolean) complex128;
            z(x float32, y float64) complex64;
            m();
        };"""
        expect = str(Program(
            [
                InterfaceType("Cool",
                    [
                        Prototype("a",[BoolType(),BoolType(),BoolType(),BoolType()],Id("complex128")),
                        Prototype("z",[Id("float32"),Id("float64")],Id("complex64")),
                        Prototype("m",[],VoidType())
                    ]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_interface_decl_with_array_param(self):
        input = """type Cool interface {
            a(b,c,d,e [5] boolean) complex128;
            z(x [5] float32, y [5] float64) complex64;
            m();
        };"""
        expect = str(Program(
            [
                InterfaceType("Cool",
                    [
                        Prototype("a",[
                            ArrayType([IntLiteral(5)],BoolType()),
                            ArrayType([IntLiteral(5)],BoolType()),
                            ArrayType([IntLiteral(5)],BoolType()),
                            ArrayType([IntLiteral(5)],BoolType())
                        ],Id("complex128")),
                        Prototype("z",[
                            ArrayType([IntLiteral(5)],Id("float32")),
                            ArrayType([IntLiteral(5)],Id("float64"))
                        ],Id("complex64")),
                        Prototype("m",[],VoidType())
                    ]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_interface_declare_with_array_return_type(self):
        input = """type Cool interface {
            a(b,c,d,e boolean) [5] complex128;
            z(x float32, y float64) [5] complex64;
            m();
        };"""
        expect = str(Program(
            [
                InterfaceType("Cool",
                    [
                        Prototype("a",[BoolType(),BoolType(),BoolType(),BoolType()],ArrayType([IntLiteral(5)],Id("complex128"))),
                        Prototype("z",[Id("float32"),Id("float64")],ArrayType([IntLiteral(5)],Id("complex64"))),
                        Prototype("m",[],VoidType())
                    ]
                )
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_function_declare_simple(self):
        input ="""func J97(){};"""
        expect = str(Program(
            [
                FuncDecl("J97",[],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_function_declare_with_simple_param(self):
        input = """func J97(x int){};"""
        expect = str(Program(
            [
                FuncDecl("J97",[ParamDecl("x",IntType())],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_function_declare_with_many_param1(self):
        input = """func J97(x int, y float, z string){};"""
        expect = str(Program(
            [
                FuncDecl("J97",
                         [ParamDecl("x",IntType()),
                          ParamDecl("y",FloatType()),
                          ParamDecl("z",StringType())],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_function_declare_with_many_param2(self):
        input = """func vitinhtu(x,y boolean, sol float, x string){};"""
        expect = str(Program(    
            [
                FuncDecl("vitinhtu",
                         [ParamDecl("x",BoolType()),
                          ParamDecl("y",BoolType()),
                          ParamDecl("sol",FloatType()),
                          ParamDecl("x",StringType())],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    
    def test_function_declare_with_array_param(self):
        input = """func vitinhtu(x [5] int, y [5] float, z [5] string){};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",
                         [ParamDecl("x",ArrayType([IntLiteral(5)],IntType())),
                          ParamDecl("y",ArrayType([IntLiteral(5)],FloatType())),
                          ParamDecl("z",ArrayType([IntLiteral(5)],StringType()))],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_function_declare_with_struct_param(self):
        input = """func vitinhtu(x PPL, y Student){};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",
                         [ParamDecl("x",Id("PPL")),
                          ParamDecl("y",Id("Student"))],VoidType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,347)) 

    def test_function_declare_with_array_return_type(self):
        input = """func vitinhtu() [5] int{};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",[],ArrayType([IntLiteral(5)],IntType()),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_function_declare_with_struct_return_type(self):
        input = """func vitinhtu() PPL{};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",[],Id("PPL"),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_function_declare_with_primitive_return_type(self):
        input = """func vitinhtu() int{};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",[],IntType(),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_function_declare_with_param_and_return_type(self):
        input = """func vitinhtu(x int, y float) [2][3]oh{};"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",
                         [ParamDecl("x",IntType()),
                          ParamDecl("y",FloatType())],
                         ArrayType([IntLiteral(2),IntLiteral(3)],Id("oh")),Block([]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_function_declare_with_simple_body(self):
        input = """func vitinhtu(x int, y float) [2][3]oh{
            return x + y;
        };"""
        expect = str(Program(
            [
                FuncDecl("vitinhtu",
                         [ParamDecl("x",IntType()),
                          ParamDecl("y",FloatType())],
                         ArrayType([IntLiteral(2),IntLiteral(3)],Id("oh")),
                         Block([Return(BinaryOp("+",Id("x"),Id("y")))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_simple_arithmetic_operators1(self):
        input = """func main(){
            a:=1+2;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_simple_arithmetic_operators2(self):
        input = """func main(){
            a:=1-2;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("-",IntLiteral(1),IntLiteral(2)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_simple_arithmetic_operators3(self):
        input = """func main(){
            a:=1*2;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("*",IntLiteral(1),IntLiteral(2)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_simple_arithmetic_operators4(self):
        input = """func main(){
            a:=1/2;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("/",IntLiteral(1),IntLiteral(2)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_simple_arithmetic_operators5(self):
        input = """func main(){
            a:=1%2;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("%",IntLiteral(1),IntLiteral(2)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_precedence_arithmetic_operators1(self):
        input = """func main(){
            a:=1+2+3;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    
    def test_precedence_arithmetic_operators2(self):
        input = """func main(){
            a:=1+2-3;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("-",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_precedence_arithmetic_operators3(self):
        input = """func main(){
            a:=1*2+3;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("+",BinaryOp("*",IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_precedence_arithmetic_operators4(self):
        input = """func main(){
            a:=(1+2)*3;
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType()
                         ,Block([Assign(Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)))]))
            ]
            ))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_precedence_arithmetic_operators5(self):
        input = """func main(){
            x1 := ((-b) + (b*b - 4*a*c)*1/2) / (2*a);
        };"""
        expect = str(Program(
            [
                FuncDecl("main",[],VoidType(),
                         Block([
                            Assign(
                                Id("x1"),
                                BinaryOp(
                                    "/",
                                    BinaryOp(
                                        "+",
                                        UnaryOp(
                                            "-",
                                            Id("b")),
                                        BinaryOp(
                                            "/",
                                            BinaryOp(
                                                "*",
                                                BinaryOp(
                                                    "-",
                                                    BinaryOp(
                                                        "*",
                                                        Id("b"),
                                                        Id("b")),
                                                    BinaryOp(
                                                        "*",
                                                        BinaryOp(
                                                            "*",
                                                            IntLiteral(4),
                                                            Id("a")
                                                        ),
                                                        Id("c")
                                                    )
                                                ),
                                                IntLiteral(1)
                                            ),
                                            IntLiteral(2)
                                        )
                                    ),
                                    BinaryOp(
                                        "*",
                                        IntLiteral(2),
                                        Id("a")
                                    )
                                )
                            )            
                         ])
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_relational_operators1(self):
        input= """func main(){
            bao:= oba == boa;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("bao"),
                                BinaryOp("==",Id("oba"),Id("boa"))
                            )
                        ]
                    )
                )            
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_relational_operators2(self):
        input = """func main(){
            bao:= oba != boa;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("bao"),
                                BinaryOp("!=",Id("oba"),Id("boa"))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_relational_operators3(self):
        input = """func main(){
            var adult = age >18;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "adult",
                                None,
                                BinaryOp(">",Id("age"),IntLiteral(18))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_relational_operators4(self):
        input = """func main(){
            var adult = age <=18;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "adult",
                                None,
                                BinaryOp("<=",Id("age"),IntLiteral(18))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_negation_operators(self):
        input="""func main(){
            var a = !true;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "a",
                                None,
                                UnaryOp("!",BooleanLiteral(True))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_conjunction_operators(self):
        input = """func main(){
            var a = true && false && b ;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "a",
                                None,
                                BinaryOp("&&",BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)),Id("b"))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_disjunction_operators(self):
        input = """func main(){
            var a = true || false || b ;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "a",
                                None,
                                BinaryOp("||",BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),Id("b"))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_boolean_operators1(self):
        input = """func main(){
            uwu:= uwu && uwu || !uwu;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("uwu"),
                                BinaryOp("||",BinaryOp("&&",Id("uwu"),Id("uwu")),UnaryOp("!",Id("uwu")))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_boolean_operators2(self):
        input = """func main(){
            woo := !!foo || !bar && !baz;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("woo"),
                                BinaryOp(
                                    "||",
                                    UnaryOp(
                                        "!",
                                        UnaryOp(
                                            "!",
                                            Id("foo"))),
                                    BinaryOp(
                                        "&&",
                                        UnaryOp(
                                            "!",Id("bar")),
                                            UnaryOp(
                                                "!",Id("baz"))))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_access_array_element(self):
        input = """func main(){
            arr[0]:=3;};"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(Id("arr"),[IntLiteral(0)]),
                                IntLiteral(3)
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    def test_access_array_element_with_expression1(self):
        input = """func main(){
            arr[a+2]:=3;};"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(Id("arr"),[BinaryOp("+",Id("a"),IntLiteral(2))]),
                                IntLiteral(3)
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_access_array_element_with_expression2(self):
        input = """func main(){
            arr[-b-c]:= -b+c
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(Id("arr"),[BinaryOp("-",UnaryOp("-",Id("b")),Id("c"))]),
                                BinaryOp("+",UnaryOp("-",Id("b")),Id("c"))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_array_nested_array_access(self):
        input= """func main(){
            arr[arr[3]+c]:=1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(Id("arr"),[BinaryOp("+",ArrayCell(Id("arr"),[IntLiteral(3)]),Id("c"))]),
                                IntLiteral(1)
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_array_access_with_many_dim(self):
        input = """func main(){
            arr[1][arr[2][3]][2]:= ACID + CIA;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(
                                    Id("arr"),
                                    [
                                        IntLiteral(1),
                                        ArrayCell(
                                            Id("arr"),
                                            [
                                                IntLiteral(2),
                                                IntLiteral(3)]
                                        ),
                                        IntLiteral(2)
                                    ]
                                ),
                                BinaryOp("+",Id("ACID"),Id("CIA"))
                            )
                        ]
                    )
                )
            ]
        ))    
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_struct_access_field(self):
        input = """func main(){
            student.GPA := 4.0;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                FieldAccess(Id("student"),"GPA"),
                                FloatLiteral(4.0)
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    
    def test_struct_deep_access_field(self):
        input = """func main(){
            student.classroom.teacher.name := "Mr. Bean";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                FieldAccess(
                                    FieldAccess(
                                        FieldAccess(Id("student"),"classroom"),
                                        "teacher"),
                                    "name"),
                                StringLiteral("\"Mr. Bean\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))


    def test_struct_access_field_with_array_field(self):
        input ="""func main(){
            car.wheel[0] := "Michelin";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(
                                    FieldAccess(Id("car"),"wheel"),
                                    [IntLiteral(0)]),
                                StringLiteral("\"Michelin\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_struct_access_field_and_array_access1(self):
        input ="""func main(){
            car.wheel[0].brand := "Michelin";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(Id("car"),"wheel"),
                                        [IntLiteral(0)]),
                                    "brand"),
                                StringLiteral("\"Michelin\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_struct_access_field_and_array_access2(self):
        input ="""func main(){
            car.wheel[0][b].brand[1] := "Michelin";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(
                                    FieldAccess(
                                        ArrayCell(
                                            FieldAccess(Id("car"),"wheel"),
                                            [IntLiteral(0), Id("b")]),
                                        "brand"),
                                    [IntLiteral(1)]),
                                StringLiteral("\"Michelin\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_struct_access_field_and_array_access3(self):
        input ="""func main(){
            car[0][f].wheel[0].brand[1] := "Michelin";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(
                                    FieldAccess(
                                        ArrayCell(
                                            FieldAccess(
                                                ArrayCell(
                                                    Id("car"),
                                                    [IntLiteral(0),Id("f")]),
                                                "wheel"),
                                            [IntLiteral(0)]),
                                        "brand"),
                                    [IntLiteral(1)]),
                                StringLiteral("\"Michelin\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_struct_access_field_and_array_access4(self):
        input ="""func main(){
            car[0][f].brand := "Milkita";
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                FieldAccess(
                                    ArrayCell(
                                            Id("car"),
                                            [IntLiteral(0),Id("f")]),
                                    "brand"),
                                StringLiteral("\"Milkita\"")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_variable_declare_with_expression(self):
        input ="""func main(){
            var a int = 4%3+1-1000;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "a",
                                IntType(),
                                BinaryOp(
                                    "-",
                                    BinaryOp(
                                        "+",
                                        BinaryOp(
                                            "%",
                                            IntLiteral(4),
                                            IntLiteral(3)),
                                        IntLiteral(1)),
                                    IntLiteral(1000))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_constant_declare_with_expression(self):
        input ="""func main(){
            const a = 4%3+1-1000;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ConstDecl(
                                "a",
                               None,
                                BinaryOp(
                                    "-",
                                    BinaryOp(
                                        "+",
                                        BinaryOp(
                                            "%",
                                            IntLiteral(4),
                                            IntLiteral(3)),
                                        IntLiteral(1)),
                                    IntLiteral(1000))
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_constant_declare_with_variable(self):
        input ="""func main(){
            const a = (a+b*b)/a*b;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            ConstDecl(
                                "a",
                                None,
                                BinaryOp(
                                    "*",
                                    BinaryOp(
                                        "/",
                                        BinaryOp(
                                            "+",
                                            Id("a"),
                                            BinaryOp(
                                                "*",
                                                Id("b"),
                                                Id("b")
                                            )
                                        ),
                                        Id("a")
                                    ),
                                    Id("b")
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_array_declare_with_constant_size(self):
        input= """func main(){
            var a [MAXINT] int;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            VarDecl(
                                "a",
                                ArrayType([Id("MAXINT")],IntType()),
                                None
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_struct_declare_with_array_field(self):
        input ="""type student struct{
            name string;
            age int;
            scores [5] float;
        };"""
        expect = str(Program(
            [
                StructType(
                    "student",
                    [
                        ("name",StringType()),
                        ("age",IntType()),
                        ("scores",ArrayType([IntLiteral(5)],FloatType()))
                    ],
                    []
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_funtion_call_with_no_param(self):
        input = """func main(){
            print();
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("print",[])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_function_call_with_param(self):
        input = """func main(){
            print("Hello World",1,true,nil);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("print",[StringLiteral("\"Hello World\""),IntLiteral(1),BooleanLiteral(True),NilLiteral()])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    
    def test_function_call_with_expression_param(self):
        input = """func hello(x ,y int, z int){
        }
        func testFunc() {hello(1+2, 3*4 ,5/6);};"""
        expect = str(Program(
            [
                FuncDecl(
                    "hello",
                    [ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],
                    VoidType(),
                    Block([])
                ),
                FuncDecl(
                    "testFunc",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("hello",[BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),IntLiteral(4)),BinaryOp("/",IntLiteral(5),IntLiteral(6))])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_function_call_with_variable_param(self):
        input = """func testFunc() {hello(a, b ,c);};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testFunc",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("hello",[Id("a"),Id("b"),Id("c")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))


    def test_function_call_with_array_param(self):
        input = """func testFunc() {hello(a[0], b[1] ,c[2]);};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testFunc",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("hello",[ArrayCell(Id("a"),[IntLiteral(0)]),ArrayCell(Id("b"),[IntLiteral(1)]),ArrayCell(Id("c"),[IntLiteral(2)])])
                        ]
                    )
                )
            ]
        ))

    def test_function_call_with_struct_param(self):
        input = """func hello(x ,y int, z int){
        }
        func testFunc() {hello(a.b[2], b[2].a ,c.d);};"""
        expect = str(Program(
            [
                FuncDecl(
                    "hello",
                    [ParamDecl("x",IntType()),ParamDecl("y",IntType()),ParamDecl("z",IntType())],
                    VoidType(),
                    Block([])
                ),
                FuncDecl(
                    "testFunc",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("hello",[ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),FieldAccess(ArrayCell(Id("b"),[IntLiteral(2)]),"a"),FieldAccess(Id("c"),"d")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_function_call_with_other_function_call(self):
        input = """func testFunc() {hello(a(), b ,c(d));};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testFunc",
                    [],
                    VoidType(),
                    Block(
                        [
                            FuncCall("hello",[FuncCall("a",[]),Id("b"),FuncCall("c",[Id("d")])])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_method_call_with_no_param(self):
        input = """func main(){
            bruh.okevjp();
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_method_call_with_param(self):
        input = """func main(){
            bruh.okevjp(1,2,3);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[IntLiteral(1),IntLiteral(2),IntLiteral(3)])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_method_call_with_expression_param(self):
        input = """func main(){
            bruh.okevjp(1+2,3*4,5/6);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(
                                Id("bruh"),"okevjp",
                                [
                                    BinaryOp("+",IntLiteral(1),IntLiteral(2)),
                                    BinaryOp("*",IntLiteral(3),IntLiteral(4)),
                                    BinaryOp("/",IntLiteral(5),IntLiteral(6))
                                ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_method_call_with_variable_param(self):
        input = """func main(){
            bruh.okevjp(a,b,c);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[Id("a"),Id("b"),Id("c")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_method_call_with_array_param(self):
        input = """func main(){
            bruh.okevjp(a[0],b[1],c[2]);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[ArrayCell(Id("a"),[IntLiteral(0)]),ArrayCell(Id("b"),[IntLiteral(1)]),ArrayCell(Id("c"),[IntLiteral(2)])])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_method_call_with_struct_param(self):
        input = """func main(){
            bruh.okevjp(a.b[2],b[2].a,c.d);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[ArrayCell(FieldAccess(Id("a"),"b"),[IntLiteral(2)]),FieldAccess(ArrayCell(Id("b"),[IntLiteral(2)]),"a"),FieldAccess(Id("c"),"d")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_method_call_with_other_func_call(self):
        input = """func main(){
            bruh.okevjp(a(),b,c(d));
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[FuncCall("a",[]),Id("b"),FuncCall("c",[Id("d")])])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,401))

    def test_method_call_with_other_method_call(self):
        input = """func main(){
            bruh.okevjp(b.a(),c().d);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(Id("bruh"),"okevjp",[MethCall(Id("b"),"a",[]),FieldAccess(FuncCall("c",[]),"d")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,402))

    def test_complex_expression1(self):
        input ="""func main(){
            a:= b==c || 1+2*3-4/5>d && e<=f;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("a"),
                                BinaryOp(
                                    "||",
                                    BinaryOp(
                                        "==",
                                        Id("b"),
                                        Id("c")
                                    ),
                                    BinaryOp(
                                        "&&",
                                        BinaryOp(
                                            ">",
                                            BinaryOp(
                                                "-",
                                                BinaryOp(
                                                    "+", IntLiteral(1), BinaryOp("*", IntLiteral(2), IntLiteral(3))                   
                                                ),
                                                BinaryOp("/", IntLiteral(4), IntLiteral(5))
                                            ),
                                            Id("d")
                                        ),
                                        BinaryOp(
                                            "<=",
                                            Id("e"),
                                            Id("f")
                                        )
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,403))

    def test_complex_expression2(self):
        input ="""func main(){
            a:= a[2][3].b[4].c[5] % z == 1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("a"),
                                BinaryOp(
                                    "==",
                                    BinaryOp(
                                        "%",
                                        ArrayCell(
                                            FieldAccess(
                                                ArrayCell(
                                                    FieldAccess(
                                                        ArrayCell(
                                                            Id("a"),
                                                            [IntLiteral(2), IntLiteral(3)]),
                                                        "b"),
                                                    [IntLiteral(4)]),
                                                "c"),
                                            [IntLiteral(5)]),
                                        Id("z")),
                                    IntLiteral(1)
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,404))

    def test_complex_expression3(self):
        input="""func main(){
            a:= car.run(speed(50)).position[2].x[3] + 1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("a"),
                                BinaryOp(
                                    "+",
                                    ArrayCell(
                                        FieldAccess(
                                            ArrayCell(
                                               FieldAccess(
                                                   MethCall(
                                                         Id("car"),
                                                         "run",
                                                         [FuncCall("speed",[IntLiteral(50)])],
                                                   ),
                                                   "position"
                                               ),
                                                [IntLiteral(2)]),
                                            "x"),
                                        [IntLiteral(3)]),
                                    IntLiteral(1)
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,405))

    def test_complex_expression4(self):
        input = """func main(){
            a:= !(c.findMax(university.students[2].subject.score)[2] > highestScore);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("a"),
                                UnaryOp(
                                    "!",
                                    BinaryOp(
                                        ">",
                                        ArrayCell(
                                            MethCall(
                                                Id("c"),
                                                "findMax",
                                                [
                                                    FieldAccess(
                                                        FieldAccess(
                                                            ArrayCell(
                                                                FieldAccess(
                                                                    Id("university"),
                                                                    "students"
                                                                ),
                                                                [IntLiteral(2)]
                                                            ),
                                                            "subject"
                                                        ),
                                                        "score"
                                                    )
                                                ]
                                            ),
                                            [IntLiteral(2)]
                                        ),
                                        Id("highestScore")
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,406))

    def test_complex_method_call1(self):
        input = """func main(){
            a[1][2].c.Cal(1,2,3);
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(
                                FieldAccess(
                                    ArrayCell(
                                        Id("a"),
                                        [IntLiteral(1), IntLiteral(2)]),
                                    "c"),
                                "Cal",
                                [IntLiteral(1), IntLiteral(2), IntLiteral(3)]
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,407))
    
    def test_complex_method_call2(self):
        input = """func main(){
            wth().a[1][2].c.Cal(1+2,3*4,5/6);
        };"""
        expect= str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(FuncCall("wth", []), "a"),
                                        [IntLiteral(1), IntLiteral(2)]
                                    ),
                                    "c"),
                                "Cal",
                                [
                                    BinaryOp("+",IntLiteral(1),IntLiteral(2)),
                                    BinaryOp("*",IntLiteral(3),IntLiteral(4)),
                                    BinaryOp("/",IntLiteral(5),IntLiteral(6)
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,408))

    def test_complex_method_call3(self):
        input = """func main(){
            wth().c()[2][3].a().b()
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            MethCall(
                                MethCall(
                                    ArrayCell(
                                        MethCall(
                                            FuncCall("wth",[]),
                                            "c",
                                            []
                                        ),
                                        [IntLiteral(2), IntLiteral(3)]
                                    ),
                                    "a",
                                    []
                                ),
                                "b",
                                []
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,409))

    def test_simple_assign_statement(self):
        input = """func main(){
            a:=1%1;};"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"),BinaryOp("%",IntLiteral(1),IntLiteral(1)))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,410))

    def test_plus_assign_statement(self):
        input = """func main(){
            a+=a+1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"),BinaryOp("+",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,411))

    def test_minus_assign_statement(self):
        input = """func main(){
            a -= ---b;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                Id("a"),
                                BinaryOp("-",
                                        Id("a"),
                                        UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("b"))))))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,412))

    def test_mul_assign_statement(self):
        input = """func main(){
            a *= b*c;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"),BinaryOp("*",Id("a"),BinaryOp("*",Id("b"),Id("c"))))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,413))

    def test_div_assign_statement(self):
        input = """func main(){
            a /= b/c;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"),BinaryOp("/",Id("a"),BinaryOp("/",Id("b"),Id("c"))))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,414))

    def test_mod_assign_statement(self):
        input = """func main(){
            a %= b%c;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(Id("a"),BinaryOp("%",Id("a"),BinaryOp("%",Id("b"),Id("c"))))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,415))

    def test_field_access_assign_statement(self):
        input = """func main(){
            Toyota.wheels += 2;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(FieldAccess(Id("Toyota"),"wheels"),BinaryOp("+",FieldAccess(Id("Toyota"),"wheels"),IntLiteral(2)))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,416))

    def test_array_cell_assign_statement(self):
        input = """func main(){
            arr[2][0] %= 1;};"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(0)]),BinaryOp("%",ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(0)]),IntLiteral(1)))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,417))

    def test_complex_assign_statement1(self):
        input = """func main(){
            a[1][2].b[3].c += 1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(
                                            ArrayCell(
                                                Id("a"),
                                                [IntLiteral(1), IntLiteral(2)]),
                                            "b"),
                                        [IntLiteral(3)]),
                                    "c"),
                                BinaryOp("+",FieldAccess(ArrayCell(FieldAccess(ArrayCell(Id("a"),[IntLiteral(1), IntLiteral(2)]),"b"),[IntLiteral(3)]),"c"),IntLiteral(1)))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,418))

    def test_complex_assign_statement2(self):
        input = """func main(){
            a[1][2].e.f.b[3] %= 1;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Assign(
                                ArrayCell(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                ArrayCell(Id("a"),
                                                          [IntLiteral(1), IntLiteral(2)])
                                                ,"e")
                                            ,"f")
                                        ,"b"),
                                    [IntLiteral(3)]
                                ),
                                BinaryOp("%",ArrayCell(
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(
                                                ArrayCell(Id("a"),
                                                          [IntLiteral(1), IntLiteral(2)])
                                                ,"e")
                                            ,"f")
                                        ,"b"),
                                    [IntLiteral(3)]
                                ),IntLiteral(1)))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,419))

    def test_if_statement(self):
        input = """func main(){
            if(student.age>18){
                print("Adult");
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp(">",FieldAccess(Id("student"),"age"),IntLiteral(18)),
                                Block([FuncCall("print",[StringLiteral("\"Adult\"")])])
                                ,None
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,420))

    def test_if_else_if_statement(self):
        input = """func sleepy(){
            if(a>b){
                print("hj");
                print("a>b");
            }else if(a<b){
                print("jh");
                print("a<b");}
        };    
        """
        expect = str(Program(
            [
                FuncDecl(
                    "sleepy",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp(">",Id("a"),Id("b")),
                                Block([FuncCall("print",[StringLiteral("\"hj\"")]),FuncCall("print",[StringLiteral("\"a>b\"")])]),
                                If(
                                    BinaryOp("<",Id("a"),Id("b")),
                                    Block([FuncCall("print",[StringLiteral("\"jh\"")]),FuncCall("print",[StringLiteral("\"a<b\"")])]),
                                    None
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,421))

    def test_if_else_statement(self):
        input ="""func main(){
            if(your.feeling == "happy"){
                print("Good for you");
            }else{
                print("Cheer up");
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp("==",FieldAccess(Id("your"),"feeling"),StringLiteral("\"happy\"")),
                                Block([FuncCall("print",[StringLiteral("\"Good for you\"")])]),
                                Block([FuncCall("print",[StringLiteral("\"Cheer up\"")])])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,422))

    def test_if_else_if_else_statement(self):
        input = """func main(){
            if(a>b){
                print("a>b");
            }else if(a<b){
                print("a<b");
            }else{
                print("a=b");
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp(">",Id("a"),Id("b")),
                                Block([FuncCall("print",[StringLiteral("\"a>b\"")])]),
                                If(
                                    BinaryOp("<",Id("a"),Id("b")),
                                    Block([FuncCall("print",[StringLiteral("\"a<b\"")])]),
                                    Block([FuncCall("print",[StringLiteral("\"a=b\"")])])
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,423))

    def test_many_else_if(self):
        input = """func main(){
            if(yourGirlfriend == "single"){
                print("Good for you");
            }else if(yourGirlfriend == "taken"){
                print("Cheer up");
            }else if(yourGirlfriend == "complicated"){
                print("Good luck");
            }else if(yourGirlfriend == "married"){
                print("Good bye");
            }else{
                print("Still available");
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                BinaryOp("==",Id("yourGirlfriend"),StringLiteral("\"single\"")),
                                Block([FuncCall("print",[StringLiteral("\"Good for you\"")])]),
                                If(
                                    BinaryOp("==",Id("yourGirlfriend"),StringLiteral("\"taken\"")),
                                    Block([FuncCall("print",[StringLiteral("\"Cheer up\"")])]),
                                    If(
                                        BinaryOp("==",Id("yourGirlfriend"),StringLiteral("\"complicated\"")),
                                        Block([FuncCall("print",[StringLiteral("\"Good luck\"")])]),
                                        If(
                                            BinaryOp("==",Id("yourGirlfriend"),StringLiteral("\"married\"")),
                                            Block([FuncCall("print",[StringLiteral("\"Good bye\"")])]),
                                            Block([FuncCall("print",[StringLiteral("\"Still available\"")])])
                                        )
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,424))

    def test_nested_if_statement1(self):
        input = """func main(){
            if(!warZone){
                if(!pandemic){
                    print("Peaceful");
                }else{
                    print("Stay home");
                }
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                UnaryOp("!",Id("warZone")),
                                Block(
                                    [
                                        If(
                                            UnaryOp("!",Id("pandemic")),
                                            Block([FuncCall("print",[StringLiteral("\"Peaceful\"")])]),
                                            Block([FuncCall("print",[StringLiteral("\"Stay home\"")])])
                                        )
                                    ]
                                ),
                                None
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,425))

    def test_nested_if_statement2(self):
        input = """func main(){
            if(!warZone){
                if(!pandemic){
                    print("Peaceful");
                }else if(!hunger){
                    if(!lockdown){
                        print("Stay home");
                    }else{
                        print("Stay safe");
                    }
                }
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(
                                UnaryOp("!",Id("warZone")),
                                Block(
                                    [
                                        If(
                                            UnaryOp("!",Id("pandemic")),
                                            Block([FuncCall("print",[StringLiteral("\"Peaceful\"")])]),
                                            If(
                                                UnaryOp("!",Id("hunger")),
                                                Block(
                                                    [
                                                        If(
                                                            UnaryOp("!",Id("lockdown")),
                                                            Block([FuncCall("print",[StringLiteral("\"Stay home\"")])]),
                                                            Block([FuncCall("print",[StringLiteral("\"Stay safe\"")])])
                                                        )
                                                    ]
                                                ),
                                                None
                                            )
                                        )
                                    ]
                                ),
                                None
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,426))

    def test_if_empty_statement(self):
        input = """func main(){
            if(a>b){};
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            If(BinaryOp(">",Id("a"),Id("b")),Block([]),None)
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,427))

    def test_basic_for_statement(self):
        input = """func testfor() {for i < 10 {
i+=1;
PutStringLn(i);
};};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testfor",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForBasic(
                                BinaryOp("<",Id("i"),IntLiteral(10)),
                                Block(
                                    [
                                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                                        FuncCall("PutStringLn",[Id("i")])
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,428))

    def test_init_for_statement(self):
        input = """func testfor() {
        for i := 0; a > 10; i += 1 {
                        PutStringLn(i);
                        i+=1;
                        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testfor",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"),IntLiteral(0)),
                                BinaryOp(">",Id("a"),IntLiteral(10)),
                                Assign(Id("i"), BinaryOp("+",Id("i"),IntLiteral(1))),
                                Block(
                                    [
                                        FuncCall("PutStringLn",[Id("i")]),
                                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,429))

    def test_empty_for_statement(self):
        input = """func testfor() {
            for var i int=2;i<2;i-=1 {
            };
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "testfor",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                VarDecl("i",IntType(),IntLiteral(2)),
                                BinaryOp("<",Id("i"),IntLiteral(2)),
                                Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),
                                Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,430))

    def test_for_range_loop_with_array_literal(self):
        input = """func testForLoop() {for index, value := range [5]int{1, 2, 3, 4, 5} {
        // statements
        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("index"),
                                Id("value"),
                                ArrayLiteral(
                                    [IntLiteral(5)],
                                    IntType(),
                                    [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]
                                ),
                                Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,431))

    def test_for_range_with_array_variable(self):
        input = """func testForLoop() {for index, value := range a {
        // statements
        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("index"),
                                Id("value"),
                                Id("a"),
                                Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect, 432))

    def test_for_range_with_array_cell(self):
        input = """func testForLoop(){
            for index,value := range a[1][2].b[3]{
                // statements
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("index"),
                                Id("value"),
                                ArrayCell(
                                    FieldAccess(
                                        ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),
                                        "b"),
                                    [IntLiteral(3)]),
                                Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,433))

    def test_for_range_without_index(self):
        input = """func testForLoop(){
            for _,value := range a{
                // statements
            }
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForEach(
                                Id("_"),
                                Id("value"),
                                Id("a"),
                                Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,434))

    def test_for_loop_with_break(self):
        input = """func testForLoop() {for i := 0; i < 10; i += 1 {
            if (i == 5) {
                break;
            }
        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"),IntLiteral(0)),
                                BinaryOp("<",Id("i"),IntLiteral(10)),
                                Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==",Id("i"),IntLiteral(5)),
                                            Block([Break()]),
                                            None
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,435))

    def test_for_loop_with_continue(self):
        input = """func testForLoop() {for i := 0; i < 10; i += 1 {
            if (i == 5) {
                continue;
            }
        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"),IntLiteral(0)),
                                BinaryOp("<",Id("i"),IntLiteral(10)),
                                Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==",Id("i"),IntLiteral(5)),
                                            Block([Continue()]),
                                            None
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,436))

    def test_for_loop_with_break_and_continue(self):
        input = """func testForLoop() {for i := 0; i < 10; i += 1 {
            if (i == 5) {
                break;
            } else {
                continue;
            }
        };};"""
        expect = str(Program(
            [
                FuncDecl(
                    "testForLoop",
                    [],
                    VoidType(),
                    Block(
                        [
                            ForStep(
                                Assign(Id("i"),IntLiteral(0)),
                                BinaryOp("<",Id("i"),IntLiteral(10)),
                                Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                                Block(
                                    [
                                        If(
                                            BinaryOp("==",Id("i"),IntLiteral(5)),
                                            Block([Break()]),
                                            Block([Continue()])
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,437))  

    def test_return_statement(self):
        input = """func main(){
            return;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Return(None)
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,438))

    def test_return_with_expression(self):
        input = """func main(){
            return a[1][2].b[3].c;
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Return(
                                FieldAccess(
                                    ArrayCell(
                                        FieldAccess(
                                            ArrayCell(
                                                Id("a"),
                                                [IntLiteral(1), IntLiteral(2)])
                                                ,"b"
                                            )
                                            
                                        ,[IntLiteral(3)]),"c"
                                    )
                                )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,439))

    def test_return_with_array_literal(self):
        input = """func main(){
            return [5]num{1,2,3,4,5};
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Return(
                                ArrayLiteral(
                                    [IntLiteral(5)],
                                    Id("num"),
                                    [IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4), IntLiteral(5)]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,440))

    def test_return_with_struct_literal(self):
        input = """func main(){
            return student{name:"John",age:20};
        };"""
        expect = str(Program(
            [
                FuncDecl(
                    "main",
                    [],
                    VoidType(),
                    Block(
                        [
                            Return(
                                StructLiteral(
                                    "student",
                                    [
                                        ("name",StringLiteral("\"John\"")),
                                        ("age",IntLiteral(20))
                                    ]
                                    )
                                )
                        ])
                    )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,441))

    def test_array_var_with_init_contain_const(self):
        input = """var a = [5] int{a,b,c,d,e};"""
        expect = str(Program(
            [
                VarDecl(
                    "a",
                    None,
                    ArrayLiteral(
                        [IntLiteral(5)],
                        IntType(),
                        [Id("a"), Id("b"), Id("c"), Id("d"), Id("e")]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect, 442))


    def test_array_declare_with_other_int_lit(self):
        input ="""var arr [1][0b1010][0O777][0xFFF] string;"""
        expect = str(Program(
            [
                VarDecl(
                    "arr",
                    ArrayType(
                        [
                            IntLiteral(1),
                            IntLiteral("0b1010"),
                            IntLiteral("0O777"),
                            IntLiteral("0xFFF")
                        ],
                        StringType()
                    ),
                    None
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,443))

    def test_bool_literal(self):
        input = """var a = true;"""
        expect = str(Program(
            [
                VarDecl("a",None,BooleanLiteral("true"))
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,444))

    def test_array_literal_with_struct_literal_element(self):
        input ="""var arr = [2]student{student{name:"John",age:20},student{name:"Alice",age:21}};"""
        expect = str(Program(
            [
                VarDecl(
                    "arr",
                    None,
                    ArrayLiteral(
                        [IntLiteral(2)],
                        Id("student"),
                        [
                            StructLiteral(
                                "student",
                                [
                                    ("name",StringLiteral("\"John\"")),
                                    ("age",IntLiteral(20))
                                ]
                            ),
                            StructLiteral(
                                "student",
                                [
                                    ("name",StringLiteral("\"Alice\"")),
                                    ("age",IntLiteral(21))
                                ]
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.checkASTGen(input,expect,445))


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


#kiểu nil được dùng khi nào????
#bổ sung các kiểu số khác cho array literal*
#test complex expression*
#test complex methodcall*