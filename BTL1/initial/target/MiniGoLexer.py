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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\7\2\u0090\n\2\f\2\16\2\u0093")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009b\n\3\f\3\16\3\u009e")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3.\3.\3/\3/\3/\7/\u0157\n/\f/\16/\u015a")
        buf.write("\13/\5/\u015c\n/\3\60\3\60\3\60\6\60\u0161\n\60\r\60\16")
        buf.write("\60\u0162\3\61\3\61\3\61\6\61\u0168\n\61\r\61\16\61\u0169")
        buf.write("\3\62\3\62\3\62\6\62\u016f\n\62\r\62\16\62\u0170\3\63")
        buf.write("\6\63\u0174\n\63\r\63\16\63\u0175\3\63\3\63\7\63\u017a")
        buf.write("\n\63\f\63\16\63\u017d\13\63\3\63\5\63\u0180\n\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\7\65\u0187\n\65\f\65\16\65\u018a")
        buf.write("\13\65\3\65\3\65\3\66\3\66\3\66\7\66\u0191\n\66\f\66\16")
        buf.write("\66\u0194\13\66\3\66\3\66\3\66\3\67\3\67\3\67\7\67\u019c")
        buf.write("\n\67\f\67\16\67\u019f\13\67\38\38\58\u01a3\n8\38\38\3")
        buf.write("8\78\u01a8\n8\f8\168\u01ab\138\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\5?\u01bb\n?\3?\6?\u01be\n?\r?\16?")
        buf.write("\u01bf\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\3C\3D\6D\u01ce\n")
        buf.write("D\rD\16D\u01cf\3D\3D\3E\3E\3\u009c\2F\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}\2\177\2")
        buf.write("\u0081\2\u0083\2\u0085@\u0087A\u0089B\3\2\22\4\2\f\f\17")
        buf.write("\17\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz")
        buf.write("\5\2\62;CHch\6\2\f\f\17\17$$^^\5\2\f\f\17\17$$\4\2GGg")
        buf.write("g\4\2--//\3\2\62;\4\2C\\c|\7\2$$^^ppttvv\5\2\13\13\17")
        buf.write("\17\"\"\2\u01e7\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2")
        buf.write("\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u0096\3\2\2\2\7")
        buf.write("\u00a4\3\2\2\2\t\u00a7\3\2\2\2\13\u00ac\3\2\2\2\r\u00b0")
        buf.write("\3\2\2\2\17\u00b7\3\2\2\2\21\u00bc\3\2\2\2\23\u00c1\3")
        buf.write("\2\2\2\25\u00c8\3\2\2\2\27\u00d2\3\2\2\2\31\u00d9\3\2")
        buf.write("\2\2\33\u00dd\3\2\2\2\35\u00e3\3\2\2\2\37\u00eb\3\2\2")
        buf.write("\2!\u00f1\3\2\2\2#\u00f5\3\2\2\2%\u00fe\3\2\2\2\'\u0104")
        buf.write("\3\2\2\2)\u010a\3\2\2\2+\u010e\3\2\2\2-\u0113\3\2\2\2")
        buf.write("/\u0119\3\2\2\2\61\u011b\3\2\2\2\63\u011d\3\2\2\2\65\u011f")
        buf.write("\3\2\2\2\67\u0121\3\2\2\29\u0123\3\2\2\2;\u0126\3\2\2")
        buf.write("\2=\u0129\3\2\2\2?\u012b\3\2\2\2A\u012d\3\2\2\2C\u0130")
        buf.write("\3\2\2\2E\u0133\3\2\2\2G\u0136\3\2\2\2I\u0139\3\2\2\2")
        buf.write("K\u013b\3\2\2\2M\u013d\3\2\2\2O\u0140\3\2\2\2Q\u0143\3")
        buf.write("\2\2\2S\u0146\3\2\2\2U\u0149\3\2\2\2W\u014c\3\2\2\2Y\u014f")
        buf.write("\3\2\2\2[\u0151\3\2\2\2]\u015b\3\2\2\2_\u015d\3\2\2\2")
        buf.write("a\u0164\3\2\2\2c\u016b\3\2\2\2e\u0173\3\2\2\2g\u0181\3")
        buf.write("\2\2\2i\u0183\3\2\2\2k\u018d\3\2\2\2m\u0198\3\2\2\2o\u01a2")
        buf.write("\3\2\2\2q\u01ac\3\2\2\2s\u01ae\3\2\2\2u\u01b0\3\2\2\2")
        buf.write("w\u01b2\3\2\2\2y\u01b4\3\2\2\2{\u01b6\3\2\2\2}\u01b8\3")
        buf.write("\2\2\2\177\u01c1\3\2\2\2\u0081\u01c3\3\2\2\2\u0083\u01c5")
        buf.write("\3\2\2\2\u0085\u01c8\3\2\2\2\u0087\u01cd\3\2\2\2\u0089")
        buf.write("\u01d3\3\2\2\2\u008b\u008c\7\61\2\2\u008c\u008d\7\61\2")
        buf.write("\2\u008d\u0091\3\2\2\2\u008e\u0090\n\2\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0094\u0095\b\2\2\2\u0095\4\3\2\2\2\u0096\u0097\7\61")
        buf.write("\2\2\u0097\u0098\7,\2\2\u0098\u009c\3\2\2\2\u0099\u009b")
        buf.write("\13\2\2\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\3\2\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009f\u00a0\7,\2\2\u00a0\u00a1\7")
        buf.write("\61\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\3\2\2\u00a3")
        buf.write("\6\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7h\2\2\u00a6")
        buf.write("\b\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\u00aa\7u\2\2\u00aa\u00ab\7g\2\2\u00ab\n\3\2\2\2\u00ac")
        buf.write("\u00ad\7h\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\f\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2")
        buf.write("\u00b3\7v\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\16\3\2\2\2\u00b7\u00b8\7h\2\2\u00b8")
        buf.write("\u00b9\7w\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7e\2\2\u00bb")
        buf.write("\20\3\2\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7{\2\2\u00be")
        buf.write("\u00bf\7r\2\2\u00bf\u00c0\7g\2\2\u00c0\22\3\2\2\2\u00c1")
        buf.write("\u00c2\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4")
        buf.write("\u00c5\7w\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\24\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\u00cb\7v\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7t\2\2\u00cd")
        buf.write("\u00ce\7h\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7e\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\26\3\2\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write("\u00d7\7p\2\2\u00d7\u00d8\7i\2\2\u00d8\30\3\2\2\2\u00d9")
        buf.write("\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc")
        buf.write("\32\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7n\2\2\u00df")
        buf.write("\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("\34\3\2\2\2\u00e3\u00e4\7d\2\2\u00e4\u00e5\7q\2\2\u00e5")
        buf.write("\u00e6\7q\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7c\2\2\u00e9\u00ea\7p\2\2\u00ea\36\3\2\2\2\u00eb")
        buf.write("\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0 \3\2\2\2\u00f1")
        buf.write("\u00f2\7x\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write("\"\3\2\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7q\2\2\u00f7")
        buf.write("\u00f8\7p\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7k\2\2\u00fa")
        buf.write("\u00fb\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7g\2\2\u00fd")
        buf.write("$\3\2\2\2\u00fe\u00ff\7d\2\2\u00ff\u0100\7t\2\2\u0100")
        buf.write("\u0101\7g\2\2\u0101\u0102\7c\2\2\u0102\u0103\7m\2\2\u0103")
        buf.write("&\3\2\2\2\u0104\u0105\7t\2\2\u0105\u0106\7c\2\2\u0106")
        buf.write("\u0107\7p\2\2\u0107\u0108\7i\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write("(\3\2\2\2\u010a\u010b\7p\2\2\u010b\u010c\7k\2\2\u010c")
        buf.write("\u010d\7n\2\2\u010d*\3\2\2\2\u010e\u010f\7v\2\2\u010f")
        buf.write("\u0110\7t\2\2\u0110\u0111\7w\2\2\u0111\u0112\7g\2\2\u0112")
        buf.write(",\3\2\2\2\u0113\u0114\7h\2\2\u0114\u0115\7c\2\2\u0115")
        buf.write("\u0116\7n\2\2\u0116\u0117\7u\2\2\u0117\u0118\7g\2\2\u0118")
        buf.write(".\3\2\2\2\u0119\u011a\7-\2\2\u011a\60\3\2\2\2\u011b\u011c")
        buf.write("\7/\2\2\u011c\62\3\2\2\2\u011d\u011e\7,\2\2\u011e\64\3")
        buf.write("\2\2\2\u011f\u0120\7\61\2\2\u0120\66\3\2\2\2\u0121\u0122")
        buf.write("\7\'\2\2\u01228\3\2\2\2\u0123\u0124\7?\2\2\u0124\u0125")
        buf.write("\7?\2\2\u0125:\3\2\2\2\u0126\u0127\7#\2\2\u0127\u0128")
        buf.write("\7?\2\2\u0128<\3\2\2\2\u0129\u012a\7>\2\2\u012a>\3\2\2")
        buf.write("\2\u012b\u012c\7@\2\2\u012c@\3\2\2\2\u012d\u012e\7>\2")
        buf.write("\2\u012e\u012f\7?\2\2\u012fB\3\2\2\2\u0130\u0131\7@\2")
        buf.write("\2\u0131\u0132\7?\2\2\u0132D\3\2\2\2\u0133\u0134\7(\2")
        buf.write("\2\u0134\u0135\7(\2\2\u0135F\3\2\2\2\u0136\u0137\7~\2")
        buf.write("\2\u0137\u0138\7~\2\2\u0138H\3\2\2\2\u0139\u013a\7#\2")
        buf.write("\2\u013aJ\3\2\2\2\u013b\u013c\7?\2\2\u013cL\3\2\2\2\u013d")
        buf.write("\u013e\7<\2\2\u013e\u013f\7?\2\2\u013fN\3\2\2\2\u0140")
        buf.write("\u0141\7-\2\2\u0141\u0142\7?\2\2\u0142P\3\2\2\2\u0143")
        buf.write("\u0144\7/\2\2\u0144\u0145\7?\2\2\u0145R\3\2\2\2\u0146")
        buf.write("\u0147\7,\2\2\u0147\u0148\7?\2\2\u0148T\3\2\2\2\u0149")
        buf.write("\u014a\7\61\2\2\u014a\u014b\7?\2\2\u014bV\3\2\2\2\u014c")
        buf.write("\u014d\7\'\2\2\u014d\u014e\7?\2\2\u014eX\3\2\2\2\u014f")
        buf.write("\u0150\7.\2\2\u0150Z\3\2\2\2\u0151\u0152\7=\2\2\u0152")
        buf.write("\\\3\2\2\2\u0153\u015c\7\62\2\2\u0154\u0158\t\3\2\2\u0155")
        buf.write("\u0157\5\177@\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2")
        buf.write("\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u0153\3\2\2\2\u015b")
        buf.write("\u0154\3\2\2\2\u015c^\3\2\2\2\u015d\u015e\7\62\2\2\u015e")
        buf.write("\u0160\t\4\2\2\u015f\u0161\t\5\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163`\3\2\2\2\u0164\u0165\7\62\2\2\u0165\u0167")
        buf.write("\t\6\2\2\u0166\u0168\t\7\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016ab\3\2\2\2\u016b\u016c\7\62\2\2\u016c\u016e\t\b\2")
        buf.write("\2\u016d\u016f\t\t\2\2\u016e\u016d\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("d\3\2\2\2\u0172\u0174\5\177@\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u017b\7\60\2\2\u0178\u017a")
        buf.write("\5\177@\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017f\3\2\2\2")
        buf.write("\u017d\u017b\3\2\2\2\u017e\u0180\5}?\2\u017f\u017e\3\2")
        buf.write("\2\2\u017f\u0180\3\2\2\2\u0180f\3\2\2\2\u0181\u0182\7")
        buf.write("\60\2\2\u0182h\3\2\2\2\u0183\u0188\7$\2\2\u0184\u0187")
        buf.write("\5\u0083B\2\u0185\u0187\n\n\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018b\u018c\7$\2\2\u018cj\3\2\2\2\u018d\u0192\7")
        buf.write("$\2\2\u018e\u0191\5\u0083B\2\u018f\u0191\n\13\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3")
        buf.write("\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196\7^\2\2\u0196\u0197")
        buf.write("\13\2\2\2\u0197l\3\2\2\2\u0198\u019d\7$\2\2\u0199\u019c")
        buf.write("\5\u0083B\2\u019a\u019c\n\n\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019en\3\2\2\2\u019f\u019d\3\2\2")
        buf.write("\2\u01a0\u01a3\5\u0081A\2\u01a1\u01a3\7a\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a9\3\2\2\2\u01a4")
        buf.write("\u01a8\5\177@\2\u01a5\u01a8\5\u0081A\2\u01a6\u01a8\7a")
        buf.write("\2\2\u01a7\u01a4\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aap\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\7*\2\2\u01adr\3\2\2\2\u01ae\u01af\7+\2\2\u01af")
        buf.write("t\3\2\2\2\u01b0\u01b1\7}\2\2\u01b1v\3\2\2\2\u01b2\u01b3")
        buf.write("\7\177\2\2\u01b3x\3\2\2\2\u01b4\u01b5\7]\2\2\u01b5z\3")
        buf.write("\2\2\2\u01b6\u01b7\7_\2\2\u01b7|\3\2\2\2\u01b8\u01ba\t")
        buf.write("\f\2\2\u01b9\u01bb\t\r\2\2\u01ba\u01b9\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01be\5\177@\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0~\3\2\2\2\u01c1\u01c2\t\16\2")
        buf.write("\2\u01c2\u0080\3\2\2\2\u01c3\u01c4\t\17\2\2\u01c4\u0082")
        buf.write("\3\2\2\2\u01c5\u01c6\7^\2\2\u01c6\u01c7\t\20\2\2\u01c7")
        buf.write("\u0084\3\2\2\2\u01c8\u01c9\7\f\2\2\u01c9\u01ca\3\2\2\2")
        buf.write("\u01ca\u01cb\bC\2\2\u01cb\u0086\3\2\2\2\u01cc\u01ce\t")
        buf.write("\21\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1\u01d2\bD\2\2\u01d2\u0088\3\2\2\2\u01d3\u01d4\13")
        buf.write("\2\2\2\u01d4\u008a\3\2\2\2\31\2\u0091\u009c\u0158\u015b")
        buf.write("\u0162\u0169\u0170\u0175\u017b\u017f\u0186\u0188\u0190")
        buf.write("\u0192\u019b\u019d\u01a2\u01a7\u01a9\u01ba\u01bf\u01cf")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    BLOCK_COMMENT = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    CONST = 15
    VAR = 16
    CONTINUE = 17
    BREAK = 18
    RANGE = 19
    NIL = 20
    TRUE = 21
    FALSE = 22
    PLUS = 23
    MINUS = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS = 30
    GREATER = 31
    LESS_OR_EQUAL = 32
    GREATER_OR_EQUAL = 33
    AND = 34
    OR = 35
    NOT = 36
    ASSIGN = 37
    SHORT_ASSIGN = 38
    PLUS_ASSIGN = 39
    MINUS_ASSIGN = 40
    MUL_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    COMMA = 44
    SEMICO = 45
    DEC_LIT = 46
    BIN_LIT = 47
    OCT_LIT = 48
    HEX_LIT = 49
    FLOAT_LIT = 50
    SELECTOR = 51
    STRING_LIT = 52
    ILLEGAL_ESCAPE = 53
    UNCLOSE_STRING = 54
    ID = 55
    LPAREN = 56
    RPAREN = 57
    LBRACE = 58
    RBRACE = 59
    LBRACK = 60
    RBRACK = 61
    NL = 62
    WS = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "','", 
            "';'", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", "FOR", "RETURN", 
            "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
            "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
            "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", 
            "NOT_EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
            "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "COMMA", 
            "SEMICO", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
            "SELECTOR", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "NL", "WS", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                  "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "AND", "OR", "NOT", 
                  "ASSIGN", "SHORT_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "COMMA", "SEMICO", 
                  "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                  "SELECTOR", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "EXP", "DIGIT", "LETTER", "ESC", "NL", "WS", 
                  "ERROR_CHAR" ]

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


