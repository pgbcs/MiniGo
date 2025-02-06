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