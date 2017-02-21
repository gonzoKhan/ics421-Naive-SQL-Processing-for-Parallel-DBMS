# Generated from ClusterConfig.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13O\n\13\r\13")
        buf.write("\16\13P\3\f\6\fT\n\f\r\f\16\fU\3\r\6\rY\n\r\r\r\16\rZ")
        buf.write("\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"")
        buf.write("`\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2")
        buf.write("\2\2\5#\3\2\2\2\7-\3\2\2\2\t\62\3\2\2\2\13;\3\2\2\2\r")
        buf.write("E\3\2\2\2\17G\3\2\2\2\21I\3\2\2\2\23K\3\2\2\2\25N\3\2")
        buf.write("\2\2\27S\3\2\2\2\31X\3\2\2\2\33\34\7e\2\2\34\35\7c\2\2")
        buf.write("\35\36\7v\2\2\36\37\7c\2\2\37 \7n\2\2 !\7q\2\2!\"\7i\2")
        buf.write("\2\"\4\3\2\2\2#$\7r\2\2$%\7c\2\2%&\7t\2\2&\'\7v\2\2\'")
        buf.write("(\7k\2\2()\7v\2\2)*\7k\2\2*+\7q\2\2+,\7p\2\2,\6\3\2\2")
        buf.write("\2-.\7p\2\2./\7q\2\2/\60\7f\2\2\60\61\7g\2\2\61\b\3\2")
        buf.write("\2\2\62\63\7p\2\2\63\64\7w\2\2\64\65\7o\2\2\65\66\7p\2")
        buf.write("\2\66\67\7q\2\2\678\7f\2\289\7g\2\29:\7u\2\2:\n\3\2\2")
        buf.write("\2;<\7v\2\2<=\7c\2\2=>\7d\2\2>?\7n\2\2?@\7g\2\2@A\7p\2")
        buf.write("\2AB\7c\2\2BC\7o\2\2CD\7g\2\2D\f\3\2\2\2EF\7<\2\2F\16")
        buf.write("\3\2\2\2GH\7\61\2\2H\20\3\2\2\2IJ\7?\2\2J\22\3\2\2\2K")
        buf.write("L\7\60\2\2L\24\3\2\2\2MO\4\62;\2NM\3\2\2\2OP\3\2\2\2P")
        buf.write("N\3\2\2\2PQ\3\2\2\2Q\26\3\2\2\2RT\t\2\2\2SR\3\2\2\2TU")
        buf.write("\3\2\2\2US\3\2\2\2UV\3\2\2\2V\30\3\2\2\2WY\t\3\2\2XW\3")
        buf.write("\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\b\r")
        buf.write("\2\2]\32\3\2\2\2\6\2PUZ\3\b\2\2")
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
    NUM = 10
    CHARS = 11
    WS = 12

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'catalog'", "'partition'", "'node'", "'numnodes'", "'tablename'", 
            "':'", "'/'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "COLON", "SLASH", "EQUALS", "DOT", "NUM", "CHARS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "COLON", "SLASH", 
                  "EQUALS", "DOT", "NUM", "CHARS", "WS" ]

    grammarFileName = "ClusterConfig.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


