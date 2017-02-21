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
            if isinstance(child, ClusterConfigParser.KeyContext):
                return child.getText()

    def getValue(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ClusterConfigParser.ValueContext):
                return child.getText()

    # Exit a parse tree produced by ClusterConfigParser#catalog_info.
    def exitCatalog_info(self, ctx:ClusterConfigParser.Catalog_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)

        if 'catalog' not in self.cfg:
            self.cfg['catalog'] = dict()
        self.cfg['catalog'][key] = value

    # Exit a parse tree produced by ClusterConfigParser#node_info.
    def exitNode_info(self, ctx:ClusterConfigParser.Node_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ClusterConfigParser.NodeidContext):
                nodeid = child.getText()
        if nodeid not in self.cfg:
            self.cfg[nodeid] = dict()
        self.cfg[nodeid][key] = value

    # Exit a parse tree produced by ClusterConfigParser#partition_info.
    def exitPartition_info(self, ctx:ClusterConfigParser.Partition_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        if 'partition' not in self.cfg:
            self.cfg['partition'] = dict()
        self.cfg['partition'][key] = value

    # Exit a parse tree produced by ClusterConfigParser#numnodes.
    def exitNumnodes(self, ctx:ClusterConfigParser.NumnodesContext):
        self.cfg['numnodes'] = ctx.getChild(2).getText()

    # Exit a parse tree produced by ClusterConfigParser#tablename.
    def exitTablename(self, ctx:ClusterConfigParser.TablenameContext):
        self.cfg['tablename'] = ctx.getChild(2).getText()
