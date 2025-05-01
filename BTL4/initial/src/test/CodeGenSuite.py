import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_gllobal_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_global_var_using_other_var_for_init(self):
        input = """
        var a int = 10;
        var b int = a;
        func main() { putInt(b);};
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_global_const(self):
        input = """
        const b = 3
        func main() { putInt(b);};
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_global_float_const(self):
        input = """
        const b = 3.14
        func main() { putFloat(b);};
        """
        expect = "3.14"
        self.assertTrue(TestCodeGen.test(input,expect,509))
        
    def test_global_boolean_const(self):
        input = """
        const b = true
        func main() { putBool(b);};
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_global_string_const(self):
        input = """
        const b = "hello world"
        func main() { putString(b);};
        """
        expect = "hello world"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_default_int_global_var(self):
        input = """
        var b int;
        func main() { putInt(b);};
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,512))
        
    def test_default_float_global_var(self):
        input = """
        var b float;
        func main() { putFloat(b);};
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,513))
        
    def test_default_bool_global_var(self):
        input = """
        var b boolean;
        func main() { putBool(b);};
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_int_local_var(self):
        input = """
        func main() {
            var b int = 0;
            putInt(b);
        }
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_float_local_var(self):
        input = """
        func main() {
            var b float = 0.0;
            putFloat(b);
        }
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_bool_local_var(self):
        input = """
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    
    def test_struct_type(self):
        input = """
        var b int;
        type Student struct {
            name string ;
            age int ;
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test_type_field_is_struct(self):
        input = """
        type Student struct {
            name string ;
            age int ;
            money Balance;
        }
        type Balance struct{
            value int;
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_interface_type(self):
        input = """
        type Calculator interface {
        Add(x, y int) int;
        Subtract(a, b float, c int) float;
        Reset()
        SayHello(name string)
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_method_decl(self):
        input = """
        type BrBrPatapim struct {
            value int;
        }
        func (c BrBrPatapim) Add(x int) int {
        
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_method_decl(self):
        input = """
        type Sahur struct {
        value int;
        }
        func (c Sahur) Add(x int)  {
            c.value += x;
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
#test method name is main
#local var same name with receiver
#test order check env local->nonlocal


#     def test_function_with_param(self):
#         input = """
#         func foo(a, b int) int{
#             return a;
#         }
#         func main(){
#             putInt(foo(1,2));
#         }
# """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,507))