import pytest
from unittest.mock import MagicMock
from tb_wrapper.QueryController import *

@pytest.fixture
def query_controller():

    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return QueryController(tb_url, userfile, passwordfile)

def test_query_body_attribute(query_controller):

    filter_key_scope = "SERVER_ATTRIBUTE"
    filter_key_name = "NAME"
    filter_key_value = "VALUE"
    filter_key_type = "STRING"
    
    result_body = query_controller.query_body_attribute(filter_key_scope, filter_key_name, filter_key_value, filter_key_type) 
    assert result_body is not None
    assert result_body.key_filters[0].key.type == filter_key_scope
    assert result_body.key_filters[0].key.key == filter_key_name
    assert result_body.key_filters[0].value_type == filter_key_type

def test_find_customers_by_attribute(query_controller):

    query_controller.tb_client.find_entity_data_by_query = MagicMock(return_value="mocked_result")
    filter_key_scope = "SERVER_ATTRIBUTE"
    filter_key_name = "NAME"
    filter_key_value = "VALUE"
    filter_key_type = "STRING"

    result = query_controller.find_customers_by_attribute(filter_key_scope, filter_key_name, filter_key_value, filter_key_type)
    assert result is not None
