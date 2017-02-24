# Generated from ClusterConfig.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\21")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16[\n\16\r")
        buf.write("\16\16\16\\\3\17\6\17`\n\17\r\17\16\17a\3\20\6\20e\n\20")
        buf.write("\r\20\16\20f\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2")
        buf.write("\4\4\2C\\c|\5\2\13\f\17\17\"\"l\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\3!\3\2\2\2\5)\3\2\2\2\7\63\3\2\2\2\t8\3\2\2\2\13")
        buf.write("A\3\2\2\2\rK\3\2\2\2\17M\3\2\2\2\21O\3\2\2\2\23Q\3\2\2")
        buf.write("\2\25S\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33Z\3\2\2\2\35")
        buf.write("_\3\2\2\2\37d\3\2\2\2!\"\7e\2\2\"#\7c\2\2#$\7v\2\2$%\7")
        buf.write("c\2\2%&\7n\2\2&\'\7q\2\2\'(\7i\2\2(\4\3\2\2\2)*\7r\2\2")
        buf.write("*+\7c\2\2+,\7t\2\2,-\7v\2\2-.\7k\2\2./\7v\2\2/\60\7k\2")
        buf.write("\2\60\61\7q\2\2\61\62\7p\2\2\62\6\3\2\2\2\63\64\7p\2\2")
        buf.write("\64\65\7q\2\2\65\66\7f\2\2\66\67\7g\2\2\67\b\3\2\2\28")
        buf.write("9\7p\2\29:\7w\2\2:;\7o\2\2;<\7p\2\2<=\7q\2\2=>\7f\2\2")
        buf.write(">?\7g\2\2?@\7u\2\2@\n\3\2\2\2AB\7v\2\2BC\7c\2\2CD\7d\2")
        buf.write("\2DE\7n\2\2EF\7g\2\2FG\7p\2\2GH\7c\2\2HI\7o\2\2IJ\7g\2")
        buf.write("\2J\f\3\2\2\2KL\7<\2\2L\16\3\2\2\2MN\7\61\2\2N\20\3\2")
        buf.write("\2\2OP\7?\2\2P\22\3\2\2\2QR\7\60\2\2R\24\3\2\2\2ST\7a")
        buf.write("\2\2T\26\3\2\2\2UV\7-\2\2V\30\3\2\2\2WX\7/\2\2X\32\3\2")
        buf.write("\2\2Y[\4\62;\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2")
        buf.write("\2\2]\34\3\2\2\2^`\t\2\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2")
        buf.write("\2ab\3\2\2\2b\36\3\2\2\2ce\t\3\2\2dc\3\2\2\2ef\3\2\2\2")
        buf.write("fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\b\20\2\2i \3\2\2\2\6")
        buf.write("\2\\af\3\b\2\2")
        return buf.getvalue()


class ClusterConfigLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    COLON = 6
    SLASH = 7
    EQUALS = 8
    DOT = 9
    UNDERSCORE = 10
    PLUS = 11
    MINUS = 12
    NUM = 13
    CHARS = 14
    WS = 15

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'catalog'", "'partition'", "'node'", "'numnodes'", "'tablename'", 
            "':'", "'/'", "'='", "'.'", "'_'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "SLASH", "EQUALS", "DOT", "UNDERSCORE", "PLUS", "MINUS", 
            "NUM", "CHARS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "COLON", "SLASH", 
                  "EQUALS", "DOT", "UNDERSCORE", "PLUS", "MINUS", "NUM", 
                  "CHARS", "WS" ]

    grammarFileName = "ClusterConfig.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


