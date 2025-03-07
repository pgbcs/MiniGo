//id: 2210254
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
prevToken = None
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk==self.NL:
        result = super().emit();
        result.text = ';'
        result.type = self.SEMICO
        self.prevToken = None
        return result  
    else:
        result = super().emit();
        self.prevToken = result
        return result;
}

options{
	language=Python3;
}

program  : decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | constdecl | structdecl | interfacedecl | funcdecl | methodimple;
vardecl: normal_vardecl | arr_vardecl;
normal_vardecl: normal_vardecl_without_init | normal_vardecl_with_init;
normal_vardecl_without_init: VAR ID typedecl SEMICO;
normal_vardecl_with_init: VAR ID typedecl? ASSIGN expr SEMICO;

typedecl: INT | FLOAT | STRING | BOOLEAN | ID;

arr_vardecl: arr_vardecl_without_init | arr_vardecl_with_init;
arr_vardecl_with_init: VAR ID (arrdimlist typedecl)? ASSIGN expr SEMICO; //chang from arrliterl to expr
arr_vardecl_without_init: VAR ID arrdimlist typedecl SEMICO;

arrdimlist: arrdim arrdimlist | arrdim;
arrdim: LBRACK (DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT | ID) RBRACK;
arrliteral: arrdimlist typedecl arrlistvalue;
arrlistvalue: LBRACE listvalue RBRACE;
listvalue: value_for_arr COMMA listvalue | value_for_arr;
value_for_arr: literalvalue_for_arr | arrlistvalue;
literalvalue_for_arr: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | structinst | ID;

constdecl: CONST ID ASSIGN expr SEMICO;

//struct declare, empty struct is allowed
structdecl: TYPE ID STRUCT structbody SEMICO;
structbody: LBRACE fieldlist RBRACE;
fieldlist: field fieldlist | ;
field: ID arrdimlist? typedecl SEMICO;
//struct instance
structinst: ID structinst_body;
structinst_body: LBRACE structinst_fieldlist RBRACE;
structinst_fieldlist: structinst_fieldprime | ;
structinst_fieldprime: structinst_field COMMA structinst_fieldprime | structinst_field;
structinst_field: ID COLON expr;

//interface declare, empty interface is allowed
interfacedecl: TYPE ID INTERFACE interfacebody SEMICO;
interfacebody: LBRACE methodlist RBRACE;
methodlist: method methodlist | ;
method: ID LPAREN paramlist RPAREN returntype? SEMICO;

//function declare, empty function is allowed
funcdecl: FUNC ID LPAREN paramlist RPAREN returntype? funcbody SEMICO;
paramlist: param_group_prime | ;
param_group_prime: param_group COMMA param_group_prime | param_group;
param_group: param_mem_list arrdimlist? typedecl;
param_mem_list: ID COMMA param_mem_list | ID;

funcbody: LBRACE stmtlist RBRACE;
stmtlist: stmt stmtlist | ;

returntype: arrdimlist? typedecl;

//method implementation
methodimple: FUNC LPAREN ID ID RPAREN ID LPAREN paramlist RPAREN returntype? methodimple_body SEMICO;
methodimple_body: LBRACE stmtlist RBRACE;

//expr
expr: expr OR expr0 | expr0;
expr0: expr0 AND expr1 | expr1;
expr1: expr1 (EQUAL | NOT_EQUAL | LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) expr2 | expr2;
expr2: expr2 (PLUS | MINUS) expr3 | expr3;
expr3: expr3 (MUL | DIV | MOD) expr4 | expr4;
expr4: (MINUS | NOT) expr4 | expr5;
// expr5: expr5 SELECTOR ID | expr5 LBRACK expr RBRACK | expr5 SELECTOR ID LPAREN arglist RPAREN | expr6;
expr5: expr5 SELECTOR ID 
    | expr5 SELECTOR ID LPAREN arglist RPAREN 
    | expr5 SELECTOR ID LPAREN arglist RPAREN arrdimlist_expr
    | expr5 SELECTOR ID arrdimlist_expr
    | expr6 arrdimlist_expr 
    | expr6;
expr6: subexpr | value;

arrdimlist_expr: arrdimlist_expr arrdim_expr | arrdim_expr;
arrdim_expr: LBRACK expr RBRACK;
// access_expr: SELECTOR ID | SELECTOR ID LPAREN arglist RPAREN;

value: literalvalue | funccall;//remove methodcall here
subexpr: LPAREN expr RPAREN;
literalvalue: literalvalue_for_arr | arrliteral;

funccall: ID LPAREN arglist RPAREN;
arglist: argprime | ;
argprime: expr COMMA argprime | expr;

// methodcall: expr accesslist LPAREN arglist RPAREN;
methodcall: methodcallbody methodcalltail;
methodcallbody: methodcallbody SELECTOR ID
    | methodcallbody SELECTOR ID LPAREN arglist RPAREN
    | methodcallbody SELECTOR ID LPAREN arglist RPAREN arrdimlist_expr
    | methodcallbody SELECTOR ID arrdimlist_expr
    | funccall arrdimlist_expr
    | ID arrdimlist_expr
    | funccall
    | ID;
methodcalltail: SELECTOR ID LPAREN arglist RPAREN;

stmt: vardecl | constdecl | assignstmt | returnstmt | ifstmt | forstmt | breakstmt | continuestmt | callstmt;
assignstmt: accesslist (SHORT_ASSIGN | otherassignop ) expr SEMICO;
accesslist: ID arrdimlist_expr
    | accesslist SELECTOR ID
    | accesslist SELECTOR ID arrdimlist_expr
    | ID;
// var: ID accesslist?;
// accesslist: accesslist  access | access;
// access: arrayaccess | structaccess;
// arrayaccess: LBRACK expr RBRACK;
// structaccess: SELECTOR ID;
otherassignop: PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

returnstmt: RETURN expr? SEMICO;

callstmt: (funccall| methodcall) SEMICO;

ifstmt: firstifstmt elseifstmtlist? SEMICO;
firstifstmt: IF LPAREN expr RPAREN ifstmtbody;
ifstmtbody: LBRACE stmtlist RBRACE;
elseifstmtlist: elseifstmt elseifstmtlist | elsestmt | elseifstmt;
elseifstmt: ELSE IF LPAREN expr RPAREN ifstmtbody;
elsestmt: ELSE ifstmtbody;

forstmt: basicforstmt | init_cond_update_forstmt |rangeforstmt;
basicforstmt: FOR expr forstmtbody SEMICO;
forstmtbody: LBRACE stmtlist RBRACE;
init_cond_update_forstmt: FOR init_for SEMICO expr SEMICO assign forstmtbody SEMICO;
init_for: assign | VAR ID typedecl? ASSIGN expr;
// assign: var assignop expr;
assign: accesslist (SHORT_ASSIGN|otherassignop) expr;
rangeforstmt: FOR ID COMMA ID SHORT_ASSIGN RANGE expr forstmtbody SEMICO;

breakstmt: BREAK SEMICO;

continuestmt: CONTINUE SEMICO;




/*****LEXER RULE******/
//skip comments
// Skip single-line comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;

fragment ALLOWED_TEXT: 
    ( ~[*/] 
    | '*'+ ~[/]  
    | '/'+ ~[*]
    )* ('/'+| '*'+)?;

// Skip multi-line comments
BLOCK_COMMENT: '/*' (ALLOWED_TEXT BLOCK_COMMENT)* ALLOWED_TEXT '*/' -> skip;

COLON: ':';

//keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_OR_EQUAL: '<=';
GREATER_OR_EQUAL: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
SHORT_ASSIGN: ':=';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
SELECTOR: '.';

//separator
COMMA: ',';
SEMICO: ';';

//literals
//interger literals
DEC_LIT: '0' | [1-9] DIGIT*;
BIN_LIT: '0' [bB] [01]+;
OCT_LIT: '0' [oO] [0-7]+;
HEX_LIT: '0' [xX] [0-9a-fA-F]+;
//floating-point literals
FLOAT_LIT: DIGIT+ '.' DIGIT* EXP?;


//string literals
STRING_LIT: '"' (ESC|~[\r\n"\\])* '"';


UNCLOSE_STRING: '"' (ESC|~[\r\n\\"])* /*[\r\n]?*/;
// UNCLOSE_STRING: '"' (ESC|~["\\])* '"'?;
ILLEGAL_ESCAPE: '"' (ESC|~[\r\n"\\])* '\\' .; // throw from start to escape char
// ILLEGAL_ESCAPE: '"' (ESC|~[\r\n"])* '"';// throw whole string

// //boolean literals
// BOOL_LIT: 'true' | 'false';
// //nil literal
// NIL_LIT: 'nil';

//identifiers
ID: (LETTER|'_') (DIGIT|LETTER|'_')* ;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';


fragment EXP: [eE] [+\-]? DIGIT+ ;
fragment DIGIT: [0-9] ;
fragment LETTER: [a-zA-Z] ;
// fragment ESC: [\n\t\r\\] | '\"';
fragment ESC: '\\' [ntr"\\];

// NL: '\n' -> skip; //skip newlines
//change newline to semicolon
NL: '\r'? '\n'{
    statement_end_tokens = {
    self.ID, self.DEC_LIT, self.BIN_LIT, self.OCT_LIT, self.HEX_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.NIL, self.STRING_LIT,
    self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
    self.RETURN, self.CONTINUE, self.BREAK,
    self.RPAREN, self.RBRACK, self.RBRACE
}
    if(self.prevToken == None):
        self.skip()
    elif self.prevToken.type not in statement_end_tokens:
        self.skip()
    };
WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 



ERROR_CHAR: .;


//kiểm tra lại các vị trí sử dụng expr
