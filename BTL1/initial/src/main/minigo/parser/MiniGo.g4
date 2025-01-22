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

program  : decl+ EOF ;

decl: funcdecl | vardecl  ;

vardecl: VAR ID INT SEMICO ;

funcdecl: FUNC ID LPAREN RPAREN LBRACE RBRACE SEMICO ;

//skip comments
COMMENT: '//' ~[\r\n]* -> skip | '/*' .*? '*/' -> skip;

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
STRING_LIT: '"' (ESC|~["\\])* '"';
//boolean literals
BOOL_LIT: 'true' | 'false';
//nil literal
NIL_LIT: 'nil';

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
fragment ESC: [\n\t\r\\"\\\\];

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;