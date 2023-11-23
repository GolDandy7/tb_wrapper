import pytest
from unittest.mock import MagicMock
from src.DeviceController import DeviceController

device_info_result = {'data': [{'active': False,
           'additional_info': None,
           'created_time': 1697205661205,
           'customer_id': {'entity_type': 'CUSTOMER',
                           'id': '13814000-1dd2-11b2-8080-808080808080'},
           'customer_is_public': False,
           'customer_title': None,
           'device_data': {'configuration': {'type': 'DEFAULT'},
                           'transport_configuration': {'type': 'DEFAULT'}},
           'device_profile_id': {'entity_type': 'DEVICE_PROFILE',
                                 'id': '94dbfce0-f54f-11ed-91d5-ed8a7accb44b'},
           'device_profile_name': 'default',
           'firmware_id': None,
           'id': {'entity_type': 'DEVICE',
                  'id': 'f0f95450-69d0-11ee-8bf0-899ee6c3e465'},
           'label': None,
           'name': 'prometheus',
           'software_id': None,
           'tenant_id': {'entity_type': 'TENANT',
                         'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
           'type': 'default'}],
 'has_next': False,
 'total_elements': 11,
 'total_pages': 1}



@pytest.fixture
def device_controller():
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return DeviceController(tb_url, userfile, passwordfile)

def test_get_tenant_device(device_controller):
    # Mocking the tb_client.get_tenant_device() method
    device_controller.tb_client.get_tenant_device = MagicMock(return_value="mocked_device")
    device_name = "test_device"
    assert device_controller.get_tenant_device(device_name) == "mocked_device"


'''def test_check_device_exists_by_name(device_controller):
    # Mocking the tb_client.get_tenant_device_infos() method
    device_infos = MagicMock()
    #device_infos = [{"name": "existing_device"}, {"name": "another_device"}]
    device_infos = device_info_result
    device_controller.tb_client.get_tenant_device_infos = MagicMock(return_value=device_infos)

    existing_device_name = "existing_device"
    another_device_name = "non_existing_device"

    assert device_controller.check_device_exists_by_name(existing_device_name) is True
    assert device_controller.check_device_exists_by_name(another_device_name) is False
'''
def test_create_device_with_customer(device_controller):
    # Mocking the tb_client.save_device() method
    device_controller.tb_client.save_device = MagicMock(return_value="mocked_device")

    device_profile_id = "profile_id"
    device_name = "test_device"
    customer_obj_id = "customer_id"

    result = device_controller.create_device_with_customer(device_profile_id, device_name, customer_obj_id)

    assert result == "mocked_device"
    # Add additional assertions as needed

def test_create_device_without_customer(device_controller):
    # Mocking the tb_client.save_device() method
    device_controller.tb_client.save_device = MagicMock(return_value="mocked_device")

    device_profile_id = "profile_id"
    device_name = "test_device"

    result = device_controller.create_device_without_customer(device_profile_id, device_name)

    assert result == "mocked_device"
    # Add additional assertions as needed

def test_save_device_attributes(device_controller):
    # Mocking the tb_client.save_device_attributes() method
    device_controller.tb_client.save_device_attributes = MagicMock(return_value="mocked_result")

    device_id = "device_id"
    scope = "scope"
    body = {"attribute": "value"}

    result = device_controller.save_device_attributes(device_id, scope, body)

    assert result == "mocked_result"
    # Add additional assertions as needed

def test_get_default_device_profile_info(device_controller):
    # Mocking the tb_client.get_default_device_profile_info() method
    device_controller.tb_client.get_default_device_profile_info = MagicMock(return_value="mocked_result")

    result = device_controller.get_default_device_profile_info()

    assert result == "mocked_result"
    # Add additional assertions as needed
