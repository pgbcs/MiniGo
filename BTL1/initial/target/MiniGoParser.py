# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0275\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\6")
        buf.write("\2i\n\2\r\2\16\2j\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3t\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4~\n\4\3\5\3\5\5\5")
        buf.write("\u0082\n\5\3\6\3\6\3\6\5\6\u0087\n\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\5\b\u0092\n\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\6\t\u009a\n\t\r\t\16\t\u009b\3\t\3\t\3\t\6\t\u00a1")
        buf.write("\n\t\r\t\16\t\u00a2\3\t\3\t\3\t\5\t\u00a8\n\t\3\t\3\t")
        buf.write("\6\t\u00ac\n\t\r\t\16\t\u00ad\3\t\3\t\3\t\5\t\u00b3\n")
        buf.write("\t\3\n\3\n\3\n\3\n\7\n\u00b9\n\n\f\n\16\n\u00bc\13\n\3")
        buf.write("\n\3\n\3\n\7\n\u00c1\n\n\f\n\16\n\u00c4\13\n\5\n\u00c6")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13\u00cf\n\13")
        buf.write("\f\13\16\13\u00d2\13\13\3\13\3\13\3\13\3\f\3\f\7\f\u00d9")
        buf.write("\n\f\f\f\16\f\u00dc\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\7\16\u00e9\n\16\f\16\16\16\u00ec\13")
        buf.write("\16\3\16\5\16\u00ef\n\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\7\20\u00fa\n\20\f\20\16\20\u00fd\13\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u0107\n")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0111")
        buf.write("\n\22\3\22\3\22\3\22\7\22\u0116\n\22\f\22\16\22\u0119")
        buf.write("\13\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u0128\n\23\3\23\3\23\3\23\7\23")
        buf.write("\u012d\n\23\f\23\16\23\u0130\13\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\6\24\u0137\n\24\r\24\16\24\u0138\3\24\3\24\5\24")
        buf.write("\u013d\n\24\3\25\3\25\5\25\u0141\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0148\n\26\3\27\3\27\3\27\6\27\u014d\n\27")
        buf.write("\r\27\16\27\u014e\3\27\3\27\5\27\u0153\n\27\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0159\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\7\32\u0166\n\32\f\32\16\32")
        buf.write("\u0169\13\32\5\32\u016b\n\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u0176\n\33\f\33\16\33\u0179")
        buf.write("\13\33\5\33\u017b\n\33\3\33\3\33\3\34\3\34\3\34\3\34\5")
        buf.write("\34\u0183\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u018b")
        buf.write("\n\35\f\35\16\35\u018e\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u0196\n\36\f\36\16\36\u0199\13\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u01a1\n\37\f\37\16\37\u01a4")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \7 \u01ac\n \f \16 \u01af\13 ")
        buf.write("\3!\3!\3!\3!\3!\3!\7!\u01b7\n!\f!\16!\u01ba\13!\3\"\3")
        buf.write("\"\3\"\5\"\u01bf\n\"\3#\3#\3#\3#\3#\5#\u01c6\n#\3$\3$")
        buf.write("\3$\3$\7$\u01cc\n$\f$\16$\u01cf\13$\3%\6%\u01d2\n%\r%")
        buf.write("\16%\u01d3\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01f0\n)\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3-\3-\3-\3-\3-\3-\3-\7-\u0201\n")
        buf.write("-\f-\16-\u0204\13-\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u020f")
        buf.write("\n-\f-\16-\u0212\13-\3-\3-\7-\u0216\n-\f-\16-\u0219\13")
        buf.write("-\3-\3-\3-\3-\7-\u021f\n-\f-\16-\u0222\13-\3-\5-\u0225")
        buf.write("\n-\3-\3-\3.\3.\3.\3.\3.\7.\u022e\n.\f.\16.\u0231\13.")
        buf.write("\3.\3.\3.\3.\3.\3.\5.\u0239\n.\3.\3.\3.\3.\3.\3.\7.\u0241")
        buf.write("\n.\f.\16.\u0244\13.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.")
        buf.write("\5.\u0251\n.\3.\3.\3.\7.\u0256\n.\f.\16.\u0259\13.\3.")
        buf.write("\3.\5.\u025d\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\5\62\u026b\n\62\3\62\3\62\3\63\3\63\5\63")
        buf.write("\u0271\n\63\3\63\3\63\3\63\2\78:<>@\64\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bd\2\t\3\2\37$\3\2\32\33\3\2\34\36\4\2\33")
        buf.write("\33\'\'\3\2).\4\2\16\21::\4\2\62\62::\2\u029e\2h\3\2\2")
        buf.write("\2\4s\3\2\2\2\6}\3\2\2\2\b\u0081\3\2\2\2\n\u0086\3\2\2")
        buf.write("\2\f\u008a\3\2\2\2\16\u008e\3\2\2\2\20\u0096\3\2\2\2\22")
        buf.write("\u00b4\3\2\2\2\24\u00c9\3\2\2\2\26\u00d6\3\2\2\2\30\u00e0")
        buf.write("\3\2\2\2\32\u00ee\3\2\2\2\34\u00f0\3\2\2\2\36\u00f4\3")
        buf.write("\2\2\2 \u0101\3\2\2\2\"\u010a\3\2\2\2$\u011d\3\2\2\2&")
        buf.write("\u013c\3\2\2\2(\u0140\3\2\2\2*\u0147\3\2\2\2,\u0149\3")
        buf.write("\2\2\2.\u0158\3\2\2\2\60\u015a\3\2\2\2\62\u0160\3\2\2")
        buf.write("\2\64\u016e\3\2\2\2\66\u0182\3\2\2\28\u0184\3\2\2\2:\u018f")
        buf.write("\3\2\2\2<\u019a\3\2\2\2>\u01a5\3\2\2\2@\u01b0\3\2\2\2")
        buf.write("B\u01be\3\2\2\2D\u01c5\3\2\2\2F\u01c7\3\2\2\2H\u01d1\3")
        buf.write("\2\2\2J\u01d8\3\2\2\2L\u01dc\3\2\2\2N\u01e1\3\2\2\2P\u01ef")
        buf.write("\3\2\2\2R\u01f1\3\2\2\2T\u01f3\3\2\2\2V\u01f7\3\2\2\2")
        buf.write("X\u01f9\3\2\2\2Z\u025c\3\2\2\2\\\u025e\3\2\2\2^\u0262")
        buf.write("\3\2\2\2`\u0265\3\2\2\2b\u026a\3\2\2\2d\u026e\3\2\2\2")
        buf.write("fi\5\4\3\2gi\5\6\4\2hf\3\2\2\2hg\3\2\2\2ij\3\2\2\2jh\3")
        buf.write("\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7\2\2\3m\3\3\2\2\2nt\5\"")
        buf.write("\22\2ot\5\24\13\2pt\5\36\20\2qt\5$\23\2rt\5\b\5\2sn\3")
        buf.write("\2\2\2so\3\2\2\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2\2t\5\3\2")
        buf.write("\2\2u~\5V,\2v~\5L\'\2w~\5X-\2x~\5Z.\2y~\5^\60\2z~\5`\61")
        buf.write("\2{~\5b\62\2|~\5d\63\2}u\3\2\2\2}v\3\2\2\2}w\3\2\2\2}")
        buf.write("x\3\2\2\2}y\3\2\2\2}z\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\7\3")
        buf.write("\2\2\2\177\u0082\5\n\6\2\u0080\u0082\5\60\31\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0080\3\2\2\2\u0082\t\3\2\2\2\u0083\u0087")
        buf.write("\5\16\b\2\u0084\u0087\5\f\7\2\u0085\u0087\5\20\t\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\5V,\2\u0089\13\3\2\2")
        buf.write("\2\u008a\u008b\7\23\2\2\u008b\u008c\7:\2\2\u008c\u008d")
        buf.write("\5R*\2\u008d\r\3\2\2\2\u008e\u008f\7\23\2\2\u008f\u0091")
        buf.write("\7:\2\2\u0090\u0092\5R*\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7(\2\2\u0094")
        buf.write("\u0095\58\35\2\u0095\17\3\2\2\2\u0096\u0097\7\23\2\2\u0097")
        buf.write("\u00b2\7:\2\2\u0098\u009a\5T+\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009d\3\2\2\2\u009d\u00a7\5R*\2\u009e\u00a0\7(")
        buf.write("\2\2\u009f\u00a1\5T+\2\u00a0\u009f\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\5R*\2\u00a5\u00a6\5\22\n\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u009e\3\2\2\2\u00a7\u00a8\3")
        buf.write("\2\2\2\u00a8\u00b3\3\2\2\2\u00a9\u00ab\7(\2\2\u00aa\u00ac")
        buf.write("\5T+\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\5R*\2\u00b0\u00b1\5\22\n\2\u00b1\u00b3\3\2\2\2")
        buf.write("\u00b2\u0099\3\2\2\2\u00b2\u00a9\3\2\2\2\u00b3\21\3\2")
        buf.write("\2\2\u00b4\u00c5\7=\2\2\u00b5\u00ba\5\22\n\2\u00b6\u00b7")
        buf.write("\7\60\2\2\u00b7\u00b9\5\22\n\2\u00b8\u00b6\3\2\2\2\u00b9")
        buf.write("\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00c6\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00c2\5")
        buf.write("8\35\2\u00be\u00bf\7\60\2\2\u00bf\u00c1\58\35\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00b5\3\2\2\2\u00c5\u00bd\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c8\7>\2\2\u00c8\23\3\2\2\2\u00c9\u00ca")
        buf.write("\7\13\2\2\u00ca\u00cb\7:\2\2\u00cb\u00cc\7\f\2\2\u00cc")
        buf.write("\u00d0\7=\2\2\u00cd\u00cf\5\26\f\2\u00ce\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4")
        buf.write("\7>\2\2\u00d4\u00d5\5V,\2\u00d5\25\3\2\2\2\u00d6\u00da")
        buf.write("\7:\2\2\u00d7\u00d9\5T+\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\5R*\2\u00de")
        buf.write("\u00df\5V,\2\u00df\27\3\2\2\2\u00e0\u00e1\7:\2\2\u00e1")
        buf.write("\u00e2\7=\2\2\u00e2\u00e3\5\32\16\2\u00e3\u00e4\7>\2\2")
        buf.write("\u00e4\31\3\2\2\2\u00e5\u00ea\5\34\17\2\u00e6\u00e7\7")
        buf.write("\60\2\2\u00e7\u00e9\5\34\17\2\u00e8\u00e6\3\2\2\2\u00e9")
        buf.write("\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ef\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ef\3")
        buf.write("\2\2\2\u00ee\u00e5\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\33")
        buf.write("\3\2\2\2\u00f0\u00f1\7:\2\2\u00f1\u00f2\7\5\2\2\u00f2")
        buf.write("\u00f3\58\35\2\u00f3\35\3\2\2\2\u00f4\u00f5\7\13\2\2\u00f5")
        buf.write("\u00f6\7:\2\2\u00f6\u00f7\7\r\2\2\u00f7\u00fb\7=\2\2\u00f8")
        buf.write("\u00fa\5 \21\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3")
        buf.write("\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7>\2\2\u00ff\u0100")
        buf.write("\5V,\2\u0100\37\3\2\2\2\u0101\u0102\7:\2\2\u0102\u0103")
        buf.write("\7;\2\2\u0103\u0104\5(\25\2\u0104\u0106\7<\2\2\u0105\u0107")
        buf.write("\5R*\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0109\5V,\2\u0109!\3\2\2\2\u010a\u010b")
        buf.write("\7\n\2\2\u010b\u010c\7:\2\2\u010c\u010d\7;\2\2\u010d\u010e")
        buf.write("\5(\25\2\u010e\u0110\7<\2\2\u010f\u0111\5&\24\2\u0110")
        buf.write("\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0117\7=\2\2\u0113\u0116\5\6\4\2\u0114\u0116\5")
        buf.write("\b\5\2\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7>\2\2")
        buf.write("\u011b\u011c\5V,\2\u011c#\3\2\2\2\u011d\u011e\7\n\2\2")
        buf.write("\u011e\u011f\7;\2\2\u011f\u0120\7:\2\2\u0120\u0121\7:")
        buf.write("\2\2\u0121\u0122\7<\2\2\u0122\u0123\7:\2\2\u0123\u0124")
        buf.write("\7;\2\2\u0124\u0125\5(\25\2\u0125\u0127\7<\2\2\u0126\u0128")
        buf.write("\5&\24\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012e\7=\2\2\u012a\u012d\5\6\4\2")
        buf.write("\u012b\u012d\5\b\5\2\u012c\u012a\3\2\2\2\u012c\u012b\3")
        buf.write("\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0131")
        buf.write("\u0132\7>\2\2\u0132\u0133\5V,\2\u0133%\3\2\2\2\u0134\u013d")
        buf.write("\5R*\2\u0135\u0137\5T+\2\u0136\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u013b\5R*\2\u013b\u013d\3\2\2\2\u013c")
        buf.write("\u0134\3\2\2\2\u013c\u0136\3\2\2\2\u013d\'\3\2\2\2\u013e")
        buf.write("\u0141\5*\26\2\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2")
        buf.write("\u0140\u013f\3\2\2\2\u0141)\3\2\2\2\u0142\u0143\5,\27")
        buf.write("\2\u0143\u0144\7\60\2\2\u0144\u0145\5*\26\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0148\5,\27\2\u0147\u0142\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148+\3\2\2\2\u0149\u0152\5.\30\2\u014a")
        buf.write("\u0153\5R*\2\u014b\u014d\5T+\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0151\5R*\2\u0151\u0153\3\2")
        buf.write("\2\2\u0152\u014a\3\2\2\2\u0152\u014c\3\2\2\2\u0153-\3")
        buf.write("\2\2\2\u0154\u0155\7:\2\2\u0155\u0156\7\60\2\2\u0156\u0159")
        buf.write("\5.\30\2\u0157\u0159\7:\2\2\u0158\u0154\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159/\3\2\2\2\u015a\u015b\7\22\2\2\u015b")
        buf.write("\u015c\7:\2\2\u015c\u015d\7(\2\2\u015d\u015e\58\35\2\u015e")
        buf.write("\u015f\5V,\2\u015f\61\3\2\2\2\u0160\u0161\7:\2\2\u0161")
        buf.write("\u016a\7;\2\2\u0162\u0167\5\66\34\2\u0163\u0164\7\60\2")
        buf.write("\2\u0164\u0166\5\66\34\2\u0165\u0163\3\2\2\2\u0166\u0169")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u0162\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\7")
        buf.write("<\2\2\u016d\63\3\2\2\2\u016e\u016f\7:\2\2\u016f\u0170")
        buf.write("\7/\2\2\u0170\u0171\7:\2\2\u0171\u017a\7;\2\2\u0172\u0177")
        buf.write("\5\66\34\2\u0173\u0174\7\60\2\2\u0174\u0176\5\66\34\2")
        buf.write("\u0175\u0173\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u0172\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c\u017d\7<\2\2\u017d\65\3\2\2\2\u017e")
        buf.write("\u0183\58\35\2\u017f\u0183\5\62\32\2\u0180\u0183\5\64")
        buf.write("\33\2\u0181\u0183\5F$\2\u0182\u017e\3\2\2\2\u0182\u017f")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("\67\3\2\2\2\u0184\u0185\b\35\1\2\u0185\u0186\5:\36\2\u0186")
        buf.write("\u018c\3\2\2\2\u0187\u0188\f\4\2\2\u0188\u0189\7&\2\2")
        buf.write("\u0189\u018b\5:\36\2\u018a\u0187\3\2\2\2\u018b\u018e\3")
        buf.write("\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d9")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\b\36\1\2\u0190")
        buf.write("\u0191\5<\37\2\u0191\u0197\3\2\2\2\u0192\u0193\f\4\2\2")
        buf.write("\u0193\u0194\7%\2\2\u0194\u0196\5<\37\2\u0195\u0192\3")
        buf.write("\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198;\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b")
        buf.write("\b\37\1\2\u019b\u019c\5> \2\u019c\u01a2\3\2\2\2\u019d")
        buf.write("\u019e\f\4\2\2\u019e\u019f\t\2\2\2\u019f\u01a1\5> \2\u01a0")
        buf.write("\u019d\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3=\3\2\2\2\u01a4\u01a2\3\2\2")
        buf.write("\2\u01a5\u01a6\b \1\2\u01a6\u01a7\5@!\2\u01a7\u01ad\3")
        buf.write("\2\2\2\u01a8\u01a9\f\4\2\2\u01a9\u01aa\t\3\2\2\u01aa\u01ac")
        buf.write("\5@!\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae?\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b1\b!\1\2\u01b1\u01b2\5B\"\2\u01b2\u01b8")
        buf.write("\3\2\2\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5\t\4\2\2\u01b5")
        buf.write("\u01b7\5B\"\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9A\3\2\2")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\t\5\2\2\u01bc\u01bf")
        buf.write("\5B\"\2\u01bd\u01bf\5D#\2\u01be\u01bb\3\2\2\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bfC\3\2\2\2\u01c0\u01c6\5P)\2\u01c1\u01c2")
        buf.write("\7;\2\2\u01c2\u01c3\58\35\2\u01c3\u01c4\7<\2\2\u01c4\u01c6")
        buf.write("\3\2\2\2\u01c5\u01c0\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c6")
        buf.write("E\3\2\2\2\u01c7\u01cd\7:\2\2\u01c8\u01cc\5J&\2\u01c9\u01ca")
        buf.write("\13\2\2\2\u01ca\u01cc\7:\2\2\u01cb\u01c8\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01ceG\3\2\2\2\u01cf\u01cd\3\2\2")
        buf.write("\2\u01d0\u01d2\5T+\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3")
        buf.write("\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d6\5R*\2\u01d6\u01d7\5\22\n\2\u01d7")
        buf.write("I\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9\u01da\58\35\2\u01da")
        buf.write("\u01db\7@\2\2\u01dbK\3\2\2\2\u01dc\u01dd\5F$\2\u01dd\u01de")
        buf.write("\5N(\2\u01de\u01df\58\35\2\u01df\u01e0\5V,\2\u01e0M\3")
        buf.write("\2\2\2\u01e1\u01e2\t\6\2\2\u01e2O\3\2\2\2\u01e3\u01f0")
        buf.write("\7\62\2\2\u01e4\u01f0\7\63\2\2\u01e5\u01f0\7\64\2\2\u01e6")
        buf.write("\u01f0\7\65\2\2\u01e7\u01f0\7\66\2\2\u01e8\u01f0\7\67")
        buf.write("\2\2\u01e9\u01f0\7\30\2\2\u01ea\u01f0\7\31\2\2\u01eb\u01f0")
        buf.write("\7\27\2\2\u01ec\u01f0\5\30\r\2\u01ed\u01f0\5F$\2\u01ee")
        buf.write("\u01f0\5H%\2\u01ef\u01e3\3\2\2\2\u01ef\u01e4\3\2\2\2\u01ef")
        buf.write("\u01e5\3\2\2\2\u01ef\u01e6\3\2\2\2\u01ef\u01e7\3\2\2\2")
        buf.write("\u01ef\u01e8\3\2\2\2\u01ef\u01e9\3\2\2\2\u01ef\u01ea\3")
        buf.write("\2\2\2\u01ef\u01eb\3\2\2\2\u01ef\u01ec\3\2\2\2\u01ef\u01ed")
        buf.write("\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0Q\3\2\2\2\u01f1\u01f2")
        buf.write("\t\7\2\2\u01f2S\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5")
        buf.write("\t\b\2\2\u01f5\u01f6\7@\2\2\u01f6U\3\2\2\2\u01f7\u01f8")
        buf.write("\7\61\2\2\u01f8W\3\2\2\2\u01f9\u01fa\7\6\2\2\u01fa\u01fb")
        buf.write("\7;\2\2\u01fb\u01fc\58\35\2\u01fc\u01fd\7<\2\2\u01fd\u0202")
        buf.write("\7=\2\2\u01fe\u0201\5\6\4\2\u01ff\u0201\5\b\5\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0204\3\2\2\2")
        buf.write("\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3")
        buf.write("\2\2\2\u0204\u0202\3\2\2\2\u0205\u0217\7>\2\2\u0206\u0207")
        buf.write("\7\7\2\2\u0207\u0208\7\6\2\2\u0208\u0209\7;\2\2\u0209")
        buf.write("\u020a\58\35\2\u020a\u020b\7<\2\2\u020b\u0210\7=\2\2\u020c")
        buf.write("\u020f\5\6\4\2\u020d\u020f\5\b\5\2\u020e\u020c\3\2\2\2")
        buf.write("\u020e\u020d\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e\3")
        buf.write("\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u0210")
        buf.write("\3\2\2\2\u0213\u0214\7>\2\2\u0214\u0216\3\2\2\2\u0215")
        buf.write("\u0206\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u0224\3\2\2\2\u0219\u0217\3")
        buf.write("\2\2\2\u021a\u021b\7\7\2\2\u021b\u0220\7=\2\2\u021c\u021f")
        buf.write("\5\6\4\2\u021d\u021f\5\4\3\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021d\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0220\3")
        buf.write("\2\2\2\u0223\u0225\7>\2\2\u0224\u021a\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\5V,\2\u0227Y")
        buf.write("\3\2\2\2\u0228\u0229\7\b\2\2\u0229\u022a\58\35\2\u022a")
        buf.write("\u022f\7=\2\2\u022b\u022e\5\6\4\2\u022c\u022e\5\b\5\2")
        buf.write("\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2\u022e\u0231\3")
        buf.write("\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232")
        buf.write("\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0233\7>\2\2\u0233")
        buf.write("\u0234\5V,\2\u0234\u025d\3\2\2\2\u0235\u0238\7\b\2\2\u0236")
        buf.write("\u0239\5L\'\2\u0237\u0239\5\16\b\2\u0238\u0236\3\2\2\2")
        buf.write("\u0238\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\5")
        buf.write("8\35\2\u023b\u023c\7\61\2\2\u023c\u023d\5\\/\2\u023d\u0242")
        buf.write("\7=\2\2\u023e\u0241\5\6\4\2\u023f\u0241\5\b\5\2\u0240")
        buf.write("\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241\u0244\3\2\2\2")
        buf.write("\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0245\3")
        buf.write("\2\2\2\u0244\u0242\3\2\2\2\u0245\u0246\7>\2\2\u0246\u0247")
        buf.write("\5V,\2\u0247\u025d\3\2\2\2\u0248\u0249\7\b\2\2\u0249\u024a")
        buf.write("\7:\2\2\u024a\u024b\7\60\2\2\u024b\u024c\7:\2\2\u024c")
        buf.write("\u024d\7)\2\2\u024d\u0250\7\26\2\2\u024e\u0251\7:\2\2")
        buf.write("\u024f\u0251\5H%\2\u0250\u024e\3\2\2\2\u0250\u024f\3\2")
        buf.write("\2\2\u0251\u0252\3\2\2\2\u0252\u0257\7=\2\2\u0253\u0256")
        buf.write("\5\6\4\2\u0254\u0256\5\b\5\2\u0255\u0253\3\2\2\2\u0255")
        buf.write("\u0254\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2")
        buf.write("\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2\u0259\u0257\3")
        buf.write("\2\2\2\u025a\u025b\7>\2\2\u025b\u025d\5V,\2\u025c\u0228")
        buf.write("\3\2\2\2\u025c\u0235\3\2\2\2\u025c\u0248\3\2\2\2\u025d")
        buf.write("[\3\2\2\2\u025e\u025f\5F$\2\u025f\u0260\5N(\2\u0260\u0261")
        buf.write("\58\35\2\u0261]\3\2\2\2\u0262\u0263\7\25\2\2\u0263\u0264")
        buf.write("\5V,\2\u0264_\3\2\2\2\u0265\u0266\7\24\2\2\u0266\u0267")
        buf.write("\5V,\2\u0267a\3\2\2\2\u0268\u026b\5\62\32\2\u0269\u026b")
        buf.write("\5\64\33\2\u026a\u0268\3\2\2\2\u026a\u0269\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u026d\5V,\2\u026dc\3\2\2\2\u026e")
        buf.write("\u0270\7\t\2\2\u026f\u0271\58\35\2\u0270\u026f\3\2\2\2")
        buf.write("\u0270\u0271\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273\5")
        buf.write("V,\2\u0273e\3\2\2\2Ghjs}\u0081\u0086\u0091\u009b\u00a2")
        buf.write("\u00a7\u00ad\u00b2\u00ba\u00c2\u00c5\u00d0\u00da\u00ea")
        buf.write("\u00ee\u00fb\u0106\u0110\u0115\u0117\u0127\u012c\u012e")
        buf.write("\u0138\u013c\u0140\u0147\u014e\u0152\u0158\u0167\u016a")
        buf.write("\u0177\u017a\u0182\u018c\u0197\u01a2\u01ad\u01b8\u01be")
        buf.write("\u01c5\u01cb\u01cd\u01d3\u01ef\u0200\u0202\u020e\u0210")
        buf.write("\u0217\u021e\u0220\u0224\u022d\u022f\u0238\u0240\u0242")
        buf.write("\u0250\u0255\u0257\u025c\u026a\u0270")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "':'", "'if'", 
                     "'else'", "'for'", "'return'", "'func'", "'type'", 
                     "'struct'", "'interface'", "'string'", "'int'", "'float'", 
                     "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'nil'", "'true'", "'false'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "','", 
                     "';'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", "COLON", 
                      "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                      "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                      "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", 
                      "TRUE", "FALSE", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                      "GREATER_OR_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
                      "SHORT_ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "SELECTOR", "COMMA", "SEMICO", 
                      "DEC_LIT", "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ID", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "NL", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_stmt = 2
    RULE_blockdecl = 3
    RULE_vardecl = 4
    RULE_normal_vardecl_non_init = 5
    RULE_normal_vardecl_init = 6
    RULE_arr_vardecl = 7
    RULE_list_value = 8
    RULE_structdecl = 9
    RULE_fielddecl = 10
    RULE_structinst = 11
    RULE_fieldinstlist = 12
    RULE_fieldinst = 13
    RULE_interfacedecl = 14
    RULE_methoddecl = 15
    RULE_funcdecl = 16
    RULE_methodimple = 17
    RULE_returntype = 18
    RULE_param_list = 19
    RULE_param_group_prime = 20
    RULE_param_group = 21
    RULE_param_mem_list = 22
    RULE_constdecl = 23
    RULE_funccall = 24
    RULE_methodcall = 25
    RULE_actualparam = 26
    RULE_expr = 27
    RULE_factor1 = 28
    RULE_factor2 = 29
    RULE_factor3 = 30
    RULE_factor4 = 31
    RULE_factor5 = 32
    RULE_factor6 = 33
    RULE_var = 34
    RULE_arr_lit = 35
    RULE_arr_dim_acc = 36
    RULE_assignstmt = 37
    RULE_assign = 38
    RULE_value = 39
    RULE_typedecl = 40
    RULE_arr_dim = 41
    RULE_endstmt = 42
    RULE_ifstmt = 43
    RULE_forstmt = 44
    RULE_updatestmt = 45
    RULE_breakstmt = 46
    RULE_continuestmt = 47
    RULE_callstmt = 48
    RULE_returnstmt = 49

    ruleNames =  [ "program", "decl", "stmt", "blockdecl", "vardecl", "normal_vardecl_non_init", 
                   "normal_vardecl_init", "arr_vardecl", "list_value", "structdecl", 
                   "fielddecl", "structinst", "fieldinstlist", "fieldinst", 
                   "interfacedecl", "methoddecl", "funcdecl", "methodimple", 
                   "returntype", "param_list", "param_group_prime", "param_group", 
                   "param_mem_list", "constdecl", "funccall", "methodcall", 
                   "actualparam", "expr", "factor1", "factor2", "factor3", 
                   "factor4", "factor5", "factor6", "var", "arr_lit", "arr_dim_acc", 
                   "assignstmt", "assign", "value", "typedecl", "arr_dim", 
                   "endstmt", "ifstmt", "forstmt", "updatestmt", "breakstmt", 
                   "continuestmt", "callstmt", "returnstmt" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    BLOCK_COMMENT=2
    COLON=3
    IF=4
    ELSE=5
    FOR=6
    RETURN=7
    FUNC=8
    TYPE=9
    STRUCT=10
    INTERFACE=11
    STRING=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    CONST=16
    VAR=17
    CONTINUE=18
    BREAK=19
    RANGE=20
    NIL=21
    TRUE=22
    FALSE=23
    PLUS=24
    MINUS=25
    MUL=26
    DIV=27
    MOD=28
    EQUAL=29
    NOT_EQUAL=30
    LESS=31
    GREATER=32
    LESS_OR_EQUAL=33
    GREATER_OR_EQUAL=34
    AND=35
    OR=36
    NOT=37
    ASSIGN=38
    SHORT_ASSIGN=39
    PLUS_ASSIGN=40
    MINUS_ASSIGN=41
    MUL_ASSIGN=42
    DIV_ASSIGN=43
    MOD_ASSIGN=44
    SELECTOR=45
    COMMA=46
    SEMICO=47
    DEC_LIT=48
    BIN_LIT=49
    OCT_LIT=50
    HEX_LIT=51
    FLOAT_LIT=52
    STRING_LIT=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ID=56
    LPAREN=57
    RPAREN=58
    LBRACE=59
    RBRACE=60
    LBRACK=61
    RBRACK=62
    NL=63
    WS=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 100
                    self.decl()
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 101
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 104 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 106
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def methodimple(self):
            return self.getTypedRuleContext(MiniGoParser.MethodimpleContext,0)


        def blockdecl(self):
            return self.getTypedRuleContext(MiniGoParser.BlockdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.structdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.interfacedecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.methodimple()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.blockdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.endstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.callstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdecl" ):
                return visitor.visitBlockdecl(self)
            else:
                return visitor.visitChildren(self)




    def blockdecl(self):

        localctx = MiniGoParser.BlockdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blockdecl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.vardecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.constdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def normal_vardecl_init(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardecl_initContext,0)


        def normal_vardecl_non_init(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardecl_non_initContext,0)


        def arr_vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_vardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 129
                self.normal_vardecl_init()
                pass

            elif la_ == 2:
                self.state = 130
                self.normal_vardecl_non_init()
                pass

            elif la_ == 3:
                self.state = 131
                self.arr_vardecl()
                pass


            self.state = 134
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_vardecl_non_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_normal_vardecl_non_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_vardecl_non_init" ):
                return visitor.visitNormal_vardecl_non_init(self)
            else:
                return visitor.visitChildren(self)




    def normal_vardecl_non_init(self):

        localctx = MiniGoParser.Normal_vardecl_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_vardecl_non_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiniGoParser.VAR)
            self.state = 137
            self.match(MiniGoParser.ID)
            self.state = 138
            self.typedecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_vardecl_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_normal_vardecl_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_vardecl_init" ):
                return visitor.visitNormal_vardecl_init(self)
            else:
                return visitor.visitChildren(self)




    def normal_vardecl_init(self):

        localctx = MiniGoParser.Normal_vardecl_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_normal_vardecl_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MiniGoParser.VAR)
            self.state = 141
            self.match(MiniGoParser.ID)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 142
                self.typedecl()


            self.state = 145
            self.match(MiniGoParser.ASSIGN)
            self.state = 146
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypedeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypedeclContext,i)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def list_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_valueContext,0)


        def arr_dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dimContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_vardecl" ):
                return visitor.visitArr_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def arr_vardecl(self):

        localctx = MiniGoParser.Arr_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arr_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MiniGoParser.VAR)
            self.state = 149
            self.match(MiniGoParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 150
                    self.arr_dim()
                    self.state = 153 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 155
                self.typedecl()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 156
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 158 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 157
                        self.arr_dim()
                        self.state = 160 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==MiniGoParser.LBRACK):
                            break

                    self.state = 162
                    self.typedecl()
                    self.state = 163
                    self.list_value()


                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 167
                self.match(MiniGoParser.ASSIGN)
                self.state = 169 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 168
                    self.arr_dim()
                    self.state = 171 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 173
                self.typedecl()
                self.state = 174
                self.list_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_valueContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_valueContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_list_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_value" ):
                return visitor.visitList_value(self)
            else:
                return visitor.visitChildren(self)




    def list_value(self):

        localctx = MiniGoParser.List_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.LBRACE)
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.state = 179
                self.list_value()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 180
                    self.match(MiniGoParser.COMMA)
                    self.state = 181
                    self.list_value()
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACK]:
                self.state = 187
                self.expr(0)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 188
                    self.match(MiniGoParser.COMMA)
                    self.state = 189
                    self.expr(0)
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 197
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MiniGoParser.TYPE)
            self.state = 200
            self.match(MiniGoParser.ID)
            self.state = 201
            self.match(MiniGoParser.STRUCT)
            self.state = 202
            self.match(MiniGoParser.LBRACE)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 203
                self.fielddecl()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(MiniGoParser.RBRACE)
            self.state = 210
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def arr_dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dimContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 213
                self.arr_dim()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.typedecl()
            self.state = 220
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def fieldinstlist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldinstlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst" ):
                return visitor.visitStructinst(self)
            else:
                return visitor.visitChildren(self)




    def structinst(self):

        localctx = MiniGoParser.StructinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.ID)
            self.state = 223
            self.match(MiniGoParser.LBRACE)
            self.state = 224
            self.fieldinstlist()
            self.state = 225
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldinstlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldinst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FieldinstContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FieldinstContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldinstlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldinstlist" ):
                return visitor.visitFieldinstlist(self)
            else:
                return visitor.visitChildren(self)




    def fieldinstlist(self):

        localctx = MiniGoParser.FieldinstlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_fieldinstlist)
        self._la = 0 # Token type
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.fieldinst()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 228
                    self.match(MiniGoParser.COMMA)
                    self.state = 229
                    self.fieldinst()
                    self.state = 234
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldinstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldinst" ):
                return visitor.visitFieldinst(self)
            else:
                return visitor.visitChildren(self)




    def fieldinst(self):

        localctx = MiniGoParser.FieldinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fieldinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 239
            self.match(MiniGoParser.COLON)
            self.state = 240
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def methoddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethoddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.TYPE)
            self.state = 243
            self.match(MiniGoParser.ID)
            self.state = 244
            self.match(MiniGoParser.INTERFACE)
            self.state = 245
            self.match(MiniGoParser.LBRACE)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 246
                self.methoddecl()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(MiniGoParser.RBRACE)
            self.state = 253
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MiniGoParser.ID)
            self.state = 256
            self.match(MiniGoParser.LPAREN)
            self.state = 257
            self.param_list()
            self.state = 258
            self.match(MiniGoParser.RPAREN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 259
                self.typedecl()


            self.state = 262
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def blockdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockdeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockdeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.FUNC)
            self.state = 265
            self.match(MiniGoParser.ID)
            self.state = 266
            self.match(MiniGoParser.LPAREN)
            self.state = 267
            self.param_list()
            self.state = 268
            self.match(MiniGoParser.RPAREN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 269
                self.returntype()


            self.state = 272
            self.match(MiniGoParser.LBRACE)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 275
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 273
                    self.stmt()
                    pass
                elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 274
                    self.blockdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
            self.match(MiniGoParser.RBRACE)
            self.state = 281
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodimpleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def param_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_listContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def blockdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockdeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockdeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodimple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodimple" ):
                return visitor.visitMethodimple(self)
            else:
                return visitor.visitChildren(self)




    def methodimple(self):

        localctx = MiniGoParser.MethodimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_methodimple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.FUNC)
            self.state = 284
            self.match(MiniGoParser.LPAREN)
            self.state = 285
            self.match(MiniGoParser.ID)
            self.state = 286
            self.match(MiniGoParser.ID)
            self.state = 287
            self.match(MiniGoParser.RPAREN)
            self.state = 288
            self.match(MiniGoParser.ID)
            self.state = 289
            self.match(MiniGoParser.LPAREN)
            self.state = 290
            self.param_list()
            self.state = 291
            self.match(MiniGoParser.RPAREN)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 292
                self.returntype()


            self.state = 295
            self.match(MiniGoParser.LBRACE)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 298
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 296
                    self.stmt()
                    pass
                elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 297
                    self.blockdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 303
            self.match(MiniGoParser.RBRACE)
            self.state = 304
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def arr_dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dimContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MiniGoParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returntype)
        self._la = 0 # Token type
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.typedecl()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 307
                    self.arr_dim()
                    self.state = 310 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 312
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_group_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_group_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param_list)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.param_group_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_group_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_group(self):
            return self.getTypedRuleContext(MiniGoParser.Param_groupContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_group_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_group_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_group_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_group_prime" ):
                return visitor.visitParam_group_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_group_prime(self):

        localctx = MiniGoParser.Param_group_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param_group_prime)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.param_group()

                self.state = 321
                self.match(MiniGoParser.COMMA)
                self.state = 322
                self.param_group_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.param_group()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_mem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_mem_listContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def arr_dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dimContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_group" ):
                return visitor.visitParam_group(self)
            else:
                return visitor.visitChildren(self)




    def param_group(self):

        localctx = MiniGoParser.Param_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.param_mem_list()
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID]:
                self.state = 328
                self.typedecl()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.state = 330 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 329
                    self.arr_dim()
                    self.state = 332 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 334
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_mem_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_mem_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_mem_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_mem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_mem_list" ):
                return visitor.visitParam_mem_list(self)
            else:
                return visitor.visitChildren(self)




    def param_mem_list(self):

        localctx = MiniGoParser.Param_mem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param_mem_list)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MiniGoParser.ID)
                self.state = 339
                self.match(MiniGoParser.COMMA)
                self.state = 340
                self.param_mem_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.CONST)
            self.state = 345
            self.match(MiniGoParser.ID)
            self.state = 346
            self.match(MiniGoParser.ASSIGN)
            self.state = 347
            self.expr(0)
            self.state = 348
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def actualparam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ActualparamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ActualparamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.ID)
            self.state = 351
            self.match(MiniGoParser.LPAREN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 352
                self.actualparam()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 353
                    self.match(MiniGoParser.COMMA)
                    self.state = 354
                    self.actualparam()
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 362
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def SELECTOR(self):
            return self.getToken(MiniGoParser.SELECTOR, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def actualparam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ActualparamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ActualparamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.ID)
            self.state = 365
            self.match(MiniGoParser.SELECTOR)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.match(MiniGoParser.LPAREN)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 368
                self.actualparam()
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 369
                    self.match(MiniGoParser.COMMA)
                    self.state = 370
                    self.actualparam()
                    self.state = 375
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 378
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_actualparam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualparam" ):
                return visitor.visitActualparam(self)
            else:
                return visitor.visitChildren(self)




    def actualparam(self):

        localctx = MiniGoParser.ActualparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_actualparam)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.funccall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.methodcall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor1(self):
            return self.getTypedRuleContext(MiniGoParser.Factor1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.factor1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    self.match(MiniGoParser.OR)
                    self.state = 391
                    self.factor1(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor2(self):
            return self.getTypedRuleContext(MiniGoParser.Factor2Context,0)


        def factor1(self):
            return self.getTypedRuleContext(MiniGoParser.Factor1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_factor1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor1" ):
                return visitor.visitFactor1(self)
            else:
                return visitor.visitChildren(self)



    def factor1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Factor1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_factor1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.factor2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor1)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    self.match(MiniGoParser.AND)
                    self.state = 402
                    self.factor2(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor3(self):
            return self.getTypedRuleContext(MiniGoParser.Factor3Context,0)


        def factor2(self):
            return self.getTypedRuleContext(MiniGoParser.Factor2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MiniGoParser.LESS, 0)

        def GREATER(self):
            return self.getToken(MiniGoParser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_factor2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor2" ):
                return visitor.visitFactor2(self)
            else:
                return visitor.visitChildren(self)



    def factor2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Factor2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_factor2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.factor3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor2)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.factor3(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor4(self):
            return self.getTypedRuleContext(MiniGoParser.Factor4Context,0)


        def factor3(self):
            return self.getTypedRuleContext(MiniGoParser.Factor3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_factor3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor3" ):
                return visitor.visitFactor3(self)
            else:
                return visitor.visitChildren(self)



    def factor3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Factor3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_factor3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.factor4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor3)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.factor4(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor5(self):
            return self.getTypedRuleContext(MiniGoParser.Factor5Context,0)


        def factor4(self):
            return self.getTypedRuleContext(MiniGoParser.Factor4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_factor4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor4" ):
                return visitor.visitFactor4(self)
            else:
                return visitor.visitChildren(self)



    def factor4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Factor4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_factor4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.factor5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor4)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 435
                    self.factor5() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Factor5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor5(self):
            return self.getTypedRuleContext(MiniGoParser.Factor5Context,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def factor6(self):
            return self.getTypedRuleContext(MiniGoParser.Factor6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_factor5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor5" ):
                return visitor.visitFactor5(self)
            else:
                return visitor.visitChildren(self)




    def factor5(self):

        localctx = MiniGoParser.Factor5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_factor5)
        self._la = 0 # Token type
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.factor5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.factor6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_factor6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor6" ):
                return visitor.visitFactor6(self)
            else:
                return visitor.visitChildren(self)




    def factor6(self):

        localctx = MiniGoParser.Factor6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_factor6)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.value()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(MiniGoParser.LPAREN)
                self.state = 448
                self.expr(0)
                self.state = 449
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def arr_dim_acc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dim_accContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dim_accContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MiniGoParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(MiniGoParser.ID)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 457
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        self.state = 454
                        self.arr_dim_acc()
                        pass

                    elif la_ == 2:
                        self.state = 455
                        self.matchWildcard()
                        self.state = 456
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def list_value(self):
            return self.getTypedRuleContext(MiniGoParser.List_valueContext,0)


        def arr_dim(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Arr_dimContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Arr_dimContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arr_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 462
                self.arr_dim()
                self.state = 465 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACK):
                    break

            self.state = 467
            self.typedecl()
            self.state = 468
            self.list_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dim_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim_acc" ):
                return visitor.visitArr_dim_acc(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim_acc(self):

        localctx = MiniGoParser.Arr_dim_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arr_dim_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MiniGoParser.LBRACK)
            self.state = 471
            self.expr(0)
            self.state = 472
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.var()
            self.state = 475
            self.assign()
            self.state = 476
            self.expr(0)
            self.state = 477
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def structinst(self):
            return self.getTypedRuleContext(MiniGoParser.StructinstContext,0)


        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_value)
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(MiniGoParser.DEC_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(MiniGoParser.BIN_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(MiniGoParser.OCT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(MiniGoParser.HEX_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 486
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 487
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 488
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 489
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 490
                self.structinst()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 491
                self.var()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 492
                self.arr_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DEC_LIT(self):
            return self.getToken(MiniGoParser.DEC_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim" ):
                return visitor.visitArr_dim(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim(self):

        localctx = MiniGoParser.Arr_dimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arr_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(MiniGoParser.LBRACK)
            self.state = 498
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.DEC_LIT or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 499
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndstmt" ):
                return visitor.visitEndstmt(self)
            else:
                return visitor.visitChildren(self)




    def endstmt(self):

        localctx = MiniGoParser.EndstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_endstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACE)
            else:
                return self.getToken(MiniGoParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACE)
            else:
                return self.getToken(MiniGoParser.RBRACE, i)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def blockdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockdeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockdeclContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.IF)
            self.state = 504
            self.match(MiniGoParser.LPAREN)
            self.state = 505
            self.expr(0)
            self.state = 506
            self.match(MiniGoParser.RPAREN)
            self.state = 507
            self.match(MiniGoParser.LBRACE)
            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 510
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 508
                    self.stmt()
                    pass
                elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 509
                    self.blockdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 514
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 515
            self.match(MiniGoParser.RBRACE)
            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 516
                    self.match(MiniGoParser.ELSE)
                    self.state = 517
                    self.match(MiniGoParser.IF)
                    self.state = 518
                    self.match(MiniGoParser.LPAREN)
                    self.state = 519
                    self.expr(0)
                    self.state = 520
                    self.match(MiniGoParser.RPAREN)
                    self.state = 521
                    self.match(MiniGoParser.LBRACE)
                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                        self.state = 524
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                            self.state = 522
                            self.stmt()
                            pass
                        elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                            self.state = 523
                            self.blockdecl()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 528
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 529
                    self.match(MiniGoParser.RBRACE) 
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

            self.state = 546
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 536
                self.match(MiniGoParser.ELSE)
                self.state = 537
                self.match(MiniGoParser.LBRACE)
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 540
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 538
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 539
                        self.decl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 544
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 545
                self.match(MiniGoParser.RBRACE)


            self.state = 548
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def blockdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockdeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockdeclContext,i)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def updatestmt(self):
            return self.getTypedRuleContext(MiniGoParser.UpdatestmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def normal_vardecl_init(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardecl_initContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.match(MiniGoParser.FOR)
                self.state = 551
                self.expr(0)
                self.state = 552
                self.match(MiniGoParser.LBRACE)
                self.state = 557
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 555
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 553
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 554
                        self.blockdecl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 559
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 560
                self.match(MiniGoParser.RBRACE)
                self.state = 561
                self.endstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
                self.match(MiniGoParser.FOR)
                self.state = 566
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 564
                    self.assignstmt()
                    pass
                elif token in [MiniGoParser.VAR]:
                    self.state = 565
                    self.normal_vardecl_init()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 568
                self.expr(0)
                self.state = 569
                self.match(MiniGoParser.SEMICO)
                self.state = 570
                self.updatestmt()
                self.state = 571
                self.match(MiniGoParser.LBRACE)
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 574
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 572
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 573
                        self.blockdecl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 579
                self.match(MiniGoParser.RBRACE)
                self.state = 580
                self.endstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 582
                self.match(MiniGoParser.FOR)
                self.state = 583
                self.match(MiniGoParser.ID)
                self.state = 584
                self.match(MiniGoParser.COMMA)
                self.state = 585
                self.match(MiniGoParser.ID)
                self.state = 586
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 587
                self.match(MiniGoParser.RANGE)
                self.state = 590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 588
                    self.match(MiniGoParser.ID)
                    pass
                elif token in [MiniGoParser.LBRACK]:
                    self.state = 589
                    self.arr_lit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 592
                self.match(MiniGoParser.LBRACE)
                self.state = 597
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 595
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 593
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 594
                        self.blockdecl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 599
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 600
                self.match(MiniGoParser.RBRACE)
                self.state = 601
                self.endstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdatestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_updatestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdatestmt" ):
                return visitor.visitUpdatestmt(self)
            else:
                return visitor.visitChildren(self)




    def updatestmt(self):

        localctx = MiniGoParser.UpdatestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_updatestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.var()
            self.state = 605
            self.assign()
            self.state = 606
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.match(MiniGoParser.BREAK)
            self.state = 609
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(MiniGoParser.CONTINUE)
            self.state = 612
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 614
                self.funccall()
                pass

            elif la_ == 2:
                self.state = 615
                self.methodcall()
                pass


            self.state = 618
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def endstmt(self):
            return self.getTypedRuleContext(MiniGoParser.EndstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(MiniGoParser.RETURN)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 621
                self.expr(0)


            self.state = 624
            self.endstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.expr_sempred
        self._predicates[28] = self.factor1_sempred
        self._predicates[29] = self.factor2_sempred
        self._predicates[30] = self.factor3_sempred
        self._predicates[31] = self.factor4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def factor1_sempred(self, localctx:Factor1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def factor2_sempred(self, localctx:Factor2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def factor3_sempred(self, localctx:Factor3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def factor4_sempred(self, localctx:Factor4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




