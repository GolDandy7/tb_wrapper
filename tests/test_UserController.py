import pytest
from unittest.mock import MagicMock
from tb_wrapper.UserController import UserController

@pytest.fixture
def user_controller():
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return UserController(tb_url, userfile, passwordfile)

def test_actual_user(user_controller):
    user_controller.tb_client.get_user = MagicMock(return_value="mocked_user")
    assert user_controller.actual_user() == "mocked_user"

def test_get_users_from_customer(user_controller):
    user_controller.tb_client.get_customer_users = MagicMock(return_value="mocked_users")
    assert user_controller.get_users_from_customer(customer_id="123") == "mocked_users"

def test_get_tenant_id(user_controller):
    user = MagicMock()
    user.tenant_id.id = "mocked_tenant_id"
    user_controller.tb_client.get_user = MagicMock(return_value=user)
    assert user_controller.get_tenant_id() == "mocked_tenant_id"

def test_get_tenant_entity_id(user_controller):
    user = MagicMock()
    user.tenant_id = "mocked_tenant_entity_id"
    user_controller.tb_client.get_user = MagicMock(return_value=user)
    assert user_controller.get_tenant_entity_id() == "mocked_tenant_entity_id"
