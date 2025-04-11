import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_variable_redeclared(self):
        input = """const a = 1.5; var a int;"""
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_constant_redeclared(self):
        input = """var a int; const a=5;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_function_redeclared(self):
        input = """var bruh int;
            func bruh (){
                return;
            }
        """
        expect = """Redeclared Function: bruh\n"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_param_redeclared(self):
        input = """func bruh(x,x int){
            var a int;
        };
"""     
        expect = "Redeclared Parameter: x\n"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_var_redeclared_with_func(self):
        input = """
        func bruh(x,x int){
            var a int;
        };
        var bruh = 2;
"""     
        expect = "Redeclared Variable: bruh\n"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_two_var_redeclared(self):
        input = """var a int;
        var a int;
"""     
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_two_const_redeclared(self):
        input = """const a = 1.3;
        const b = 1.3;
        const a = 1.3;
"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_func_redeclared_with_constant(self):
        input = """const baodeptrai = 1.3;
        func baodeptrai(){
            const a = 3.13;
        }
"""
        expect = "Redeclared Function: baodeptrai\n"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_use_param_in_funcbody(self):
        input = """func foo(x int, y int){
            var a = x;
        }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_overlap_param_in_func(self):
        input = """func foo(x int, y int){
            var x string;
            var y float;
        }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_two_func_redeclared(self):
        input = """func foo(x int, y int){
            var x string;
            var y float;
        }
        func foo(){
            return;
        }
"""
        expect = "Redeclared Function: foo\n"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_overlap_funcname_in_body(self):
        input = """func foo(x int, y int){
            var foo int;
        }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_overlap_global_var_in_funcbody(self):
        input = """var b int =4
            func a(){
                var b int = b;
            }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_redeclared_variable_in_funcbody(self):
        input = """var b int = 4
            func a(){
                var b int = b;
                var b int;
            }
"""
        expect = "Redeclared Variable: b\n"
        self.assertTrue(TestChecker.test(input, expect, 414))
    #maybe write more test for func

    def test_global_struct(self):
        input = """
        var a PPL;
        type PPL struct{
            requisite string;
            min int;
            max int;
            avg float;
            passed boolean;
        };
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))    

    def test_redeclared_struct_with_variable(self):
        input = """var b int =4
            type b struct{
                test int;
            }
"""
        expect = "Redeclared Type: b\n"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_redeclared_struct_with_func(self):
        input = """func b(){
            var a int;
        }
    type b struct{
        test int;
    }
"""
        expect = "Redeclared Type: b\n"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared_2_struct(self):
        input = """    type b struct{
        test float;
    }
    type b struct{
        test int;
    }
"""
        expect = "Redeclared Type: b\n"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclared_field_in_struct(self):
        input = """
    type b struct{
        test int;
        a float;
        test string;
    }
"""
        expect = "Redeclared Field: test\n"
        self.assertTrue(TestChecker.test(input, expect, 419)) 

    def test_redeclared_field_with_struct_name(self):
        input = """
    type Bao struct{
        Bao int;
        a float;
        test string;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420)) 

    def test_field_and_other_var_same_name(self):
        input = """
        var test int;
    type b struct{
        test int;
        a float;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421)) 

    def test_interfaceType(self):
        input = """
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
    var test Calculator;
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422)) 

    def test_global_inrterface(self):
        input = """
        var test Calculator;
        var test1 int;
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423)) 

    def test_redeclared_interface_with_var(self):
        input = """
    var Calculator int;
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
"""
        expect = "Redeclared Type: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 424)) 

    def test_redeclared_interface_with_func(self):
        input = """
    func Calculator(){
        return 1;
    }
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
    var test Calculator;
"""
        expect = "Redeclared Type: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 425)) 

    def test_redeclared_var_with_interface(self):
        input = """
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
    var Calculator int;
"""
        expect = "Redeclared Variable: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 426)) 

    def test_redeclared_func_with_interface(self):
        input = """
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
    func Calculator(){
    return 1;
    }
"""
        expect = "Redeclared Function: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 427)) 

    def test_var_in_block_have_same_name_with_interface(self):
        input = """

    func foo(){
        var Calculator int;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428)) 

    def test_redeclared_interface_with_struct(self):
        input = """
    type Calculator struct {
        Bao int;
        a float;
        test string;
    }
    
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
"""
        expect = "Redeclared Type: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 429)) 

    def test_redeclared_interface(self):
        input = """
    type Calculator interface {
    Add(x, y int) int;
    Subtract(a, b float, c int) float;
    Reset()
    SayHello(name string)
}
    type Calculator interface {
        Greet()
    }
"""
        expect = "Redeclared Type: Calculator\n"
        self.assertTrue(TestChecker.test(input, expect, 430)) 

    def test_redeclared_prototype(self):
        input = """
    type Greeting interface {
        Hi()
        Hello()
        Hi()
    }
"""
        expect = "Redeclared Prototype: Hi\n"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_redeclared_prototype1(self):
        input = """
    type Greeting interface {
        Hi()
        Hi()
        Hello()
    }
"""
        expect = "Redeclared Prototype: Hi\n"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_redeclared_prototype2(self):
        input = """
    type Greeting interface {
        Hello()
        Hi()
        Hi()
    }
"""
        expect = "Redeclared Prototype: Hi\n"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_method_decl(self):
        input = """
        type Calculator struct {
            value int;
        }
        func (c Calculator) Add(x int) {
            var a int;
        }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_redeclared_method(self):
        input = """
        func (c Calculator) Add(x int) {
            var a int;
        }
        func (b Calculator) Add(x float) {
            var a int;
        }
        type Calculator struct {
            value int;
        }
"""
        expect = "Redeclared Method: Add\n"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_two_struct_same_method(self):
        input = """
        func (c J97Vitinhtu) RejectAdd(x int) {
            var a int;
        }
        func (b Vrus) Reject(x float) {
            var a int;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_declared_many_method_for_struct(self):
        input = """
        func (c J97Vitinhtu) RejectAdd(x int) {
            var a int;
        }
        func (b Vrus) Reject(x float) {
            var a int;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_redeclared_method_with_func(self):
        input = """
        func (c J97Vitinhtu) Reject(x int) {
            var a int;
        }
        func RejectAdd(x int ){
            var x = 5;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_method_same_name_with_receiver(self):
        input = """
        func (c J97Vitinhtu) Reject(x int) int{
            var a int;
            return 5;
        }
        func (b Vrus) b(x float) int{
            var a int;
            return 3;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_method_same_name_with_struct_type(self):
        input = """
        func (c J97Vitinhtu) RejectAdd(x int) {
            var a int;
        }
        func (b Vrus) Vrus(x float) {
            var a int;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_method_same_name_with_constant(self):
        input = """
        const Reject = 20;
        func (c J97Vitinhtu) RejectAdd(x int) {
            var a int;
        }
        func (b Vrus) Reject(x float) {
            var a int;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_redeclared_method_with_field(self):
        input = """
        const Reject = 20;
        func (c J97Vitinhtu) RejectAdd(x int) int {
            var a int;
            return 10;
        }
        func (b Vrus) value(x float) int {
            var a int;
            return 10;
        }
        type J97Vitinhtu struct {
            value int;
        }
        type Vrus struct{
            value int;
        }  
"""
        expect= "Redeclared Method: value\n"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_undeclared_identifier_in_const(self):
        input = """const a = b;
        const b = 1.2;"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,444))
  
    def test_undeclared_identifier_in_func_body(self):
        input = """
    func levi(){
        var a int = b;
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_undeclared_identifier_in_return_stmt(self):
        input = """
    func levi(){
        return ackerman
    }
"""
        expect = "Undeclared Identifier: ackerman\n"
        self.assertTrue(TestChecker.test(input,expect,446))       

    def test_undeclared_function(self):
        input = """
    func greeting(){
        b();
    }
"""
        expect = "Undeclared Function: b\n"
        self.assertTrue(TestChecker.test(input,expect,447))   

    def test_undeclared_function_in_method(self):
        input = """
    func (a C) greeting(){
        b();
    }
    type C struct{
        name int
    }
"""
        expect = "Undeclared Function: b\n"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_struct_depend_on_together(self):
        input = """
    type A struct {
        a B;
    }

    type B struct{
        b A;
    }
"""
        expect =""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_interface_depen_on_together(self):
        input = """
    type A interface {
        a() B;
    }

    type B interface{
        b() A;
    }
"""
        expect =""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_redeclared_variable_in_if_scope(self):
        input = """
    func main(){
        var a int;
        if (a<1){
            var a int;
            var b int;
            var b string;
        }
    }
"""
        expect = "Redeclared Variable: b\n"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_redeclared_variable_in_forbasic_scope(self):
        input = """
    func main(){
        var a int;
        for (a<1){
            var a int;
            var b int;
            var b string;
        }
    }
"""
        expect = "Redeclared Variable: b\n"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_redeclared_variable_in_forstep_scope(self):
        input = """
    func main(){
        var a int;
        for i := 0; i < 10; i += 1{
            var a int;
            var b int;
            var b string;
        }
    }
"""
        expect = "Redeclared Variable: b\n"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_redeclared_const_in_forEach_scope(self):
        input = """
    func main(){
        var a int;
        for index, value := range [5]int{1,2,3,4,5}{
            var a int;
            var b int;
            const b = 7;
        }
    }
"""
        expect = "Redeclared Constant: b\n"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_redeclared_init_var_forStep_scope(self):
        input = """
    func main(){
        var a int;
        for i := 0; i < 10; i += 1{
            var a int;
            var b int;
            var i string;
        }
    }
"""
        expect = "Redeclared Variable: i\n"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_redeclared_index_forEach_scope(self):
        input = """
    func main(){
        for index, value := range [5]int{1,2,3,4,5}{
            var index int;
            var b int;
            const b = 7;
        }
    }
""" 
        expect = "Redeclared Variable: index\n"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_redeclared_value_forEach_scope(self):
        input = """
    func main(){
        for index, value := range [5]int{1,2,3,4,5}{
            var value int;
            var b int;
            const b = 7;
        }
    }
""" 
        expect = "Redeclared Variable: value\n"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_redeclared_field_in_structLiteral(self):
        input= """
    func main(){
        const b = Person{name: "bao", name: "abc"}
    }
    type Person struct{
        name string;
    }
"""
        expect="Redeclared Field: name\n"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_undeclared_variable_init_var1(self):
        input = """
    var a int = (a+1)/2;
"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_undeclared_varible_init_var2(self):
        input = """
    var a int = (a*1)-2;
"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_undeclared_variable_init_var3(self):
        input = """
    var baodeptrai = (b%2);
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_undeclare_varible_init_var4(self):
        input = """
    var baodeptrai = (-2>b)||(-1<2);
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_undeclared_variable_init_var5(self):
        input = """
    var baodeptrai = a.b;
"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_undeclared_init_const(self):
        input ="""
    const a = b<=2;
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_undeclared_variable_in_funcbody(self):
        input ="""
    func main(){
        var a = -b >= -5;
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_undeclare_identifier_in_if(self):
        input = """
    func J97(a int){
        if(true){
            var a int = b;
        }
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_undeclared_identifier_in_for(self):
        input = """
    func J97(a int){
        for(true){
            var a int = b;
        }
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_undeclared_identifier_in_assign(self):
        input = """
    func chu7gao(a int){
        for(true){
            a:=b+1
        }
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_undeclared_identifier_in_assign1(self):
        input = """
    func chu7gao(a int){
        for(true){
            a+=b+1
        }
    }
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_undeclared_funcall_in_if(self):
        input = """
    func main(){
        if(false){
            if(true){
                b();
            }
        }
    }
"""
        expect = "Undeclared Function: b\n"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_undeclared_funcall_in_for(self):
        input = """
    func main(){
        var a int;
        for i := 0; i < 10; i += 1{
            oh_no_riel();
        }
    }
"""
        expect = "Undeclared Function: oh_no_riel\n"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_undeclared_arg_in_funcall(self):
        input = """
    func main(){
        var a int;
        for index, value := range [5]int{1,2,3,4,5}{
            b(c);
        }
    }
    func b(a int){
        return;
    }
"""
        expect = "Undeclared Identifier: c\n"
        self.assertTrue(TestChecker.test(input,expect,472))
    def test_recursion_funccall(self):
        input = """
    func main(){
        var a int;
        for index, value := range [5]int{1,2,3,4,5}{
            main();
        }
    }
    func b(a int){
        return;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_undeclared_method_call_in_struct(self):
        input = """
    func main(){
        var a mewmew;
        a.a();
    }
    type mewmew struct{
        a mewmew;
    }
"""
        expect = "Undeclared Method: a\n"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_undeclared_method_call_of_interface(self):
        input = """
    func main(){
        var a mewmew;
        a.a();
    }
    type mewmew interface{
        b() mewmew;
    }
"""
        expect = "Undeclared Method: a\n"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_recursion_method_call(self):
        input = """
    func main(){
        var a mewmew;
        a.a();
    }
    func(a mewmew) a(){
        a()
    }
    type mewmew struct{
        b mewmew;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_other_method_call_in_method_declared_struct(self):
        input = """
    func main(){
        var a mewmew;
        a.a();
    }
    func(a mewmew) a(){
        a.c();
    }
    func(a mewmew) c(){
        return;
    }
    type mewmew struct{
        b mewmew;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_access_fields_in_if_scope(self):
        input = """
    func main(){
        var b b;
        if(true){
            a:=b.b
        }
    }
    type b struct{
        b b;
    }
"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_redeclared_fields_in_if_scope(self):
        input = """
    func main(){
        var b b;
        if(true){
            a:=b.b
        }
    }
    type b struct{
        a b;
    }
"""
        expect = "Undeclared Field: b\n"
        self.assertTrue(TestChecker.test(input,expect,479))

#check hiệu lực của các biến khi ra khỏi scope của nó ví dụ như các biến đặc biệt ở for,...
    def test_out_scope_varible_in_global(self):
        input = """
    func main(){
        var b int;
    }
    var a = b;
"""
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_out_scope_varible_in_if(self):
        input = """
    func main(){
        var b int;
        if(true){
            var a int;
        }
        var c = a;
    }
"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_undeclared_identifier_in_basic_loop(self):
        input = """
    func main(){
        var b int;
        for i < 10 {
            return;
        }
    }
"""
        expect = "Undeclared Identifier: i\n"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_out_scope_varible_in_for_each(self):
        input = """
    func main(){
        var b int;
        for index, value := range [2]int{1,2} {
            return;
        }
        var c = index;
    }
"""
        expect = "Undeclared Identifier: index\n"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_out_scope_variable_in_for_step(self):
        input = """
    func main(){
        for i := 0; i < 10; i += 1 {
            return;
        }
        var a = i;
    }
"""
        expect = "Undeclared Identifier: i\n"
        self.assertTrue(TestChecker.test(input,expect, 484))
    
    def test_undeclared_with_op_assign(self):
        input = """
    func main(){
        a+=1;
    }
"""
        expect = "Undeclared Identifier: a\n"
        self.assertTrue(TestChecker.test(input,expect, 485))

    def test_type_mismatch_assign_with_mtype(self):
        input ="""
    func main(){
        a := b
    }
    func b(){
        main()
    }
"""
        expect="Type Mismatch: Assign(Id(a),Id(b))\n"
        self.assertTrue(TestChecker.test(input,expect, 486))

    def test_type_mismatch_assign1(self):
        input ="""
    func main(){
        var a float;
        var b int;
        a := b
    }

"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 487))

    def test_type_mismatch_assign2(self):
        input ="""
    func main(){
        var a float;
        var b int;
        b := a
    }

"""
        expect="Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 488))

    def test_type_mismatch_assign3(self):
        input ="""
    func main(){
        var a float;
        var b string;
        b := a
    }

"""
        expect="Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 489))

    def test_type_mismatch_assign4(self):
        input ="""
    func main(){
        var a int;
        var b string;
        b := a
    }

"""
        expect="Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 490))

    def test_type_mismatch_assign5(self):
        input ="""
    func main(){
        var a int;
        var b Vjp;
        b := a
    }
    type Vjp struct{
        a int
    }
"""
        expect="Type Mismatch: Assign(Id(b),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 491))

    def test_type_assign_variable_with_array_literal(self):
        input ="""
    func main(){
        a:= [3]int{1,2,3}
        for index, value := range a{
            main();
        }
    }
    type Vjp struct{
        a int
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 492))

    def test_type_assign_variable_with_struct_literal(self):
        input ="""
    func main(){
        a:= Vjp{};
    }
    type Vjp struct{
        a int
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 493))

    def test_assign_struct_for_struct_same_name(self):
        input ="""
    func main(){
        a:= Vjp{};
        b := a;
    }
    type Vjp struct{
        a int
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 494))

    def test_assign_struct_for_struct_diff_name(self):
        input ="""
    func main(){
        a:= Vjp{};
        var b Pro = a;
    }
    type Vjp struct{
        a int
    }
    type Pro struct{
        a int
    }
"""
        expect="Type Mismatch: VarDecl(b,Id(Pro),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 495))

    def test_assign_interface_for_interface_same_name(self):
        input ="""
    func main(){
        var a Vjp;
        var b Vjp =a;
    }
    type Vjp interface{
        a();
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 496))

    def test_assign_interface_for_interface_diff_name(self):
        input ="""
    func main(){
        var a Vjp;
        var b Pro =a;
    }
    type Vjp interface{
        a();
    }
    type Pro interface{
        a();
    }
"""
        expect="Type Mismatch: VarDecl(b,Id(Pro),Id(a))\n"
        self.assertTrue(TestChecker.test(input,expect, 497))

    def test_assign_struct_for_interface_imple_complete(self):
        input ="""
    func main(){
        var a Vjp;
        var b Pro; 
        b:=a;
    }
    type Vjp struct{
        b int;
    }
    func (v Vjp) a(){
        return;
    }
    type Pro interface{
        a();
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 498))
    
    def test_assign_struct_for_interface_imple_complete2(self):
        input ="""
    func main(){
        var a Vjp;
        var b Pro; 
        b:=a;
    }
    type Vjp struct{
        c int;
    }
    func (v Vjp) b(){
        return;
    }
    func (v Vjp) a(){
        return;
    }
    type Pro interface{
        a();
        b();
    }
"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 499))

    def test_assign_array(self):
        input ="""
    var a [5][2]int = [5]int{1,2,3,4,5}
"""
        expect="Type Mismatch: VarDecl(a,ArrayType(IntType,[IntLiteral(5),IntLiteral(2)]),ArrayLiteral([IntLiteral(5)],IntType,[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))\n"
        self.assertTrue(TestChecker.test(input,expect, 500))

    def test_check_compatible_type_in_param(self):
        input ="""
    func main(){
        var b int;
        var c Person;
        a(b, c);
    }
    func a(x float, y Person){

    }
    type Person struct{
        age int;
    }

"""
        expect=""
        self.assertTrue(TestChecker.test(input,expect, 501))
#     def test_use_funcname_as_arg(self):
#         input = """
#     func main(){
#         var a int;
#         for index, value := range [5]int{1,2,3,4,5}{
#             b(b);
#         }
#     }
#     func b(a int){
#         return;
#     }
# """
#         expect = "Type Mismatch: FuncCall(b,[Id(b)])\n"
#         self.assertTrue(TestChecker.test(input,expect,493))


#     def test_const_init_by_other_const_init(self):
#         input = """
#     const a = 1;
#     const b = a;
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,493))

#     def test_const_init_by_other_variable(self):
#         input = """
#     var a = 1;
#     const b = a;
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,494))

#     def test_struct_and_interface_depend_on_together(self):
#         input = """
#     type A struct {
#         a B;
#     }

#     type B interface{
#         b() A;
#     }
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,495))

    
        
#     def test_function_with_many_return(self):
#         input = """
#         func WHO(a boolean) int{
#             if(a){ return true;}
#             return 1;
#         }
# """
#         expect = "Type Mismatch: FuncDecl(WHO,[ParDecl(a,BoolType)],IntType,Block([If(Id(a),Block([Return(BooleanLiteral(true))])),Return(IntLiteral(1))]))\n"
#         self.assertTrue(TestChecker.test(input,expect,496))

#     def test_function_with_many_return_in_deepblock(self):
#         input = """
#         func WHO(a boolean) boolean{
#             if(a){
#                 if(true){
#                     return 1;
#                 }
#                 return false
#             }
#             return false;
#         }
# """
#         expect = "Type Mismatch: FuncDecl(WHO,[ParDecl(a,BoolType)],BoolType,Block([If(Id(a),Block([If(BooleanLiteral(true),Block([Return(IntLiteral(1))])),Return(BooleanLiteral(false))])),Return(BooleanLiteral(false))]))\n"
#         self.assertTrue(TestChecker.test(input,expect,497))

# #test gán struct cho interface khi chưa đủ method, khi nhiều hơn
# #cần viết undeclared id trong các expr
# #viết test thể hiện thứ tự sử dụng scope
# #Viết test nếu arraycell lớn hơn số chiều của mảng ?
# #Kiểm tra return nằm sâu bên trong các block khác thì func có check đúng ko
# #Nhớ check tên hàm bị dùng như var
#     def test_type_mismatch(self):
#         input = """var a int = 1.2;"""
#         expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
#         self.assertTrue(TestChecker.test(input,expect,498))

#     def test_undeclared_type_in_structLiteral(self):
#         input = """
#         func main(){
#             var a = Person{name: "Alice", age: 30}
#         }
# """     
#         expect = "Undeclared Identifier: Person\n"
#         self.assertTrue(TestChecker.test(input,expect,499))

#     def test_assign_mismatch(self):
#         input="""
#         func main(){
#         var a int;
#             a:=true;
#         }
# """
#         expect ="Type Mismatch: Assign(Id(a),BooleanLiteral(true))\n"
#         self.assertTrue(TestChecker.test(input,expect,500))

#     def test_create_undeclared_varible(self):
#         input="""
#         func main(){
#             a:=true;
#             var b boolean = a;
#         }
# """
#         expect =""
#         self.assertTrue(TestChecker.test(input,expect,501))

#     def test_init_value_of_const(self):
#         input="""
#     const c = 2*3
#     const a = 1+c
#     var b int = a;
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input,expect,502))