import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,303))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,305))
    #test variable declare
    def test_scalar_variable_declare1(self):
        input = """var i int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))
    def test_scalar_variable_declare2(self):
        input = """var i boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,307))
    def test_scalar_variable_declare_with_struct_type(self):
        input = """var i foo;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,308))
    def test_scalar_variable_with_init(self):
        input = """var i int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,309))
    def test_scalar_variable_missing_type(self):
        input = """var i = \"hello world\";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,310))
    def test_scalar_variable_missing_id(self):
        input = """var = 1;"""
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.checkParser(input,expect,311))
    
    #constant declare
    def test_constant_declare(self):
        input = """const Pi = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))
    def test_constant_declare_missing_id(self):
        input = """const = 3.14;"""
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.checkParser(input,expect,313))
    def test_constant_declare_missing_value(self):
        input = """const Pi;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.checkParser(input,expect,314))
    def test_constant_declare_missing_equal(self):
        input = """const Pi 3.14;"""
        expect = "Error on line 1 col 10: 3.14"
        self.assertTrue(TestParser.checkParser(input,expect,315))
    def test_constant_init_by_var(self):
        input = """const Pi = i;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,316))

    #array declare
    def test_array_declare_without_init(self):
        input = """var a [5] int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,317))
    def test_array_declare_without_init_many_dim(self):
        input = """var a [5][5][10][10] string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,318))
    def test_array_declare_without_size(self):
        input = """var a [] int;"""
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.checkParser(input,expect,319))
    def test_array_declare_with_negative_size(self):
        input = """var a [-5] int;"""
        expect = "Error on line 1 col 8: -"
        self.assertTrue(TestParser.checkParser(input,expect,320))
    def test_array_declare_with_init(self):
        input = """var a [5] int = [5] int{1,2,3,4,5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,321))
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,322))
    def test_array_declare_with_init_not_enough_element(self):
        input = """var a [5] int = [5] int{1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,323))
    def test_array_declare_with_init_too_many_element(self):
        input = """var a [5] int = [5] int{1,2,3,4,5,6};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,324))
    def test_array_declare_with_not_equal_dim(self):
        input = """var a [1][2] int = [2][1]int{{1},{2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,325))
    def test_array_declare_with_not_enough_dim(self):
        input = """var a [1][2] int = [1]int{1};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,326))
    #struct declare
    def test_struct_declare(self):
        input = """type foo struct {
            a int;
            b float64;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,327))
    def test_struct_declare_missing_id(self):
        input = """type struct {
            a int;
            b float;
        };"""
        expect = "Error on line 1 col 6: struct"
        self.assertTrue(TestParser.checkParser(input,expect,328))
    def test_struct_declare_missing_semi(self):
        input = """type foo struct {
            a int;
            b float
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,329))
    def test_struct_declare_method_in_struct(self):
        input = """type foo struct {
            a int;
            b float;
            func main() {};
        };"""
        expect = "Error on line 4 col 13: func"
        self.assertTrue(TestParser.checkParser(input,expect,330))
    def test_use_instance_of_struct(self):
        input = """type student struct {
            name string;
            age int;
        };
        var s student = student{name: "Nguyen Van A",age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,331))
    def test_declare_struct_method(self):
        input = """func (s student) getAge() int {
            return s.age
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,332))
    def test_call_method_of_struct(self):
        input = """PutStringLn(s.getAge());"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,333))
    def test_nested_struct(self):
        input ="""type student struct{
            name string;
            age int;
            type address struct{
                street string;
                city string;
            };
        };"""
        expect = "Error on line 4 col 13: type"
        self.assertTrue(TestParser.checkParser(input,expect,334))
    #test interface declare
    def test_interface_declare(self):
        input = """type Calculator interface {
Add(x, y int) int;
Subtract(a, b float, c int) float;
Reset()
SayHello(name string)
};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,335))
    def test_interface_declare_missing_id(self):
        input = """type interface {
Add(x, y int) int;
Subtract(a, b float, c int) float;
Reset()
SayHello(name string)
};"""
        expect = "Error on line 1 col 6: interface"
        self.assertTrue(TestParser.checkParser(input,expect,336))
    
    #test function declare
    def test_function_declare(self):
        input = """func main() {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,337))
    def test_function_declare_with_param(self):
        input = """func main(a int, b float, c string) {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,338))
    def test_function_declare_with_return(self):
        input = """func main() int {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,339))
    def test_function_declare_with_param_and_return(self):
        input = """func main(a int, b float, c string) int {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,340))
    def test_function_declare_with_param_and_return_and_body(self):
        input = """func main(a int, b float, c string) int {
            return 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,341))
    def test_function_declare_with_param_sharing_same_type(self):
        input = """func main(a, b, c int) int {
            return 1;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,342))
    
    #test expression
    def test_complex_arithmetic_operators1(self):
        input = """func main() {
            a = b + c - d * e / f % g;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,343))    
    def test_complex_arithmetic_operators2(self):
        input = """func main() {
            a = b + c - d * e / f % g;
            b = a * c / d % e + f - g;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,344))
    def test_complex_arithmetic_operators3(self):
        input = """func main() {
            a = b + c - d * e / f % g;
            b = a * c / d % e + f - g;
            c = a + b + c + d + e;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,345))
    def test_complex_arithmetic_operators4(self):
        input = """func main() {
            a = a-b+c*d/e%f+g;
            b = d*e/f%g+a;
            c = e+ 2*f - 3/g + 4*h + 5+i;
            d = (a+b)*c/d;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,346))

    def test_relational_operators1(self):
        input = """func main() {
            bao = oba == boa;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,347))
    def test_relational_operators2(self):
        input = """func main() {
            bdh = sda != cdss;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,348))
    def test_relational_operators3(self):
        input =  """X = y >= z + 1"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,349))
    def test_relational_operators4(self):
        input =  """X = y <= z * 732004"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,350))
    def test_relational_operators5(self):
        input =  """X = y < z - 1505"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,351))
    def test_relational_operators6(self):
        input =  """X = y > z / 2225"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,352))
    #khai báo hàm lồng hàm thì sao
    #test lại các declare với expr