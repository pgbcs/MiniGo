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
        buf.write("\u02e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u00b6\n\4\3\5\3\5\5\5\u00ba\n\5\3\6\3\6\5\6\u00be\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b\u00c8\n\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u00d2\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00d9\n\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00e9\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00fc\n\21\3\22\3\22\5")
        buf.write("\22\u0100\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u010d\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u0123\n\27\3\30\3\30\5")
        buf.write("\30\u0127\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\5\33\u0135\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u013c\n\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \5")
        buf.write(" \u0150\n \3!\3!\3!\3!\3!\5!\u0157\n!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\5\"\u0161\n\"\3\"\3\"\3\"\3#\3#\5#\u0168")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u016f\n$\3%\3%\5%\u0173\n%\3%\3")
        buf.write("%\3&\3&\3&\3&\5&\u017b\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(")
        buf.write("\5(\u0185\n(\3)\5)\u0188\n)\3)\3)\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\5*\u0196\n*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\7,\u01a5\n,\f,\16,\u01a8\13,\3-\3-\3-\3-\3-\3")
        buf.write("-\7-\u01b0\n-\f-\16-\u01b3\13-\3.\3.\3.\3.\3.\3.\7.\u01bb")
        buf.write("\n.\f.\16.\u01be\13.\3/\3/\3/\3/\3/\3/\7/\u01c6\n/\f/")
        buf.write("\16/\u01c9\13/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01d1")
        buf.write("\n\60\f\60\16\60\u01d4\13\60\3\61\3\61\3\61\5\61\u01d9")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\5\62\u01e0\n\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62")
        buf.write("\u01f8\n\62\f\62\16\62\u01fb\13\62\3\63\3\63\5\63\u01ff")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\7\64\u0206\n\64\f\64\16")
        buf.write("\64\u0209\13\64\3\65\3\65\3\65\3\65\3\66\3\66\5\66\u0211")
        buf.write("\n\66\3\67\3\67\3\67\3\67\38\38\58\u0219\n8\39\39\39\3")
        buf.write("9\39\3:\3:\5:\u0222\n:\3;\3;\3;\3;\3;\5;\u0229\n;\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0236\n=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\7")
        buf.write("=\u024e\n=\f=\16=\u0251\13=\3>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\5?\u0262\n?\3@\3@\3@\5@\u0267\n@\3")
        buf.write("@\3@\3@\3A\3A\3A\3A\5A\u0270\nA\3A\3A\3A\3A\3A\3A\3A\7")
        buf.write("A\u0279\nA\fA\16A\u027c\13A\3B\3B\3C\3C\5C\u0282\nC\3")
        buf.write("C\3C\3D\3D\5D\u0288\nD\3D\3D\3E\3E\5E\u028e\nE\3E\3E\3")
        buf.write("F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3H\3H\3H\3H\3H\5H\u02a1\n")
        buf.write("H\3I\3I\3I\3I\3I\3I\3I\3J\3J\3J\3K\3K\3K\5K\u02b0\nK\3")
        buf.write("L\3L\3L\3L\3L\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3N\3N\3N\3")
        buf.write("O\3O\3O\3O\5O\u02c8\nO\3O\3O\5O\u02cc\nO\3P\3P\3P\5P\u02d1")
        buf.write("\nP\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3S\3")
        buf.write("S\3S\3S\2\13VXZ\\^bfx\u0080T\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\u009e\u00a0\u00a2\u00a4\2\t\4\2\16\21::\4\2\62\65::\3")
        buf.write("\2\37$\3\2\32\33\3\2\34\36\4\2\33\33\'\'\3\2*.\2\u02e6")
        buf.write("\2\u00a6\3\2\2\2\4\u00ad\3\2\2\2\6\u00b5\3\2\2\2\b\u00b9")
        buf.write("\3\2\2\2\n\u00bd\3\2\2\2\f\u00bf\3\2\2\2\16\u00c4\3\2")
        buf.write("\2\2\20\u00cd\3\2\2\2\22\u00d1\3\2\2\2\24\u00d3\3\2\2")
        buf.write("\2\26\u00de\3\2\2\2\30\u00e8\3\2\2\2\32\u00ea\3\2\2\2")
        buf.write("\34\u00ee\3\2\2\2\36\u00f2\3\2\2\2 \u00fb\3\2\2\2\"\u00ff")
        buf.write("\3\2\2\2$\u010c\3\2\2\2&\u010e\3\2\2\2(\u0114\3\2\2\2")
        buf.write("*\u011a\3\2\2\2,\u0122\3\2\2\2.\u0124\3\2\2\2\60\u012b")
        buf.write("\3\2\2\2\62\u012e\3\2\2\2\64\u0134\3\2\2\2\66\u013b\3")
        buf.write("\2\2\28\u013d\3\2\2\2:\u0141\3\2\2\2<\u0147\3\2\2\2>\u014f")
        buf.write("\3\2\2\2@\u0151\3\2\2\2B\u015a\3\2\2\2D\u0167\3\2\2\2")
        buf.write("F\u016e\3\2\2\2H\u0170\3\2\2\2J\u017a\3\2\2\2L\u017c\3")
        buf.write("\2\2\2N\u0184\3\2\2\2P\u0187\3\2\2\2R\u018b\3\2\2\2T\u019a")
        buf.write("\3\2\2\2V\u019e\3\2\2\2X\u01a9\3\2\2\2Z\u01b4\3\2\2\2")
        buf.write("\\\u01bf\3\2\2\2^\u01ca\3\2\2\2`\u01d8\3\2\2\2b\u01df")
        buf.write("\3\2\2\2d\u01fe\3\2\2\2f\u0200\3\2\2\2h\u020a\3\2\2\2")
        buf.write("j\u0210\3\2\2\2l\u0212\3\2\2\2n\u0218\3\2\2\2p\u021a\3")
        buf.write("\2\2\2r\u0221\3\2\2\2t\u0228\3\2\2\2v\u022a\3\2\2\2x\u0235")
        buf.write("\3\2\2\2z\u0252\3\2\2\2|\u0261\3\2\2\2~\u0263\3\2\2\2")
        buf.write("\u0080\u026f\3\2\2\2\u0082\u027d\3\2\2\2\u0084\u027f\3")
        buf.write("\2\2\2\u0086\u0287\3\2\2\2\u0088\u028b\3\2\2\2\u008a\u0291")
        buf.write("\3\2\2\2\u008c\u0297\3\2\2\2\u008e\u02a0\3\2\2\2\u0090")
        buf.write("\u02a2\3\2\2\2\u0092\u02a9\3\2\2\2\u0094\u02af\3\2\2\2")
        buf.write("\u0096\u02b1\3\2\2\2\u0098\u02b6\3\2\2\2\u009a\u02ba\3")
        buf.write("\2\2\2\u009c\u02cb\3\2\2\2\u009e\u02cd\3\2\2\2\u00a0\u02d4")
        buf.write("\3\2\2\2\u00a2\u02de\3\2\2\2\u00a4\u02e1\3\2\2\2\u00a6")
        buf.write("\u00a7\5\4\3\2\u00a7\u00a8\7\2\2\3\u00a8\3\3\2\2\2\u00a9")
        buf.write("\u00aa\5\6\4\2\u00aa\u00ab\5\4\3\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00ae\5\6\4\2\u00ad\u00a9\3\2\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ae\5\3\2\2\2\u00af\u00b6\5\b\5\2\u00b0\u00b6")
        buf.write("\5&\24\2\u00b1\u00b6\5(\25\2\u00b2\u00b6\5:\36\2\u00b3")
        buf.write("\u00b6\5B\"\2\u00b4\u00b6\5R*\2\u00b5\u00af\3\2\2\2\u00b5")
        buf.write("\u00b0\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\7\3\2\2")
        buf.write("\2\u00b7\u00ba\5\n\6\2\u00b8\u00ba\5\22\n\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\t\3\2\2\2\u00bb\u00be")
        buf.write("\5\f\7\2\u00bc\u00be\5\16\b\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\13\3\2\2\2\u00bf\u00c0\7\23\2\2\u00c0")
        buf.write("\u00c1\7:\2\2\u00c1\u00c2\5\20\t\2\u00c2\u00c3\7\61\2")
        buf.write("\2\u00c3\r\3\2\2\2\u00c4\u00c5\7\23\2\2\u00c5\u00c7\7")
        buf.write(":\2\2\u00c6\u00c8\5\20\t\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\7(\2\2\u00ca")
        buf.write("\u00cb\5V,\2\u00cb\u00cc\7\61\2\2\u00cc\17\3\2\2\2\u00cd")
        buf.write("\u00ce\t\2\2\2\u00ce\21\3\2\2\2\u00cf\u00d2\5\26\f\2\u00d0")
        buf.write("\u00d2\5\24\13\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d2\23\3\2\2\2\u00d3\u00d4\7\23\2\2\u00d4\u00d8\7")
        buf.write(":\2\2\u00d5\u00d6\5\30\r\2\u00d6\u00d7\5\20\t\2\u00d7")
        buf.write("\u00d9\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00db\7(\2\2\u00db\u00dc\5")
        buf.write("V,\2\u00dc\u00dd\7\61\2\2\u00dd\25\3\2\2\2\u00de\u00df")
        buf.write("\7\23\2\2\u00df\u00e0\7:\2\2\u00e0\u00e1\5\30\r\2\u00e1")
        buf.write("\u00e2\5\20\t\2\u00e2\u00e3\7\61\2\2\u00e3\27\3\2\2\2")
        buf.write("\u00e4\u00e5\5\32\16\2\u00e5\u00e6\5\30\r\2\u00e6\u00e9")
        buf.write("\3\2\2\2\u00e7\u00e9\5\32\16\2\u00e8\u00e4\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\31\3\2\2\2\u00ea\u00eb\7?\2\2\u00eb")
        buf.write("\u00ec\t\3\2\2\u00ec\u00ed\7@\2\2\u00ed\33\3\2\2\2\u00ee")
        buf.write("\u00ef\5\30\r\2\u00ef\u00f0\5\20\t\2\u00f0\u00f1\5\36")
        buf.write("\20\2\u00f1\35\3\2\2\2\u00f2\u00f3\7=\2\2\u00f3\u00f4")
        buf.write("\5 \21\2\u00f4\u00f5\7>\2\2\u00f5\37\3\2\2\2\u00f6\u00f7")
        buf.write("\5\"\22\2\u00f7\u00f8\7\60\2\2\u00f8\u00f9\5 \21\2\u00f9")
        buf.write("\u00fc\3\2\2\2\u00fa\u00fc\5\"\22\2\u00fb\u00f6\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc!\3\2\2\2\u00fd\u0100\5$\23")
        buf.write("\2\u00fe\u0100\5\36\20\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100#\3\2\2\2\u0101\u010d\7\62\2\2\u0102\u010d")
        buf.write("\7\63\2\2\u0103\u010d\7\64\2\2\u0104\u010d\7\65\2\2\u0105")
        buf.write("\u010d\7\66\2\2\u0106\u010d\7\67\2\2\u0107\u010d\7\30")
        buf.write("\2\2\u0108\u010d\7\31\2\2\u0109\u010d\7\27\2\2\u010a\u010d")
        buf.write("\5\60\31\2\u010b\u010d\7:\2\2\u010c\u0101\3\2\2\2\u010c")
        buf.write("\u0102\3\2\2\2\u010c\u0103\3\2\2\2\u010c\u0104\3\2\2\2")
        buf.write("\u010c\u0105\3\2\2\2\u010c\u0106\3\2\2\2\u010c\u0107\3")
        buf.write("\2\2\2\u010c\u0108\3\2\2\2\u010c\u0109\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010b\3\2\2\2\u010d%\3\2\2\2\u010e\u010f")
        buf.write("\7\22\2\2\u010f\u0110\7:\2\2\u0110\u0111\7(\2\2\u0111")
        buf.write("\u0112\5V,\2\u0112\u0113\7\61\2\2\u0113\'\3\2\2\2\u0114")
        buf.write("\u0115\7\13\2\2\u0115\u0116\7:\2\2\u0116\u0117\7\f\2\2")
        buf.write("\u0117\u0118\5*\26\2\u0118\u0119\7\61\2\2\u0119)\3\2\2")
        buf.write("\2\u011a\u011b\7=\2\2\u011b\u011c\5,\27\2\u011c\u011d")
        buf.write("\7>\2\2\u011d+\3\2\2\2\u011e\u011f\5.\30\2\u011f\u0120")
        buf.write("\5,\27\2\u0120\u0123\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u011e\3\2\2\2\u0122\u0121\3\2\2\2\u0123-\3\2\2\2\u0124")
        buf.write("\u0126\7:\2\2\u0125\u0127\5\30\r\2\u0126\u0125\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\5")
        buf.write("\20\t\2\u0129\u012a\7\61\2\2\u012a/\3\2\2\2\u012b\u012c")
        buf.write("\7:\2\2\u012c\u012d\5\62\32\2\u012d\61\3\2\2\2\u012e\u012f")
        buf.write("\7=\2\2\u012f\u0130\5\64\33\2\u0130\u0131\7>\2\2\u0131")
        buf.write("\63\3\2\2\2\u0132\u0135\5\66\34\2\u0133\u0135\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135\65\3\2")
        buf.write("\2\2\u0136\u0137\58\35\2\u0137\u0138\7\60\2\2\u0138\u0139")
        buf.write("\5\66\34\2\u0139\u013c\3\2\2\2\u013a\u013c\58\35\2\u013b")
        buf.write("\u0136\3\2\2\2\u013b\u013a\3\2\2\2\u013c\67\3\2\2\2\u013d")
        buf.write("\u013e\7:\2\2\u013e\u013f\7\5\2\2\u013f\u0140\5V,\2\u0140")
        buf.write("9\3\2\2\2\u0141\u0142\7\13\2\2\u0142\u0143\7:\2\2\u0143")
        buf.write("\u0144\7\r\2\2\u0144\u0145\5<\37\2\u0145\u0146\7\61\2")
        buf.write("\2\u0146;\3\2\2\2\u0147\u0148\7=\2\2\u0148\u0149\5> \2")
        buf.write("\u0149\u014a\7>\2\2\u014a=\3\2\2\2\u014b\u014c\5@!\2\u014c")
        buf.write("\u014d\5> \2\u014d\u0150\3\2\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u014b\3\2\2\2\u014f\u014e\3\2\2\2\u0150?\3\2\2\2\u0151")
        buf.write("\u0152\7:\2\2\u0152\u0153\7;\2\2\u0153\u0154\5D#\2\u0154")
        buf.write("\u0156\7<\2\2\u0155\u0157\5P)\2\u0156\u0155\3\2\2\2\u0156")
        buf.write("\u0157\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\7\61\2")
        buf.write("\2\u0159A\3\2\2\2\u015a\u015b\7\n\2\2\u015b\u015c\7:\2")
        buf.write("\2\u015c\u015d\7;\2\2\u015d\u015e\5D#\2\u015e\u0160\7")
        buf.write("<\2\2\u015f\u0161\5P)\2\u0160\u015f\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\5L\'\2\u0163")
        buf.write("\u0164\7\61\2\2\u0164C\3\2\2\2\u0165\u0168\5F$\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0168E\3\2\2\2\u0169\u016a\5H%\2\u016a\u016b\7\60\2\2")
        buf.write("\u016b\u016c\5F$\2\u016c\u016f\3\2\2\2\u016d\u016f\5H")
        buf.write("%\2\u016e\u0169\3\2\2\2\u016e\u016d\3\2\2\2\u016fG\3\2")
        buf.write("\2\2\u0170\u0172\5J&\2\u0171\u0173\5\30\r\2\u0172\u0171")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\5\20\t\2\u0175I\3\2\2\2\u0176\u0177\7:\2\2\u0177")
        buf.write("\u0178\7\60\2\2\u0178\u017b\5J&\2\u0179\u017b\7:\2\2\u017a")
        buf.write("\u0176\3\2\2\2\u017a\u0179\3\2\2\2\u017bK\3\2\2\2\u017c")
        buf.write("\u017d\7=\2\2\u017d\u017e\5N(\2\u017e\u017f\7>\2\2\u017f")
        buf.write("M\3\2\2\2\u0180\u0181\5|?\2\u0181\u0182\5N(\2\u0182\u0185")
        buf.write("\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0180\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185O\3\2\2\2\u0186\u0188\5\30\r\2\u0187")
        buf.write("\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018a\5\20\t\2\u018aQ\3\2\2\2\u018b\u018c\7\n\2")
        buf.write("\2\u018c\u018d\7;\2\2\u018d\u018e\7:\2\2\u018e\u018f\7")
        buf.write(":\2\2\u018f\u0190\7<\2\2\u0190\u0191\7:\2\2\u0191\u0192")
        buf.write("\7;\2\2\u0192\u0193\5D#\2\u0193\u0195\7<\2\2\u0194\u0196")
        buf.write("\5P)\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0198\5T+\2\u0198\u0199\7\61\2\2\u0199")
        buf.write("S\3\2\2\2\u019a\u019b\7=\2\2\u019b\u019c\5N(\2\u019c\u019d")
        buf.write("\7>\2\2\u019dU\3\2\2\2\u019e\u019f\b,\1\2\u019f\u01a0")
        buf.write("\5X-\2\u01a0\u01a6\3\2\2\2\u01a1\u01a2\f\4\2\2\u01a2\u01a3")
        buf.write("\7&\2\2\u01a3\u01a5\5X-\2\u01a4\u01a1\3\2\2\2\u01a5\u01a8")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("W\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01aa\b-\1\2\u01aa")
        buf.write("\u01ab\5Z.\2\u01ab\u01b1\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad")
        buf.write("\u01ae\7%\2\2\u01ae\u01b0\5Z.\2\u01af\u01ac\3\2\2\2\u01b0")
        buf.write("\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b2Y\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\b.\1\2")
        buf.write("\u01b5\u01b6\5\\/\2\u01b6\u01bc\3\2\2\2\u01b7\u01b8\f")
        buf.write("\4\2\2\u01b8\u01b9\t\4\2\2\u01b9\u01bb\5\\/\2\u01ba\u01b7")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd[\3\2\2\2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c0\b/\1\2\u01c0\u01c1\5^\60\2\u01c1\u01c7\3\2\2\2")
        buf.write("\u01c2\u01c3\f\4\2\2\u01c3\u01c4\t\5\2\2\u01c4\u01c6\5")
        buf.write("^\60\2\u01c5\u01c2\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8]\3\2\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01ca\u01cb\b\60\1\2\u01cb\u01cc\5`\61\2\u01cc")
        buf.write("\u01d2\3\2\2\2\u01cd\u01ce\f\4\2\2\u01ce\u01cf\t\6\2\2")
        buf.write("\u01cf\u01d1\5`\61\2\u01d0\u01cd\3\2\2\2\u01d1\u01d4\3")
        buf.write("\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3_")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d6\t\7\2\2\u01d6")
        buf.write("\u01d9\5`\61\2\u01d7\u01d9\5b\62\2\u01d8\u01d5\3\2\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d9a\3\2\2\2\u01da\u01db\b\62\1")
        buf.write("\2\u01db\u01dc\5d\63\2\u01dc\u01dd\5f\64\2\u01dd\u01e0")
        buf.write("\3\2\2\2\u01de\u01e0\5d\63\2\u01df\u01da\3\2\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01f9\3\2\2\2\u01e1\u01e2\f\b\2\2")
        buf.write("\u01e2\u01e3\7/\2\2\u01e3\u01f8\7:\2\2\u01e4\u01e5\f\7")
        buf.write("\2\2\u01e5\u01e6\7/\2\2\u01e6\u01e7\7:\2\2\u01e7\u01e8")
        buf.write("\7;\2\2\u01e8\u01e9\5r:\2\u01e9\u01ea\7<\2\2\u01ea\u01f8")
        buf.write("\3\2\2\2\u01eb\u01ec\f\6\2\2\u01ec\u01ed\7/\2\2\u01ed")
        buf.write("\u01ee\7:\2\2\u01ee\u01ef\7;\2\2\u01ef\u01f0\5r:\2\u01f0")
        buf.write("\u01f1\7<\2\2\u01f1\u01f2\5f\64\2\u01f2\u01f8\3\2\2\2")
        buf.write("\u01f3\u01f4\f\5\2\2\u01f4\u01f5\7/\2\2\u01f5\u01f6\7")
        buf.write(":\2\2\u01f6\u01f8\5f\64\2\u01f7\u01e1\3\2\2\2\u01f7\u01e4")
        buf.write("\3\2\2\2\u01f7\u01eb\3\2\2\2\u01f7\u01f3\3\2\2\2\u01f8")
        buf.write("\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2")
        buf.write("\u01fac\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01ff\5l\67")
        buf.write("\2\u01fd\u01ff\5j\66\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd")
        buf.write("\3\2\2\2\u01ffe\3\2\2\2\u0200\u0201\b\64\1\2\u0201\u0202")
        buf.write("\5h\65\2\u0202\u0207\3\2\2\2\u0203\u0204\f\4\2\2\u0204")
        buf.write("\u0206\5h\65\2\u0205\u0203\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208g\3\2\2")
        buf.write("\2\u0209\u0207\3\2\2\2\u020a\u020b\7?\2\2\u020b\u020c")
        buf.write("\5V,\2\u020c\u020d\7@\2\2\u020di\3\2\2\2\u020e\u0211\5")
        buf.write("n8\2\u020f\u0211\5p9\2\u0210\u020e\3\2\2\2\u0210\u020f")
        buf.write("\3\2\2\2\u0211k\3\2\2\2\u0212\u0213\7;\2\2\u0213\u0214")
        buf.write("\5V,\2\u0214\u0215\7<\2\2\u0215m\3\2\2\2\u0216\u0219\5")
        buf.write("$\23\2\u0217\u0219\5\34\17\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0219o\3\2\2\2\u021a\u021b\7:\2\2\u021b")
        buf.write("\u021c\7;\2\2\u021c\u021d\5r:\2\u021d\u021e\7<\2\2\u021e")
        buf.write("q\3\2\2\2\u021f\u0222\5t;\2\u0220\u0222\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0221\u0220\3\2\2\2\u0222s\3\2\2\2\u0223")
        buf.write("\u0224\5V,\2\u0224\u0225\7\60\2\2\u0225\u0226\5t;\2\u0226")
        buf.write("\u0229\3\2\2\2\u0227\u0229\5V,\2\u0228\u0223\3\2\2\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229u\3\2\2\2\u022a\u022b\5x=\2\u022b")
        buf.write("\u022c\5z>\2\u022cw\3\2\2\2\u022d\u022e\b=\1\2\u022e\u022f")
        buf.write("\5p9\2\u022f\u0230\5f\64\2\u0230\u0236\3\2\2\2\u0231\u0232")
        buf.write("\7:\2\2\u0232\u0236\5f\64\2\u0233\u0236\5p9\2\u0234\u0236")
        buf.write("\7:\2\2\u0235\u022d\3\2\2\2\u0235\u0231\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u024f\3\2\2\2")
        buf.write("\u0237\u0238\f\n\2\2\u0238\u0239\7/\2\2\u0239\u024e\7")
        buf.write(":\2\2\u023a\u023b\f\t\2\2\u023b\u023c\7/\2\2\u023c\u023d")
        buf.write("\7:\2\2\u023d\u023e\7;\2\2\u023e\u023f\5r:\2\u023f\u0240")
        buf.write("\7<\2\2\u0240\u024e\3\2\2\2\u0241\u0242\f\b\2\2\u0242")
        buf.write("\u0243\7/\2\2\u0243\u0244\7:\2\2\u0244\u0245\7;\2\2\u0245")
        buf.write("\u0246\5r:\2\u0246\u0247\7<\2\2\u0247\u0248\5f\64\2\u0248")
        buf.write("\u024e\3\2\2\2\u0249\u024a\f\7\2\2\u024a\u024b\7/\2\2")
        buf.write("\u024b\u024c\7:\2\2\u024c\u024e\5f\64\2\u024d\u0237\3")
        buf.write("\2\2\2\u024d\u023a\3\2\2\2\u024d\u0241\3\2\2\2\u024d\u0249")
        buf.write("\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f")
        buf.write("\u0250\3\2\2\2\u0250y\3\2\2\2\u0251\u024f\3\2\2\2\u0252")
        buf.write("\u0253\7/\2\2\u0253\u0254\7:\2\2\u0254\u0255\7;\2\2\u0255")
        buf.write("\u0256\5r:\2\u0256\u0257\7<\2\2\u0257{\3\2\2\2\u0258\u0262")
        buf.write("\5\b\5\2\u0259\u0262\5&\24\2\u025a\u0262\5~@\2\u025b\u0262")
        buf.write("\5\u0084C\2\u025c\u0262\5\u0088E\2\u025d\u0262\5\u0094")
        buf.write("K\2\u025e\u0262\5\u00a2R\2\u025f\u0262\5\u00a4S\2\u0260")
        buf.write("\u0262\5\u0086D\2\u0261\u0258\3\2\2\2\u0261\u0259\3\2")
        buf.write("\2\2\u0261\u025a\3\2\2\2\u0261\u025b\3\2\2\2\u0261\u025c")
        buf.write("\3\2\2\2\u0261\u025d\3\2\2\2\u0261\u025e\3\2\2\2\u0261")
        buf.write("\u025f\3\2\2\2\u0261\u0260\3\2\2\2\u0262}\3\2\2\2\u0263")
        buf.write("\u0266\5\u0080A\2\u0264\u0267\7)\2\2\u0265\u0267\5\u0082")
        buf.write("B\2\u0266\u0264\3\2\2\2\u0266\u0265\3\2\2\2\u0267\u0268")
        buf.write("\3\2\2\2\u0268\u0269\5V,\2\u0269\u026a\7\61\2\2\u026a")
        buf.write("\177\3\2\2\2\u026b\u026c\bA\1\2\u026c\u026d\7:\2\2\u026d")
        buf.write("\u0270\5f\64\2\u026e\u0270\7:\2\2\u026f\u026b\3\2\2\2")
        buf.write("\u026f\u026e\3\2\2\2\u0270\u027a\3\2\2\2\u0271\u0272\f")
        buf.write("\5\2\2\u0272\u0273\7/\2\2\u0273\u0279\7:\2\2\u0274\u0275")
        buf.write("\f\4\2\2\u0275\u0276\7/\2\2\u0276\u0277\7:\2\2\u0277\u0279")
        buf.write("\5f\64\2\u0278\u0271\3\2\2\2\u0278\u0274\3\2\2\2\u0279")
        buf.write("\u027c\3\2\2\2\u027a\u0278\3\2\2\2\u027a\u027b\3\2\2\2")
        buf.write("\u027b\u0081\3\2\2\2\u027c\u027a\3\2\2\2\u027d\u027e\t")
        buf.write("\b\2\2\u027e\u0083\3\2\2\2\u027f\u0281\7\t\2\2\u0280\u0282")
        buf.write("\5V,\2\u0281\u0280\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0283")
        buf.write("\3\2\2\2\u0283\u0284\7\61\2\2\u0284\u0085\3\2\2\2\u0285")
        buf.write("\u0288\5p9\2\u0286\u0288\5v<\2\u0287\u0285\3\2\2\2\u0287")
        buf.write("\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\7\61\2")
        buf.write("\2\u028a\u0087\3\2\2\2\u028b\u028d\5\u008aF\2\u028c\u028e")
        buf.write("\5\u008eH\2\u028d\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e")
        buf.write("\u028f\3\2\2\2\u028f\u0290\7\61\2\2\u0290\u0089\3\2\2")
        buf.write("\2\u0291\u0292\7\6\2\2\u0292\u0293\7;\2\2\u0293\u0294")
        buf.write("\5V,\2\u0294\u0295\7<\2\2\u0295\u0296\5\u008cG\2\u0296")
        buf.write("\u008b\3\2\2\2\u0297\u0298\7=\2\2\u0298\u0299\5N(\2\u0299")
        buf.write("\u029a\7>\2\2\u029a\u008d\3\2\2\2\u029b\u029c\5\u0090")
        buf.write("I\2\u029c\u029d\5\u008eH\2\u029d\u02a1\3\2\2\2\u029e\u02a1")
        buf.write("\5\u0092J\2\u029f\u02a1\5\u0090I\2\u02a0\u029b\3\2\2\2")
        buf.write("\u02a0\u029e\3\2\2\2\u02a0\u029f\3\2\2\2\u02a1\u008f\3")
        buf.write("\2\2\2\u02a2\u02a3\7\7\2\2\u02a3\u02a4\7\6\2\2\u02a4\u02a5")
        buf.write("\7;\2\2\u02a5\u02a6\5V,\2\u02a6\u02a7\7<\2\2\u02a7\u02a8")
        buf.write("\5\u008cG\2\u02a8\u0091\3\2\2\2\u02a9\u02aa\7\7\2\2\u02aa")
        buf.write("\u02ab\5\u008cG\2\u02ab\u0093\3\2\2\2\u02ac\u02b0\5\u0096")
        buf.write("L\2\u02ad\u02b0\5\u009aN\2\u02ae\u02b0\5\u00a0Q\2\u02af")
        buf.write("\u02ac\3\2\2\2\u02af\u02ad\3\2\2\2\u02af\u02ae\3\2\2\2")
        buf.write("\u02b0\u0095\3\2\2\2\u02b1\u02b2\7\b\2\2\u02b2\u02b3\5")
        buf.write("V,\2\u02b3\u02b4\5\u0098M\2\u02b4\u02b5\7\61\2\2\u02b5")
        buf.write("\u0097\3\2\2\2\u02b6\u02b7\7=\2\2\u02b7\u02b8\5N(\2\u02b8")
        buf.write("\u02b9\7>\2\2\u02b9\u0099\3\2\2\2\u02ba\u02bb\7\b\2\2")
        buf.write("\u02bb\u02bc\5\u009cO\2\u02bc\u02bd\7\61\2\2\u02bd\u02be")
        buf.write("\5V,\2\u02be\u02bf\7\61\2\2\u02bf\u02c0\5\u009eP\2\u02c0")
        buf.write("\u02c1\5\u0098M\2\u02c1\u02c2\7\61\2\2\u02c2\u009b\3\2")
        buf.write("\2\2\u02c3\u02cc\5\u009eP\2\u02c4\u02c5\7\23\2\2\u02c5")
        buf.write("\u02c7\7:\2\2\u02c6\u02c8\5\20\t\2\u02c7\u02c6\3\2\2\2")
        buf.write("\u02c7\u02c8\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02ca\7")
        buf.write("(\2\2\u02ca\u02cc\5V,\2\u02cb\u02c3\3\2\2\2\u02cb\u02c4")
        buf.write("\3\2\2\2\u02cc\u009d\3\2\2\2\u02cd\u02d0\5\u0080A\2\u02ce")
        buf.write("\u02d1\7)\2\2\u02cf\u02d1\5\u0082B\2\u02d0\u02ce\3\2\2")
        buf.write("\2\u02d0\u02cf\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d3")
        buf.write("\5V,\2\u02d3\u009f\3\2\2\2\u02d4\u02d5\7\b\2\2\u02d5\u02d6")
        buf.write("\7:\2\2\u02d6\u02d7\7\60\2\2\u02d7\u02d8\7:\2\2\u02d8")
        buf.write("\u02d9\7)\2\2\u02d9\u02da\7\26\2\2\u02da\u02db\5V,\2\u02db")
        buf.write("\u02dc\5\u0098M\2\u02dc\u02dd\7\61\2\2\u02dd\u00a1\3\2")
        buf.write("\2\2\u02de\u02df\7\25\2\2\u02df\u02e0\7\61\2\2\u02e0\u00a3")
        buf.write("\3\2\2\2\u02e1\u02e2\7\24\2\2\u02e2\u02e3\7\61\2\2\u02e3")
        buf.write("\u00a5\3\2\2\2:\u00ad\u00b5\u00b9\u00bd\u00c7\u00d1\u00d8")
        buf.write("\u00e8\u00fb\u00ff\u010c\u0122\u0126\u0134\u013b\u014f")
        buf.write("\u0156\u0160\u0167\u016e\u0172\u017a\u0184\u0187\u0195")
        buf.write("\u01a6\u01b1\u01bc\u01c7\u01d2\u01d8\u01df\u01f7\u01f9")
        buf.write("\u01fe\u0207\u0210\u0218\u0221\u0228\u0235\u024d\u024f")
        buf.write("\u0261\u0266\u026f\u0278\u027a\u0281\u0287\u028d\u02a0")
        buf.write("\u02af\u02c7\u02cb\u02d0")
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
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

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
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_normal_vardecl = 4
    RULE_normal_vardecl_without_init = 5
    RULE_normal_vardecl_with_init = 6
    RULE_typedecl = 7
    RULE_arr_vardecl = 8
    RULE_arr_vardecl_with_init = 9
    RULE_arr_vardecl_without_init = 10
    RULE_arrdimlist = 11
    RULE_arrdim = 12
    RULE_arrliteral = 13
    RULE_arrlistvalue = 14
    RULE_listvalue = 15
    RULE_value_for_arr = 16
    RULE_literalvalue_for_arr = 17
    RULE_constdecl = 18
    RULE_structdecl = 19
    RULE_structbody = 20
    RULE_fieldlist = 21
    RULE_field = 22
    RULE_structinst = 23
    RULE_structinst_body = 24
    RULE_structinst_fieldlist = 25
    RULE_structinst_fieldprime = 26
    RULE_structinst_field = 27
    RULE_interfacedecl = 28
    RULE_interfacebody = 29
    RULE_methodlist = 30
    RULE_method = 31
    RULE_funcdecl = 32
    RULE_paramlist = 33
    RULE_param_group_prime = 34
    RULE_param_group = 35
    RULE_param_mem_list = 36
    RULE_funcbody = 37
    RULE_stmtlist = 38
    RULE_returntype = 39
    RULE_methodimple = 40
    RULE_methodimple_body = 41
    RULE_expr = 42
    RULE_expr0 = 43
    RULE_expr1 = 44
    RULE_expr2 = 45
    RULE_expr3 = 46
    RULE_expr4 = 47
    RULE_expr5 = 48
    RULE_expr6 = 49
    RULE_arrdimlist_expr = 50
    RULE_arrdim_expr = 51
    RULE_value = 52
    RULE_subexpr = 53
    RULE_literalvalue = 54
    RULE_funccall = 55
    RULE_arglist = 56
    RULE_argprime = 57
    RULE_methodcall = 58
    RULE_methodcallbody = 59
    RULE_methodcalltail = 60
    RULE_stmt = 61
    RULE_assignstmt = 62
    RULE_accesslist = 63
    RULE_otherassignop = 64
    RULE_returnstmt = 65
    RULE_callstmt = 66
    RULE_ifstmt = 67
    RULE_firstifstmt = 68
    RULE_ifstmtbody = 69
    RULE_elseifstmtlist = 70
    RULE_elseifstmt = 71
    RULE_elsestmt = 72
    RULE_forstmt = 73
    RULE_basicforstmt = 74
    RULE_forstmtbody = 75
    RULE_init_cond_update_forstmt = 76
    RULE_init_for = 77
    RULE_assign = 78
    RULE_rangeforstmt = 79
    RULE_breakstmt = 80
    RULE_continuestmt = 81

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "normal_vardecl", 
                   "normal_vardecl_without_init", "normal_vardecl_with_init", 
                   "typedecl", "arr_vardecl", "arr_vardecl_with_init", "arr_vardecl_without_init", 
                   "arrdimlist", "arrdim", "arrliteral", "arrlistvalue", 
                   "listvalue", "value_for_arr", "literalvalue_for_arr", 
                   "constdecl", "structdecl", "structbody", "fieldlist", 
                   "field", "structinst", "structinst_body", "structinst_fieldlist", 
                   "structinst_fieldprime", "structinst_field", "interfacedecl", 
                   "interfacebody", "methodlist", "method", "funcdecl", 
                   "paramlist", "param_group_prime", "param_group", "param_mem_list", 
                   "funcbody", "stmtlist", "returntype", "methodimple", 
                   "methodimple_body", "expr", "expr0", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "arrdimlist_expr", 
                   "arrdim_expr", "value", "subexpr", "literalvalue", "funccall", 
                   "arglist", "argprime", "methodcall", "methodcallbody", 
                   "methodcalltail", "stmt", "assignstmt", "accesslist", 
                   "otherassignop", "returnstmt", "callstmt", "ifstmt", 
                   "firstifstmt", "ifstmtbody", "elseifstmtlist", "elseifstmt", 
                   "elsestmt", "forstmt", "basicforstmt", "forstmtbody", 
                   "init_cond_update_forstmt", "init_for", "assign", "rangeforstmt", 
                   "breakstmt", "continuestmt" ]

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

        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.decllist()
            self.state = 165
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MiniGoParser.DecllistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MiniGoParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.decl()
                self.state = 168
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.decl()
                pass


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

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


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
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.structdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 176
                self.interfacedecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 177
                self.funcdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                self.methodimple()
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

        def normal_vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardeclContext,0)


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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.normal_vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.arr_vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_vardecl_without_init(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardecl_without_initContext,0)


        def normal_vardecl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Normal_vardecl_with_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_normal_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_vardecl" ):
                return visitor.visitNormal_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def normal_vardecl(self):

        localctx = MiniGoParser.Normal_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_normal_vardecl)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.normal_vardecl_without_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.normal_vardecl_with_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_vardecl_without_initContext(ParserRuleContext):
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


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_normal_vardecl_without_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_vardecl_without_init" ):
                return visitor.visitNormal_vardecl_without_init(self)
            else:
                return visitor.visitChildren(self)




    def normal_vardecl_without_init(self):

        localctx = MiniGoParser.Normal_vardecl_without_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_vardecl_without_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.VAR)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 191
            self.typedecl()
            self.state = 192
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_vardecl_with_initContext(ParserRuleContext):
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


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_normal_vardecl_with_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_vardecl_with_init" ):
                return visitor.visitNormal_vardecl_with_init(self)
            else:
                return visitor.visitChildren(self)




    def normal_vardecl_with_init(self):

        localctx = MiniGoParser.Normal_vardecl_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_normal_vardecl_with_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MiniGoParser.VAR)
            self.state = 195
            self.match(MiniGoParser.ID)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                self.state = 196
                self.typedecl()


            self.state = 199
            self.match(MiniGoParser.ASSIGN)
            self.state = 200
            self.expr(0)
            self.state = 201
            self.match(MiniGoParser.SEMICO)
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
        self.enterRule(localctx, 14, self.RULE_typedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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


    class Arr_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_vardecl_without_init(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_vardecl_without_initContext,0)


        def arr_vardecl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_vardecl_with_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_vardecl" ):
                return visitor.visitArr_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def arr_vardecl(self):

        localctx = MiniGoParser.Arr_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arr_vardecl)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.arr_vardecl_without_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.arr_vardecl_with_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_vardecl_with_initContext(ParserRuleContext):
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


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_vardecl_with_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_vardecl_with_init" ):
                return visitor.visitArr_vardecl_with_init(self)
            else:
                return visitor.visitChildren(self)




    def arr_vardecl_with_init(self):

        localctx = MiniGoParser.Arr_vardecl_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arr_vardecl_with_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.VAR)
            self.state = 210
            self.match(MiniGoParser.ID)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 211
                self.arrdimlist()
                self.state = 212
                self.typedecl()


            self.state = 216
            self.match(MiniGoParser.ASSIGN)
            self.state = 217
            self.expr(0)
            self.state = 218
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_vardecl_without_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_vardecl_without_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_vardecl_without_init" ):
                return visitor.visitArr_vardecl_without_init(self)
            else:
                return visitor.visitChildren(self)




    def arr_vardecl_without_init(self):

        localctx = MiniGoParser.Arr_vardecl_without_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arr_vardecl_without_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.VAR)
            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 222
            self.arrdimlist()
            self.state = 223
            self.typedecl()
            self.state = 224
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdimlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrdim(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimContext,0)


        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrdimlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdimlist" ):
                return visitor.visitArrdimlist(self)
            else:
                return visitor.visitChildren(self)




    def arrdimlist(self):

        localctx = MiniGoParser.ArrdimlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrdimlist)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.arrdim()
                self.state = 227
                self.arrdimlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.arrdim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdimContext(ParserRuleContext):
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

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrdim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdim" ):
                return visitor.visitArrdim(self)
            else:
                return visitor.visitChildren(self)




    def arrdim(self):

        localctx = MiniGoParser.ArrdimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrdim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MiniGoParser.LBRACK)
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 234
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def arrlistvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrlistvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrliteral" ):
                return visitor.visitArrliteral(self)
            else:
                return visitor.visitChildren(self)




    def arrliteral(self):

        localctx = MiniGoParser.ArrliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.arrdimlist()
            self.state = 237
            self.typedecl()
            self.state = 238
            self.arrlistvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def listvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ListvalueContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrlistvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlistvalue" ):
                return visitor.visitArrlistvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrlistvalue(self):

        localctx = MiniGoParser.ArrlistvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrlistvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.LBRACE)
            self.state = 241
            self.listvalue()
            self.state = 242
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_for_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Value_for_arrContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def listvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ListvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListvalue" ):
                return visitor.visitListvalue(self)
            else:
                return visitor.visitChildren(self)




    def listvalue(self):

        localctx = MiniGoParser.ListvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listvalue)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.value_for_arr()
                self.state = 245
                self.match(MiniGoParser.COMMA)
                self.state = 246
                self.listvalue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.value_for_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_for_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalvalue_for_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Literalvalue_for_arrContext,0)


        def arrlistvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrlistvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_value_for_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_for_arr" ):
                return visitor.visitValue_for_arr(self)
            else:
                return visitor.visitChildren(self)




    def value_for_arr(self):

        localctx = MiniGoParser.Value_for_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_value_for_arr)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.literalvalue_for_arr()
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.arrlistvalue()
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


    class Literalvalue_for_arrContext(ParserRuleContext):
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


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literalvalue_for_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralvalue_for_arr" ):
                return visitor.visitLiteralvalue_for_arr(self)
            else:
                return visitor.visitChildren(self)




    def literalvalue_for_arr(self):

        localctx = MiniGoParser.Literalvalue_for_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literalvalue_for_arr)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(MiniGoParser.DEC_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.BIN_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(MiniGoParser.OCT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(MiniGoParser.HEX_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 260
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 262
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 263
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 264
                self.structinst()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 265
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


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

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
            self.state = 268
            self.match(MiniGoParser.CONST)
            self.state = 269
            self.match(MiniGoParser.ID)
            self.state = 270
            self.match(MiniGoParser.ASSIGN)
            self.state = 271
            self.expr(0)
            self.state = 272
            self.match(MiniGoParser.SEMICO)
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

        def structbody(self):
            return self.getTypedRuleContext(MiniGoParser.StructbodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(MiniGoParser.TYPE)
            self.state = 275
            self.match(MiniGoParser.ID)
            self.state = 276
            self.match(MiniGoParser.STRUCT)
            self.state = 277
            self.structbody()
            self.state = 278
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def fieldlist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructbody" ):
                return visitor.visitStructbody(self)
            else:
                return visitor.visitChildren(self)




    def structbody(self):

        localctx = MiniGoParser.StructbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_structbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.LBRACE)
            self.state = 281
            self.fieldlist()
            self.state = 282
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def fieldlist(self):
            return self.getTypedRuleContext(MiniGoParser.FieldlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fieldlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldlist" ):
                return visitor.visitFieldlist(self)
            else:
                return visitor.visitChildren(self)




    def fieldlist(self):

        localctx = MiniGoParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_fieldlist)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.field()
                self.state = 285
                self.fieldlist()
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


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(MiniGoParser.ID)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 291
                self.arrdimlist()


            self.state = 294
            self.typedecl()
            self.state = 295
            self.match(MiniGoParser.SEMICO)
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

        def structinst_body(self):
            return self.getTypedRuleContext(MiniGoParser.Structinst_bodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structinst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst" ):
                return visitor.visitStructinst(self)
            else:
                return visitor.visitChildren(self)




    def structinst(self):

        localctx = MiniGoParser.StructinstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_structinst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.ID)
            self.state = 298
            self.structinst_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structinst_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structinst_fieldlist(self):
            return self.getTypedRuleContext(MiniGoParser.Structinst_fieldlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structinst_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst_body" ):
                return visitor.visitStructinst_body(self)
            else:
                return visitor.visitChildren(self)




    def structinst_body(self):

        localctx = MiniGoParser.Structinst_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_structinst_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MiniGoParser.LBRACE)
            self.state = 301
            self.structinst_fieldlist()
            self.state = 302
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structinst_fieldlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structinst_fieldprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structinst_fieldprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structinst_fieldlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst_fieldlist" ):
                return visitor.visitStructinst_fieldlist(self)
            else:
                return visitor.visitChildren(self)




    def structinst_fieldlist(self):

        localctx = MiniGoParser.Structinst_fieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_structinst_fieldlist)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.structinst_fieldprime()
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


    class Structinst_fieldprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structinst_field(self):
            return self.getTypedRuleContext(MiniGoParser.Structinst_fieldContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structinst_fieldprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structinst_fieldprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structinst_fieldprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst_fieldprime" ):
                return visitor.visitStructinst_fieldprime(self)
            else:
                return visitor.visitChildren(self)




    def structinst_fieldprime(self):

        localctx = MiniGoParser.Structinst_fieldprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_structinst_fieldprime)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.structinst_field()
                self.state = 309
                self.match(MiniGoParser.COMMA)
                self.state = 310
                self.structinst_fieldprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.structinst_field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structinst_fieldContext(ParserRuleContext):
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
            return MiniGoParser.RULE_structinst_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructinst_field" ):
                return visitor.visitStructinst_field(self)
            else:
                return visitor.visitChildren(self)




    def structinst_field(self):

        localctx = MiniGoParser.Structinst_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_structinst_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MiniGoParser.ID)
            self.state = 316
            self.match(MiniGoParser.COLON)
            self.state = 317
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

        def interfacebody(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacebodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interfacedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MiniGoParser.TYPE)
            self.state = 320
            self.match(MiniGoParser.ID)
            self.state = 321
            self.match(MiniGoParser.INTERFACE)
            self.state = 322
            self.interfacebody()
            self.state = 323
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacebodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def methodlist(self):
            return self.getTypedRuleContext(MiniGoParser.MethodlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacebody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacebody" ):
                return visitor.visitInterfacebody(self)
            else:
                return visitor.visitChildren(self)




    def interfacebody(self):

        localctx = MiniGoParser.InterfacebodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_interfacebody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.LBRACE)
            self.state = 326
            self.methodlist()
            self.state = 327
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def methodlist(self):
            return self.getTypedRuleContext(MiniGoParser.MethodlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodlist" ):
                return visitor.visitMethodlist(self)
            else:
                return visitor.visitChildren(self)




    def methodlist(self):

        localctx = MiniGoParser.MethodlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_methodlist)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.method()
                self.state = 330
                self.methodlist()
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


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.ID)
            self.state = 336
            self.match(MiniGoParser.LPAREN)
            self.state = 337
            self.paramlist()
            self.state = 338
            self.match(MiniGoParser.RPAREN)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 339
                self.returntype()


            self.state = 342
            self.match(MiniGoParser.SEMICO)
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

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcbody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncbodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.FUNC)
            self.state = 345
            self.match(MiniGoParser.ID)
            self.state = 346
            self.match(MiniGoParser.LPAREN)
            self.state = 347
            self.paramlist()
            self.state = 348
            self.match(MiniGoParser.RPAREN)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 349
                self.returntype()


            self.state = 352
            self.funcbody()
            self.state = 353
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_group_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_group_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramlist)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
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
        self.enterRule(localctx, 68, self.RULE_param_group_prime)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.param_group()
                self.state = 360
                self.match(MiniGoParser.COMMA)
                self.state = 361
                self.param_group_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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


        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_group" ):
                return visitor.visitParam_group(self)
            else:
                return visitor.visitChildren(self)




    def param_group(self):

        localctx = MiniGoParser.Param_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_param_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.param_mem_list()
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 367
                self.arrdimlist()


            self.state = 370
            self.typedecl()
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
        self.enterRule(localctx, 72, self.RULE_param_mem_list)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(MiniGoParser.ID)
                self.state = 373
                self.match(MiniGoParser.COMMA)
                self.state = 374
                self.param_mem_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MiniGoParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.LBRACE)
            self.state = 379
            self.stmtlist()
            self.state = 380
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MiniGoParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmtlist)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.stmt()
                self.state = 383
                self.stmtlist()
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


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def arrdimlist(self):
            return self.getTypedRuleContext(MiniGoParser.ArrdimlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MiniGoParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returntype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACK:
                self.state = 388
                self.arrdimlist()


            self.state = 391
            self.typedecl()
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

        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def methodimple_body(self):
            return self.getTypedRuleContext(MiniGoParser.Methodimple_bodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def returntype(self):
            return self.getTypedRuleContext(MiniGoParser.ReturntypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodimple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodimple" ):
                return visitor.visitMethodimple(self)
            else:
                return visitor.visitChildren(self)




    def methodimple(self):

        localctx = MiniGoParser.MethodimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_methodimple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.FUNC)
            self.state = 394
            self.match(MiniGoParser.LPAREN)
            self.state = 395
            self.match(MiniGoParser.ID)
            self.state = 396
            self.match(MiniGoParser.ID)
            self.state = 397
            self.match(MiniGoParser.RPAREN)
            self.state = 398
            self.match(MiniGoParser.ID)
            self.state = 399
            self.match(MiniGoParser.LPAREN)
            self.state = 400
            self.paramlist()
            self.state = 401
            self.match(MiniGoParser.RPAREN)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 402
                self.returntype()


            self.state = 405
            self.methodimple_body()
            self.state = 406
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methodimple_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodimple_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodimple_body" ):
                return visitor.visitMethodimple_body(self)
            else:
                return visitor.visitChildren(self)




    def methodimple_body(self):

        localctx = MiniGoParser.Methodimple_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_methodimple_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.LBRACE)
            self.state = 409
            self.stmtlist()
            self.state = 410
            self.match(MiniGoParser.RBRACE)
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

        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.expr0(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.match(MiniGoParser.OR)
                    self.state = 417
                    self.expr0(0) 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr0(self):
            return self.getTypedRuleContext(MiniGoParser.Expr0Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)



    def expr0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr0, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 431
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr0)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self.match(MiniGoParser.AND)
                    self.state = 428
                    self.expr1(0) 
                self.state = 433
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


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
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 442
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 437
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 438
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS) | (1 << MiniGoParser.GREATER) | (1 << MiniGoParser.LESS_OR_EQUAL) | (1 << MiniGoParser.GREATER_OR_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 439
                    self.expr2(0) 
                self.state = 444
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 448
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 449
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 450
                    self.expr3(0) 
                self.state = 455
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 464
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 459
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 460
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 461
                    self.expr4() 
                self.state = 466
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MiniGoParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 468
                self.expr4()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.expr5(0)
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


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def arrdimlist_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Arrdimlist_exprContext,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def SELECTOR(self):
            return self.getToken(MiniGoParser.SELECTOR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 473
                self.expr6()
                self.state = 474
                self.arrdimlist_expr(0)
                pass

            elif la_ == 2:
                self.state = 476
                self.expr6()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 501
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 479
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 480
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 481
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 482
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 483
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 484
                        self.match(MiniGoParser.ID)
                        self.state = 485
                        self.match(MiniGoParser.LPAREN)
                        self.state = 486
                        self.arglist()
                        self.state = 487
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 489
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 490
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 491
                        self.match(MiniGoParser.ID)
                        self.state = 492
                        self.match(MiniGoParser.LPAREN)
                        self.state = 493
                        self.arglist()
                        self.state = 494
                        self.match(MiniGoParser.RPAREN)
                        self.state = 495
                        self.arrdimlist_expr(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expr5Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                        self.state = 497
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 498
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 499
                        self.match(MiniGoParser.ID)
                        self.state = 500
                        self.arrdimlist_expr(0)
                        pass

             
                self.state = 505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexpr(self):
            return self.getTypedRuleContext(MiniGoParser.SubexprContext,0)


        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr6)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.subexpr()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.value()
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


    class Arrdimlist_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrdim_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Arrdim_exprContext,0)


        def arrdimlist_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Arrdimlist_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrdimlist_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdimlist_expr" ):
                return visitor.visitArrdimlist_expr(self)
            else:
                return visitor.visitChildren(self)



    def arrdimlist_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Arrdimlist_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_arrdimlist_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.arrdim_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Arrdimlist_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arrdimlist_expr)
                    self.state = 513
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 514
                    self.arrdim_expr() 
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arrdim_exprContext(ParserRuleContext):
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
            return MiniGoParser.RULE_arrdim_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdim_expr" ):
                return visitor.visitArrdim_expr(self)
            else:
                return visitor.visitChildren(self)




    def arrdim_expr(self):

        localctx = MiniGoParser.Arrdim_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arrdim_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.LBRACK)
            self.state = 521
            self.expr(0)
            self.state = 522
            self.match(MiniGoParser.RBRACK)
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

        def literalvalue(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralvalueContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_value)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.literalvalue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MiniGoParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MiniGoParser.LPAREN)
            self.state = 529
            self.expr(0)
            self.state = 530
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalvalue_for_arr(self):
            return self.getTypedRuleContext(MiniGoParser.Literalvalue_for_arrContext,0)


        def arrliteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literalvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralvalue" ):
                return visitor.visitLiteralvalue(self)
            else:
                return visitor.visitChildren(self)




    def literalvalue(self):

        localctx = MiniGoParser.LiteralvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literalvalue)
        try:
            self.state = 534
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.literalvalue_for_arr()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.arrliteral()
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


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.ID)
            self.state = 537
            self.match(MiniGoParser.LPAREN)
            self.state = 538
            self.arglist()
            self.state = 539
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = MiniGoParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arglist)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.DEC_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.argprime()
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


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = MiniGoParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_argprime)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.expr(0)
                self.state = 546
                self.match(MiniGoParser.COMMA)
                self.state = 547
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.expr(0)
                pass


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

        def methodcallbody(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallbodyContext,0)


        def methodcalltail(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcalltailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_methodcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.methodcallbody(0)
            self.state = 553
            self.methodcalltail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def arrdimlist_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Arrdimlist_exprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def methodcallbody(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallbodyContext,0)


        def SELECTOR(self):
            return self.getToken(MiniGoParser.SELECTOR, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcallbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcallbody" ):
                return visitor.visitMethodcallbody(self)
            else:
                return visitor.visitChildren(self)



    def methodcallbody(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MethodcallbodyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_methodcallbody, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 556
                self.funccall()
                self.state = 557
                self.arrdimlist_expr(0)
                pass

            elif la_ == 2:
                self.state = 559
                self.match(MiniGoParser.ID)
                self.state = 560
                self.arrdimlist_expr(0)
                pass

            elif la_ == 3:
                self.state = 561
                self.funccall()
                pass

            elif la_ == 4:
                self.state = 562
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 589
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 587
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.MethodcallbodyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_methodcallbody)
                        self.state = 565
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 566
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 567
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.MethodcallbodyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_methodcallbody)
                        self.state = 568
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 569
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 570
                        self.match(MiniGoParser.ID)
                        self.state = 571
                        self.match(MiniGoParser.LPAREN)
                        self.state = 572
                        self.arglist()
                        self.state = 573
                        self.match(MiniGoParser.RPAREN)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.MethodcallbodyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_methodcallbody)
                        self.state = 575
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 576
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 577
                        self.match(MiniGoParser.ID)
                        self.state = 578
                        self.match(MiniGoParser.LPAREN)
                        self.state = 579
                        self.arglist()
                        self.state = 580
                        self.match(MiniGoParser.RPAREN)
                        self.state = 581
                        self.arrdimlist_expr(0)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.MethodcallbodyContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_methodcallbody)
                        self.state = 583
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 584
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 585
                        self.match(MiniGoParser.ID)
                        self.state = 586
                        self.arrdimlist_expr(0)
                        pass

             
                self.state = 591
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MethodcalltailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECTOR(self):
            return self.getToken(MiniGoParser.SELECTOR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcalltail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcalltail" ):
                return visitor.visitMethodcalltail(self)
            else:
                return visitor.visitChildren(self)




    def methodcalltail(self):

        localctx = MiniGoParser.MethodcalltailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_methodcalltail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.SELECTOR)
            self.state = 593
            self.match(MiniGoParser.ID)
            self.state = 594
            self.match(MiniGoParser.LPAREN)
            self.state = 595
            self.arglist()
            self.state = 596
            self.match(MiniGoParser.RPAREN)
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

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


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


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_stmt)
        try:
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.constdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self.assignstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 601
                self.returnstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 602
                self.ifstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 603
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 604
                self.breakstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 605
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 606
                self.callstmt()
                pass


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

        def accesslist(self):
            return self.getTypedRuleContext(MiniGoParser.AccesslistContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def otherassignop(self):
            return self.getTypedRuleContext(MiniGoParser.OtherassignopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.accesslist(0)
            self.state = 612
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SHORT_ASSIGN]:
                self.state = 610
                self.match(MiniGoParser.SHORT_ASSIGN)
                pass
            elif token in [MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.state = 611
                self.otherassignop()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 614
            self.expr(0)
            self.state = 615
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrdimlist_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Arrdimlist_exprContext,0)


        def accesslist(self):
            return self.getTypedRuleContext(MiniGoParser.AccesslistContext,0)


        def SELECTOR(self):
            return self.getToken(MiniGoParser.SELECTOR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_accesslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccesslist" ):
                return visitor.visitAccesslist(self)
            else:
                return visitor.visitChildren(self)



    def accesslist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AccesslistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_accesslist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 618
                self.match(MiniGoParser.ID)
                self.state = 619
                self.arrdimlist_expr(0)
                pass

            elif la_ == 2:
                self.state = 620
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 632
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 630
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.AccesslistContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_accesslist)
                        self.state = 623
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 624
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 625
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.AccesslistContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_accesslist)
                        self.state = 626
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 627
                        self.match(MiniGoParser.SELECTOR)
                        self.state = 628
                        self.match(MiniGoParser.ID)
                        self.state = 629
                        self.arrdimlist_expr(0)
                        pass

             
                self.state = 634
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OtherassignopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return MiniGoParser.RULE_otherassignop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherassignop" ):
                return visitor.visitOtherassignop(self)
            else:
                return visitor.visitChildren(self)




    def otherassignop(self):

        localctx = MiniGoParser.OtherassignopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_otherassignop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

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
        self.enterRule(localctx, 130, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(MiniGoParser.RETURN)
            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.DEC_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK))) != 0):
                self.state = 638
                self.expr(0)


            self.state = 641
            self.match(MiniGoParser.SEMICO)
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

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

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
        self.enterRule(localctx, 132, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 643
                self.funccall()
                pass

            elif la_ == 2:
                self.state = 644
                self.methodcall()
                pass


            self.state = 647
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

        def firstifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.FirstifstmtContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def elseifstmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElseifstmtlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.firstifstmt()
            self.state = 651
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 650
                self.elseifstmtlist()


            self.state = 653
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirstifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ifstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_firstifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFirstifstmt" ):
                return visitor.visitFirstifstmt(self)
            else:
                return visitor.visitChildren(self)




    def firstifstmt(self):

        localctx = MiniGoParser.FirstifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_firstifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            self.match(MiniGoParser.IF)
            self.state = 656
            self.match(MiniGoParser.LPAREN)
            self.state = 657
            self.expr(0)
            self.state = 658
            self.match(MiniGoParser.RPAREN)
            self.state = 659
            self.ifstmtbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmtbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmtbody" ):
                return visitor.visitIfstmtbody(self)
            else:
                return visitor.visitChildren(self)




    def ifstmtbody(self):

        localctx = MiniGoParser.IfstmtbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_ifstmtbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(MiniGoParser.LBRACE)
            self.state = 662
            self.stmtlist()
            self.state = 663
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifstmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElseifstmtContext,0)


        def elseifstmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.ElseifstmtlistContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseifstmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmtlist" ):
                return visitor.visitElseifstmtlist(self)
            else:
                return visitor.visitChildren(self)




    def elseifstmtlist(self):

        localctx = MiniGoParser.ElseifstmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_elseifstmtlist)
        try:
            self.state = 670
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 665
                self.elseifstmt()
                self.state = 666
                self.elseifstmtlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.elsestmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 669
                self.elseifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ifstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmt" ):
                return visitor.visitElseifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifstmt(self):

        localctx = MiniGoParser.ElseifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_elseifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.match(MiniGoParser.ELSE)
            self.state = 673
            self.match(MiniGoParser.IF)
            self.state = 674
            self.match(MiniGoParser.LPAREN)
            self.state = 675
            self.expr(0)
            self.state = 676
            self.match(MiniGoParser.RPAREN)
            self.state = 677
            self.ifstmtbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ifstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = MiniGoParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(MiniGoParser.ELSE)
            self.state = 680
            self.ifstmtbody()
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

        def basicforstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BasicforstmtContext,0)


        def init_cond_update_forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.Init_cond_update_forstmtContext,0)


        def rangeforstmt(self):
            return self.getTypedRuleContext(MiniGoParser.RangeforstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_forstmt)
        try:
            self.state = 685
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 682
                self.basicforstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 683
                self.init_cond_update_forstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 684
                self.rangeforstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicforstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def forstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtbodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basicforstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicforstmt" ):
                return visitor.visitBasicforstmt(self)
            else:
                return visitor.visitChildren(self)




    def basicforstmt(self):

        localctx = MiniGoParser.BasicforstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_basicforstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.match(MiniGoParser.FOR)
            self.state = 688
            self.expr(0)
            self.state = 689
            self.forstmtbody()
            self.state = 690
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlistContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmtbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmtbody" ):
                return visitor.visitForstmtbody(self)
            else:
                return visitor.visitChildren(self)




    def forstmtbody(self):

        localctx = MiniGoParser.ForstmtbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_forstmtbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self.match(MiniGoParser.LBRACE)
            self.state = 693
            self.stmtlist()
            self.state = 694
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_cond_update_forstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def init_for(self):
            return self.getTypedRuleContext(MiniGoParser.Init_forContext,0)


        def SEMICO(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICO)
            else:
                return self.getToken(MiniGoParser.SEMICO, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def forstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtbodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_cond_update_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_cond_update_forstmt" ):
                return visitor.visitInit_cond_update_forstmt(self)
            else:
                return visitor.visitChildren(self)




    def init_cond_update_forstmt(self):

        localctx = MiniGoParser.Init_cond_update_forstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_init_cond_update_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(MiniGoParser.FOR)
            self.state = 697
            self.init_for()
            self.state = 698
            self.match(MiniGoParser.SEMICO)
            self.state = 699
            self.expr(0)
            self.state = 700
            self.match(MiniGoParser.SEMICO)
            self.state = 701
            self.assign()
            self.state = 702
            self.forstmtbody()
            self.state = 703
            self.match(MiniGoParser.SEMICO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


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
            return MiniGoParser.RULE_init_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for" ):
                return visitor.visitInit_for(self)
            else:
                return visitor.visitChildren(self)




    def init_for(self):

        localctx = MiniGoParser.Init_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_init_for)
        self._la = 0 # Token type
        try:
            self.state = 713
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 705
                self.assign()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 706
                self.match(MiniGoParser.VAR)
                self.state = 707
                self.match(MiniGoParser.ID)
                self.state = 709
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 708
                    self.typedecl()


                self.state = 711
                self.match(MiniGoParser.ASSIGN)
                self.state = 712
                self.expr(0)
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accesslist(self):
            return self.getTypedRuleContext(MiniGoParser.AccesslistContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def otherassignop(self):
            return self.getTypedRuleContext(MiniGoParser.OtherassignopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
            self.accesslist(0)
            self.state = 718
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SHORT_ASSIGN]:
                self.state = 716
                self.match(MiniGoParser.SHORT_ASSIGN)
                pass
            elif token in [MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.state = 717
                self.otherassignop()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 720
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeforstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def forstmtbody(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtbodyContext,0)


        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_rangeforstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeforstmt" ):
                return visitor.visitRangeforstmt(self)
            else:
                return visitor.visitChildren(self)




    def rangeforstmt(self):

        localctx = MiniGoParser.RangeforstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_rangeforstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.match(MiniGoParser.FOR)
            self.state = 723
            self.match(MiniGoParser.ID)
            self.state = 724
            self.match(MiniGoParser.COMMA)
            self.state = 725
            self.match(MiniGoParser.ID)
            self.state = 726
            self.match(MiniGoParser.SHORT_ASSIGN)
            self.state = 727
            self.match(MiniGoParser.RANGE)
            self.state = 728
            self.expr(0)
            self.state = 729
            self.forstmtbody()
            self.state = 730
            self.match(MiniGoParser.SEMICO)
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

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(MiniGoParser.BREAK)
            self.state = 733
            self.match(MiniGoParser.SEMICO)
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

        def SEMICO(self):
            return self.getToken(MiniGoParser.SEMICO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
            self.match(MiniGoParser.CONTINUE)
            self.state = 736
            self.match(MiniGoParser.SEMICO)
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
        self._predicates[42] = self.expr_sempred
        self._predicates[43] = self.expr0_sempred
        self._predicates[44] = self.expr1_sempred
        self._predicates[45] = self.expr2_sempred
        self._predicates[46] = self.expr3_sempred
        self._predicates[48] = self.expr5_sempred
        self._predicates[50] = self.arrdimlist_expr_sempred
        self._predicates[59] = self.methodcallbody_sempred
        self._predicates[63] = self.accesslist_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr0_sempred(self, localctx:Expr0Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

    def arrdimlist_expr_sempred(self, localctx:Arrdimlist_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def methodcallbody_sempred(self, localctx:MethodcallbodyContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 5)
         

    def accesslist_sempred(self, localctx:AccesslistContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         




