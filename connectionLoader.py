import mysql.connector
import re

# Connects to given node and inserts data into it and then updates catalog.
# First call establishConnection() and then loadData(). Finally call commit() or rollback()
class connectionLoader(object):
    # nodeinfo: dictionary of result for this node from dtables.
    # data: list of tuples where each row of csvfile is a tuple containing the separate columns.
    # catalog_params: dictionary used as parameters for catalog connection.
    # nodeparams: dictionary used as parameters for node connection.
    def __init__(self, nodeinfo, data, clustercfg):
        self.nodeinfo = nodeinfo
        self.data = data
        self.clustercfg = clustercfg
        self.catalog_params = self.__getCatalogParams()
        self.nodeparams = self.__getNodeParams()
        self.connection = None
        self.cursor = None

    # Function for updating params if needed.
    def updateNodeParams(self):
        self.nodeparams = self.__getNodeParams()

    def show(self):
        print("NODEINFO:")
        print(self.nodeinfo)
        print("CATALOG PARAMETERS:")
        print(self.catalog_params)
        print("DATA:")
        for x in self.data: print(x)

    # Makes a connection with the node.
    def establishConnection(self):
        try:
            self.connection = mysql.connector.connect(**self.nodeparams)
            # print("Established connection:") # COMMENT OUT
            # print(self.nodeparams) # COMMENT OUT
        except mysql.connector.Error as err:
            print("ERROR: Connecting with node{}:\nnodeinfo: {}\n".format(self.nodeinfo['nodeid'], self.nodeinfo))
            print(err)
        except BaseException as e:
            print("ERROR: Connecting with node{}:\nnodeinfo: {}\n".format(self.nodeinfo['nodeid'], self.nodeinfo))
            print(str(e))

    # Must be called after establishConnection. It inserts the data into the database for the connection.
    def loadData(self):
        if self.connection:
            try:
                self.cursor = self.connection.cursor(buffered=True)
                self.cursor.execute("SELECT * FROM {};".format(self.nodeinfo['tname']))
                fieldnames = [i[0] for i in self.cursor.description]
                insert_statement = "INSERT INTO {} (".format(self.nodeinfo['tname'])

                # Add in column names
                for col in fieldnames:
                    insert_statement += col + ", "
                insert_statement = insert_statement[:-2]
                insert_statement += ") VALUES ("
                for i in fieldnames:
                    insert_statement += "%s, "
                insert_statement = insert_statement[:-2]
                insert_statement += ")"

                # print("insert_statement:\n{}".format(insert_statement)) # COMMENT OUT
                # print(self.data) # COMMENT OUT

                self.cursor.executemany(insert_statement, self.data)
            except mysql.connector.Error as err:
                print("ERROR: Loading with node{}:\nnodeinfo: {}\n".format(self.nodeinfo['nodeid'], self.nodeinfo))
                print(err)
            except BaseException as e:
                print("Failed to load data:")
                print(str(e))
        else:
            raise Exception("Connection not established before attempting to load data.")

    def commit(self):
        self.connection.commit()

        update_catalog = (
            "UPDATE DTABLES "
            "SET partmtd=%s, "
            "partcol=%s, "
            "partparam1=%s, "
            "partparam2=%s "
            "WHERE tname=%s AND nodeid=%s;"
        )

        results = None
        try:
            connection = mysql.connector.connect(**self.catalog_params)
            cursor = connection.cursor()

            node = self.clustercfg[str(self.nodeinfo['nodeid'])]
            partitioning = self.clustercfg['partition']
            if partitioning['method'] == 'range':
                method = 1;
            elif partitioning['method'] == 'hash':
                method = 2;
            else:
                method = 0
            cursor.execute(
                            update_catalog,
                            (method, partitioning['column'], node['param1'],
                            node['param2'], self.nodeinfo['tname'], self.nodeinfo['nodeid'])
                        )
            connection.commit()

        except mysql.connector.Error as err:
            print(err)
        except BaseException as err:
            print(str(err))
        finally:
            cursor.close()
            connection.close()

    def rollback(self):
        self.connection.rollback()

    def closeConnection(self):
        try:
            self.cursor.close()
        except:
            pass
        try:
            self.connection.close()
        except:
            pass

    def __getCatalogParams(self):
        try:
            (host, port, database) = self.__parseURL(self.clustercfg['catalog']['hostname'])
            return  {
                        'host': host,
                        'port': port,
                        'database': database,
                        'user': self.clustercfg['catalog']['username'],
                        'password': self.clustercfg['catalog']['passwd']

                    }
        except BaseException as e:
            print("getCatalogParams error:")
            print(str(e))
            return None


    # returns dictionary of params for connection to node
    # nodeparams returned: user, passwd, host, port, database
    def __getNodeParams(self):
        try:
            user = self.nodeinfo['nodeuser']
            passwd = self.nodeinfo['nodepasswd']
            (host, port, database) = self.__parseURL(self.nodeinfo['nodeurl'])

            return {
                'user': user,
                'passwd': passwd,
                'host': host,
                'port': port,
                'database': database
            }
        except BaseException as e:
            print("Error getting node params:")
            print(str(e))
            return None


    # Grabs the host, port, and database from the hostname url.
    def __parseURL(self,url):
        hostmatch = re.search('^.*//([\.\d]+):(\d+)/(.*)$', url, flags=re.IGNORECASE)
        if hostmatch and len(hostmatch.groups()) == 3:
            return hostmatch.groups()
        else:
            return None
