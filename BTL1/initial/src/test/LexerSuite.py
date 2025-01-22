import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #test identifier
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",100))
    def test_upper_identifier(self):
        """test upper identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ABC","ABC,<EOF>",101))
    def test_mix_identifier(self):
        """test lower and upper identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aBC","aBC,<EOF>",102))
    def test_identifier_with_number(self):
        """test identifier with number"""
        self.assertTrue(TestLexer.checkLexeme("a123","a123,<EOF>",103))
    def test_identifier_with_underscore(self):
        """test identifier with underscore"""
        self.assertTrue(TestLexer.checkLexeme("_a_b_c","_a_b_c,<EOF>",104))
    def test_identifier_begin_with_number(self):
        """test identifier begin with number"""
        self.assertTrue(TestLexer.checkLexeme("123a","123,a,<EOF>",105))
    def test_long_identifier(self):
        """test long identifier"""
        long_identifier = "a"*100000
        self.assertTrue(TestLexer.checkLexeme(long_identifier,long_identifier+",<EOF>",106))

    #test comment
    def test_line_comment(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme("//abc","<EOF>",107))
    def test_block_comment(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme('''/*abc
                                                    cde*/''',"<EOF>",108))
    def test_mix_comment(self):
        """test mix comment"""
        self.assertTrue(TestLexer.checkLexeme('''//abc
                                                abc
                                                /*cde*/''',"abc,<EOF>",109))

    #test keywords
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",110))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",111))
    def test_keyword_break(self):
        """test keyword break"""
        self.assertTrue(TestLexer.checkLexeme("break;","break,;,<EOF>",112))
    def test_keyword_if_else(self):
        """test keyword if else"""
        self.assertTrue(TestLexer.checkLexeme("if (a==2){} else{}","if,(,a,==,2,),{,},else,{,},<EOF>",113))
    def test_keyword_return(self):
        """test keyword return"""
        self.assertTrue(TestLexer.checkLexeme("return 2;","return,2,;,<EOF>",114))
    def test_keyword_for(self):
        """test keyword for"""
        self.assertTrue(TestLexer.checkLexeme("for (i=0;i<10;i=i+1){}","for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,},<EOF>",115))
    def test_keyword_continue(self):
        """test keyword continue"""
        self.assertTrue(TestLexer.checkLexeme("continue;","continue,;,<EOF>",116))
    def test_keyword_type(self):
        """test keyword type"""
        self.assertTrue(TestLexer.checkLexeme("type Age int;","type,Age,int,;,<EOF>",117))
    def test_keyword_string(self):
        """test keyword string"""
        self.assertTrue(TestLexer.checkLexeme("var s string;","var,s,string,;,<EOF>",118))
    def test_keyword_float(self):
        """test keyword float"""
        self.assertTrue(TestLexer.checkLexeme("var f float;","var,f,float,;,<EOF>",119))
    def test_keyword_boolean(self):
        """test keyword boolean"""
        self.assertTrue(TestLexer.checkLexeme("var b boolean;","var,b,boolean,;,<EOF>",120))
    def test_keyword_struct(self):
        """test keyword struct"""
        self.assertTrue(TestLexer.checkLexeme("type abc struct {a int; b float;}","type,abc,struct,{,a,int,;,b,float,;,},<EOF>",121))
    def test_keyword_interface(self):
        """test keyword interface"""
        self.assertTrue(TestLexer.checkLexeme("type abc interface{func a();}","type,abc,interface,{,func,a,(,),;,},<EOF>",122))
    def test_keyword_const(self):
        """test keyword const"""
        self.assertTrue(TestLexer.checkLexeme("const a=2;","const,a,=,2,;,<EOF>",123))
    def test_keyword_nil(self):
        """test keyword nil"""
        self.assertTrue(TestLexer.checkLexeme("var a nil;","var,a,nil,;,<EOF>",124))
    def test_keyword_true(self):
        """test keyword true"""
        self.assertTrue(TestLexer.checkLexeme("var a true;","var,a,true,;,<EOF>",125))
    def test_keyword_false(self):
        """test keyword false"""
        self.assertTrue(TestLexer.checkLexeme("var a false;","var,a,false,;,<EOF>",126))
    
    #test operators
    def test_operator_plus(self):
        """test operator plus"""
        self.assertTrue(TestLexer.checkLexeme("a+b","a,+,b,<EOF>",127))
    def test_operator_minus(self):
        """test operator minus"""
        self.assertTrue(TestLexer.checkLexeme("a-b","a,-,b,<EOF>",128))
    def test_operator_multiply(self):
        """test operator multiply"""
        self.assertTrue(TestLexer.checkLexeme("a*b","a,*,b,<EOF>",129))
    def test_operator_divide(self):
        """test operator divide"""
        self.assertTrue(TestLexer.checkLexeme("a/b","a,/,b,<EOF>",130))
    def test_operator_mod(self):
        """test operator mod"""
        self.assertTrue(TestLexer.checkLexeme("a%b","a,%,b,<EOF>",131))
    def test_operator_and(self):
        """test operator and"""
        self.assertTrue(TestLexer.checkLexeme("a&&b","a,&&,b,<EOF>",132))
    def test_operator_or(self):
        """test operator or"""
        self.assertTrue(TestLexer.checkLexeme("a||b","a,||,b,<EOF>",133))
    def test_operator_not(self):
        """test operator not"""
        self.assertTrue(TestLexer.checkLexeme("!a","!,a,<EOF>",134))
    def test_operator_equal(self):
        """test operator equal"""
        self.assertTrue(TestLexer.checkLexeme("a==b","a,==,b,<EOF>",135))
    def test_operator_not_equal(self):
        """test operator not equal"""
        self.assertTrue(TestLexer.checkLexeme("a!=b","a,!=,b,<EOF>",136))
    def test_operator_less_than(self):
        """test operator less than"""
        self.assertTrue(TestLexer.checkLexeme("a<b","a,<,b,<EOF>",137))
    def test_operator_less_than_or_equal(self):
        """test operator less than or equal"""
        self.assertTrue(TestLexer.checkLexeme("a<=b","a,<=,b,<EOF>",138))
    def test_operator_greater_than(self):
        """test operator greater than"""
        self.assertTrue(TestLexer.checkLexeme("a>b","a,>,b,<EOF>",139))
    def test_operator_greater_than_or_equal(self):
        """test operator greater than or equal"""
        self.assertTrue(TestLexer.checkLexeme("a>=b","a,>=,b,<EOF>",140))
    def test_operator_assign(self):
        pass
    

    # #test wrong token
    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",114))