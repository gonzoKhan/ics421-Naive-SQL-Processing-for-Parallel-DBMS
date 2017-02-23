import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from .MySQLGrammar.MySQLParser import MySQLParser
from .MySQLGrammar.MySQLListener import MySQLListener

class SQLLoader(MySQLListener):

    def __init__(self):
        self.sql = {}

    def getSQL(self):
        return self.sql

    def getStatement(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'select_statementContext':
                return child.getText()
            else:
                print(type(child).__name__)

    def getSelectList(self,ctx):
        for i in range(ctx.getChildCount()):
            # print (i)
            child = ctx.getChild(i)
            if type(ctx.getChild(i)).__name__ == 'Select_listContext':
                return child.getText()

    def getTableName(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'Escape_idContext':
                return child.getText()

    # Enter a parse tree produced by MySQLParser#select_expression.
    def enterSelect_expression(self, ctx:MySQLParser.Select_expressionContext):
        selectList = self.getSelectList(ctx)
        self.sql['select'] = selectList

    # Enter a parse tree produced by MySQLParser#table_name.
    def enterTable_name(self, ctx:MySQLParser.Table_nameContext):
        tablename = self.getTableName(ctx)
        self.sql['tablename'] = tablename
