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

    # def getStatement(self,ctx):
    #     for i in range(ctx.getChildCount()):
    #         child = ctx.getChild(i)
    #         if type(child).__name__ == 'Select_expressionContext':
    #             return child.getText()
    #         else:
    #             print(type(child).__name__)

    def getTableName(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'Escape_idContext':
                return child.getText()

    # # Enter a parse tree produced by MySQLParser#select_statement.
    # def enterSelect_statement(self, ctx:MySQLParser.Select_statementContext):
    #     statement = self.getStatement(ctx)
    #     self.sql['query'] = statement

    # Enter a parse tree produced by MySQLParser#table_name.
    def enterTable_name(self, ctx:MySQLParser.Table_nameContext):
        tablename = self.getTableName(ctx)
        self.sql['tablename'] = tablename
