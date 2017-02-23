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

    # Get partition method and then proceed
    if 'partition' in clustercfg and 'method' in clustercfg['partition']:
        partmtd = clustercfg['partition']['method']
        if partmtd == 'notpartition':
            noPartitioning(clustercfg, csvfile)
        elif partmtd == 'range':
            rangePartitioning(clustercfg, csvfile)
        elif partmtd == 'hash':
            hashPartitioning(clustercfg, csvfile)

# No partitioning method so insert everything into all tables
def noPartitioning(clustercfg, csvfile):
    print("Not Partitioned:")
    print(clustercfg)
    print(csvfile)

    nodeinfo = getNodeInfo(clustercfg)
    print(nodeinfo)
    connection_list = connectionLoader(nodeinfo, csvfile, getCatalogParams(clustercfg))
    if nodeinfo and clustercfg['numnodes'] == len(nodeinfo):
        pass
    else:
        print("Error in unpartitioned csv loading. \nnodeinfo_length={}\nnodeinfo={}\nnumnodes={}".format(len(nodeinfo), nodeinfo, clustercfg['numnodes']))

# Range partitioning
def rangePartitioning(clustercfg, csvfile):
    print("Range Partitioned:")
    print("clustercfg")
    print(clustercfg)
    print("csvfile")
    print(csvfile)
    nodeinfo = getNodeInfo(clustercfg)
    print("nodeinfo")
    print(nodeinfo)

# Hash partitioning
def hashPartitioning(clustercfg, csvfile):
    print("Hash Partitioned:")
    print("clustercfg")
    print(clustercfg)
    print("csvfile")
    print(csvfile)

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
