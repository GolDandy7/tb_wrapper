from MainController import MainController
from tb_rest_client.rest_client_ce import *
from handle_exception import *

@handle_tb_wrapper_exception
class UserController(MainController):
    tb_client = None
    
    def __init__(self, tb_url, userfile, passwordfile):
        super().__init__(tb_url, userfile, passwordfile)

    def actual_user(self):
        return self.tb_client.get_user()

    def get_users_from_customer(self, customer_id):
        return self.tb_client.get_customer_users(customer_id=customer_id, page_size=1000, page=0)

    def get_tenant_id(self):
        return self.tb_client.get_user().tenant_id.id

    def get_tenant_entity_id(self):
        return self.tb_client.get_user().tenant_id