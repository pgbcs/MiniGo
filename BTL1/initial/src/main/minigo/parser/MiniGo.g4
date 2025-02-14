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

program  : (decl|stmt)+ EOF;

decl: funcdecl | structdecl | interfacedecl | methodimple | blockdecl;
stmt: endstmt | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | callstmt | returnstmt;
blockdecl: vardecl | constdecl;
// mainfunc: FUNC 'main' LPAREN RPAREN LBRACE RBRACE endstmt;

//variable declaration
vardecl: (normal_vardecl_init | normal_vardecl_non_init |arr_vardecl) endstmt;

//normal variable declaration
normal_vardecl_non_init: VAR ID typedecl;
normal_vardecl_init: VAR ID typedecl? ASSIGN expr;

// //normal variable declaration
// normal_vardecl: EQUAL expr | typedecl (EQUAL expr)?;
//array variable declaration
arr_vardecl: VAR ID (arr_dim+ typedecl (ASSIGN arr_dim+ typedecl list_value)? | ASSIGN arr_dim+ typedecl list_value);

//có thể dùng một mảng toàn nil???
list_value: LBRACE (list_value (COMMA list_value)* | expr (COMMA expr)*) RBRACE;


//struct
structdecl: TYPE ID STRUCT LBRACE fielddecl* RBRACE endstmt;

fielddecl: ID (arr_dim)* typedecl endstmt;

// struct instance
structinst: ID LBRACE fieldinstlist RBRACE;

fieldinstlist: (fieldinst (COMMA fieldinst)*) | ; 

fieldinst: ID COLON expr;

//interface
interfacedecl: TYPE ID INTERFACE LBRACE methoddecl* RBRACE endstmt;

methoddecl: ID LPAREN param_list RPAREN typedecl? endstmt;

//TODO: add function body
//fucntion declaration
funcdecl: FUNC ID LPAREN param_list RPAREN returntype? LBRACE (stmt|blockdecl)* RBRACE endstmt;

methodimple: FUNC LPAREN ID ID RPAREN ID LPAREN param_list RPAREN returntype? LBRACE (stmt|blockdecl)* RBRACE endstmt;

returntype: typedecl | arr_dim+ typedecl;

param_list: param_group_prime | ;//need test without ?
param_group_prime: param_group (COMMA param_group_prime) | param_group;
param_group: param_mem_list (typedecl | arr_dim+ typedecl);
param_mem_list: ID COMMA param_mem_list | ID;

//constant declaration
constdecl: CONST ID ASSIGN expr endstmt; //what happend if assign a variable to a constant?

funccall: ID LPAREN (actualparam (COMMA actualparam)*)? RPAREN;

methodcall: ID SELECTOR ID LPAREN (actualparam (COMMA actualparam)*)? RPAREN;

actualparam: expr | funccall | methodcall | var;


//expression
expr: expr OR factor1 | factor1;
factor1: factor1 AND factor2 | factor2;
factor2: factor2 (EQUAL| NOT_EQUAL | LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) factor3 | factor3;
factor3: factor3 (PLUS | MINUS) factor4 | factor4;
factor4: factor4 (MUL | DIV | MOD) factor5 | factor5;
factor5: (MINUS | NOT) factor5 | factor6;
factor6: value | LPAREN expr RPAREN;

var: ID (arr_dim_acc | .ID)*;
arr_lit: arr_dim+ typedecl list_value;
arr_dim_acc: LBRACK expr RBRACK;
//assignment
assignstmt: var assign expr endstmt;

assign: SHORT_ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

//value declaration
value: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | structinst | var | structinst | arr_lit;

//type declaration
typedecl: INT | FLOAT | STRING | BOOLEAN | ID;

// type_with_init: INT EQUAL DEC_LIT | FLOAT EQUAL FLOAT_LIT | STRING EQUAL STRING_LIT | BOOLEAN EQUAL TRUE | BOOLEAN EQUAL FALSE;

//array dimension
arr_dim: LBRACK (DEC_LIT | ID) RBRACK; //ID is constant name

//TODO: need check again
endstmt: SEMICO;


ifstmt: IF LPAREN expr RPAREN LBRACE (stmt | blockdecl)* RBRACE (ELSE IF LPAREN expr RPAREN LBRACE (stmt|blockdecl)* RBRACE)* (ELSE LBRACE (stmt | decl)* RBRACE)? endstmt;
forstmt: FOR expr LBRACE (stmt | blockdecl)* RBRACE endstmt
 | FOR (assignstmt | normal_vardecl_init) expr SEMICO updatestmt LBRACE (stmt | blockdecl)* RBRACE endstmt
 | FOR ID COMMA ID SHORT_ASSIGN RANGE ( ID | arr_lit) LBRACE (stmt | blockdecl)* RBRACE endstmt;

updatestmt: var assign expr;

breakstmt: BREAK endstmt;
continuestmt: CONTINUE endstmt;
callstmt: (funccall | methodcall) endstmt;
returnstmt: RETURN expr? endstmt;

//skip comments
// Skip single-line comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;

fragment ALLOWED_TEXT: 
    ( ~[*/] 
    | '*'+ ~[/]  
    | '/'+ ~[*]
    )* ('/'+| '*'+)?;

// Skip multi-line comments
BLOCK_COMMENT: '/*' ALLOWED_TEXT BLOCK_COMMENT* ALLOWED_TEXT '*/' -> skip;

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


UNCLOSE_STRING: '"' (ESC|~[\r\n"\\])* /*[\r\n]?*/;
// UNCLOSE_STRING: '"' (ESC|~["\\])* '"'?;
ILLEGAL_ESCAPE: '"' (ESC|~[\r\n"\\])* '\\' .?; // throw from start to escape char
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
NL: '\n'{
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


/*update 14/2/2025: 
remove ASSIGN in assign stmt,
remove ID in arr_acc
modify paramlist
modify forstmt
add array literal
*/

/*if in block not allow empty statement, I will modify: 
ifstmt: IF LPAREN expr RPAREN LBRACE (stmt | decl)+ RBRACE (ELSE IF LPAREN expr RPAREN LBRACE (stmt|decl)+ RBRACE)* (ELSE LBRACE (stmt | decl)+ RBRACE)? endstmt;
forstmt: FOR expr LBRACE (stmt | decl)+ RBRACE endstmt 
        | FOR (assignstmt | normal_vardecl_init) SEMICO expr SEMICO assignstmt LBRACE (stmt | decl)+ RBRACE endstmt
        | FOR ID COMMA ID SHORT_ASSIGN RANGE ( ID | typedecl arr_dim+ list_value) LBRACE (stmt | decl)+ RBRACE endstmt;
funcdecl: FUNC ID LPAREN param_list RPAREN typedecl? LBRACE (stmt|decl)+ RBRACE endstmt;
methodimple: FUNC LPAREN ID ID RPAREN ID LPAREN param_list RPAREN typedecl? LBRACE (stmt|decl)+ RBRACE endstmt;
interfacedecl: TYPE ID INTERFACE LBRACE methoddecl+ RBRACE endstmt;
structdecl: TYPE ID STRUCT LBRACE fielddecl+ RBRACE endstmt;
*/