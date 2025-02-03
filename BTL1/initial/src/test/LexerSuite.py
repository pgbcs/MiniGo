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
        """test operator assign"""
        self.assertTrue(TestLexer.checkLexeme("a=b","a,=,b,<EOF>",141))
    def test_operator_plus_assign(self):
        """test operator plus assign"""
        self.assertTrue(TestLexer.checkLexeme("a+=b","a,+=,b,<EOF>",142))
    def test_operator_minus_assign(self):
        """test operator minus assign"""
        self.assertTrue(TestLexer.checkLexeme("a-=b","a,-=,b,<EOF>",143))
    def test_operator_multiply_assign(self):
        """test operator multiply assign"""
        self.assertTrue(TestLexer.checkLexeme("a*=b","a,*=,b,<EOF>",144))
    def test_operator_divide_assign(self):
        """test operator divide assign"""
        self.assertTrue(TestLexer.checkLexeme("a/=b","a,/=,b,<EOF>",145))
    def test_operator_mod_assign(self):
        """test operator mod assign"""
        self.assertTrue(TestLexer.checkLexeme("a%=b","a,%=,b,<EOF>",146))
    def test_operator_select(self):
        """test operator select"""
        self.assertTrue(TestLexer.checkLexeme("a.b","a,.,b,<EOF>",147))
    def test_operator_select_chain(self):
        """test operator select chain"""
        self.assertTrue(TestLexer.checkLexeme("a.b.c","a,.,b,.,c,<EOF>",148))
    def test_consecutive_operators1(self):
        """test consecutive operators"""
        self.assertTrue(TestLexer.checkLexeme("a+++b---c","a,+,+,+,b,-,-,-,c,<EOF>",149))
    def test_consecutive_operators2(self):
        """test consecutive operators"""
        self.assertTrue(TestLexer.checkLexeme("a&&&b|||c","a,&&,ErrorToken &",150))
    def test_consecutive_operators3(self):
        """test consecutive operators"""
        self.assertTrue(TestLexer.checkLexeme("num**2", "num,*,*,2,<EOF>", 151))
    def test_operators_in_string(self):
        """test operators in string"""
        self.assertTrue(TestLexer.checkLexeme("\"a+b\"","\"a+b\",<EOF>",152))
    def test_operators_with_whitespace(self):
        """test operators with whitespace"""
        self.assertTrue(TestLexer.checkLexeme("x\t*\ty", "x,*,y,<EOF>", 153))
    def test_operators_with_complex_expression(self):
        """test operators with complex expression"""
        self.assertTrue(TestLexer.checkLexeme("a+b*c/d-e","a,+,b,*,c,/,d,-,e,<EOF>",154))
    def test_operators_in_comment1(self):
        """Test operators inside comments"""
        self.assertTrue(TestLexer.checkLexeme("// This is a comment with + - * /", "<EOF>", 155))
    def test_operators_in_comment2(self):
        """Test operators inside comments"""
        self.assertTrue(TestLexer.checkLexeme("/* == != >= <= */", "<EOF>", 156))
    
    #test seperators
    def test_seperator_comma(self):
        """test seperator comma"""
        self.assertTrue(TestLexer.checkLexeme("a,b","a,,,b,<EOF>",157))
    def test_seperator_semicolon(self):
        """test seperator semicolon"""
        self.assertTrue(TestLexer.checkLexeme("a;b","a,;,b,<EOF>",158))
    def test_seperator_comma_with_bracket(self):
        """test seperator comma with bracket"""
        self.assertTrue(TestLexer.checkLexeme("a,(b,c)","a,,,(,b,,,c,),<EOF>",159))
    def test_seperator_comma_with_brace(self):
        """test seperator comma with brace"""
        self.assertTrue(TestLexer.checkLexeme("a,{b,c}","a,,,{,b,,,c,},<EOF>",160))
    def test_seperator_comma_with_square_bracket(self):
        """test seperator comma with square bracket"""
        self.assertTrue(TestLexer.checkLexeme("a,[b,c]","a,,,[,b,,,c,],<EOF>",161))
    def test_separators_in_array_declaration(self):
        """test separators in array declaration"""
        self.assertTrue(TestLexer.checkLexeme("arr := [1, 2, 3];", "arr,:=,[,1,,,2,,,3,],;,<EOF>", 162))
    def test_separators_with_complex_code(self):
        """test separators with complex code"""
        self.assertTrue(TestLexer.checkLexeme("""func foo(a int, b float) {
                arr := [1, 2, 3];
                if (a > b) { return; }
            }""", 
        "func,foo,(,a,int,,,b,float,),{,arr,:=,[,1,,,2,,,3,],;,if,(,a,>,b,),{,return,;,},},<EOF>", 163))

    #test literals
    #test integer literal
    def test_decimal_integer_literal(self):
        """test decimal integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123","var,a,=,123,<EOF>",164))
    def test_binary_integer_literal1(self):
        """test binary integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0b101","var,a,=,0b101,<EOF>",165))
    def test_binary_integer_literal2(self):
        """test binary integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0B101","var,a,=,0B101,<EOF>",166))
    def test_octal_integer_literal1(self):
        """test octal integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0o123","var,a,=,0o123,<EOF>",167))
    def test_octal_integer_literal2(self):
        """test octal integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0O123","var,a,=,0O123,<EOF>",168))
    def test_hexadecimal_integer_literal1(self):
        """test hexadecimal integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0x123","var,a,=,0x123,<EOF>",169))
    def test_hexadecimal_integer_literal2(self):
        """test hexadecimal integer literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 0X123","var,a,=,0X123,<EOF>",170))

    #test floating-point literal
    def test_floating_point(self):
        """test floating-point literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.0","var,a,=,123.0,<EOF>",171))
    def test_floating_point_with_no_fractional_part(self):
        """test floating-point literal with no fractional part"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.","var,a,=,123.,<EOF>",172))
    def test_floating_point_with_no_integral_part(self):
        """test floating-point literal with no integral part"""
        self.assertTrue(TestLexer.checkLexeme("var a = .123","var,a,=,.,123,<EOF>",173))
    def test_floating_point_with_exponent1(self):
        """test floating-point literal with exponent"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.e10","var,a,=,123.e10,<EOF>",174))
    def test_floating_point_with_exponent2(self):
        """test floating-point literal with exponent"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.1E10","var,a,=,123.1E10,<EOF>",175))
    def test_floating_point_with_negative_exponent(self):
        """test floating-point literal with negative exponent"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.e-10","var,a,=,123.e-10,<EOF>",176))
    def test_floating_point_with_positive_exponent(self):
        """test floating-point literal with positive exponent"""
        self.assertTrue(TestLexer.checkLexeme("var a = 123.2E+10","var,a,=,123.2E+10,<EOF>",177))
    
    #test string literal
    def test_string_literal(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = \"abc\"","var,a,=,\"abc\",<EOF>",178))
    def test_string_literal_with_escape_sequence(self):
        """test string literal with escape sequence"""
        self.assertTrue(TestLexer.checkLexeme("var a = \"\\\"abc\\\"\"","var,a,=,\"\\\"abc\\\"\",<EOF>",179))
    def test_string_literal_with_all_escape_sequence(self):
        """test string literal with all escape sequence"""
        self.assertTrue(TestLexer.checkLexeme("var a = \"\\n\\t\\r\\\\\\\"\"", "var,a,=,\"\\n\\t\\r\\\\\\\"\",<EOF>", 180))
    def test_empty_string_literal(self):
        """Test empty string"""
        self.assertTrue(TestLexer.checkLexeme('""', '"",<EOF>', 181))
    def test_string_literal_with_mixed_content(self):
        """Test string with mixed letters, numbers, and symbols"""
        self.assertTrue(TestLexer.checkLexeme('"Hello123!@#"', 
                                              '"Hello123!@#",<EOF>', 182))
    def test_string_literal_with_newline(self):
        """Test string with newline character"""
        self.assertTrue(TestLexer.checkLexeme("\"Hello \n world!\"", 
                                              'Unclosed string: "Hello ', 183))
    def test_string_literal_with_double_quote(self):
        """Test string with double quote character"""
        self.assertTrue(TestLexer.checkLexeme('"Hello \\"world\\"!"', 
                                              '"Hello \\"world\\"!",<EOF>', 184))
    def test_unclosed_string(self):
        """Test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme('"Hello', 'Unclosed string: "Hello', 185))
    def test_string_literal_with_triple_quote(self):
        """Test string with triple quote"""
        self.assertTrue(TestLexer.checkLexeme('"""Hello"""', '"","Hello","",<EOF>', 186))
    def test_string_literal_with_tab_escape_sequence(self):
        """Test string with tab escape sequence"""
        self.assertTrue(TestLexer.checkLexeme('"Hello\tworld!"', '"Hello\tworld!",<EOF>', 187))
    def test_string_literal_with_illigal_escape_sequence(self):
        """Test string with illigal escape sequence"""
        self.assertTrue(TestLexer.checkLexeme('"Hello \\a world!"', 'Illegal escape in string: "Hello \\a', 188))
    
    #test boolean literal
    def test_boolean_literal_true(self):
        """test boolean literal true"""
        self.assertTrue(TestLexer.checkLexeme("var a = true","var,a,=,true,<EOF>",189))
    def test_boolean_literal_false(self):
        """test boolean literal false"""
        self.assertTrue(TestLexer.checkLexeme("var a = false","var,a,=,false,<EOF>",190))
    #test nil literal
    def test_nil_literal(self):
        """test nil literal"""
        self.assertTrue(TestLexer.checkLexeme("var a = nil","var,a,=,nil,<EOF>",191))
    
    #test wrong token
    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",192))
    
    def test_identifier_contain_keyword(self):
        """test identifier contain keyword"""
        self.assertTrue(TestLexer.checkLexeme("ifelse","ifelse,<EOF>",193))
    def test_float_with_double_point(self):
        """test float with double point"""
        self.assertTrue(TestLexer.checkLexeme("123..123","123.,.,123,<EOF>",194))
    def test_string_literal_with_many_backslash(self):
        """test string with many backslash"""
        self.assertTrue(TestLexer.checkLexeme("\"\\\"\\\"\"","\"\\\"\\\"\",<EOF>",195))
    def test_wrong_token2(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("func foo(x, y: int) {}", "func,foo,(,x,,,y,ErrorToken :", 196))
    #more test cases
    def test_more_test_cases1(self):
        """test more test cases"""
        self.assertTrue(TestLexer.checkLexeme("a := 1; b := 2;", "a,:=,1,;,b,:=,2,;,<EOF>", 197))
    def test_more_test_cases2(self):
        """test complex code"""
        self.assertTrue(TestLexer.checkLexeme("""func foo(a int, b float) {
            arr := [1, 2, 3];
            if (a > b) { return; }
        }""", 
        "func,foo,(,a,int,,,b,float,),{,arr,:=,[,1,,,2,,,3,],;,if,(,a,>,b,),{,return,;,},},<EOF>", 198))
    def test_more_test_cases3(self):
        """test complex code"""
        self.assertTrue(TestLexer.checkLexeme("""func foo(a int, b float) {
            arr := [1, 2, 3];
            if (a > b) { return; }
        }""", 
        "func,foo,(,a,int,,,b,float,),{,arr,:=,[,1,,,2,,,3,],;,if,(,a,>,b,),{,return,;,},},<EOF>", 199))

    def test_error_token11(self):
        # Numeric literal with an extra dot causing a malformed number.
        # The lexer should form the first valid token "1.2" and then report the extra '.' as an error.
        self.assertTrue(TestLexer.checkLexeme("1.2.3", "1.2,ErrorToken .", 281))
    # def test_string_literal_with_single_quote(self):
    #     """Test string with single quote character"""
    #     self.assertTrue(TestLexer.checkLexeme("'Hello \\'world\\'!'", 
    #                                           "'Hello \\'world\\'!',<EOF>", 200))