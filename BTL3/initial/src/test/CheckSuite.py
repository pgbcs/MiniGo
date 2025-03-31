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


    def test_type_mismatch(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_undeclared_identifier(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,499))
  