import sys
import re

import mysql.connector

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.ClusterConfigGrammar.ClusterConfigLexer import ClusterConfigLexer
from lib.ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
from lib.ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener

from lib.CSVGrammar.csvfileLexer import csvfileLexer
from lib.CSVGrammar.csvfileParser import csvfileParser
from lib.CSVGrammar.csvfileListener import csvfileListener

from lib.ClusterConfigLoader import ClusterConfigLoader
from lib.csvfileLoader import csvfileLoader

from connectionLoader import connectionLoader

def main(clustername, csvname):
    # Use antlr4 to parse clustercfg
    cluster_input = FileStream(clustername)
    cluster_lexer = ClusterConfigLexer(cluster_input)
    cluster_stream = CommonTokenStream(cluster_lexer)
    cluster_parser = ClusterConfigParser(cluster_stream)
    cluster_tree = cluster_parser.config()

    cluster_loader = ClusterConfigLoader()
    cluster_walker = ParseTreeWalker()
    cluster_walker.walk(cluster_loader, cluster_tree)
    clustercfg = cluster_loader.getCFG()

    # Use antlr4 to parse csvfile
    csv_input = FileStream(csvname)
    csv_lexer = csvfileLexer(csv_input)
    csv_stream = CommonTokenStream(csv_lexer)
    csv_parser = csvfileParser(csv_stream)
    csv_tree = csv_parser.rows()

    csv_loader = csvfileLoader()
    csv_walker = ParseTreeWalker()
    csv_walker.walk(csv_loader, csv_tree)
    csvfile = csv_loader.getCSV()

    print("clustercfg")
    print(clustercfg)
    print("csvfile")
    print(csvfile)

    # Get partition method and get list of connectionLoaders
    conn_list = None
    if 'partition' in clustercfg and 'method' in clustercfg['partition']:
        partmtd = clustercfg['partition']['method']
        if partmtd == 'notpartition':
            conn_list = noPartitioning(clustercfg, csvfile)
        elif partmtd == 'range':
            conn_list = rangePartitioning(clustercfg, csvfile)
        elif partmtd == 'hash':
            conn_list = hashPartitioning(clustercfg, csvfile)

    if conn_list:
        print("Got conn_list")
        print(conn_list)

# No partitioning method so insert everything into all tables
def noPartitioning(clustercfg, csvfile):
    conn_list = list()
    nodes = getNodeInfo(clustercfg)
    if len(nodes) <= int(clustercfg['numnodes']):
        for (i, node) in enumerate(nodes):
            if str(node['nodeid']) in clustercfg:
                catalog = getCatalogParams(clustercfg)
                conn_list.insert(-1, connectionLoader(node, csvfile, catalog) )

    return conn_list

# Range partitioning
def rangePartitioning(clustercfg, csvfile):
    conn_list = list()
    nodes = getNodeInfo(clustercfg)
    columns = getColumns(nodes[0])
    colnum = None

    # Get column number for sorting
    for (i, column) in enumerate(columns):
        if column == clustercfg['partition']['column']:
            colnum = i
    print(columns)
    print("colnum:{}".format(colnum))

    # sort csvfile
    csvfile = sorted(csvfile, key=lambda x: int(x[colnum]))
    for row in csvfile:
        print(row)

    if columns and len(nodes) <= int(clustercfg['numnodes']):
        for (i, node) in enumerate(nodes):
            if str(node['nodeid']) in clustercfg:
                catalog = getCatalogParams(clustercfg)
                conn_list.insert(-1, connectionLoader(node, csvfile, catalog) )

    return conn_list


# Hash partitioning
def hashPartitioning(clustercfg, csvfile):
    pass

# Takes the clustercfg dictionary and returns a list of dictionaries containing info on each node with the table from clustercfg.
def getNodeInfo(clustercfg):
    catalog_query = (
        "SELECT * "
        "FROM DTABLES "
        "WHERE tname = %s;"
    )

    catalog = getCatalogParams(clustercfg)
    # print("catalog")
    # print(catalog)
    if catalog:
        results = None
        try:
            connection = mysql.connector.connect(**catalog)
            cursor = connection.cursor(dictionary=True)
            # print("catalog_query")
            # print(catalog_query)
            cursor.execute(catalog_query, (clustercfg['tablename'],))
            results = cursor.fetchall()

            # Get a list of dictionaries.
            for row in cursor:
                print(row)
                results.append(row)

        except mysql.connector.Error as err:
            print(err)
        except Error as err:
            print(str(err))
        finally:
            cursor.close()
            connection.close()
        if len(results) > 0:
            return results

    return None

def getCatalogParams(clustercfg):
    try:
        (host, port, database) = parseURL(clustercfg['catalog']['hostname'])
        return  {
                    'host': host,
                    'port': port,
                    'database': database,
                    'user': clustercfg['catalog']['username'],
                    'password': clustercfg['catalog']['passwd']

                }
    except:
        return None

def getColumns(node):
    try:
        user = node['nodeuser']
        passwd = node['nodepasswd']
        (host, port, database) = parseURL(node['nodeurl'])
        conn_params = {
            'user': user,
            'passwd': passwd,
            'host': host,
            'port': port,
            'database': database
        }
        connection = mysql.connector.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM {};".format(node['tname']))
        column_names = [i[0] for i in cursor.description]
        return column_names
    except BaseException as e:
        print(cursor.statement)
        print("Could not get columns in getColumns()")
        print(str(e))
        print("Arg:")
        print(node)
        return None

# Grabs the address, port, and database from the hostname url.
def parseURL(url):
    hostmatch = re.search('^.*//([\.\d]+):(\d+)/(.*)$', url, flags=re.IGNORECASE)
    if hostmatch and len(hostmatch.groups()) == 3:
        return hostmatch.groups()
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'clustercfg'
    if len(sys.argv) > 2:
        csvname = sys.argv[2]
    else:
        csvname = 'csvfile'

    main(clustername, csvname)
