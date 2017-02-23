import sys
from antlr4 import *
from antlr4.InputStream import InputStream

from .CSVGrammar.csvfileParser import csvfileParser
from .CSVGrammar.csvfileListener import csvfileListener

class csvfileLoader(csvfileListener):

    def __init__(self):
        self.csv = list()

    def getCSV(self):
        return self.csv

    # Exit a parse tree produced by csvfileParser#row.
    def exitRow(self, ctx:csvfileParser.RowContext):
        row_elements = list()
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, csvfileParser.ColumnContext):
                row_elements.append(child.getText().strip('"'))

        self.csv.append(tuple(row_elements))
