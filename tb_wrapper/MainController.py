from tb_wrapper.ConnectionSingleton import *

class MainController:
    tb_client = None

    def __init__(self, tb_url, userfile, passwordfile):
        connection = ConnectionSingleton.getInstance(tb_url, userfile, passwordfile)
        self.tb_client = connection.tb_connection

    def logout(self):
        ConnectionSingleton.destroyConnection()
        self.tb_client = None