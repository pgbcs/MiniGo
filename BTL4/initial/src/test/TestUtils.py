import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/minigo/parser/' in sys.path:
    sys.path.append('./main/minigo/parser/')
if os.path.isdir('../target/main/minigo/parser') and not '../target/main/minigo/parser/' in sys.path:
    sys.path.append('../target/main/minigo/parser/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = MiniGoLexer
Parser = MiniGoParser

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestLexer.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
    
    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir,str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+";"+str(tok.type)+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestParser.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir , str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestAST:
    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestAST.check(SOL_DIR,inputfile,num)
        dest = open(os.path.join(SOL_DIR,str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir,str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()

class TestChecker:
    @staticmethod
    def test(input,expect,num):       
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input       
        TestChecker.check(SOL_DIR,asttree,num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,asttree,num):  
        dest = open(os.path.join(soldir, str(num) + ".txt"),"w")     
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        TestCodeGen.check(SOL_DIR,asttree,num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,asttree,num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"),"w")
        try:
            codeGen.gen(asttree, path)
            classPreviewPATH = "../classPreview"
            subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/*.j",shell=True,stderr=subprocess.STDOUT)
            
        #     subprocess.run(
        #     f"java -jar {JASMIN_JAR} -d {classPreviewPATH}/{os.path.basename(path)} {path}/*.j",
        #     shell=True,
        #     check=True,
        #     stderr=subprocess.STDOUT
        # )
            
            subprocess.run("java -cp ./lib;. MiniGoClass",shell=True, stdout = f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        finally:
            f.close()
            
            
