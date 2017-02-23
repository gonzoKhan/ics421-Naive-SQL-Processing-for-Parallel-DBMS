# Generated from ClusterConfig.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\17")
        buf.write("b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\6\fS\n\f\r\f\16\fT\3\r\6\rX\n\r\r\r\16\rY\3\16\6")
        buf.write("\16]\n\16\r\16\16\16^\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4")
        buf.write("\4\2C\\c|\5\2\13\f\17\17\"\"d\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5%\3\2\2")
        buf.write("\2\7/\3\2\2\2\t\64\3\2\2\2\13=\3\2\2\2\rG\3\2\2\2\17I")
        buf.write("\3\2\2\2\21K\3\2\2\2\23M\3\2\2\2\25O\3\2\2\2\27R\3\2\2")
        buf.write("\2\31W\3\2\2\2\33\\\3\2\2\2\35\36\7e\2\2\36\37\7c\2\2")
        buf.write("\37 \7v\2\2 !\7c\2\2!\"\7n\2\2\"#\7q\2\2#$\7i\2\2$\4\3")
        buf.write("\2\2\2%&\7r\2\2&\'\7c\2\2\'(\7t\2\2()\7v\2\2)*\7k\2\2")
        buf.write("*+\7v\2\2+,\7k\2\2,-\7q\2\2-.\7p\2\2.\6\3\2\2\2/\60\7")
        buf.write("p\2\2\60\61\7q\2\2\61\62\7f\2\2\62\63\7g\2\2\63\b\3\2")
        buf.write("\2\2\64\65\7p\2\2\65\66\7w\2\2\66\67\7o\2\2\678\7p\2\2")
        buf.write("89\7q\2\29:\7f\2\2:;\7g\2\2;<\7u\2\2<\n\3\2\2\2=>\7v\2")
        buf.write("\2>?\7c\2\2?@\7d\2\2@A\7n\2\2AB\7g\2\2BC\7p\2\2CD\7c\2")
        buf.write("\2DE\7o\2\2EF\7g\2\2F\f\3\2\2\2GH\7<\2\2H\16\3\2\2\2I")
        buf.write("J\7\61\2\2J\20\3\2\2\2KL\7?\2\2L\22\3\2\2\2MN\7\60\2\2")
        buf.write("N\24\3\2\2\2OP\7a\2\2P\26\3\2\2\2QS\4\62;\2RQ\3\2\2\2")
        buf.write("ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\30\3\2\2\2VX\t\2\2\2W")
        buf.write("V\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\32\3\2\2\2[]")
        buf.write("\t\3\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_`\3")
        buf.write("\2\2\2`a\b\16\2\2a\34\3\2\2\2\6\2TY^\3\b\2\2")
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
    NUM = 11
    CHARS = 12
    WS = 13

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'catalog'", "'partition'", "'node'", "'numnodes'", "'tablename'", 
            "':'", "'/'", "'='", "'.'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "SLASH", "EQUALS", "DOT", "UNDERSCORE", "NUM", "CHARS", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "COLON", "SLASH", 
                  "EQUALS", "DOT", "UNDERSCORE", "NUM", "CHARS", "WS" ]

    grammarFileName = "ClusterConfig.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


