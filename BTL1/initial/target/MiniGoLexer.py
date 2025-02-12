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
        buf.write("\u01fb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\7\4\u00be\n\4\f\4\16\4\u00c1")
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
        buf.write("\3\62\7\62\u017f\n\62\f\62\16\62\u0182\13\62\5\62\u0184")
        buf.write("\n\62\3\63\3\63\3\63\6\63\u0189\n\63\r\63\16\63\u018a")
        buf.write("\3\64\3\64\3\64\6\64\u0190\n\64\r\64\16\64\u0191\3\65")
        buf.write("\3\65\3\65\6\65\u0197\n\65\r\65\16\65\u0198\3\66\6\66")
        buf.write("\u019c\n\66\r\66\16\66\u019d\3\66\3\66\7\66\u01a2\n\66")
        buf.write("\f\66\16\66\u01a5\13\66\3\66\5\66\u01a8\n\66\3\67\3\67")
        buf.write("\3\67\7\67\u01ad\n\67\f\67\16\67\u01b0\13\67\3\67\3\67")
        buf.write("\38\38\38\78\u01b7\n8\f8\168\u01ba\138\39\39\39\79\u01bf")
        buf.write("\n9\f9\169\u01c2\139\39\39\59\u01c6\n9\3:\3:\5:\u01ca")
        buf.write("\n:\3:\3:\3:\7:\u01cf\n:\f:\16:\u01d2\13:\3;\3;\3<\3<")
        buf.write("\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\5A\u01e2\nA\3A\6A\u01e5")
        buf.write("\nA\rA\16A\u01e6\3B\3B\3C\3C\3D\3D\3D\3E\3E\3E\3F\6F\u01f4")
        buf.write("\nF\rF\16F\u01f5\3F\3F\3G\3G\2\2H\3\3\5\2\7\4\t\5\13\6")
        buf.write("\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20")
        buf.write("!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67")
        buf.write("\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60")
        buf.write("a\61c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}?\177@\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089A\u008bB\u008dC\3\2\24")
        buf.write("\4\2\f\f\17\17\4\2,,\61\61\3\2\61\61\3\2,,\3\2\63;\4\2")
        buf.write("DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\6\2")
        buf.write("\f\f\17\17$$^^\4\2GGgg\4\2--//\3\2\62;\4\2C\\c|\7\2$$")
        buf.write("^^ppttvv\5\2\13\13\16\17\"\"\2\u0216\2\3\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3")
        buf.write("\u008f\3\2\2\2\5\u00a9\3\2\2\2\7\u00b8\3\2\2\2\t\u00c8")
        buf.write("\3\2\2\2\13\u00ca\3\2\2\2\r\u00cd\3\2\2\2\17\u00d2\3\2")
        buf.write("\2\2\21\u00d6\3\2\2\2\23\u00dd\3\2\2\2\25\u00e2\3\2\2")
        buf.write("\2\27\u00e7\3\2\2\2\31\u00ee\3\2\2\2\33\u00f8\3\2\2\2")
        buf.write("\35\u00ff\3\2\2\2\37\u0103\3\2\2\2!\u0109\3\2\2\2#\u0111")
        buf.write("\3\2\2\2%\u0117\3\2\2\2\'\u011b\3\2\2\2)\u0124\3\2\2\2")
        buf.write("+\u012a\3\2\2\2-\u0130\3\2\2\2/\u0134\3\2\2\2\61\u0139")
        buf.write("\3\2\2\2\63\u013f\3\2\2\2\65\u0141\3\2\2\2\67\u0143\3")
        buf.write("\2\2\29\u0145\3\2\2\2;\u0147\3\2\2\2=\u0149\3\2\2\2?\u014c")
        buf.write("\3\2\2\2A\u014f\3\2\2\2C\u0151\3\2\2\2E\u0153\3\2\2\2")
        buf.write("G\u0156\3\2\2\2I\u0159\3\2\2\2K\u015c\3\2\2\2M\u015f\3")
        buf.write("\2\2\2O\u0161\3\2\2\2Q\u0163\3\2\2\2S\u0166\3\2\2\2U\u0169")
        buf.write("\3\2\2\2W\u016c\3\2\2\2Y\u016f\3\2\2\2[\u0172\3\2\2\2")
        buf.write("]\u0175\3\2\2\2_\u0177\3\2\2\2a\u0179\3\2\2\2c\u0183\3")
        buf.write("\2\2\2e\u0185\3\2\2\2g\u018c\3\2\2\2i\u0193\3\2\2\2k\u019b")
        buf.write("\3\2\2\2m\u01a9\3\2\2\2o\u01b3\3\2\2\2q\u01bb\3\2\2\2")
        buf.write("s\u01c9\3\2\2\2u\u01d3\3\2\2\2w\u01d5\3\2\2\2y\u01d7\3")
        buf.write("\2\2\2{\u01d9\3\2\2\2}\u01db\3\2\2\2\177\u01dd\3\2\2\2")
        buf.write("\u0081\u01df\3\2\2\2\u0083\u01e8\3\2\2\2\u0085\u01ea\3")
        buf.write("\2\2\2\u0087\u01ec\3\2\2\2\u0089\u01ef\3\2\2\2\u008b\u01f3")
        buf.write("\3\2\2\2\u008d\u01f9\3\2\2\2\u008f\u0090\7\61\2\2\u0090")
        buf.write("\u0091\7\61\2\2\u0091\u0095\3\2\2\2\u0092\u0094\n\2\2")
        buf.write("\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0098\u0099\b\2\2\2\u0099\4\3\2\2\2\u009a")
        buf.write("\u00a8\n\3\2\2\u009b\u009d\7,\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a8\n\4\2\2\u00a1\u00a3")
        buf.write("\7\61\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a8\n\5\2\2\u00a7\u009a\3\2\2\2\u00a7\u009c\3")
        buf.write("\2\2\2\u00a7\u00a2\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b6\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ac\u00ae\7\61\2\2\u00ad\u00ac\3\2\2")
        buf.write("\2\u00ae\u00af\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b7\3\2\2\2\u00b1\u00b3\7,\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00ad\3")
        buf.write("\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\6")
        buf.write("\3\2\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba\7,\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bf\5\5\3\2\u00bc\u00be\5\7\4\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3")
        buf.write("\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\5\5\3\2\u00c3\u00c4\7,\2\2\u00c4")
        buf.write("\u00c5\7\61\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\b\4\2")
        buf.write("\2\u00c7\b\3\2\2\2\u00c8\u00c9\7<\2\2\u00c9\n\3\2\2\2")
        buf.write("\u00ca\u00cb\7k\2\2\u00cb\u00cc\7h\2\2\u00cc\f\3\2\2\2")
        buf.write("\u00cd\u00ce\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7u")
        buf.write("\2\2\u00d0\u00d1\7g\2\2\u00d1\16\3\2\2\2\u00d2\u00d3\7")
        buf.write("h\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7t\2\2\u00d5\20\3")
        buf.write("\2\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\22\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df")
        buf.write("\7w\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7e\2\2\u00e1\24")
        buf.write("\3\2\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7{\2\2\u00e4\u00e5")
        buf.write("\7r\2\2\u00e5\u00e6\7g\2\2\u00e6\26\3\2\2\2\u00e7\u00e8")
        buf.write("\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7v\2\2\u00ed\30")
        buf.write("\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\32\3\2\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\34\3\2\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102\36")
        buf.write("\3\2\2\2\u0103\u0104\7h\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7c\2\2\u0107\u0108\7v\2\2\u0108 \3")
        buf.write("\2\2\2\u0109\u010a\7d\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7q\2\2\u010c\u010d\7n\2\2\u010d\u010e\7g\2\2\u010e\u010f")
        buf.write("\7c\2\2\u010f\u0110\7p\2\2\u0110\"\3\2\2\2\u0111\u0112")
        buf.write("\7e\2\2\u0112\u0113\7q\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7v\2\2\u0116$\3\2\2\2\u0117\u0118")
        buf.write("\7x\2\2\u0118\u0119\7c\2\2\u0119\u011a\7t\2\2\u011a&\3")
        buf.write("\2\2\2\u011b\u011c\7e\2\2\u011c\u011d\7q\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7v\2\2\u011f\u0120\7k\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7w\2\2\u0122\u0123\7g\2\2\u0123(\3")
        buf.write("\2\2\2\u0124\u0125\7d\2\2\u0125\u0126\7t\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127\u0128\7c\2\2\u0128\u0129\7m\2\2\u0129*\3")
        buf.write("\2\2\2\u012a\u012b\7t\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7i\2\2\u012e\u012f\7g\2\2\u012f,\3")
        buf.write("\2\2\2\u0130\u0131\7p\2\2\u0131\u0132\7k\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133.\3\2\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7t\2\2\u0136\u0137\7w\2\2\u0137\u0138\7g\2\2\u0138\60")
        buf.write("\3\2\2\2\u0139\u013a\7h\2\2\u013a\u013b\7c\2\2\u013b\u013c")
        buf.write("\7n\2\2\u013c\u013d\7u\2\2\u013d\u013e\7g\2\2\u013e\62")
        buf.write("\3\2\2\2\u013f\u0140\7-\2\2\u0140\64\3\2\2\2\u0141\u0142")
        buf.write("\7/\2\2\u0142\66\3\2\2\2\u0143\u0144\7,\2\2\u01448\3\2")
        buf.write("\2\2\u0145\u0146\7\61\2\2\u0146:\3\2\2\2\u0147\u0148\7")
        buf.write("\'\2\2\u0148<\3\2\2\2\u0149\u014a\7?\2\2\u014a\u014b\7")
        buf.write("?\2\2\u014b>\3\2\2\2\u014c\u014d\7#\2\2\u014d\u014e\7")
        buf.write("?\2\2\u014e@\3\2\2\2\u014f\u0150\7>\2\2\u0150B\3\2\2\2")
        buf.write("\u0151\u0152\7@\2\2\u0152D\3\2\2\2\u0153\u0154\7>\2\2")
        buf.write("\u0154\u0155\7?\2\2\u0155F\3\2\2\2\u0156\u0157\7@\2\2")
        buf.write("\u0157\u0158\7?\2\2\u0158H\3\2\2\2\u0159\u015a\7(\2\2")
        buf.write("\u015a\u015b\7(\2\2\u015bJ\3\2\2\2\u015c\u015d\7~\2\2")
        buf.write("\u015d\u015e\7~\2\2\u015eL\3\2\2\2\u015f\u0160\7#\2\2")
        buf.write("\u0160N\3\2\2\2\u0161\u0162\7?\2\2\u0162P\3\2\2\2\u0163")
        buf.write("\u0164\7<\2\2\u0164\u0165\7?\2\2\u0165R\3\2\2\2\u0166")
        buf.write("\u0167\7-\2\2\u0167\u0168\7?\2\2\u0168T\3\2\2\2\u0169")
        buf.write("\u016a\7/\2\2\u016a\u016b\7?\2\2\u016bV\3\2\2\2\u016c")
        buf.write("\u016d\7,\2\2\u016d\u016e\7?\2\2\u016eX\3\2\2\2\u016f")
        buf.write("\u0170\7\61\2\2\u0170\u0171\7?\2\2\u0171Z\3\2\2\2\u0172")
        buf.write("\u0173\7\'\2\2\u0173\u0174\7?\2\2\u0174\\\3\2\2\2\u0175")
        buf.write("\u0176\7\60\2\2\u0176^\3\2\2\2\u0177\u0178\7.\2\2\u0178")
        buf.write("`\3\2\2\2\u0179\u017a\7=\2\2\u017ab\3\2\2\2\u017b\u0184")
        buf.write("\7\62\2\2\u017c\u0180\t\6\2\2\u017d\u017f\5\u0083B\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3")
        buf.write("\2\2\2\u0183\u017b\3\2\2\2\u0183\u017c\3\2\2\2\u0184d")
        buf.write("\3\2\2\2\u0185\u0186\7\62\2\2\u0186\u0188\t\7\2\2\u0187")
        buf.write("\u0189\t\b\2\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018bf\3\2\2")
        buf.write("\2\u018c\u018d\7\62\2\2\u018d\u018f\t\t\2\2\u018e\u0190")
        buf.write("\t\n\2\2\u018f\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192h\3\2\2\2\u0193")
        buf.write("\u0194\7\62\2\2\u0194\u0196\t\13\2\2\u0195\u0197\t\f\2")
        buf.write("\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199j\3\2\2\2\u019a\u019c")
        buf.write("\5\u0083B\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a3\7\60\2\2\u01a0\u01a2\5\u0083B\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a8\5\u0081A\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8l\3\2\2\2\u01a9\u01ae\7$\2\2\u01aa\u01ad")
        buf.write("\5\u0087D\2\u01ab\u01ad\n\r\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ae\3")
        buf.write("\2\2\2\u01b1\u01b2\7$\2\2\u01b2n\3\2\2\2\u01b3\u01b8\7")
        buf.write("$\2\2\u01b4\u01b7\5\u0087D\2\u01b5\u01b7\n\r\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9p\3\2\2")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01bb\u01c0\7$\2\2\u01bc\u01bf")
        buf.write("\5\u0087D\2\u01bd\u01bf\n\r\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3")
        buf.write("\2\2\2\u01c3\u01c5\7^\2\2\u01c4\u01c6\13\2\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6r\3\2\2\2\u01c7\u01ca")
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
        buf.write("\u0088\3\2\2\2\u01ef\u01f0\7\f\2\2\u01f0\u01f1\bE\3\2")
        buf.write("\u01f1\u008a\3\2\2\2\u01f2\u01f4\t\23\2\2\u01f3\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f6\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\bF\2\2")
        buf.write("\u01f8\u008c\3\2\2\2\u01f9\u01fa\13\2\2\2\u01fa\u008e")
        buf.write("\3\2\2\2!\2\u0095\u009e\u00a4\u00a7\u00a9\u00af\u00b4")
        buf.write("\u00b6\u00bf\u0180\u0183\u018a\u0191\u0198\u019d\u01a3")
        buf.write("\u01a7\u01ac\u01ae\u01b6\u01b8\u01be\u01c0\u01c5\u01c9")
        buf.write("\u01ce\u01d0\u01e1\u01e6\u01f5\4\b\2\2\3E\2")
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
            "','", "';'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'\n'" ]

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


    lineCount = 1
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
                
     


