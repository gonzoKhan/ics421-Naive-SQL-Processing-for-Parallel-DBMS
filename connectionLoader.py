import mysql.connector

# Connects to given node and inserts data into it and then updates catalog.
# First call establishConnection() and then loadData(). Finally call commit() or rollback()
class connectionLoader():
    # nodeinfo: dictionary of result for this node from dtables.
    # data: list of tuples where each row of csvfile is a tuple containing the separate columns.
    # catalog_params: dictionary used as parameters for catalog connection.
    # nodeparams: dictionary used as parameters for node connection.
    def __init__(self, nodeinfo, data, catalog_params):
        self.nodeinfo = nodeinfo
        self.data = data
        self.catalog_params = catalog_params
        self.nodeparams = self.__getNodeParams()
        self.connection = None
        self.cursor = None

    # Function for updating params if needed.
    def updateNodeParams(self):
        self.nodeparams = self.__getNodeParams()

    # Makes a connection with the node.
    def establishConnection(self):
        try:
            self.connection = mysql.connector.connect(**self.nodeparams)
        except mysql.connector.Error as err:
            print("ERROR: Connecting with node{}:\nnodeinfo:\n".format(nodeinfo['nodeid'], nodeinfo))
            print(err)
        except Error as err:
            print("ERROR: Connecting with node{}:\nnodeinfo:\n".format(nodeinfo['nodeid'], nodeinfo))
            print(str(err))

    # Must be called after establishConnection. It inserts the data into the database for the connection.
    def loadData(self):
        if self.connection:
            try:
                self.cursor = self.connection.cursor()
                self.cursor.execute("SELECT * FROM %s", (nodeinfo['tablename']))
                fieldnames = [for i[0] in self.cursor.description]
                insert_statement = "INSERT INTO %(table)s ("

                # Add in column names
                for col in fieldnames:
                    insert_statement.append(col + ", ")
                insert_statement.rstrip(',')
                insert_statement.append(") VALUES (")
                for i in fieldnames:
                    insert_statement.append("%s, ")
                insert_statement.rstrip(',')
                insert_statement.append(")")

                print("insert_statement:\n{}".format(insert_statement))

                self.cursor.executemany(insert_statement, self.data)


    # returns dictionary of params for connection to node
    # nodeparams returned: user, passwd, host, port, database
    def __getNodeParams(self):
        try:
            user = self.nodeinfo['nodeuser']
            passwd = self.nodeinfo['nodepasswd']
            (host, port, database) = self.__parseURL(nodeinfo['nodeurl'])

            return {
                'user': user,
                'passwd': passwd,
                'host': host,
                'port': port,
                'database': database
            }
        except:
            return None


    # Grabs the host, port, and database from the hostname url.
    def __parseURL(url):
        hostmatch = re.search('^.*//([\.\d]+):(\d+)/(.*)$', url, flags=re.IGNORECASE)
        if hostmatch and len(hostmatch.groups()) == 3:
            return hostmatch.groups()
        else:
            return None
