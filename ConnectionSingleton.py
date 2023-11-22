from tb_rest_client.rest_client_ce import *

class ConnectionSingleton:
    tb_connection = None

    @staticmethod
    def getInstance(tb_url, userfile, passwordfile):
        if ConnectionSingleton.tb_connection == None:
            ConnectionSingleton.tb_connection = ConnectionSingleton.__init__private(tb_url, userfile, passwordfile)
        return ConnectionSingleton.tb_connection

    def __init__private(tb_url, userfile, passwordfile):        
        connection = ConnectionSingleton()
        connection.getConnection(tb_url, userfile, passwordfile)
        return connection

    @staticmethod
    def destroyConnection():
        ConnectionSingleton.tb_connection = None

    # Viene chiamato solo se la connection non è già stato istanziato
    def getConnection(self, tb_url, userfile, passwordfile):
            self.tb_connection = RestClientCE(base_url=tb_url)
            with open(userfile) as f: 
                USERNAME = f.readline().strip()
            with open(passwordfile) as f: 
                PASSWORD = f.readline().strip()
            return self.tb_connection.login(username=USERNAME, password=PASSWORD)
    
    def get_client(self):
        return self.tb_connection