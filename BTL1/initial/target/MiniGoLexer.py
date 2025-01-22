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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0099\n\3\f\3\16\3\u009c")
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
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3/\7/\u0154\n/\f/\16/\u0157\13")
        buf.write("/\5/\u0159\n/\3\60\3\60\3\60\6\60\u015e\n\60\r\60\16\60")
        buf.write("\u015f\3\61\3\61\3\61\6\61\u0165\n\61\r\61\16\61\u0166")
        buf.write("\3\62\3\62\3\62\6\62\u016c\n\62\r\62\16\62\u016d\3\63")
        buf.write("\6\63\u0171\n\63\r\63\16\63\u0172\3\63\3\63\7\63\u0177")
        buf.write("\n\63\f\63\16\63\u017a\13\63\3\63\5\63\u017d\n\63\3\64")
        buf.write("\3\64\3\64\7\64\u0182\n\64\f\64\16\64\u0185\13\64\3\64")
        buf.write("\3\64\3\65\3\65\5\65\u018b\n\65\3\65\3\65\3\65\7\65\u0190")
        buf.write("\n\65\f\65\16\65\u0193\13\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\5<\u01a3\n<\3<\6<\u01a6\n<\r")
        buf.write("<\16<\u01a7\3=\3=\3>\3>\3?\3?\5?\u01b0\n?\3@\3@\3@\3@")
        buf.write("\3A\6A\u01b7\nA\rA\16A\u01b8\3A\3A\3B\3B\3B\7B\u01c0\n")
        buf.write("B\fB\16B\u01c3\13B\3B\3B\3C\3C\3C\7C\u01ca\nC\fC\16C\u01cd")
        buf.write("\13C\3D\3D\3\u009a\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177=\u0081>\u0083?")
        buf.write("\u0085@\u0087A\3\2\22\4\2\f\f\17\17\3\2\63;\4\2DDdd\3")
        buf.write("\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2$$^^\4")
        buf.write("\2GGgg\4\2--//\3\2\62;\4\2C\\c|\5\2\13\f\17\17^^\5\2\13")
        buf.write("\13\17\17\"\"\3\2$$\2\u01e3\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u0094\3\2\2")
        buf.write("\2\7\u00a2\3\2\2\2\t\u00a5\3\2\2\2\13\u00aa\3\2\2\2\r")
        buf.write("\u00ae\3\2\2\2\17\u00b5\3\2\2\2\21\u00ba\3\2\2\2\23\u00bf")
        buf.write("\3\2\2\2\25\u00c6\3\2\2\2\27\u00d0\3\2\2\2\31\u00d7\3")
        buf.write("\2\2\2\33\u00db\3\2\2\2\35\u00e1\3\2\2\2\37\u00e9\3\2")
        buf.write("\2\2!\u00ef\3\2\2\2#\u00f3\3\2\2\2%\u00fc\3\2\2\2\'\u0102")
        buf.write("\3\2\2\2)\u0108\3\2\2\2+\u010c\3\2\2\2-\u0111\3\2\2\2")
        buf.write("/\u0117\3\2\2\2\61\u0119\3\2\2\2\63\u011b\3\2\2\2\65\u011d")
        buf.write("\3\2\2\2\67\u011f\3\2\2\29\u0121\3\2\2\2;\u0124\3\2\2")
        buf.write("\2=\u0127\3\2\2\2?\u0129\3\2\2\2A\u012b\3\2\2\2C\u012e")
        buf.write("\3\2\2\2E\u0131\3\2\2\2G\u0134\3\2\2\2I\u0137\3\2\2\2")
        buf.write("K\u0139\3\2\2\2M\u013b\3\2\2\2O\u013e\3\2\2\2Q\u0141\3")
        buf.write("\2\2\2S\u0144\3\2\2\2U\u0147\3\2\2\2W\u014a\3\2\2\2Y\u014c")
        buf.write("\3\2\2\2[\u014e\3\2\2\2]\u0158\3\2\2\2_\u015a\3\2\2\2")
        buf.write("a\u0161\3\2\2\2c\u0168\3\2\2\2e\u0170\3\2\2\2g\u017e\3")
        buf.write("\2\2\2i\u018a\3\2\2\2k\u0194\3\2\2\2m\u0196\3\2\2\2o\u0198")
        buf.write("\3\2\2\2q\u019a\3\2\2\2s\u019c\3\2\2\2u\u019e\3\2\2\2")
        buf.write("w\u01a0\3\2\2\2y\u01a9\3\2\2\2{\u01ab\3\2\2\2}\u01af\3")
        buf.write("\2\2\2\177\u01b1\3\2\2\2\u0081\u01b6\3\2\2\2\u0083\u01bc")
        buf.write("\3\2\2\2\u0085\u01c6\3\2\2\2\u0087\u01ce\3\2\2\2\u0089")
        buf.write("\u008a\7\61\2\2\u008a\u008b\7\61\2\2\u008b\u008f\3\2\2")
        buf.write("\2\u008c\u008e\n\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\b\2\2\2")
        buf.write("\u0093\4\3\2\2\2\u0094\u0095\7\61\2\2\u0095\u0096\7,\2")
        buf.write("\2\u0096\u009a\3\2\2\2\u0097\u0099\13\2\2\2\u0098\u0097")
        buf.write("\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u009b\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2")
        buf.write("\u009d\u009e\7,\2\2\u009e\u009f\7\61\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a1\b\3\2\2\u00a1\6\3\2\2\2\u00a2\u00a3")
        buf.write("\7k\2\2\u00a3\u00a4\7h\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\n\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7t\2\2\u00ad\f\3\2\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2")
        buf.write("\7w\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7p\2\2\u00b4\16")
        buf.write("\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\u00b9\7e\2\2\u00b9\20\3\2\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7{\2\2\u00bc\u00bd\7r\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\22\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\24\3\2\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7g\2\2\u00cf\26")
        buf.write("\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7i\2\2\u00d6\30\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7v\2\2\u00da\32\3\2\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7v\2\2\u00e0\34\3\2\2\2\u00e1\u00e2")
        buf.write("\7d\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee \3\2\2\2\u00ef\u00f0\7x\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7t\2\2\u00f2\"\3\2\2\2\u00f3\u00f4")
        buf.write("\7e\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa")
        buf.write("\7w\2\2\u00fa\u00fb\7g\2\2\u00fb$\3\2\2\2\u00fc\u00fd")
        buf.write("\7d\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7m\2\2\u0101&\3\2\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106\u0107\7g\2\2\u0107(\3\2\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b*\3")
        buf.write("\2\2\2\u010c\u010d\7v\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7w\2\2\u010f\u0110\7g\2\2\u0110,\3\2\2\2\u0111\u0112")
        buf.write("\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7g\2\2\u0116.\3\2\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118\60\3\2\2\2\u0119\u011a\7/\2\2\u011a\62\3")
        buf.write("\2\2\2\u011b\u011c\7,\2\2\u011c\64\3\2\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e\66\3\2\2\2\u011f\u0120\7\'\2\2\u01208")
        buf.write("\3\2\2\2\u0121\u0122\7?\2\2\u0122\u0123\7?\2\2\u0123:")
        buf.write("\3\2\2\2\u0124\u0125\7#\2\2\u0125\u0126\7?\2\2\u0126<")
        buf.write("\3\2\2\2\u0127\u0128\7>\2\2\u0128>\3\2\2\2\u0129\u012a")
        buf.write("\7@\2\2\u012a@\3\2\2\2\u012b\u012c\7>\2\2\u012c\u012d")
        buf.write("\7?\2\2\u012dB\3\2\2\2\u012e\u012f\7@\2\2\u012f\u0130")
        buf.write("\7?\2\2\u0130D\3\2\2\2\u0131\u0132\7(\2\2\u0132\u0133")
        buf.write("\7(\2\2\u0133F\3\2\2\2\u0134\u0135\7~\2\2\u0135\u0136")
        buf.write("\7~\2\2\u0136H\3\2\2\2\u0137\u0138\7#\2\2\u0138J\3\2\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aL\3\2\2\2\u013b\u013c\7-\2")
        buf.write("\2\u013c\u013d\7?\2\2\u013dN\3\2\2\2\u013e\u013f\7/\2")
        buf.write("\2\u013f\u0140\7?\2\2\u0140P\3\2\2\2\u0141\u0142\7,\2")
        buf.write("\2\u0142\u0143\7?\2\2\u0143R\3\2\2\2\u0144\u0145\7\61")
        buf.write("\2\2\u0145\u0146\7?\2\2\u0146T\3\2\2\2\u0147\u0148\7\'")
        buf.write("\2\2\u0148\u0149\7?\2\2\u0149V\3\2\2\2\u014a\u014b\7\60")
        buf.write("\2\2\u014bX\3\2\2\2\u014c\u014d\7.\2\2\u014dZ\3\2\2\2")
        buf.write("\u014e\u014f\7=\2\2\u014f\\\3\2\2\2\u0150\u0159\7\62\2")
        buf.write("\2\u0151\u0155\t\3\2\2\u0152\u0154\5y=\2\u0153\u0152\3")
        buf.write("\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u0150\3\2\2\2\u0158\u0151\3\2\2\2\u0159^\3\2\2\2\u015a")
        buf.write("\u015b\7\62\2\2\u015b\u015d\t\4\2\2\u015c\u015e\t\5\2")
        buf.write("\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160`\3\2\2\2\u0161\u0162")
        buf.write("\7\62\2\2\u0162\u0164\t\6\2\2\u0163\u0165\t\7\2\2\u0164")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167b\3\2\2\2\u0168\u0169\7\62\2")
        buf.write("\2\u0169\u016b\t\b\2\2\u016a\u016c\t\t\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016ed\3\2\2\2\u016f\u0171\5y=\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0178\7")
        buf.write("\60\2\2\u0175\u0177\5y=\2\u0176\u0175\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017d\5w<\2\u017c")
        buf.write("\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017df\3\2\2\2\u017e")
        buf.write("\u0183\7$\2\2\u017f\u0182\5}?\2\u0180\u0182\n\n\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\7$\2\2\u0187h\3")
        buf.write("\2\2\2\u0188\u018b\5{>\2\u0189\u018b\7a\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018b\u0191\3\2\2\2\u018c")
        buf.write("\u0190\5y=\2\u018d\u0190\5{>\2\u018e\u0190\7a\2\2\u018f")
        buf.write("\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192j\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\7*\2\2\u0195l\3\2\2\2\u0196\u0197\7+\2\2\u0197n\3\2\2")
        buf.write("\2\u0198\u0199\7}\2\2\u0199p\3\2\2\2\u019a\u019b\7\177")
        buf.write("\2\2\u019br\3\2\2\2\u019c\u019d\7]\2\2\u019dt\3\2\2\2")
        buf.write("\u019e\u019f\7_\2\2\u019fv\3\2\2\2\u01a0\u01a2\t\13\2")
        buf.write("\2\u01a1\u01a3\t\f\2\2\u01a2\u01a1\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u01a6\5y=\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8x\3\2\2\2\u01a9\u01aa\t\r\2\2\u01aa")
        buf.write("z\3\2\2\2\u01ab\u01ac\t\16\2\2\u01ac|\3\2\2\2\u01ad\u01b0")
        buf.write("\t\17\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0~\3\2\2\2\u01b1\u01b2\7\f\2\2\u01b2")
        buf.write("\u01b3\3\2\2\2\u01b3\u01b4\b@\2\2\u01b4\u0080\3\2\2\2")
        buf.write("\u01b5\u01b7\t\20\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bb\bA\2\2\u01bb\u0082\3\2\2\2")
        buf.write("\u01bc\u01c1\7$\2\2\u01bd\u01c0\5}?\2\u01be\u01c0\n\21")
        buf.write("\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7$\2\2")
        buf.write("\u01c5\u0084\3\2\2\2\u01c6\u01cb\7$\2\2\u01c7\u01ca\5")
        buf.write("}?\2\u01c8\u01ca\n\n\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u0086\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01cf\13\2\2\2\u01cf\u0088\3\2\2\2\32\2\u008f\u009a")
        buf.write("\u0155\u0158\u015f\u0166\u016d\u0172\u0178\u017c\u0181")
        buf.write("\u0183\u018a\u018f\u0191\u01a2\u01a7\u01af\u01b8\u01bf")
        buf.write("\u01c1\u01c9\u01cb\3\b\2\2")
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
    PLUS_ASSIGN = 38
    MINUS_ASSIGN = 39
    MUL_ASSIGN = 40
    DIV_ASSIGN = 41
    MOD_ASSIGN = 42
    SELECTOR = 43
    COMMA = 44
    SEMICO = 45
    DEC_LIT = 46
    BIN_LIT = 47
    OCT_LIT = 48
    HEX_LIT = 49
    FLOAT_LIT = 50
    STRING_LIT = 51
    ID = 52
    LPAREN = 53
    RPAREN = 54
    LBRACE = 55
    RBRACE = 56
    LBRACK = 57
    RBRACK = 58
    NL = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "','", 
            "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", "FOR", "RETURN", 
            "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
            "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
            "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", 
            "NOT_EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
            "AND", "OR", "NOT", "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "SELECTOR", "COMMA", 
            "SEMICO", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
            "STRING_LIT", "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LBRACK", "RBRACK", "NL", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "BLOCK_COMMENT", "IF", "ELSE", "FOR", 
                  "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", 
                  "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                  "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "AND", "OR", "NOT", 
                  "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "SELECTOR", "COMMA", "SEMICO", 
                  "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                  "STRING_LIT", "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACK", "RBRACK", "EXP", "DIGIT", "LETTER", "ESC", "NL", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

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


