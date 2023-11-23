import pytest
from unittest.mock import MagicMock
from src.QueryController import *

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

    expected_body = {
        "entity_fields": [{"type": "ENTITY_FIELD", "key": "name"}],
        "entity_filter": {
            "type": "entityType",
            "entity_type": "CUSTOMER",
            "resolve_multiple": True
        },
        "key_filters": [{
            "key": {"type": filter_key_scope, "key": filter_key_name},
            "value_type": filter_key_type,
            "predicate": {
                "operation": "EQUAL",
                "value": {"defaultValue": filter_key_value},
                "type": filter_key_type
            }
        }],
        "page_link": {"page": 0, "page_size": 1000, "dynamic": True},
        "latest_values": [{"type": filter_key_scope, "key": filter_key_name}]
    }
    #non posso farel'assertion equals a meno che non prenda anche tutti i campi che genera in automatico l'api
    assert query_controller.query_body_attribute(filter_key_scope, filter_key_name, filter_key_value, filter_key_type) is not None

def test_find_customers_by_attribute(query_controller):
    # Mocking the tb_client.find_entity_data_by_query() method
    query_controller.tb_client.find_entity_data_by_query = MagicMock(return_value="mocked_result")

    filter_key_scope = "SERVER_ATTRIBUTE"
    filter_key_name = "NAME"
    filter_key_value = "VALUE"
    filter_key_type = "STRING"

    result = query_controller.find_customers_by_attribute(filter_key_scope, filter_key_name, filter_key_value, filter_key_type)

    assert result is not None
    # Add additional assertions as needed
