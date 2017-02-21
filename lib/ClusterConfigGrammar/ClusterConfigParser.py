# Generated from ClusterConfig.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\6\7;\n\7\r\7\16\7<\3\b\3\b\3\b\3")
        buf.write("\b\3\t\6\tD\n\t\r\t\16\tE\3\n\6\nI\n\n\r\n\16\nJ\3\13")
        buf.write("\6\13N\n\13\r\13\16\13O\3\13\2\2\f\2\4\6\b\n\f\16\20\22")
        buf.write("\24\2\4\3\2\f\r\4\2\b\t\13\rP\2\27\3\2\2\2\4 \3\2\2\2")
        buf.write("\6\"\3\2\2\2\b(\3\2\2\2\n\61\3\2\2\2\f\67\3\2\2\2\16>")
        buf.write("\3\2\2\2\20C\3\2\2\2\22H\3\2\2\2\24M\3\2\2\2\26\30\5\4")
        buf.write("\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3")
        buf.write("\2\2\2\32\3\3\2\2\2\33!\5\6\4\2\34!\5\b\5\2\35!\5\n\6")
        buf.write("\2\36!\5\f\7\2\37!\5\16\b\2 \33\3\2\2\2 \34\3\2\2\2 \35")
        buf.write("\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\5\3\2\2\2\"#\7\3\2\2")
        buf.write("#$\7\13\2\2$%\5\22\n\2%&\7\n\2\2&\'\5\24\13\2\'\7\3\2")
        buf.write("\2\2()\7\4\2\2)*\7\13\2\2*+\7\5\2\2+,\5\20\t\2,-\7\13")
        buf.write("\2\2-.\5\22\n\2./\7\n\2\2/\60\5\24\13\2\60\t\3\2\2\2\61")
        buf.write("\62\7\4\2\2\62\63\7\13\2\2\63\64\5\22\n\2\64\65\7\n\2")
        buf.write("\2\65\66\5\24\13\2\66\13\3\2\2\2\678\7\6\2\28:\7\n\2\2")
        buf.write("9;\7\f\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\r")
        buf.write("\3\2\2\2>?\7\7\2\2?@\7\n\2\2@A\5\22\n\2A\17\3\2\2\2BD")
        buf.write("\7\f\2\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\21\3")
        buf.write("\2\2\2GI\t\2\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2")
        buf.write("\2K\23\3\2\2\2LN\t\3\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2")
        buf.write("OP\3\2\2\2P\25\3\2\2\2\b\31 <EJO")
        return buf.getvalue()


class ClusterConfigParser ( Parser ):

    grammarFileName = "ClusterConfig.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'catalog'", "'partition'", "'node'", 
                     "'numnodes'", "'tablename'", "':'", "'/'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COLON", "SLASH", "EQUALS", 
                      "DOT", "NUM", "CHARS", "WS" ]

    RULE_config = 0
    RULE_stat = 1
    RULE_catalog_info = 2
    RULE_node_info = 3
    RULE_partition_info = 4
    RULE_numnodes = 5
    RULE_tablename = 6
    RULE_nodeid = 7
    RULE_key = 8
    RULE_value = 9

    ruleNames =  [ "config", "stat", "catalog_info", "node_info", "partition_info", 
                   "numnodes", "tablename", "nodeid", "key", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    COLON=6
    SLASH=7
    EQUALS=8
    DOT=9
    NUM=10
    CHARS=11
    WS=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ConfigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterConfigParser.StatContext)
            else:
                return self.getTypedRuleContext(ClusterConfigParser.StatContext,i)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)




    def config(self):

        localctx = ClusterConfigParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.stat()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.T__0) | (1 << ClusterConfigParser.T__1) | (1 << ClusterConfigParser.T__3) | (1 << ClusterConfigParser.T__4))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catalog_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Catalog_infoContext,0)


        def node_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Node_infoContext,0)


        def partition_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Partition_infoContext,0)


        def numnodes(self):
            return self.getTypedRuleContext(ClusterConfigParser.NumnodesContext,0)


        def tablename(self):
            return self.getTypedRuleContext(ClusterConfigParser.TablenameContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = ClusterConfigParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.catalog_info()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.node_info()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.partition_info()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.numnodes()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.tablename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catalog_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_catalog_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatalog_info" ):
                listener.enterCatalog_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatalog_info" ):
                listener.exitCatalog_info(self)




    def catalog_info(self):

        localctx = ClusterConfigParser.Catalog_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_catalog_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ClusterConfigParser.T__0)
            self.state = 33
            self.match(ClusterConfigParser.DOT)
            self.state = 34
            self.key()
            self.state = 35
            self.match(ClusterConfigParser.EQUALS)
            self.state = 36
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.DOT)
            else:
                return self.getToken(ClusterConfigParser.DOT, i)

        def nodeid(self):
            return self.getTypedRuleContext(ClusterConfigParser.NodeidContext,0)


        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_node_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_info" ):
                listener.enterNode_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_info" ):
                listener.exitNode_info(self)




    def node_info(self):

        localctx = ClusterConfigParser.Node_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ClusterConfigParser.T__1)
            self.state = 39
            self.match(ClusterConfigParser.DOT)
            self.state = 40
            self.match(ClusterConfigParser.T__2)
            self.state = 41
            self.nodeid()
            self.state = 42
            self.match(ClusterConfigParser.DOT)
            self.state = 43
            self.key()
            self.state = 44
            self.match(ClusterConfigParser.EQUALS)
            self.state = 45
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Partition_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_partition_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartition_info" ):
                listener.enterPartition_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartition_info" ):
                listener.exitPartition_info(self)




    def partition_info(self):

        localctx = ClusterConfigParser.Partition_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_partition_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ClusterConfigParser.T__1)
            self.state = 48
            self.match(ClusterConfigParser.DOT)
            self.state = 49
            self.key()
            self.state = 50
            self.match(ClusterConfigParser.EQUALS)
            self.state = 51
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumnodesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_numnodes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumnodes" ):
                listener.enterNumnodes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumnodes" ):
                listener.exitNumnodes(self)




    def numnodes(self):

        localctx = ClusterConfigParser.NumnodesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numnodes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ClusterConfigParser.T__3)
            self.state = 54
            self.match(ClusterConfigParser.EQUALS)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.match(ClusterConfigParser.NUM)
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TablenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_tablename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTablename" ):
                listener.enterTablename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTablename" ):
                listener.exitTablename(self)




    def tablename(self):

        localctx = ClusterConfigParser.TablenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tablename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ClusterConfigParser.T__4)
            self.state = 61
            self.match(ClusterConfigParser.EQUALS)
            self.state = 62
            self.key()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NodeidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_nodeid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeid" ):
                listener.enterNodeid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeid" ):
                listener.exitNodeid(self)




    def nodeid(self):

        localctx = ClusterConfigParser.NodeidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nodeid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.match(ClusterConfigParser.NUM)
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.CHARS)
            else:
                return self.getToken(ClusterConfigParser.CHARS, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ClusterConfigParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==ClusterConfigParser.NUM or _la==ClusterConfigParser.CHARS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM or _la==ClusterConfigParser.CHARS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.CHARS)
            else:
                return self.getToken(ClusterConfigParser.CHARS, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.DOT)
            else:
                return self.getToken(ClusterConfigParser.DOT, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.SLASH)
            else:
                return self.getToken(ClusterConfigParser.SLASH, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.COLON)
            else:
                return self.getToken(ClusterConfigParser.COLON, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ClusterConfigParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.COLON) | (1 << ClusterConfigParser.SLASH) | (1 << ClusterConfigParser.DOT) | (1 << ClusterConfigParser.NUM) | (1 << ClusterConfigParser.CHARS))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.COLON) | (1 << ClusterConfigParser.SLASH) | (1 << ClusterConfigParser.DOT) | (1 << ClusterConfigParser.NUM) | (1 << ClusterConfigParser.CHARS))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





