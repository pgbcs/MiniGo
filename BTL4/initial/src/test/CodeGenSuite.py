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

    def test_basic_for_loop(self):
        input = """
    func main(){
        var i = 0;
        for i < 3 {
            // loop body
            putIntLn(i);
            i+=1
        }
    }

"""
        expect = "0\n1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_for_step(self):
        input = """
    func main(){
        for var i int= 0; i < 10; i += 1 {
         // loop body
        putInt(i)
    }
    }
"""
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test_assign_to_create_new_var(self):
        input = """
    func main(){
        i:=100
        putInt(i)
    }
"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_global_float_var(self):
        input = """
        var a = 1.5
        func main(){
            putFloat(a);
        }
"""
        expect ="1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    def test_global_boolean_var(self):
        input = """
        var a = true
        func main(){
            putBool(a);
        }
"""
        expect ="true"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_global_string_var(self):
        input = """
        var a = "hello"
        func main(){
            putString(a);
        }
"""
        expect ="hello"
        self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    def test_init_var_with_func_call(self):
        input = """
        func foo() int{
            return 1;
        }
        func main(){
            var a = foo();
            putInt(a);
        }
"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_init_var_with_expr(self):
        input = """
        func main(){
            var a = 1 + 2;
            putInt(a);
        }
"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test_init_var_with_expr1(self):
        input = """
        func main(){
            var a = 1 + 2 * 3;
            putInt(a);
        }
"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_init_var_with_expr2(self):
        input = """
        func main(){
            var a = 1 + 2 * 3 - 4 / 2;
            putInt(a);
        }
"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_init_var_with_arraycell(self):
        input = """
        func main(){
            var a[2][2] int = [2][2]int{{1, 2}, {3, 4}};
            b := a[0][1] + a[1][0];
            putInt(b);
        }
"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_init_var_with_string_arraycell(self):
        input = """
        func main(){
            var a[2][2] string = [2][2]string{{"hello", "world"}, {"foo", "bar"}};
            b := a[0][1] + a[1][0];
            putString(b);
        }
"""
        expect = "worldfoo"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_struct_var(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func main(){
            var p Person = Person{name: "John", age: 30};
            putString(p.name);
        }
"""
        expect = "John"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    def test_local_constant(self):
        input = """
        func main(){
            const a = 10;
            putInt(a);
        }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_local_float_constant(self):
        input = """
        func main(){
            const a = 3.14;
            putFloat(a);
        }
"""
        expect = "3.14"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test_local_boolean_constant(self):
        input = """
        func main(){
            const a = true;
            putBool(a);
        }
"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_local_string_constant(self):
        input = """
        func main(){
            const a = "hello";
            putString(a);
        }
"""
        expect = "hello"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test_local_struct_constant(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func main(){
            const p = Person{name: "John", age: 30};
            putString(p.name);
        }
"""
        expect = "John"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_local_array_constant(self):
        input = """
        func main(){
            const a = [2][2]int{{1, 2}, {3, 4}};
            putInt(a[0][1]);
        }
"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test_local_expression_constant(self):
        input = """
        func main(){
            const a = 1 + 2 * 3 - 4 / 2;
            putInt(a);
        }
"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_local_string_expression_constant(self):
        input = """
        func main(){
            const a = "hello" + " world";
            putString(a);
        }
"""
        expect = "hello world"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_local_var_with_same_name_as_global(self):
        input = """
        var a = 10;
        func main(){
            var a = 20;
            putInt(a);
        }
"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test_local_var_with_same_name_as_param(self):
        input = """
        func foo(a int) int {
            var a = 20;
            return a;
        }
        func main(){
            putInt(foo(10));
        }
"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test_array_declare_with_init_many_dim(self):
        input = """
var a [5][5][5] int = [5][5][5]int{
    {
        {57, 12, 140, 125, 114},
        {71, 52, 44, 216, 16},
        {15, 47, 111, 119, 13},
        {101, 214, 112, 229, 142},
        {3, 81, 216, 174, 142}    },
    {
        {79, 110, 172, 52, 47},
        {194, 49, 183, 176, 135},
        {22, 235, 63, 193, 40},
        {150, 185, 98, 35, 23},
        {116, 148, 40, 119, 51}    },
    {
        {194, 142, 232, 186, 83},
        {189, 181, 107, 136, 36},
        {87, 125, 83, 236, 194},
        {138, 112, 166, 28, 117},
        {16, 161, 205, 137, 33}   },
    {
        {108, 161, 108, 255, 202},
        {234, 73, 135, 71, 126},
        {134, 219, 204, 185, 112},
        {70, 252, 46, 24, 56},
        {78, 81, 216, 32, 197}    },
    {
        {195, 239, 128, 5, 58},
        {136, 174, 57, 150, 222},
        {80, 232, 1, 134, 91},
        {54, 152, 101, 78, 191},
        {82, 0, 165, 250, 9}    }};
func main(){
    putInt(a[0][0][0]);
}
"""
        expect = "57"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_assign_array_for_other_array(self):
        input = """
        var a[2][2] int = [2][2]int{{1, 2}, {3, 4}};
        var b[2] int = a[0];
        func main(){
            putInt(b[1]);
        }
"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_struct_depend_on_other_struct(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        type Student struct {
            person Person;
            grade int;
        }
        func main(){
            var s Student = Student{person: Person{name: "John", age: 20}, grade: 90};
            putString(s.person.name);
        }
"""
        expect = "John"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_referece_to_arraycell(self):
        input = """
        func main(){
            var a[5] int = [5] int {1, 2, 3, 4, 5};
            b := a;
            b[0] := 10;
            putInt(a[0]);
        }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

#     def test_arraycell_without_init(self):
#         input = """
    
#     func main(){
#         var a[5] int;
#         a[0]:=1
#         putInt(a[0])
#     }
# """     
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test_string_ref(self):
        input = """
        func foo(a string){
            a+=" world"
        }
        func main(){
            var a string = "hello";
            foo(a)
            putString(a);
    }
            """
        expect = "hello world"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_struct_declare_with_array_field(self):
        print("test_struct_declare_with_array_field")
        input = """
        type Person struct {
            name string;
            age int;
            scores [3] int;
        }
        func main(){
            var p Person = Person{name: "John", age: 30, scores: [3]int{90, 80, 70}};
            putFloat(p.scores[0]);
        }
"""
        expect = "90.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))


    def test_interface6(self):
        input = """
        func ( a A ) print() {
            putStringLn(a.name)
            putIntLn(a.age)
        }

        func main() {
            var a Printable 
            a := A{age: 8, name: "nicole"}
            a.print()
        }

        type Printable interface{
            print()
        }
        type A struct {
            age int
            name string
        }
        """
        expect = "nicole\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_test_interface7(self):
        input = """
        func ( a A ) print() {
            putStringLn(a.name)
            putIntLn(a.age)
        }

        func main() {
            var a Printable 
            a := A{age: 8, name: "nicole"}
            var b Printable
            b := B{age: 10, name: "nicole"}
            a.print()
            b.print()
        }

        type Printable interface{
            print()
        }
        type A struct {
            age int
            name string
        }
        type B struct{
            age int
            name string
        }
        func ( a B ) print() {
            putStringLn(a.name)
            putIntLn(a.age)
        }
        """
        expect = "nicole\n8\nnicole\n10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test_interface8(self):
        input = """
        type Printer interface {
            print()
        }

        type Person struct {
            name string
        }

        func (p Person) print() {
            putStringLn(p.name)
        }

        func (p Pearson) say() {
            putStringLn(p.name)
        }

        func main() {
            var people Printer
            //people := Person{name: "Anna"}
            people := Pearson{name: "Bob"}
            //people.print()
        }

        type Pearson struct {
            name string
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    # def test_interface9(self):
    #     input = """
    #     type Printer interface {
    #         print()
    #     }

    #     type Person struct {
    #         name string
    #     }

    #     func (p Person) print() {
    #         putStringLn(p.name)
    #     }

    #     func (p Pearson) say() {
    #         putStringLn(p.name)
    #     }

    #     func main() {
    #         var people Printer
    #         //people := Person{name: "Anna"}
    #         people := Pearson{name: "Bob"}
    #         people.print()
    #     }

    #     type Pearson struct {
    #         name string
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 592))
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