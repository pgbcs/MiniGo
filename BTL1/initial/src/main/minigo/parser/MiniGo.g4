//id: 2210254
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : decl* mainfunc decl* EOF;

decl: funcdecl | vardecl;

mainfunc: FUNC 'main' LPAREN RPAREN LBRACE RBRACE endstmt;

//variable declaration
vardecl: VAR ID (normal_vardecl | arr_vardecl) endstmt;

//normal variable declaration
normal_vardecl: EQUAL expr | type (EQUAL expr)?;
//array variable declaration
arr_vardecl: arr_dim+ type (EQUAL arr_dim+ type list_value)? | EQUAL arr_dim+ type list_value;

//có thể dùng một mảng toàn nil???
list_value: '{' (list_value (COMMA list_value)* | expr (COMMA expr)*) '}';


//struct
structdecl: TYPE ID STRUCT LBRACE fielddecl* RBRACE endstmt;

fielddecl: ID type endstmt;

// struct instance
structinst: ID LBRACE fieldinst* RBRACE endstmt;

fieldinst: ID expr endstmt;

//interface
interfacedecl: TYPE ID INTERFACE LBRACE methoddecl* RBRACE endstmt;

methoddecl: ID LPAREN param_list RPAREN type? endstmt;

//fucntion declaration
funcdecl: FUNC ID LPAREN param_list RPAREN LBRACE RBRACE endstmt;

param_list: (ID type? (COMMA ID type?)*)?;//need test without ?

//constant declaration
//TODO: add expression
constdecl: CONST ID expr endstmt;



//expression
expr: expr OR factor1 | factor1;
factor1: factor1 AND factor2 | factor2;
factor2: factor2 (EQUAL| NOT_EQUAL | LESS | GREATER | LESS_OR_EQUAL | GREATER_OR_EQUAL) factor3 | factor3;
factor3: factor3 (PLUS | MINUS) factor4 | factor4;
factor4: factor4 (MUL | DIV | MOD) factor5 | factor5;
factor5: (MINUS | NOT) factor6 | factor6;
factor6: value | ID | LPAREN expr RPAREN;

//assignment
assignstmt: (ID arr_dim* (.ID)* ) assign expr endstmt;

assign: ASSIGN | SHORT_ASSIGN | PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

//value declaration
value: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | structinst | ID arr_dim* (.ID)*;

//type declaration
type: INT | FLOAT | STRING | BOOLEAN | ID;

// type_with_init: INT EQUAL DEC_LIT | FLOAT EQUAL FLOAT_LIT | STRING EQUAL STRING_LIT | BOOLEAN EQUAL TRUE | BOOLEAN EQUAL FALSE;

//array dimension
arr_dim: LBRACK (DEC_LIT | ID) RBRACK; //ID is constant name

//TODO: need check again
endstmt: SEMICO | NL;



//skip comments
// Skip single-line comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Skip multi-line comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;


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

// UNCLOSE_STRING: '"' (ESC|~["\\])* '"'?;
ILLEGAL_ESCAPE: '"' (ESC|~[\r\n"])* '\\'.; // throw from start to escape char
// ILLEGAL_ESCAPE: '"' (ESC|~[\r\n"])* '"';// throw whole string
UNCLOSE_STRING: '"' (ESC|~[\r\n"\\])* /*[\r\n]?*/;
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

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 



ERROR_CHAR: .;