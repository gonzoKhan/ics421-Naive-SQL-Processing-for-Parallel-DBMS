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

    print("\nclustercfg contents:\n{")
    for x in clustercfg: print("{}: {}".format(x, clustercfg[x]))
    print("}")
    print("\ncsvfile (unsorted):")
    for x in csvfile: print(x)

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
        print("\nGot conn_list:")
        for conn in conn_list:
            print("\nConnection Info:")
            conn.show()
        try:
            for conn in conn_list:
                conn.establishConnection()
            try:
                for conn in conn_list:
                    conn.loadData()
                try:
                    for conn in conn_list:
                        conn.commit()
                except BaseException as e:
                    print("Error when commiting:")
                    print(str(e))
            except BaseException as e:
                print("Could not load Data:")
                print(str(e))
        except BaseException as e:
            print("Could not establish connection:")
            print(str(e))
    else:
        print("Connection list could not be established.")

# No partitioning method so insert everything into all tables
def noPartitioning(clustercfg, csvfile):
    conn_list = list()
    nodes = getNodeInfo(clustercfg)
    catalog = getCatalogParams(clustercfg)
    for (i, node) in enumerate(nodes):
        if str(node['nodeid']) in clustercfg: # Weeding out extra nodes not in clustercfg
            conn_list.insert(-1, connectionLoader(node, csvfile, catalog) )

    return conn_list

# Range partitioning
def rangePartitioning(clustercfg, csvfile):
    conn_list = list() # For storing connections.
    nodes = getNodeInfo(clustercfg) # For connecting to nodes.
    catalog = getCatalogParams(clustercfg) # For connecting to catalog.
    columns = getColumns(nodes[0]) # For figuring out which column number to range by.
    colnum = None

    # Get column number for sorting
    for (i, column) in enumerate(columns):
        if column == clustercfg['partition']['column']:
            colnum = i

    # sort csvfile
    csvfile = sorted(csvfile, key=lambda x: int(x[colnum]))

    print("\ncsvfile (sorted):") # COMMENT OUT
    for row in csvfile: print(row) # COMMENT OUT
    print("\nCOLUMNS (where column '{}' is in position {}):\n{}".format(clustercfg['partition']['column'], colnum, columns)) # COMMENT OUT


    for (i, node) in enumerate(nodes):
        if str(node['nodeid']) in clustercfg:
            # Get data in range
            print("\nnode{}".format(node['nodeid'])) # COMMENT OUT
            print("Range: {} to {}".format(clustercfg[str(node['nodeid'])]['param1'], clustercfg[str(node['nodeid'])]['param2'])) # COMMENT OUT
            (startrow, endrow) = getRangeSlice(
                                    clustercfg[str(node['nodeid'])]['param1'],
                                    clustercfg[str(node['nodeid'])]['param2'],
                                    colnum, csvfile
                                )
            print("Result ({}:{}) out of (0:{}):".format(startrow, endrow, len(csvfile))) # COMMENT OUT
            for row in csvfile[startrow:endrow]: print(row) # COMMENT OUT
            if startrow is not None and endrow is not None:
                conn_list.insert(-1, connectionLoader(node, csvfile[startrow:endrow], catalog) )
            else:
                return None

    return conn_list

# returns the beginning and ending index for slice for given range.
def getRangeSlice(low, high, colnum, csvfile):
    try:
        startrow = None
        endrow = None
        get_endrow = 0
        if low == '-inf':
            startrow = 0
            get_endrow = 1
        else:
            low = float(low)
        if high == '+inf':
            endrow = len(csvfile) - 1
            get_endrow = -1
        else:
            high = float(high)

        for (i, row) in enumerate(csvfile):
            if startrow is None and float(row[colnum]) >= low:
                # print("{}>={}".format(row[colnum], low)) # COMMENT OUT
                startrow = i
                if get_endrow == 0:
                    get_endrow = 1
            elif get_endrow > 0 and float(row[colnum]) <= high:
                # print("{}<={}".format(row[colnum], high)) # COMMENT OUT
                endrow = i
        endrow = endrow + 1 # to include last element for slice command
        return (startrow, endrow)
    except BaseException as e:
        print("Problem with range parameters:")
        print(str(e))
        return (None, None)

# Hash partitioning
def hashPartitioning(clustercfg, csvfile):
    conn_list = list()
    nodes = getNodeInfo(clustercfg)
    catalog = getCatalogParams(clustercfg)
    candidates, colNumber = catalogCompliance(clustercfg,nodes)
    partparam1 = len(candidates)

    for x in range(partparam1):
        thisPart = candidates[x]['nodeid']
        print(thisPart)
        templist = list()
        for (i,row) in enumerate(csvfile):
            part = ((int(row[colNumber]) % int(partparam1)) +1)
            if thisPart == part:
                templist.insert(-1, row)
        conn_list.insert(-1, connectionLoader(candidates[x], templist, catalog) )

    return conn_list

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
# A check to see that the partition column requested exists in the table, and that the nodes are partitioned for the same type
def catalogCompliance(clustercfg, nodes):
        candidates = list()
        partCol = getColumns(nodes[0])
        colNumber = None
        #Checks every col against the potential range column
        for col in range(len(partCol)):
            if clustercfg['partition']['column'] == partCol[int(col)]:
                colNumber = int(col)
                # Checks candidate nodes for correct partition
                for (i, node) in enumerate(nodes):
                    # if 2 == nodes[i]['partmtd']:
                    candidates.insert(0,nodes[i])
                return candidates , colNumber

        print("The available columns for this table are: {0}. \n {1} is not a column in this table.".format(partCol,clustercfg['partition']['column']))
        return candidates , colNumber

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
