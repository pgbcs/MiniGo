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
        buf.write("\u024d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\6\2[\n")
        buf.write("\2\r\2\16\2\\\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3g\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4q\n\4\3\5\3\5\3\5")
        buf.write("\5\5v\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u0081")
        buf.write("\n\7\3\7\3\7\3\7\3\b\3\b\3\b\6\b\u0089\n\b\r\b\16\b\u008a")
        buf.write("\3\b\3\b\3\b\6\b\u0090\n\b\r\b\16\b\u0091\3\b\3\b\3\b")
        buf.write("\5\b\u0097\n\b\3\b\3\b\6\b\u009b\n\b\r\b\16\b\u009c\3")
        buf.write("\b\3\b\3\b\5\b\u00a2\n\b\3\t\3\t\3\t\3\t\7\t\u00a8\n\t")
        buf.write("\f\t\16\t\u00ab\13\t\3\t\3\t\3\t\7\t\u00b0\n\t\f\t\16")
        buf.write("\t\u00b3\13\t\5\t\u00b5\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\7\n\u00be\n\n\f\n\16\n\u00c1\13\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\7\13\u00c8\n\13\f\13\16\13\u00cb\13\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00d8\n\r\f")
        buf.write("\r\16\r\u00db\13\r\3\r\5\r\u00de\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\7\17\u00e9\n\17\f\17\16\17")
        buf.write("\u00ec\13\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00f6\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u0100\n\21\3\21\3\21\3\21\7\21\u0105\n\21\f\21\16")
        buf.write("\21\u0108\13\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u0117\n\22\3\22\3\22\3")
        buf.write("\22\7\22\u011c\n\22\f\22\16\22\u011f\13\22\3\22\3\22\3")
        buf.write("\22\3\23\3\23\5\23\u0126\n\23\3\23\3\23\3\23\5\23\u012b")
        buf.write("\n\23\7\23\u012d\n\23\f\23\16\23\u0130\13\23\5\23\u0132")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u013f\n\25\f\25\16\25\u0142\13\25\5\25\u0144")
        buf.write("\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u014f\n\26\f\26\16\26\u0152\13\26\5\26\u0154\n\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u015c\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u0164\n\30\f\30\16\30\u0167\13")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u016f\n\31\f\31")
        buf.write("\16\31\u0172\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u017a\n\32\f\32\16\32\u017d\13\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\7\33\u0185\n\33\f\33\16\33\u0188\13\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\7\34\u0190\n\34\f\34\16\34\u0193")
        buf.write("\13\34\3\35\3\35\3\35\5\35\u0198\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u01a0\n\36\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u01a6\n\37\f\37\16\37\u01a9\13\37\3 \3 \3 \5 \u01ae\n")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\5#\u01c4\n#\3$\3$\3%\3%\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\7\'\u01d5\n\'\f\'\16\'\u01d8\13\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01e3\n\'\f\'")
        buf.write("\16\'\u01e6\13\'\3\'\3\'\7\'\u01ea\n\'\f\'\16\'\u01ed")
        buf.write("\13\'\3\'\3\'\3\'\3\'\7\'\u01f3\n\'\f\'\16\'\u01f6\13")
        buf.write("\'\3\'\5\'\u01f9\n\'\3\'\3\'\3(\3(\3(\3(\3(\7(\u0202\n")
        buf.write("(\f(\16(\u0205\13(\3(\3(\3(\3(\3(\3(\5(\u020d\n(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\7(\u0216\n(\f(\16(\u0219\13(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\6(\u0227\n(\r(\16(\u0228")
        buf.write("\3(\3(\5(\u022d\n(\3(\3(\3(\7(\u0232\n(\f(\16(\u0235\13")
        buf.write("(\3(\3(\5(\u0239\n(\3)\3)\3)\3*\3*\3*\3+\3+\5+\u0243\n")
        buf.write("+\3+\3+\3,\3,\5,\u0249\n,\3,\3,\3,\2\7.\60\62\64\66-\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTV\2\t\3\2\37$\3\2\32\33\3\2\34\36\4")
        buf.write("\2\33\33\'\'\3\2(.\4\2\16\21::\4\2\62\62::\2\u027b\2Z")
        buf.write("\3\2\2\2\4f\3\2\2\2\6p\3\2\2\2\bu\3\2\2\2\ny\3\2\2\2\f")
        buf.write("}\3\2\2\2\16\u0085\3\2\2\2\20\u00a3\3\2\2\2\22\u00b8\3")
        buf.write("\2\2\2\24\u00c5\3\2\2\2\26\u00cf\3\2\2\2\30\u00dd\3\2")
        buf.write("\2\2\32\u00df\3\2\2\2\34\u00e3\3\2\2\2\36\u00f0\3\2\2")
        buf.write("\2 \u00f9\3\2\2\2\"\u010c\3\2\2\2$\u0131\3\2\2\2&\u0133")
        buf.write("\3\2\2\2(\u0139\3\2\2\2*\u0147\3\2\2\2,\u015b\3\2\2\2")
        buf.write(".\u015d\3\2\2\2\60\u0168\3\2\2\2\62\u0173\3\2\2\2\64\u017e")
        buf.write("\3\2\2\2\66\u0189\3\2\2\28\u0197\3\2\2\2:\u019f\3\2\2")
        buf.write("\2<\u01a1\3\2\2\2>\u01aa\3\2\2\2@\u01b1\3\2\2\2B\u01b6")
        buf.write("\3\2\2\2D\u01c3\3\2\2\2F\u01c5\3\2\2\2H\u01c7\3\2\2\2")
        buf.write("J\u01cb\3\2\2\2L\u01cd\3\2\2\2N\u0238\3\2\2\2P\u023a\3")
        buf.write("\2\2\2R\u023d\3\2\2\2T\u0242\3\2\2\2V\u0246\3\2\2\2X[")
        buf.write("\5\4\3\2Y[\5\6\4\2ZX\3\2\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3")
        buf.write("\2\2\2\\]\3\2\2\2]^\3\2\2\2^_\7\2\2\3_\3\3\2\2\2`g\5 ")
        buf.write("\21\2ag\5\b\5\2bg\5&\24\2cg\5\22\n\2dg\5\34\17\2eg\5\"")
        buf.write("\22\2f`\3\2\2\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2")
        buf.write("\2fe\3\2\2\2g\5\3\2\2\2hq\5J&\2iq\5@!\2jq\5L\'\2kq\5N")
        buf.write("(\2lq\5P)\2mq\5R*\2nq\5T+\2oq\5V,\2ph\3\2\2\2pi\3\2\2")
        buf.write("\2pj\3\2\2\2pk\3\2\2\2pl\3\2\2\2pm\3\2\2\2pn\3\2\2\2p")
        buf.write("o\3\2\2\2q\7\3\2\2\2rv\5\f\7\2sv\5\n\6\2tv\5\16\b\2ur")
        buf.write("\3\2\2\2us\3\2\2\2ut\3\2\2\2vw\3\2\2\2wx\5J&\2x\t\3\2")
        buf.write("\2\2yz\7\23\2\2z{\7:\2\2{|\5F$\2|\13\3\2\2\2}~\7\23\2")
        buf.write("\2~\u0080\7:\2\2\177\u0081\5F$\2\u0080\177\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7(\2\2")
        buf.write("\u0083\u0084\5.\30\2\u0084\r\3\2\2\2\u0085\u0086\7\23")
        buf.write("\2\2\u0086\u00a1\7:\2\2\u0087\u0089\5H%\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u0096\5F$\2\u008d")
        buf.write("\u008f\7(\2\2\u008e\u0090\5H%\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\5F$\2\u0094\u0095\5\20")
        buf.write("\t\2\u0095\u0097\3\2\2\2\u0096\u008d\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u00a2\3\2\2\2\u0098\u009a\7(\2\2\u0099")
        buf.write("\u009b\5H%\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\5F$\2\u009f\u00a0\5\20\t\2\u00a0\u00a2\3")
        buf.write("\2\2\2\u00a1\u0088\3\2\2\2\u00a1\u0098\3\2\2\2\u00a2\17")
        buf.write("\3\2\2\2\u00a3\u00b4\7=\2\2\u00a4\u00a9\5\20\t\2\u00a5")
        buf.write("\u00a6\7\60\2\2\u00a6\u00a8\5\20\t\2\u00a7\u00a5\3\2\2")
        buf.write("\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00b5\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write("\u00b1\5.\30\2\u00ad\u00ae\7\60\2\2\u00ae\u00b0\5.\30")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00a4\3\2\2\2\u00b4\u00ac\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b7\7>\2\2\u00b7\21\3\2\2")
        buf.write("\2\u00b8\u00b9\7\13\2\2\u00b9\u00ba\7:\2\2\u00ba\u00bb")
        buf.write("\7\f\2\2\u00bb\u00bf\7=\2\2\u00bc\u00be\5\24\13\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c2\u00c3\7>\2\2\u00c3\u00c4\5J&\2\u00c4\23\3")
        buf.write("\2\2\2\u00c5\u00c9\7:\2\2\u00c6\u00c8\5H%\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cc\u00cd\5F$\2\u00cd\u00ce\5J&\2\u00ce\25\3\2\2\2")
        buf.write("\u00cf\u00d0\7:\2\2\u00d0\u00d1\7=\2\2\u00d1\u00d2\5\30")
        buf.write("\r\2\u00d2\u00d3\7>\2\2\u00d3\27\3\2\2\2\u00d4\u00d9\5")
        buf.write("\32\16\2\u00d5\u00d6\7\60\2\2\u00d6\u00d8\5\32\16\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00de\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00d4\3\2\2\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00de\31\3\2\2\2\u00df\u00e0\7:\2\2\u00e0\u00e1")
        buf.write("\7\5\2\2\u00e1\u00e2\5.\30\2\u00e2\33\3\2\2\2\u00e3\u00e4")
        buf.write("\7\13\2\2\u00e4\u00e5\7:\2\2\u00e5\u00e6\7\r\2\2\u00e6")
        buf.write("\u00ea\7=\2\2\u00e7\u00e9\5\36\20\2\u00e8\u00e7\3\2\2")
        buf.write("\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed")
        buf.write("\u00ee\7>\2\2\u00ee\u00ef\5J&\2\u00ef\35\3\2\2\2\u00f0")
        buf.write("\u00f1\7:\2\2\u00f1\u00f2\7;\2\2\u00f2\u00f3\5$\23\2\u00f3")
        buf.write("\u00f5\7<\2\2\u00f4\u00f6\5F$\2\u00f5\u00f4\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\5J&\2\u00f8")
        buf.write("\37\3\2\2\2\u00f9\u00fa\7\n\2\2\u00fa\u00fb\7:\2\2\u00fb")
        buf.write("\u00fc\7;\2\2\u00fc\u00fd\5$\23\2\u00fd\u00ff\7<\2\2\u00fe")
        buf.write("\u0100\5F$\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\u0106\7=\2\2\u0102\u0105\5\6\4\2")
        buf.write("\u0103\u0105\5\4\3\2\u0104\u0102\3\2\2\2\u0104\u0103\3")
        buf.write("\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010a\7>\2\2\u010a\u010b\5J&\2\u010b!\3\2\2\2\u010c\u010d")
        buf.write("\7\n\2\2\u010d\u010e\7;\2\2\u010e\u010f\7:\2\2\u010f\u0110")
        buf.write("\7:\2\2\u0110\u0111\7<\2\2\u0111\u0112\7:\2\2\u0112\u0113")
        buf.write("\7;\2\2\u0113\u0114\5$\23\2\u0114\u0116\7<\2\2\u0115\u0117")
        buf.write("\5F$\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u011d\7=\2\2\u0119\u011c\5\6\4\2\u011a")
        buf.write("\u011c\5\4\3\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u0120\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121")
        buf.write("\7>\2\2\u0121\u0122\5J&\2\u0122#\3\2\2\2\u0123\u0125\7")
        buf.write(":\2\2\u0124\u0126\5F$\2\u0125\u0124\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u012e\3\2\2\2\u0127\u0128\7\60\2\2\u0128")
        buf.write("\u012a\7:\2\2\u0129\u012b\5F$\2\u012a\u0129\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u0127\3\2\2\2")
        buf.write("\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0123")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132%\3\2\2\2\u0133\u0134")
        buf.write("\7\22\2\2\u0134\u0135\7:\2\2\u0135\u0136\7(\2\2\u0136")
        buf.write("\u0137\5.\30\2\u0137\u0138\5J&\2\u0138\'\3\2\2\2\u0139")
        buf.write("\u013a\7:\2\2\u013a\u0143\7;\2\2\u013b\u0140\5,\27\2\u013c")
        buf.write("\u013d\7\60\2\2\u013d\u013f\5,\27\2\u013e\u013c\3\2\2")
        buf.write("\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u013b\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0146\7<\2\2\u0146)\3\2\2\2\u0147\u0148\7:\2\2")
        buf.write("\u0148\u0149\7/\2\2\u0149\u014a\7:\2\2\u014a\u0153\7;")
        buf.write("\2\2\u014b\u0150\5,\27\2\u014c\u014d\7\60\2\2\u014d\u014f")
        buf.write("\5,\27\2\u014e\u014c\3\2\2\2\u014f\u0152\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0153\u014b\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156\7<\2\2\u0156+\3")
        buf.write("\2\2\2\u0157\u015c\5.\30\2\u0158\u015c\5(\25\2\u0159\u015c")
        buf.write("\5*\26\2\u015a\u015c\5<\37\2\u015b\u0157\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c-\3\2\2\2\u015d\u015e\b\30\1\2\u015e\u015f\5\60")
        buf.write("\31\2\u015f\u0165\3\2\2\2\u0160\u0161\f\4\2\2\u0161\u0162")
        buf.write("\7&\2\2\u0162\u0164\5\60\31\2\u0163\u0160\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166/\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\b\31\1")
        buf.write("\2\u0169\u016a\5\62\32\2\u016a\u0170\3\2\2\2\u016b\u016c")
        buf.write("\f\4\2\2\u016c\u016d\7%\2\2\u016d\u016f\5\62\32\2\u016e")
        buf.write("\u016b\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\61\3\2\2\2\u0172\u0170\3\2")
        buf.write("\2\2\u0173\u0174\b\32\1\2\u0174\u0175\5\64\33\2\u0175")
        buf.write("\u017b\3\2\2\2\u0176\u0177\f\4\2\2\u0177\u0178\t\2\2\2")
        buf.write("\u0178\u017a\5\64\33\2\u0179\u0176\3\2\2\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\63\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\b\33\1\2\u017f")
        buf.write("\u0180\5\66\34\2\u0180\u0186\3\2\2\2\u0181\u0182\f\4\2")
        buf.write("\2\u0182\u0183\t\3\2\2\u0183\u0185\5\66\34\2\u0184\u0181")
        buf.write("\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\65\3\2\2\2\u0188\u0186\3\2\2\2\u0189")
        buf.write("\u018a\b\34\1\2\u018a\u018b\58\35\2\u018b\u0191\3\2\2")
        buf.write("\2\u018c\u018d\f\4\2\2\u018d\u018e\t\4\2\2\u018e\u0190")
        buf.write("\58\35\2\u018f\u018c\3\2\2\2\u0190\u0193\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\67\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0194\u0195\t\5\2\2\u0195\u0198\58\35\2")
        buf.write("\u0196\u0198\5:\36\2\u0197\u0194\3\2\2\2\u0197\u0196\3")
        buf.write("\2\2\2\u01989\3\2\2\2\u0199\u01a0\5D#\2\u019a\u01a0\5")
        buf.write("<\37\2\u019b\u019c\7;\2\2\u019c\u019d\5.\30\2\u019d\u019e")
        buf.write("\7<\2\2\u019e\u01a0\3\2\2\2\u019f\u0199\3\2\2\2\u019f")
        buf.write("\u019a\3\2\2\2\u019f\u019b\3\2\2\2\u01a0;\3\2\2\2\u01a1")
        buf.write("\u01a7\7:\2\2\u01a2\u01a6\5> \2\u01a3\u01a4\13\2\2\2\u01a4")
        buf.write("\u01a6\7:\2\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3\2\2\2")
        buf.write("\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8=\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ad")
        buf.write("\7?\2\2\u01ab\u01ae\5.\30\2\u01ac\u01ae\7:\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\7@\2\2\u01b0?\3\2\2\2\u01b1\u01b2\5<\37\2\u01b2")
        buf.write("\u01b3\5B\"\2\u01b3\u01b4\5.\30\2\u01b4\u01b5\5J&\2\u01b5")
        buf.write("A\3\2\2\2\u01b6\u01b7\t\6\2\2\u01b7C\3\2\2\2\u01b8\u01c4")
        buf.write("\7\62\2\2\u01b9\u01c4\7\63\2\2\u01ba\u01c4\7\64\2\2\u01bb")
        buf.write("\u01c4\7\65\2\2\u01bc\u01c4\7\66\2\2\u01bd\u01c4\7\67")
        buf.write("\2\2\u01be\u01c4\7\30\2\2\u01bf\u01c4\7\31\2\2\u01c0\u01c4")
        buf.write("\7\27\2\2\u01c1\u01c4\5\26\f\2\u01c2\u01c4\5<\37\2\u01c3")
        buf.write("\u01b8\3\2\2\2\u01c3\u01b9\3\2\2\2\u01c3\u01ba\3\2\2\2")
        buf.write("\u01c3\u01bb\3\2\2\2\u01c3\u01bc\3\2\2\2\u01c3\u01bd\3")
        buf.write("\2\2\2\u01c3\u01be\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c3\u01c0")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("E\3\2\2\2\u01c5\u01c6\t\7\2\2\u01c6G\3\2\2\2\u01c7\u01c8")
        buf.write("\7?\2\2\u01c8\u01c9\t\b\2\2\u01c9\u01ca\7@\2\2\u01caI")
        buf.write("\3\2\2\2\u01cb\u01cc\7\61\2\2\u01ccK\3\2\2\2\u01cd\u01ce")
        buf.write("\7\6\2\2\u01ce\u01cf\7;\2\2\u01cf\u01d0\5.\30\2\u01d0")
        buf.write("\u01d1\7<\2\2\u01d1\u01d6\7=\2\2\u01d2\u01d5\5\6\4\2\u01d3")
        buf.write("\u01d5\5\4\3\2\u01d4\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3")
        buf.write("\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01eb")
        buf.write("\7>\2\2\u01da\u01db\7\7\2\2\u01db\u01dc\7\6\2\2\u01dc")
        buf.write("\u01dd\7;\2\2\u01dd\u01de\5.\30\2\u01de\u01df\7<\2\2\u01df")
        buf.write("\u01e4\7=\2\2\u01e0\u01e3\5\6\4\2\u01e1\u01e3\5\4\3\2")
        buf.write("\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3")
        buf.write("\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7>\2\2\u01e8")
        buf.write("\u01ea\3\2\2\2\u01e9\u01da\3\2\2\2\u01ea\u01ed\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01f8\3")
        buf.write("\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef\7\7\2\2\u01ef\u01f4")
        buf.write("\7=\2\2\u01f0\u01f3\5\6\4\2\u01f1\u01f3\5\4\3\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2")
        buf.write("\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3")
        buf.write("\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f9\7>\2\2\u01f8\u01ee")
        buf.write("\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fb\5J&\2\u01fbM\3\2\2\2\u01fc\u01fd\7\b\2\2\u01fd")
        buf.write("\u01fe\5.\30\2\u01fe\u0203\7=\2\2\u01ff\u0202\5\6\4\2")
        buf.write("\u0200\u0202\5\4\3\2\u0201\u01ff\3\2\2\2\u0201\u0200\3")
        buf.write("\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3\2\2\2\u0206")
        buf.write("\u0207\7>\2\2\u0207\u0208\5J&\2\u0208\u0239\3\2\2\2\u0209")
        buf.write("\u020c\7\b\2\2\u020a\u020d\5@!\2\u020b\u020d\5\f\7\2\u020c")
        buf.write("\u020a\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u020f\7\61\2\2\u020f\u0210\5.\30\2\u0210\u0211")
        buf.write("\7\61\2\2\u0211\u0212\5@!\2\u0212\u0217\7=\2\2\u0213\u0216")
        buf.write("\5\6\4\2\u0214\u0216\5\4\3\2\u0215\u0213\3\2\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0217\3")
        buf.write("\2\2\2\u021a\u021b\7>\2\2\u021b\u021c\5J&\2\u021c\u0239")
        buf.write("\3\2\2\2\u021d\u021e\7\b\2\2\u021e\u021f\7:\2\2\u021f")
        buf.write("\u0220\7\60\2\2\u0220\u0221\7:\2\2\u0221\u0222\7)\2\2")
        buf.write("\u0222\u022c\7\26\2\2\u0223\u022d\7:\2\2\u0224\u0226\5")
        buf.write("F$\2\u0225\u0227\5H%\2\u0226\u0225\3\2\2\2\u0227\u0228")
        buf.write("\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u022b\5\20\t\2\u022b\u022d\3\2\2")
        buf.write("\2\u022c\u0223\3\2\2\2\u022c\u0224\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u0233\7=\2\2\u022f\u0232\5\6\4\2\u0230")
        buf.write("\u0232\5\4\3\2\u0231\u022f\3\2\2\2\u0231\u0230\3\2\2\2")
        buf.write("\u0232\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3")
        buf.write("\2\2\2\u0234\u0236\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237")
        buf.write("\7>\2\2\u0237\u0239\5J&\2\u0238\u01fc\3\2\2\2\u0238\u0209")
        buf.write("\3\2\2\2\u0238\u021d\3\2\2\2\u0239O\3\2\2\2\u023a\u023b")
        buf.write("\7\25\2\2\u023b\u023c\5J&\2\u023cQ\3\2\2\2\u023d\u023e")
        buf.write("\7\24\2\2\u023e\u023f\5J&\2\u023fS\3\2\2\2\u0240\u0243")
        buf.write("\5(\25\2\u0241\u0243\5*\26\2\u0242\u0240\3\2\2\2\u0242")
        buf.write("\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245\5J&\2\u0245")
        buf.write("U\3\2\2\2\u0246\u0248\7\t\2\2\u0247\u0249\5.\30\2\u0248")
        buf.write("\u0247\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024a\u024b\5J&\2\u024bW\3\2\2\2DZ\\fpu\u0080\u008a\u0091")
        buf.write("\u0096\u009c\u00a1\u00a9\u00b1\u00b4\u00bf\u00c9\u00d9")
        buf.write("\u00dd\u00ea\u00f5\u00ff\u0104\u0106\u0116\u011b\u011d")
        buf.write("\u0125\u012a\u012e\u0131\u0140\u0143\u0150\u0153\u015b")
        buf.write("\u0165\u0170\u017b\u0186\u0191\u0197\u019f\u01a5\u01a7")
        buf.write("\u01ad\u01c3\u01d4\u01d6\u01e2\u01e4\u01eb\u01f2\u01f4")
        buf.write("\u01f8\u0201\u0203\u020c\u0215\u0217\u0228\u022c\u0231")
        buf.write("\u0233\u0238\u0242\u0248")
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
    RULE_vardecl = 3
    RULE_normal_vardecl_non_init = 4
    RULE_normal_vardecl_init = 5
    RULE_arr_vardecl = 6
    RULE_list_value = 7
    RULE_structdecl = 8
    RULE_fielddecl = 9
    RULE_structinst = 10
    RULE_fieldinstlist = 11
    RULE_fieldinst = 12
    RULE_interfacedecl = 13
    RULE_methoddecl = 14
    RULE_funcdecl = 15
    RULE_methodimple = 16
    RULE_param_list = 17
    RULE_constdecl = 18
    RULE_funccall = 19
    RULE_methodcall = 20
    RULE_actualparam = 21
    RULE_expr = 22
    RULE_factor1 = 23
    RULE_factor2 = 24
    RULE_factor3 = 25
    RULE_factor4 = 26
    RULE_factor5 = 27
    RULE_factor6 = 28
    RULE_var = 29
    RULE_arr_dim_acc = 30
    RULE_assignstmt = 31
    RULE_assign = 32
    RULE_value = 33
    RULE_typedecl = 34
    RULE_arr_dim = 35
    RULE_endstmt = 36
    RULE_ifstmt = 37
    RULE_forstmt = 38
    RULE_breakstmt = 39
    RULE_continuestmt = 40
    RULE_callstmt = 41
    RULE_returnstmt = 42

    ruleNames =  [ "program", "decl", "stmt", "vardecl", "normal_vardecl_non_init", 
                   "normal_vardecl_init", "arr_vardecl", "list_value", "structdecl", 
                   "fielddecl", "structinst", "fieldinstlist", "fieldinst", 
                   "interfacedecl", "methoddecl", "funcdecl", "methodimple", 
                   "param_list", "constdecl", "funccall", "methodcall", 
                   "actualparam", "expr", "factor1", "factor2", "factor3", 
                   "factor4", "factor5", "factor6", "var", "arr_dim_acc", 
                   "assignstmt", "assign", "value", "typedecl", "arr_dim", 
                   "endstmt", "ifstmt", "forstmt", "breakstmt", "continuestmt", 
                   "callstmt", "returnstmt" ]

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
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 86
                    self.decl()
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 87
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 92
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


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def methodimple(self):
            return self.getTypedRuleContext(MiniGoParser.MethodimpleContext,0)


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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.constdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.interfacedecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.methodimple()
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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.endstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.callstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.returnstmt()
                pass


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
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 112
                self.normal_vardecl_init()
                pass

            elif la_ == 2:
                self.state = 113
                self.normal_vardecl_non_init()
                pass

            elif la_ == 3:
                self.state = 114
                self.arr_vardecl()
                pass


            self.state = 117
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
        self.enterRule(localctx, 8, self.RULE_normal_vardecl_non_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniGoParser.VAR)
            self.state = 120
            self.match(MiniGoParser.ID)
            self.state = 121
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
        self.enterRule(localctx, 10, self.RULE_normal_vardecl_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniGoParser.VAR)
            self.state = 124
            self.match(MiniGoParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 125
                self.typedecl()


            self.state = 128
            self.match(MiniGoParser.ASSIGN)
            self.state = 129
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
        self.enterRule(localctx, 12, self.RULE_arr_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MiniGoParser.VAR)
            self.state = 132
            self.match(MiniGoParser.ID)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACK]:
                self.state = 134 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 133
                    self.arr_dim()
                    self.state = 136 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 138
                self.typedecl()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN:
                    self.state = 139
                    self.match(MiniGoParser.ASSIGN)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 140
                        self.arr_dim()
                        self.state = 143 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==MiniGoParser.LBRACK):
                            break

                    self.state = 145
                    self.typedecl()
                    self.state = 146
                    self.list_value()


                pass
            elif token in [MiniGoParser.ASSIGN]:
                self.state = 150
                self.match(MiniGoParser.ASSIGN)
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 151
                    self.arr_dim()
                    self.state = 154 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACK):
                        break

                self.state = 156
                self.typedecl()
                self.state = 157
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
        self.enterRule(localctx, 14, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniGoParser.LBRACE)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.state = 162
                self.list_value()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 163
                    self.match(MiniGoParser.COMMA)
                    self.state = 164
                    self.list_value()
                    self.state = 169
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN]:
                self.state = 170
                self.expr(0)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 171
                    self.match(MiniGoParser.COMMA)
                    self.state = 172
                    self.expr(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 180
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
        self.enterRule(localctx, 16, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiniGoParser.TYPE)
            self.state = 183
            self.match(MiniGoParser.ID)
            self.state = 184
            self.match(MiniGoParser.STRUCT)
            self.state = 185
            self.match(MiniGoParser.LBRACE)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 186
                self.fielddecl()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(MiniGoParser.RBRACE)
            self.state = 193
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
        self.enterRule(localctx, 18, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.ID)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACK:
                self.state = 196
                self.arr_dim()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.typedecl()
            self.state = 203
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
        self.enterRule(localctx, 20, self.RULE_structinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.ID)
            self.state = 206
            self.match(MiniGoParser.LBRACE)
            self.state = 207
            self.fieldinstlist()
            self.state = 208
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
        self.enterRule(localctx, 22, self.RULE_fieldinstlist)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.fieldinst()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 211
                    self.match(MiniGoParser.COMMA)
                    self.state = 212
                    self.fieldinst()
                    self.state = 217
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
        self.enterRule(localctx, 24, self.RULE_fieldinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 222
            self.match(MiniGoParser.COLON)
            self.state = 223
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
        self.enterRule(localctx, 26, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.TYPE)
            self.state = 226
            self.match(MiniGoParser.ID)
            self.state = 227
            self.match(MiniGoParser.INTERFACE)
            self.state = 228
            self.match(MiniGoParser.LBRACE)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 229
                self.methoddecl()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(MiniGoParser.RBRACE)
            self.state = 236
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
        self.enterRule(localctx, 28, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.ID)
            self.state = 239
            self.match(MiniGoParser.LPAREN)
            self.state = 240
            self.param_list()
            self.state = 241
            self.match(MiniGoParser.RPAREN)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 242
                self.typedecl()


            self.state = 245
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


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MiniGoParser.FUNC)
            self.state = 248
            self.match(MiniGoParser.ID)
            self.state = 249
            self.match(MiniGoParser.LPAREN)
            self.state = 250
            self.param_list()
            self.state = 251
            self.match(MiniGoParser.RPAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 252
                self.typedecl()


            self.state = 255
            self.match(MiniGoParser.LBRACE)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 258
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 256
                    self.stmt()
                    pass
                elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 257
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(MiniGoParser.RBRACE)
            self.state = 264
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


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodimple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodimple" ):
                return visitor.visitMethodimple(self)
            else:
                return visitor.visitChildren(self)




    def methodimple(self):

        localctx = MiniGoParser.MethodimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_methodimple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.FUNC)
            self.state = 267
            self.match(MiniGoParser.LPAREN)
            self.state = 268
            self.match(MiniGoParser.ID)
            self.state = 269
            self.match(MiniGoParser.ID)
            self.state = 270
            self.match(MiniGoParser.RPAREN)
            self.state = 271
            self.match(MiniGoParser.ID)
            self.state = 272
            self.match(MiniGoParser.LPAREN)
            self.state = 273
            self.param_list()
            self.state = 274
            self.match(MiniGoParser.RPAREN)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 275
                self.typedecl()


            self.state = 278
            self.match(MiniGoParser.LBRACE)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 281
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 279
                    self.stmt()
                    pass
                elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 280
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 286
            self.match(MiniGoParser.RBRACE)
            self.state = 287
            self.endstmt()
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypedeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypedeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = MiniGoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 289
                self.match(MiniGoParser.ID)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 290
                    self.typedecl()


                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 293
                    self.match(MiniGoParser.COMMA)
                    self.state = 294
                    self.match(MiniGoParser.ID)
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                        self.state = 295
                        self.typedecl()


                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
        self.enterRule(localctx, 36, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.CONST)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 307
            self.match(MiniGoParser.ASSIGN)
            self.state = 308
            self.expr(0)
            self.state = 309
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
        self.enterRule(localctx, 38, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MiniGoParser.ID)
            self.state = 312
            self.match(MiniGoParser.LPAREN)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN))) != 0):
                self.state = 313
                self.actualparam()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 314
                    self.match(MiniGoParser.COMMA)
                    self.state = 315
                    self.actualparam()
                    self.state = 320
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 323
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
        self.enterRule(localctx, 40, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.ID)
            self.state = 326
            self.match(MiniGoParser.SELECTOR)
            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.match(MiniGoParser.LPAREN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN))) != 0):
                self.state = 329
                self.actualparam()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 330
                    self.match(MiniGoParser.COMMA)
                    self.state = 331
                    self.actualparam()
                    self.state = 336
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 339
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
        self.enterRule(localctx, 42, self.RULE_actualparam)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.funccall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.methodcall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.factor1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    self.match(MiniGoParser.OR)
                    self.state = 352
                    self.factor1(0) 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_factor1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.factor2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor1)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.match(MiniGoParser.AND)
                    self.state = 363
                    self.factor2(0) 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_factor2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.factor3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor2)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 374
                    self.factor3(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_factor3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.factor4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor3)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.factor4(0) 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_factor4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.factor5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Factor4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor4)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 396
                    self.factor5() 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_factor5)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 403
                self.factor5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
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


        def var(self):
            return self.getTypedRuleContext(MiniGoParser.VarContext,0)


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
        self.enterRule(localctx, 56, self.RULE_factor6)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(MiniGoParser.LPAREN)
                self.state = 410
                self.expr(0)
                self.state = 411
                self.match(MiniGoParser.RPAREN)
                pass


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
        self.enterRule(localctx, 58, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.ID)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        self.state = 416
                        self.arr_dim_acc()
                        pass

                    elif la_ == 2:
                        self.state = 417
                        self.matchWildcard()
                        self.state = 418
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_dim_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dim_acc" ):
                return visitor.visitArr_dim_acc(self)
            else:
                return visitor.visitChildren(self)




    def arr_dim_acc(self):

        localctx = MiniGoParser.Arr_dim_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arr_dim_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.LBRACK)
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 425
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 426
                self.match(MiniGoParser.ID)
                pass


            self.state = 429
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
        self.enterRule(localctx, 62, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.var()
            self.state = 432
            self.assign()
            self.state = 433
            self.expr(0)
            self.state = 434
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
        self.enterRule(localctx, 64, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.SHORT_ASSIGN) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_value)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(MiniGoParser.DEC_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(MiniGoParser.BIN_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.match(MiniGoParser.OCT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.match(MiniGoParser.HEX_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 442
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 444
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 445
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 446
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 447
                self.structinst()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 448
                self.var()
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
        self.enterRule(localctx, 68, self.RULE_typedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
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
        self.enterRule(localctx, 70, self.RULE_arr_dim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(MiniGoParser.LBRACK)
            self.state = 454
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.DEC_LIT or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 455
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
        self.enterRule(localctx, 72, self.RULE_endstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
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


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.IF)
            self.state = 460
            self.match(MiniGoParser.LPAREN)
            self.state = 461
            self.expr(0)
            self.state = 462
            self.match(MiniGoParser.RPAREN)
            self.state = 463
            self.match(MiniGoParser.LBRACE)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                self.state = 466
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                    self.state = 464
                    self.stmt()
                    pass
                elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 465
                    self.decl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 471
            self.match(MiniGoParser.RBRACE)
            self.state = 489
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 472
                    self.match(MiniGoParser.ELSE)
                    self.state = 473
                    self.match(MiniGoParser.IF)
                    self.state = 474
                    self.match(MiniGoParser.LPAREN)
                    self.state = 475
                    self.expr(0)
                    self.state = 476
                    self.match(MiniGoParser.RPAREN)
                    self.state = 477
                    self.match(MiniGoParser.LBRACE)
                    self.state = 482
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                        self.state = 480
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                            self.state = 478
                            self.stmt()
                            pass
                        elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                            self.state = 479
                            self.decl()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 484
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 485
                    self.match(MiniGoParser.RBRACE) 
                self.state = 491
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 492
                self.match(MiniGoParser.ELSE)
                self.state = 493
                self.match(MiniGoParser.LBRACE)
                self.state = 498
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 496
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 494
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 495
                        self.decl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 500
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 501
                self.match(MiniGoParser.RBRACE)


            self.state = 504
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


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def SEMICO(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICO)
            else:
                return self.getToken(MiniGoParser.SEMICO, i)

        def assignstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignstmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,i)


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
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.match(MiniGoParser.FOR)
                self.state = 507
                self.expr(0)
                self.state = 508
                self.match(MiniGoParser.LBRACE)
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 511
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 509
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 510
                        self.decl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 515
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 516
                self.match(MiniGoParser.RBRACE)
                self.state = 517
                self.endstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.match(MiniGoParser.FOR)
                self.state = 522
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 520
                    self.assignstmt()
                    pass
                elif token in [MiniGoParser.VAR]:
                    self.state = 521
                    self.normal_vardecl_init()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 524
                self.match(MiniGoParser.SEMICO)
                self.state = 525
                self.expr(0)
                self.state = 526
                self.match(MiniGoParser.SEMICO)
                self.state = 527
                self.assignstmt()
                self.state = 528
                self.match(MiniGoParser.LBRACE)
                self.state = 533
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 531
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 529
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 530
                        self.decl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 535
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 536
                self.match(MiniGoParser.RBRACE)
                self.state = 537
                self.endstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.match(MiniGoParser.FOR)
                self.state = 540
                self.match(MiniGoParser.ID)
                self.state = 541
                self.match(MiniGoParser.COMMA)
                self.state = 542
                self.match(MiniGoParser.ID)
                self.state = 543
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 544
                self.match(MiniGoParser.RANGE)
                self.state = 554
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                if la_ == 1:
                    self.state = 545
                    self.match(MiniGoParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 546
                    self.typedecl()
                    self.state = 548 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 547
                        self.arr_dim()
                        self.state = 550 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==MiniGoParser.LBRACK):
                            break

                    self.state = 552
                    self.list_value()
                    pass


                self.state = 556
                self.match(MiniGoParser.LBRACE)
                self.state = 561
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.SEMICO) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 559
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.SEMICO, MiniGoParser.ID]:
                        self.state = 557
                        self.stmt()
                        pass
                    elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                        self.state = 558
                        self.decl()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 563
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 564
                self.match(MiniGoParser.RBRACE)
                self.state = 565
                self.endstmt()
                pass


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
        self.enterRule(localctx, 78, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(MiniGoParser.BREAK)
            self.state = 569
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
        self.enterRule(localctx, 80, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(MiniGoParser.CONTINUE)
            self.state = 572
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
        self.enterRule(localctx, 82, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 574
                self.funccall()
                pass

            elif la_ == 2:
                self.state = 575
                self.methodcall()
                pass


            self.state = 578
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
        self.enterRule(localctx, 84, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(MiniGoParser.RETURN)
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN))) != 0):
                self.state = 581
                self.expr(0)


            self.state = 584
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
        self._predicates[22] = self.expr_sempred
        self._predicates[23] = self.factor1_sempred
        self._predicates[24] = self.factor2_sempred
        self._predicates[25] = self.factor3_sempred
        self._predicates[26] = self.factor4_sempred
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
         




