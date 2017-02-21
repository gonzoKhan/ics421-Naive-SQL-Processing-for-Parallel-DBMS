import sys

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
            notPartitioned(clustercfg)
        elif partmtd == 'range':
            rangePartitioned(clustercfg)
        elif partmtd == 'hash':
            hashPartitioned(clustercfg)

def notPartitioned(clustercfg):
    print("Not Partitioned:")
    print(clustercfg)

def rangePartitioned(clustercfg):
    print("Range Partitioned:")
    print(clustercfg)

def hashPartitioned(clustercfg):
    print("Hash Partitioned:")
    print(clustercfg)

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
