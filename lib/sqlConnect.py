import threading
import mysql.connector
import re

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQLGrammar.MySQLLexer import MySQLLexer
from lib.MySQLGrammar.MySQLListener import MySQLListener
from lib.MySQLGrammar.MySQLParser import MySQLParser
from lib.SQLLoader import SQLLoader


# Allows multithreading when creating a connection to database and executing a ddl.
class SQLconnectionThread (threading.Thread):
    def __init__(self, threadID, config, sql, driver, catalog_info):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.config = config
        self.sqlfile = sql
        self.driver = driver
        self.catalog_info = catalog_info
        self.toSQL = ""

    # Parses and runs the sqlfile
    def __selectStatement(self):

        #Use antlr4 to parse sqlfile
        sql_input = FileStream(self.sqlfile)
        sql_lexer = MySQLLexer(sql_input)
        sql_stream = CommonTokenStream(sql_lexer)
        sql_parser = MySQLParser(sql_stream)
        sql_tree = sql_parser.statement()

        sql_loader = SQLLoader()
        walker = ParseTreeWalker()
        walker.walk(sql_loader, sql_tree)

        # print(sql_loader.getSQL())

        simpleSelect = ("SELECT {0} FROM {1}; ")
        # simpleSelect = ("SELECT * FROM Books;")

        self.toSQL = simpleSelect.format(sql_loader.sql['select'], sql_loader.sql['tablename'])

    def run(self):
        try:
            self.__selectStatement()
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            cursor.execute(self.toSQL)
            results = cursor.fetchall()
            print(results)
            cursor.close()
            connection.close()


            print("SUCCESS: THREAD{0} (database={1},hostname={2}): Sucessfully executed SQL".format(self.threadID, self.config['database'], self.config['host']))

        except mysql.connector.Error as err:
            print("FAILURE: THREAD{0} (database={1},hostname={2}): ".format(self.threadID, self.config['database'], self.config['host']) + err.msg)
