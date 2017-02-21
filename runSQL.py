import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from lib.ClusterConfigGrammar.ClusterConfigLexer import ClusterConfigLexer
from lib.ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
from lib.ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener
from lib.ClusterConfigLoader import ClusterConfigLoader

from lib.MySQLGrammar.MySQLLexer import MySQLLexer
from lib.MySQLGrammar.MySQLListener import MySQLListener
from lib.MySQLGrammar.MySQLParser import MySQLParser
from lib.SQLLoader import SQLLoader

if __name__ == '__main__':
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'clustercfg'
    if len(sys.argv) > 2:
        sqlfile = sys.argv[2]
    else:
        sqlfile = 'sqlfile'

    # Use antlr4 to parse clustercfg
    cluster_input = FileStream(clustername)
    cluster_lexer = ClusterConfigLexer(cluster_input)
    cluster_stream = CommonTokenStream(cluster_lexer)
    cluster_parser = ClusterConfigParser(cluster_stream)
    cluster_tree = cluster_parser.config()

    loader = ClusterConfigLoader()
    walker = ParseTreeWalker()
    walker.walk(loader, cluster_tree)
    print(loader.getCFG())

    #Use antlr4 to parse sqlfile
    sql_input = FileStream(sqlfile)
    sql_lexer = MySQLLexer(sql_input)
    sql_stream = CommonTokenStream(sql_lexer)
    sql_parser = MySQLParser(sql_stream)
    sql_tree = sql_parser.statement()

    sql_loader = SQLLoader()
    walker = ParseTreeWalker()
    walker.walk(sql_loader, sql_tree)
    print(sql_loader.getSQL())
