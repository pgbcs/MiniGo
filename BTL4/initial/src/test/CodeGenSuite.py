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
        func main() { 
            putInt(b);
        };
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

    def test_method_decl1(self):
        input = """
        type ABCD struct {
        value int;
        }
        func (c ABCD) Add(x int) int {
            c.value += x;
            return c.value
        }
        func main() {
            var b boolean = false;
            putBool(b);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_field_access(self):
        input = """
        type Crocodilo struct {
            value int;
        }
        func main() {
            var b = Crocodilo{value: 4};
            putInt(b.value);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test_funccall_with_return_value_as_stmt(self):
        input = """
        func Foo(a int) int {
            return a;
        }
        func main(){
            var a = 4;
            Foo(a);
            putInt(Foo(a));
        }
"""
        expect= "4"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_funcall_as_epxr(self):
        input = """
        type ABCD struct {
        value int;
        }
        func (c ABCD) Add(x int) int {
            c.value += x;
            return c.value
        }
        func main() {
            var b ABCD = ABCD{value: 2}
            putInt(b.Add(3));
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_unary_op(self):
        input = """
    var a = true;
    var b = 1;
    func B (c int) int{
        return 1;
    }
    func main(){
        putIntLn(-B(b))
        putBoolLn(!a)
    }
"""
        expect = "-1\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_array_type(self):
        input = """
    func main(){
        var b int = 5;
        var c [3][2][2] int = [3][2][2]int{
            {
                {1, 2}, {3, 4}            },
            {
                {5, 6}, {7, 8}            },
            {
                {9, 10}, {11, 12}}};
        putInt(c[0][0][1]);
    }
"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_shortcircuit_and(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = (c==d&&c<d&&c>d);
        putBool(b);
  
 }  
"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test_shortcircuit_or(self):
        input = """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = (c==d||c<d||c>d);
        putBool(b);
  
 }  
"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    def test_shortcircuit_and_or(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = ((false||c==d)&&c<d&&(c>d));
        putBool(b);
  
 }  
"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_shortcircuit_and_or1(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = ((false||c>d)&&c<d&&(c<d));
        putBool(b);
  
 }  
"""
        expect = "false" 
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_shortcircuit_and_or2(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = ((false||c<d)&&c<d&&(c<d));
        putBool(b);
  
 }  
"""
        expect = "true" 
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_shortcircuit_and_or3(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = c<d&&(c<d)&&((false||c<d));
        putBool(b);
  
 }  
"""
        expect = "true" 
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_shortcircuit_and_or4(self):
        input =  """
    func main(){
        var c = 2;
        var d = 5;
        var b boolean = c>d||(c>d)||((true&&c<d));
        putBool(b);
  
 }  
"""
        expect = "true" 
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_two_short_circuit(self):
        input =  """
    func main(){
        var a = true
        var b = false
        var c = true
        var d = true
        var e = true
        var f boolean = (a||b&&c)&&d&&e;
        putBool(f);
  
 }  
"""
        expect = "true" 
        self.assertTrue(TestCodeGen.test(input, expect, 535))


    def test_assign_arraycell(self):
        input = """
        func main(){
            var a[2][2] string=[2][2] string{{"abc", "hello"},{"ghi", "jkl"}}
            putString(a[0][1] + " ")
            a[0][1] := "world"
            putString(a[0][1])
        }
"""
        expect = "hello world"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_compare_string(self):
        input = """
        func main(){
            var a[2][2] string=[2][2] string{{"abc", "hello"},{"ghi", "jkl"}}
            putBoolLn(a[0][1] ==  "hello")
            a[0][1] := "world"
            putBoolLn(a[0][1] ==  "hello")
        }
"""
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_short_circuit_with_string(self):
        print(538)
        input = """
        func main(){
            var a[2][2] string=[2][2] string{{"abc", "hello"},{"ghi", "jkl"}}
            putBoolLn(a[0][1] ==  "hello"&&a[0][0]>"abcd"&&a[1][0]<="ghi" || a[1][1] >= "jkl")
        }
"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_if_stmt(self):
        input = """func factorial(n int) int {
                if (n < 0) { return -1; } else {
                    return 1
                }
            }
            func main() {
                putIntLn(factorial(-102))
            };
        """
        expect = "-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_unreachable_stmt(self):
        input = """
    func foo() int{
        return 1;
        var a int =2;
        return a;
    }
    func main(){
        putInt(foo());
    }

"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_unreachable_stmt1(self):
        input = """
    func foo(n int) int{
        if (n<2){
            if(n<100){
                return -1;
            }else{
                return 0;
            }
        }else{
            return 0;
        }
    }
    func main(){
        putInt(foo(1));
    }

"""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    
#test method name is main
#local var same name with receiver
#test order check env local->nonlocal
#need write more test case for string

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