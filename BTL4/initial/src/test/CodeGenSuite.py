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


    # def test_string_ref(self):
    #     input = """
    #     func foo(a string){
    #         a+=" world"
    #     }
    #     func main(){
    #         var a string = "hello";
    #         foo(a)
    #         putString(a);
    # }
    #         """
    #     expect = "hello world"
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_struct_declare_with_array_field(self):
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

    def test_assign_assign_float_array_to_int_array1(self):
        input = """
        func main(){
            var a[5] int = [5] int {1, 2, 3, 4, 5};
            var b[5] float;
            b:=a
            putFloat(b[0]);
        }
"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_assign_assign_float_array_to_int_array2(self):
        input = """
        func main(){
            var a[5] int;
            var b[5] float;
            b:=a
            b := [5] float {1.0, 2.0, 3.0, 4.0, 5.0};
            putFloat(b[0]);
        }
"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 572))



    def test_assign_int_array_to_float_array3(self):
        input = """
        func main(){
            var a[5] int = [5] int {4, 2, 3, 4, 5};
            var b A = A{name: "hello", arr: [5] float {1.0, 2.0, 3.0, 4.0, 5.0}};
            b.arr := a
            putFloat(b.arr[0]);
        }
        type A struct {
            name string;
            // array of float
            arr [5] float;
        }
"""
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_assign_int_array_to_float_array4(self):
        #use slicing array
        input = """
        func main(){
            var a[5] int = [5] int {4, 2, 3, 4, 5};
            var b[2][5] float = [2][5] float{{1.0, 2.0, 3.0, 4.0, 5.0}, {6.0, 7.0, 8.0, 9.0, 10.0}};
            b[0] := a
            putFloat(b[0][0]);
        }
"""
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_assign_int_array_to_float_array5(self):
        #use funcall to have int array
        input = """
        func foo() [5] int {
            return [5] int {1, 2, 3, 4, 5};
        }
        func main(){
            var b[5] float = foo();
            putFloat(b[0]);
        };
    """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    def test_assign_int_to_float_var1(self):
        input = """
        func main(){
            var a int = 5;
            var b float = a;
            putFloat(b);
        }
"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_assign_int_to_float_var2(self):
        #global var
        input = """
        var a int = 5;
        var c float = a;
        func main(){
            var b float = a;
            putFloat(b);
            putFloat(c);
        }
"""
        expect = "5.05.0"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_assign_int_arr_to_float_arr6(self):
        #with global var and funcall
        input = """
        var a[5] int = [5] int {1, 2, 3, 4, 5};
        var b[5] float = a;
        func main(){
            putFloat(b[0]);
        }
"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_struct_method_with_param(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) greet(name string) {
            putString("Hello, " + name + "! My name is " + p.name);
        }
        func main(){
            var p Person = Person{name: "John", age: 30};
            p.greet("Alice");
        }
"""
        expect = "Hello, Alice! My name is John"
        self.assertTrue(TestCodeGen.test(input, expect, 579))


    def test_struct_method_return_other_struct(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func (p Person) getOlder(years int) Person {
            return Person{name: p.name, age: p.age + years};
        }
        func main(){
            var p Person = Person{name: "John", age: 30};
            var olderPerson = p.getOlder(5);
            putInt(olderPerson.age);
        }
"""
        expect = "35"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_int_function(self):
        #include param and no param
        input = """
        func add(a int, b int) int {
            return a + b;
        }
        func main() {
            var a int = 5;
            var b int = 10;
            var c int = add(a, b);
            putInt(c);
            putInt(add(3, 4));
            putInt(add(1, 2) + add(3, 4));
            putInt(add(add(1, 2), add(3, 4)));
        }
"""
        expect = "1571010"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_float_function(self):
        #include param and no param
        input = """
        func add(a float, b float) float {
            return a + b;
        }
        func main() {
            var a float = 5.5;
            var b float = 10.5;
            var c float = add(a, b);
            putFloatLn(c);
            putFloatLn(add(3.5, 4.5));
            putFloatLn(add(1.5, 2.5) + add(3.5, 4.5));
            putFloatLn(add(add(1.5, 2.5), add(3.5, 4.5)));
        }
"""
        expect = "16.0\n8.0\n12.0\n12.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_sum_of_int_and_float(self):
        input = """
        func main() {
            var a int = 5;
            var b float = 10.5;
            var c float = a + b;
            putFloatLn(c);
        }
"""
        expect = "15.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test_bool_function(self):
        #include param and no param
        input = """
        func isEven(n int) boolean {
            return n % 2 == 0;
        }
        func main() {
            var a int = 5;
            var b int = 10;
            var c boolean = isEven(a);
            putBoolLn(c);
            putBoolLn(isEven(b));
            putBoolLn(isEven(3) && isEven(4));
        }
"""
        expect = "false\ntrue\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_string_function(self):
        #include param and no param
        input = """
        func greet(name string) string {
            return "Hello, " + name + "!";
        }
        func main() {
            var a string = "Alice";
            var b string = greet(a);
            putStringLn(b);
            putStringLn(greet("Bob"));
            putStringLn(greet("Charlie") + " " + greet("Dave"));
        }
"""
        expect = "Hello, Alice!\nHello, Bob!\nHello, Charlie! Hello, Dave!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_function_return_struct(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func createPerson(name string, age int) Person {
            return Person{name: name, age: age};
        }
        func main() {
            var p Person = createPerson("Alice", 25);
            putStringLn(p.name);
            putIntLn(p.age);
        }
"""
        expect = "Alice\n25\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test_function_return_interface(self):
        input = """
        type Shape interface {
            area() float
        }
        type Circle struct {
            radius float
        }
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius
        }
        func createCircle(radius float) Shape {
            return Circle{radius: radius}
        }
        func main() {
            var c Shape = createCircle(5.0)
            putFloatLn(c.area())
        }
"""
        expect = "78.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_function_return_array(self):
        input = """
        func createArray() [5]int {
            return [5]int{1, 2, 3, 4, 5};
        }
        func main() {
            var arr [5]int = createArray();
            putIntLn(arr[0]);
            putIntLn(arr[1]);
            putIntLn(arr[2]);
        }
"""
        expect = "1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    


    # def test_struct_method_with_

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

    def test_test_funcall_with_interface_as_param(self):
        input = """
        type Shape interface {
            area() float
        }
        type Circle struct {
            radius float
        }
        func getArea(s Shape) float {
            return s.area()
        }
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius
        }
        func createCircle(radius float) Shape {
            return Circle{radius: radius}
        }
        func main() {
            var c Shape = createCircle(5.0)
            putFloatLn(getArea(c))
        }
"""
        expect = "78.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_float_function_but_return_int(self):
        input = """
        func add(a int, b int) float {
            return a + b;
        }
        func main() {
            var a int = 5;
            var b int = 10;
            var c float = add(a, b);
            putFloat(c);
        }
"""
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_pass_by_value_with_primitive_type(self):
        input = """
        func foo(a int) {
            a := 10;
        }
        func main() {
            var a int = 5;
            foo(a);
            putInt(a);
        }
"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test_pass_by_ref_with_struct(self):
        input = """
        type Person struct {
            name string;
            age int;
        }
        func foo(p Person) {
            p.age := 10;
        }
        func main() {
            var p Person = Person{name: "Alice", age: 5};
            foo(p);
            putInt(p.age);
        }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_pass_by_ref_with_array(self):
        input = """
        func foo(arr [5]int) {
            arr[0] := 10;
        }
        func main() {
            var arr [5]int = [5]int{1, 2, 3, 4, 5};
            foo(arr);
            putInt(arr[0]);
        }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_pass_by_ref_with_interface(self):
        input = """
        type Shape interface {
            area() float
        }
        type Circle struct {
            radius float
        }
        func foo(s Shape) {
            s := Circle{radius: 10.0}
        }
        func (c Circle) area() float {
            return 3.14 * c.radius * c.radius
        }
        
        func main() {
            var c Shape = Circle{radius: 5.0}
            foo(c)
            putFloatLn(c.area())
        }
"""
        expect = "78.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_arraycell_with_index_is_expr(self):
        input = """
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b int = 2
            putInt(a[b])
        }
"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_break_stmt(self):
        input = """
        func main() {
            for i := 0; i < 10; i+=1 {
                if (i == 5) {
                    break
                }
                putInt(i)
            }
        }
"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_continue_stmt(self):
        input = """
        func main() {
            for i := 0; i < 10; i+=1 {
                if (i == 5) {
                    continue
                }
                putInt(i)
            }
        }
"""
        expect = "012346789"
        self.assertTrue(TestCodeGen.test(input, expect, 600))

    def test_access_arraycell_with_expr(self):
        input = """
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b int = 2
            putInt(a[-b+3])
        }
"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 601))

    def test_access_arraycell_with_expr1(self):
        #funcall to get index
        input = """
        func getIndex() int {
            return 2
        }
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            putInt(a[getIndex()])
        }
"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 602))

    def test_access_arraycell_with_expr2(self):
        #other araycell
        input = """
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b[5] int = [5]int{6, 7, 8, 9, 10}
            putInt(b[a[0]])
        }
"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 603))
    
    def test_access_arraycell_with_expr3(self):
        #index is field access
        input = """
        type Index struct {
            value int
        }
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b Index = Index{value: 2}
            putInt(a[b.value])  
        }
"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 604))
    
    def test_access_arraycell_with_expr4(self):
        #index is method call
        input = """
        type Index struct {
            value int
        }
        func (i Index) getValue() int {
            return i.value
        }
        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b Index = Index{value: 2}
            putInt(a[b.getValue()])  
        }
"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 605))
    
    def test_access_arraycell_with_expr5(self):
        #index is method call with param
        input = """
        type Index struct {
            value int
        }

        func main() {
            var a[5] int = [5]int{1, 2, 3, 4, 5}
            var b Index = Index{value: 2}
            putInt(a[b.getValue(1)])  
        }
        func (i Index) getValue(off int) int {
            return i.value + off
        }
"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 606))

    def test_field_access_with_expr(self):
        #field of struct
        input = """
        type Person struct {
            name string
            age int
        }
        func main() {
            var a[5] Person = [5]Person{Person{name: "Alice", age: 20}, Person{name: "Bob", age: 25}, Person{name: "Charlie", age: 30}, Person{name: "David", age: 35}, Person{name: "Eve", age: 40}}
            putInt(a[2].age)
        }
"""
        expect = "30"
        self.assertTrue(TestCodeGen.test(input, expect, 607))
    
    def test_field_access_with_expr1(self):
        #funcall to get struct
        input = """
        type Person struct {
            name string
            age int
        }
        func getPerson() Person {
            return Person{name: "Alice", age: 20}
        }
        func main() {
            var a Person = getPerson()
            putInt(a.age)
        }
"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 608))

    def test_field_access_with_field_and_array_access(self):
        #field of struct and array access
        input = """

        func main() {
            var car = Car{wheel: [4]Wheel{Wheel{brand: "Michelin"}, Wheel{brand: "Bridgestone"}, Wheel{brand: "Goodyear"}, Wheel{brand: "Dunlop"}}}
            car.wheel[0].brand := "Michelin";
            putString(car.wheel[0].brand)
        }
        type Wheel struct {
            brand string
        }
        type Car struct {
            wheel [4]Wheel
        }
"""
        expect = "Michelin"
        self.assertTrue(TestCodeGen.test(input, expect, 609))

    def test_field_access_with_field_and_array_access1(self):
        input ="""func main(){
            var b int = 1
            var car = Car{wheel: [4][2]Wheel{ { Wheel{brand: [2] string{"Michelin", "Br Br"}}, Wheel{brand: [2] string {"Bridgestone", "Hmmm"}} }, {Wheel{brand: [2] string {"Goodyear", "GoodLife"}}, Wheel{brand: [2] string{"Dunlop", "Jumbo"}}}, {Wheel{brand: [2] string {"Pirelli", "TungTungSahur"}}, Wheel{brand: [2] string {"Continental", "Bruh"}}}, {Wheel{brand: [2] string{"Hankook", "Boa"}}, Wheel{brand: [2] string {"Toyo", "ta"}}}}}
            car.wheel[0][b].brand[1] := "Bridgestone";
            putString(car.wheel[0][1].brand[0])
        };
        type Wheel struct {
            brand [2] string
        }
        type Car struct {
            wheel [4][2]Wheel
        }
        """
        expect = "Bridgestone"
        self.assertTrue(TestCodeGen.test(input, expect, 610))
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

        func (p Person) say() {
            putStringLn(p.name)
        }

    # def test_floatop_all(self):
    #     input = """


    def test_for_short_circuit(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            if (a > b && 0/0 > 0) {
                putIntLn(a + b);
            }            else{
                putIntLn(a - b);
            }
        }
        """
        expect = "-5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 611))

    def test_float_short_circuit(self):
        input = """
        func main() {
            var a float = 5.5;
            var b float = 10.0;
            if (a > b && 0/0 > 0) {
                putFloatLn(a + b);
            }            else{
                putFloatLn(a - b);
            }
        }
        """
        expect = "-4.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 612))

    def test_string_short_circuit(self):
        input = """
        func main() {
            var a string = "hello";
            var b string = "world";
            if (a == b && 0/0 > 0) {
                putStringLn(a + b);
            }            else{
                putStringLn(a + " " + b);
            }
        }
        """
        expect = "hello world\n"
        self.assertTrue(TestCodeGen.test(input, expect, 613))
    #     func main() {
    #     input = """
    #     func main() {
    #         var a float = 5.5;
    #         var b float = 2.0;

    #         putFloatLn(a + b);      // 7.5
    #         putFloatLn(a - b);      // 3.5
    #         putFloatLn(a * b);      // 11.0
    #         putFloatLn(a / b);      // 2.75

    #         putBoolLn(a == b);      // false
    #         putBoolLn(a != b);      // true
    #         putBoolLn(a < b);       // false
    #         putBoolLn(a <= b);      // false
    #         putBoolLn(a > b);       // true
    #         putBoolLn(a >= b);      // true
    #     }
    #     """
    #     expect = "7.5\n3.5\n11.0\n2.75\nfalse\ntrue\nfalse\nfalse\ntrue\ntrue\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 594))
#test method name is main
#local var same name with receiver
#test order check env local->nonlocal
#need write more test case for string
#write test case for method call like function call
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