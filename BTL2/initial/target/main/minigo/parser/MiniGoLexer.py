# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\6\n8\n\n\r\n\16\n9\3\13\3\13\3\13\3\13\3\f\6\fA\n")
        buf.write("\f\r\f\16\fB\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\2\2\20")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\3\2\4\3\2c|\5\2\13\13\17\17\"\"\2M\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\3\37\3\2\2\2\5#\3\2\2\2\7\'\3\2\2\2\t)\3")
        buf.write("\2\2\2\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21\64\3")
        buf.write("\2\2\2\23\67\3\2\2\2\25;\3\2\2\2\27@\3\2\2\2\31F\3\2\2")
        buf.write("\2\33H\3\2\2\2\35J\3\2\2\2\37 \7x\2\2 !\7c\2\2!\"\7t\2")
        buf.write("\2\"\4\3\2\2\2#$\7k\2\2$%\7p\2\2%&\7v\2\2&\6\3\2\2\2\'")
        buf.write("(\7=\2\2(\b\3\2\2\2)*\7h\2\2*+\7w\2\2+,\7p\2\2,-\7e\2")
        buf.write("\2-\n\3\2\2\2./\7*\2\2/\f\3\2\2\2\60\61\7+\2\2\61\16\3")
        buf.write("\2\2\2\62\63\7}\2\2\63\20\3\2\2\2\64\65\7\177\2\2\65\22")
        buf.write("\3\2\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2")
        buf.write("\29:\3\2\2\2:\24\3\2\2\2;<\7\f\2\2<=\3\2\2\2=>\b\13\2")
        buf.write("\2>\26\3\2\2\2?A\t\3\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2")
        buf.write("BC\3\2\2\2CD\3\2\2\2DE\b\f\2\2E\30\3\2\2\2FG\13\2\2\2")
        buf.write("G\32\3\2\2\2HI\13\2\2\2I\34\3\2\2\2JK\13\2\2\2K\36\3\2")
        buf.write("\2\2\5\29B\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ID = 9
    NL = 10
    WS = 11
    ERROR_CHAR = 12
    ILLEGAL_ESCAPE = 13
    UNCLOSE_STRING = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'int'", "';'", "'func'", "'('", "')'", "'{'", "'}'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


