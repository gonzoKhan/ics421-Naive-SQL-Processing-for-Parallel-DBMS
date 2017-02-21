import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from .ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
from .ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener

class ClusterConfigLoader(ClusterConfigListener):

    def __init__(self):
        self.cfg = {}

    def getCFG(self):
        return self.cfg

    def getKey(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'KeyContext':
                return child.getText()

    def getValue(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'ValueContext':
                return child.getText()

    # Exit a parse tree produced by ClusterConfigParser#catalog_info.
    def exitCatalog_info(self, ctx:ClusterConfigParser.Catalog_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        self.cfg['catalog', key] = value

    # Exit a parse tree produced by ClusterConfigParser#node_info.
    def exitNode_info(self, ctx:ClusterConfigParser.Node_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'NodeidContext':
                nodeid = child.getText()

        self.cfg[nodeid, key] = value

    # Exit a parse tree produced by ClusterConfigParser#partition_info.
    def exitPartition_info(self, ctx:ClusterConfigParser.Partition_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        self.cfg['partition', key] = value

    # Exit a parse tree produced by ClusterConfigParser#numnodes.
    def exitNumnodes(self, ctx:ClusterConfigParser.NumnodesContext):
        pass

    # Exit a parse tree produced by ClusterConfigParser#tablename.
    def exitTablename(self, ctx:ClusterConfigParser.TablenameContext):
        pass
