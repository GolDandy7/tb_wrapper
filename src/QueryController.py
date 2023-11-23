from src.MainController import MainController
from tb_rest_client.rest_client_ce import *
from src.handle_exception import *

@handle_tb_wrapper_exception
class QueryController(MainController):
    tb_client = None
    
    def __init__(self, tb_url, userfile, passwordfile):
        super().__init__(tb_url, userfile, passwordfile)

    def query_body_attribute(self, filter_key_scope, filter_key_name, filter_key_value, filter_key_type):
        predicate = {"operation": "EQUAL",
                    "value": {"defaultValue": filter_key_value},
                    "type": filter_key_type}    
        ef = EntityFilter(entity_type="CUSTOMER",type="entityType",resolve_multiple=True)
        filter_key = EntityKey(key=filter_key_name,type=filter_key_scope)
        mfilter = KeyFilter(key=filter_key, value_type=filter_key_type,predicate=predicate)
        
        field = EntityKey(type="ENTITY_FIELD",key="name")
        latest_values_field = EntityKey(type=filter_key_scope,key=filter_key_name)

        page = EntityDataPageLink(page=0,page_size=1000,dynamic=True)

        body = EntityDataQuery(entity_fields=[field],entity_filter=ef, key_filters=[mfilter], page_link=page,latest_values=[latest_values_field])
        
        return body

    def find_customers_by_attribute(self, filter_key_scope, filter_key_name, filter_key_value, filter_key_type):
        body = self.query_body_attribute(filter_key_scope,filter_key_name,filter_key_value,filter_key_type)
        return self.tb_client.find_entity_data_by_query(body=body)