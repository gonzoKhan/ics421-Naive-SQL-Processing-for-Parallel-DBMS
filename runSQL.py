import sys
import re
import mysql.connector

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

from lib.sqlConnect import SQLconnectionThread
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

    hostinfo = re.search('^.*//([\.\d]+):(\d+)/(.*)$', loader.cfg['catalog']['hostname'], flags=re.IGNORECASE)

    # # Grab the config for the catalog
    c_driver = loader.cfg['catalog']['driver']
    c_hostname = hostinfo.group(1)
    c_username = loader.cfg['catalog']['username']
    c_password = loader.cfg['catalog']['passwd']

    catalog_info = {
        'driver': c_driver,
        'hostname': c_hostname,
        'username': c_username,
        'password': c_password
    }

    catalog_config = {
        'user': c_username,
        'password':c_password,
        'host': hostinfo.group(1),
        'port': hostinfo.group(2),
        'database': hostinfo.group(3),
    }
    # print(catalog_config)

    nodelist = dict()

    nodesQuery = ("SELECT nodeid, nodeuser, nodepasswd, nodeurl, nodedriver FROM DTABLES WHERE tname = "'"{0}"'";")

    # print (nodesQuery.format(sql_loader.sql['tablename']))
    catalog = mysql.connector.connect(**catalog_config)
    crsr = catalog.cursor()
    crsr.execute(nodesQuery.format(sql_loader.sql['tablename']))
    nodelist = crsr.fetchall()
    numnodes = len(nodelist)

    # print (catalog_info)

# For loop that generates a dictionary object containing the parameters
# for a nodes connection then makes a connectionThread for each node.

threads = list()

try:
    for x in range(numnodes):
        nid, user, password, url, driver = nodelist[x]
        nodehost = re.search('^.*//([\.\d]+):(\d+)/(.*)$', url, flags=re.IGNORECASE)
        nodeconfig = {
            'user': user,
            'password': password,
            'host': nodehost.group(1),
            'port': nodehost.group(2),
            'database': nodehost.group(3)
        }
        # print(nodeconfig)
        threads.insert( -1, SQLconnectionThread(nid, nodeconfig, sqlfile, driver, catalog_info) )

    # For loop that runs each connectionThread.
    for conn in threads:
        conn.run()

except KeyError as err:
    print('INVALID FORMAT IN CLUSTERCONFIG: Expected ' + str(err))
    print('FAILED TO EXECUTE DDL')
