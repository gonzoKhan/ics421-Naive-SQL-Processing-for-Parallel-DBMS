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

from connectionThread import connectionThread

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
    # print(loader.getCFG())
    numnodes = loader.cfg['numnodes']

    # # Grab the config for the catalog
    c_driver = loader.cfg['catalog']['driver']
    c_hostname = loader.cfg['catalog']['hostname']
    c_username = loader.cfg['catalog']['username']
    c_password = loader.cfg['catalog']['passwd']

    catalog_info = {
        'driver': c_driver,
        'hostname': c_hostname,
        'username': c_username,
        'password': c_password
    }

    #Use antlr4 to parse sqlfile
    sql_input = FileStream(sqlfile)
    sql_lexer = MySQLLexer(sql_input)
    sql_stream = CommonTokenStream(sql_lexer)
    sql_parser = MySQLParser(sql_stream)
    sql_tree = sql_parser.statement()

    sql_loader = SQLLoader()
    walker = ParseTreeWalker()
    walker.walk(sql_loader, sql_tree)
    # print(sql_loader.getSQL())

# List of dictionary objects that will hold the parsed config data.
nodes = [dict() for x in range(int(numnodes))]

for node in range(int(numnodes)):
    nodes[node]['username'] = loader.cfg['catalog']['username']
    nodes[node]['passwd'] = loader.cfg['catalog']['passwd']
    nodes[node]['hostname'] = loader.cfg['catalog']['hostname']
    nodes[node]['driver'] = loader.cfg['catalog']['driver']
    nodes[node]['tablename'] = sql_loader.sql['tablename']
    nodes[node]['database'] = 'node' + str(node+1)

sqlname = sqlfile
sqlopen = open(sqlname, 'r')
sql = sqlopen.read()

# For loop that generates a dictionary object containing the parameters
# for a nodes connection then makes a connectionThread for each node.
threads = list()
try:
    for idnum in range(int(numnodes)):
        config = {
            'user': nodes[idnum]['username'],
            'password': nodes[idnum]['passwd'],
            'host': nodes[idnum]['hostname'],
            'database': 'node' + str(idnum+1)
        }
        threads.insert( -1, connectionThread(idnum+1, config, sql, nodes[idnum]['driver'], catalog_info) )

    # For loop that runs each connectionThread.
    for conn in threads:
        conn.run()
except KeyError as err:
    print('INVALID FORMAT IN CLUSTERCONFIG: Expected ' + str(err))
    print('FAILED TO EXECUTE DDL')
