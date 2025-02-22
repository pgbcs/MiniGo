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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\2\3\2\3\3\3\3\6\3\u009d\n\3\r")
        buf.write("\3\16\3\u009e\3\3\3\3\6\3\u00a3\n\3\r\3\16\3\u00a4\3\3")
        buf.write("\7\3\u00a8\n\3\f\3\16\3\u00ab\13\3\3\3\6\3\u00ae\n\3\r")
        buf.write("\3\16\3\u00af\3\3\6\3\u00b3\n\3\r\3\16\3\u00b4\5\3\u00b7")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u00bf\n\4\f\4\16\4\u00c2")
        buf.write("\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,")
        buf.write("\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\7\62\u0180\n\62\f\62\16\62\u0183\13\62\5\62\u0185")
        buf.write("\n\62\3\63\3\63\3\63\6\63\u018a\n\63\r\63\16\63\u018b")
        buf.write("\3\64\3\64\3\64\6\64\u0191\n\64\r\64\16\64\u0192\3\65")
        buf.write("\3\65\3\65\6\65\u0198\n\65\r\65\16\65\u0199\3\66\6\66")
        buf.write("\u019d\n\66\r\66\16\66\u019e\3\66\3\66\7\66\u01a3\n\66")
        buf.write("\f\66\16\66\u01a6\13\66\3\66\5\66\u01a9\n\66\3\67\3\67")
        buf.write("\3\67\7\67\u01ae\n\67\f\67\16\67\u01b1\13\67\3\67\3\67")
        buf.write("\38\38\38\78\u01b8\n8\f8\168\u01bb\138\39\39\39\79\u01c0")
        buf.write("\n9\f9\169\u01c3\139\39\39\39\3:\3:\5:\u01ca\n:\3:\3:")
        buf.write("\3:\7:\u01cf\n:\f:\16:\u01d2\13:\3;\3;\3<\3<\3=\3=\3>")
        buf.write("\3>\3?\3?\3@\3@\3A\3A\5A\u01e2\nA\3A\6A\u01e5\nA\rA\16")
        buf.write("A\u01e6\3B\3B\3C\3C\3D\3D\3D\3E\5E\u01f1\nE\3E\3E\3E\3")
        buf.write("F\6F\u01f7\nF\rF\16F\u01f8\3F\3F\3G\3G\2\2H\3\3\5\2\7")
        buf.write("\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35")
        buf.write("\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32")
        buf.write("\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y")
        buf.write("-[.]/_\60a\61c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?")
        buf.write("\177@\u0081\2\u0083\2\u0085\2\u0087\2\u0089A\u008bB\u008d")
        buf.write("C\3\2\24\4\2\f\f\17\17\4\2,,\61\61\3\2\61\61\3\2,,\3\2")
        buf.write("\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62")
        buf.write(";CHch\6\2\f\f\17\17$$^^\4\2GGgg\4\2--//\3\2\62;\4\2C\\")
        buf.write("c|\7\2$$^^ppttvv\5\2\13\13\16\17\"\"\2\u0219\2\3\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\3\u008f\3\2\2\2\5\u00a9\3\2\2\2\7\u00b8\3\2\2")
        buf.write("\2\t\u00c9\3\2\2\2\13\u00cb\3\2\2\2\r\u00ce\3\2\2\2\17")
        buf.write("\u00d3\3\2\2\2\21\u00d7\3\2\2\2\23\u00de\3\2\2\2\25\u00e3")
        buf.write("\3\2\2\2\27\u00e8\3\2\2\2\31\u00ef\3\2\2\2\33\u00f9\3")
        buf.write("\2\2\2\35\u0100\3\2\2\2\37\u0104\3\2\2\2!\u010a\3\2\2")
        buf.write("\2#\u0112\3\2\2\2%\u0118\3\2\2\2\'\u011c\3\2\2\2)\u0125")
        buf.write("\3\2\2\2+\u012b\3\2\2\2-\u0131\3\2\2\2/\u0135\3\2\2\2")
        buf.write("\61\u013a\3\2\2\2\63\u0140\3\2\2\2\65\u0142\3\2\2\2\67")
        buf.write("\u0144\3\2\2\29\u0146\3\2\2\2;\u0148\3\2\2\2=\u014a\3")
        buf.write("\2\2\2?\u014d\3\2\2\2A\u0150\3\2\2\2C\u0152\3\2\2\2E\u0154")
        buf.write("\3\2\2\2G\u0157\3\2\2\2I\u015a\3\2\2\2K\u015d\3\2\2\2")
        buf.write("M\u0160\3\2\2\2O\u0162\3\2\2\2Q\u0164\3\2\2\2S\u0167\3")
        buf.write("\2\2\2U\u016a\3\2\2\2W\u016d\3\2\2\2Y\u0170\3\2\2\2[\u0173")
        buf.write("\3\2\2\2]\u0176\3\2\2\2_\u0178\3\2\2\2a\u017a\3\2\2\2")
        buf.write("c\u0184\3\2\2\2e\u0186\3\2\2\2g\u018d\3\2\2\2i\u0194\3")
        buf.write("\2\2\2k\u019c\3\2\2\2m\u01aa\3\2\2\2o\u01b4\3\2\2\2q\u01bc")
        buf.write("\3\2\2\2s\u01c9\3\2\2\2u\u01d3\3\2\2\2w\u01d5\3\2\2\2")
        buf.write("y\u01d7\3\2\2\2{\u01d9\3\2\2\2}\u01db\3\2\2\2\177\u01dd")
        buf.write("\3\2\2\2\u0081\u01df\3\2\2\2\u0083\u01e8\3\2\2\2\u0085")
        buf.write("\u01ea\3\2\2\2\u0087\u01ec\3\2\2\2\u0089\u01f0\3\2\2\2")
        buf.write("\u008b\u01f6\3\2\2\2\u008d\u01fc\3\2\2\2\u008f\u0090\7")
        buf.write("\61\2\2\u0090\u0091\7\61\2\2\u0091\u0095\3\2\2\2\u0092")
        buf.write("\u0094\n\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\b\2\2\2\u0099\4")
        buf.write("\3\2\2\2\u009a\u00a8\n\3\2\2\u009b\u009d\7,\2\2\u009c")
        buf.write("\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a8\n")
        buf.write("\4\2\2\u00a1\u00a3\7\61\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a8\n\5\2\2\u00a7\u009a\3")
        buf.write("\2\2\2\u00a7\u009c\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00b6\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\7\61\2")
        buf.write("\2\u00ad\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b7\3\2\2\2\u00b1")
        buf.write("\u00b3\7,\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b7\3")
        buf.write("\2\2\2\u00b6\u00ad\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\6\3\2\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba")
        buf.write("\7,\2\2\u00ba\u00c0\3\2\2\2\u00bb\u00bc\5\5\3\2\u00bc")
        buf.write("\u00bd\5\7\4\2\u00bd\u00bf\3\2\2\2\u00be\u00bb\3\2\2\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4")
        buf.write("\5\5\3\2\u00c4\u00c5\7,\2\2\u00c5\u00c6\7\61\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\b\4\2\2\u00c8\b\3\2\2\2\u00c9")
        buf.write("\u00ca\7<\2\2\u00ca\n\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc")
        buf.write("\u00cd\7h\2\2\u00cd\f\3\2\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write("\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7g\2\2\u00d2")
        buf.write("\16\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7q\2\2\u00d5")
        buf.write("\u00d6\7t\2\2\u00d6\20\3\2\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7w\2\2\u00db")
        buf.write("\u00dc\7t\2\2\u00dc\u00dd\7p\2\2\u00dd\22\3\2\2\2\u00de")
        buf.write("\u00df\7h\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1\7p\2\2\u00e1")
        buf.write("\u00e2\7e\2\2\u00e2\24\3\2\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\u00e5\7{\2\2\u00e5\u00e6\7r\2\2\u00e6\u00e7\7g\2\2\u00e7")
        buf.write("\26\3\2\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7t\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7e\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee\30\3\2\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7h\2\2\u00f5\u00f6\7c\2\2\u00f6")
        buf.write("\u00f7\7e\2\2\u00f7\u00f8\7g\2\2\u00f8\32\3\2\2\2\u00f9")
        buf.write("\u00fa\7u\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7t\2\2\u00fc")
        buf.write("\u00fd\7k\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7i\2\2\u00ff")
        buf.write("\34\3\2\2\2\u0100\u0101\7k\2\2\u0101\u0102\7p\2\2\u0102")
        buf.write("\u0103\7v\2\2\u0103\36\3\2\2\2\u0104\u0105\7h\2\2\u0105")
        buf.write("\u0106\7n\2\2\u0106\u0107\7q\2\2\u0107\u0108\7c\2\2\u0108")
        buf.write("\u0109\7v\2\2\u0109 \3\2\2\2\u010a\u010b\7d\2\2\u010b")
        buf.write("\u010c\7q\2\2\u010c\u010d\7q\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f\u0110\7c\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\"\3\2\2\2\u0112\u0113\7e\2\2\u0113\u0114\7q\2\2\u0114")
        buf.write("\u0115\7p\2\2\u0115\u0116\7u\2\2\u0116\u0117\7v\2\2\u0117")
        buf.write("$\3\2\2\2\u0118\u0119\7x\2\2\u0119\u011a\7c\2\2\u011a")
        buf.write("\u011b\7t\2\2\u011b&\3\2\2\2\u011c\u011d\7e\2\2\u011d")
        buf.write("\u011e\7q\2\2\u011e\u011f\7p\2\2\u011f\u0120\7v\2\2\u0120")
        buf.write("\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123\7w\2\2\u0123")
        buf.write("\u0124\7g\2\2\u0124(\3\2\2\2\u0125\u0126\7d\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128\u0129\7c\2\2\u0129")
        buf.write("\u012a\7m\2\2\u012a*\3\2\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7c\2\2\u012d\u012e\7p\2\2\u012e\u012f\7i\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130,\3\2\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("\u0133\7k\2\2\u0133\u0134\7n\2\2\u0134.\3\2\2\2\u0135")
        buf.write("\u0136\7v\2\2\u0136\u0137\7t\2\2\u0137\u0138\7w\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\60\3\2\2\2\u013a\u013b\7h\2\2\u013b")
        buf.write("\u013c\7c\2\2\u013c\u013d\7n\2\2\u013d\u013e\7u\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\62\3\2\2\2\u0140\u0141\7-\2\2\u0141")
        buf.write("\64\3\2\2\2\u0142\u0143\7/\2\2\u0143\66\3\2\2\2\u0144")
        buf.write("\u0145\7,\2\2\u01458\3\2\2\2\u0146\u0147\7\61\2\2\u0147")
        buf.write(":\3\2\2\2\u0148\u0149\7\'\2\2\u0149<\3\2\2\2\u014a\u014b")
        buf.write("\7?\2\2\u014b\u014c\7?\2\2\u014c>\3\2\2\2\u014d\u014e")
        buf.write("\7#\2\2\u014e\u014f\7?\2\2\u014f@\3\2\2\2\u0150\u0151")
        buf.write("\7>\2\2\u0151B\3\2\2\2\u0152\u0153\7@\2\2\u0153D\3\2\2")
        buf.write("\2\u0154\u0155\7>\2\2\u0155\u0156\7?\2\2\u0156F\3\2\2")
        buf.write("\2\u0157\u0158\7@\2\2\u0158\u0159\7?\2\2\u0159H\3\2\2")
        buf.write("\2\u015a\u015b\7(\2\2\u015b\u015c\7(\2\2\u015cJ\3\2\2")
        buf.write("\2\u015d\u015e\7~\2\2\u015e\u015f\7~\2\2\u015fL\3\2\2")
        buf.write("\2\u0160\u0161\7#\2\2\u0161N\3\2\2\2\u0162\u0163\7?\2")
        buf.write("\2\u0163P\3\2\2\2\u0164\u0165\7<\2\2\u0165\u0166\7?\2")
        buf.write("\2\u0166R\3\2\2\2\u0167\u0168\7-\2\2\u0168\u0169\7?\2")
        buf.write("\2\u0169T\3\2\2\2\u016a\u016b\7/\2\2\u016b\u016c\7?\2")
        buf.write("\2\u016cV\3\2\2\2\u016d\u016e\7,\2\2\u016e\u016f\7?\2")
        buf.write("\2\u016fX\3\2\2\2\u0170\u0171\7\61\2\2\u0171\u0172\7?")
        buf.write("\2\2\u0172Z\3\2\2\2\u0173\u0174\7\'\2\2\u0174\u0175\7")
        buf.write("?\2\2\u0175\\\3\2\2\2\u0176\u0177\7\60\2\2\u0177^\3\2")
        buf.write("\2\2\u0178\u0179\7.\2\2\u0179`\3\2\2\2\u017a\u017b\7=")
        buf.write("\2\2\u017bb\3\2\2\2\u017c\u0185\7\62\2\2\u017d\u0181\t")
        buf.write("\6\2\2\u017e\u0180\5\u0083B\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u017c\3")
        buf.write("\2\2\2\u0184\u017d\3\2\2\2\u0185d\3\2\2\2\u0186\u0187")
        buf.write("\7\62\2\2\u0187\u0189\t\7\2\2\u0188\u018a\t\b\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018cf\3\2\2\2\u018d\u018e\7\62\2")
        buf.write("\2\u018e\u0190\t\t\2\2\u018f\u0191\t\n\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193h\3\2\2\2\u0194\u0195\7\62\2\2\u0195")
        buf.write("\u0197\t\13\2\2\u0196\u0198\t\f\2\2\u0197\u0196\3\2\2")
        buf.write("\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a")
        buf.write("\3\2\2\2\u019aj\3\2\2\2\u019b\u019d\5\u0083B\2\u019c\u019b")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a4\7\60\2")
        buf.write("\2\u01a1\u01a3\5\u0083B\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\5\u0081")
        buf.write("A\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9l\3\2")
        buf.write("\2\2\u01aa\u01af\7$\2\2\u01ab\u01ae\5\u0087D\2\u01ac\u01ae")
        buf.write("\n\r\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\7")
        buf.write("$\2\2\u01b3n\3\2\2\2\u01b4\u01b9\7$\2\2\u01b5\u01b8\5")
        buf.write("\u0087D\2\u01b6\u01b8\n\r\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01b9\u01ba\3\2\2\2\u01bap\3\2\2\2\u01bb\u01b9\3\2\2")
        buf.write("\2\u01bc\u01c1\7$\2\2\u01bd\u01c0\5\u0087D\2\u01be\u01c0")
        buf.write("\n\r\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0")
        buf.write("\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\7")
        buf.write("^\2\2\u01c5\u01c6\13\2\2\2\u01c6r\3\2\2\2\u01c7\u01ca")
        buf.write("\5\u0085C\2\u01c8\u01ca\7a\2\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u01d0\3\2\2\2\u01cb\u01cf\5\u0083")
        buf.write("B\2\u01cc\u01cf\5\u0085C\2\u01cd\u01cf\7a\2\2\u01ce\u01cb")
        buf.write("\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1t\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\7*\2\2")
        buf.write("\u01d4v\3\2\2\2\u01d5\u01d6\7+\2\2\u01d6x\3\2\2\2\u01d7")
        buf.write("\u01d8\7}\2\2\u01d8z\3\2\2\2\u01d9\u01da\7\177\2\2\u01da")
        buf.write("|\3\2\2\2\u01db\u01dc\7]\2\2\u01dc~\3\2\2\2\u01dd\u01de")
        buf.write("\7_\2\2\u01de\u0080\3\2\2\2\u01df\u01e1\t\16\2\2\u01e0")
        buf.write("\u01e2\t\17\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2")
        buf.write("\2\u01e2\u01e4\3\2\2\2\u01e3\u01e5\5\u0083B\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u0082\3\2\2\2\u01e8\u01e9\t\20\2")
        buf.write("\2\u01e9\u0084\3\2\2\2\u01ea\u01eb\t\21\2\2\u01eb\u0086")
        buf.write("\3\2\2\2\u01ec\u01ed\7^\2\2\u01ed\u01ee\t\22\2\2\u01ee")
        buf.write("\u0088\3\2\2\2\u01ef\u01f1\7\17\2\2\u01f0\u01ef\3\2\2")
        buf.write("\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3")
        buf.write("\7\f\2\2\u01f3\u01f4\bE\3\2\u01f4\u008a\3\2\2\2\u01f5")
        buf.write("\u01f7\t\23\2\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2")
        buf.write("\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u01fb\bF\2\2\u01fb\u008c\3\2\2\2\u01fc")
        buf.write("\u01fd\13\2\2\2\u01fd\u008e\3\2\2\2!\2\u0095\u009e\u00a4")
        buf.write("\u00a7\u00a9\u00af\u00b4\u00b6\u00c0\u0181\u0184\u018b")
        buf.write("\u0192\u0199\u019e\u01a4\u01a8\u01ad\u01af\u01b7\u01b9")
        buf.write("\u01bf\u01c1\u01c9\u01ce\u01d0\u01e1\u01e6\u01f0\u01f8")
        buf.write("\4\b\2\2\3E\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    BLOCK_COMMENT = 2
    COLON = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNC = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    NIL = 21
    TRUE = 22
    FALSE = 23
    PLUS = 24
    MINUS = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQUAL = 29
    NOT_EQUAL = 30
    LESS = 31
    GREATER = 32
    LESS_OR_EQUAL = 33
    GREATER_OR_EQUAL = 34
    AND = 35
    OR = 36
    NOT = 37
    ASSIGN = 38
    SHORT_ASSIGN = 39
    PLUS_ASSIGN = 40
    MINUS_ASSIGN = 41
    MUL_ASSIGN = 42
    DIV_ASSIGN = 43
    MOD_ASSIGN = 44
    SELECTOR = 45
    COMMA = 46
    SEMICO = 47
    DEC_LIT = 48
    BIN_LIT = 49
    OCT_LIT = 50
    HEX_LIT = 51
    FLOAT_LIT = 52
    STRING_LIT = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    ID = 56
    LPAREN = 57
    RPAREN = 58
    LBRACE = 59
    RBRACE = 60
    LBRACK = 61
    RBRACK = 62
    NL = 63
    WS = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "','", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "COLON", "IF", "ELSE", "FOR", 
            "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
            "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
            "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
            "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "SELECTOR", 
            "COMMA", "SEMICO", "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", 
            "FLOAT_LIT", "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "NL", "WS", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "ALLOWED_TEXT", "BLOCK_COMMENT", "COLON", 
                  "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", 
                  "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", "PLUS_ASSIGN", 
                  "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "SELECTOR", "COMMA", "SEMICO", "DEC_LIT", "BIN_LIT", "OCT_LIT", 
                  "HEX_LIT", "FLOAT_LIT", "STRING_LIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ID", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "EXP", "DIGIT", "LETTER", 
                  "ESC", "NL", "WS", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.NL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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
                
     


