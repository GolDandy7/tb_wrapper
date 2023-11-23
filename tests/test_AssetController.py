import pytest
from unittest.mock import MagicMock
from src.AssetController import AssetController

@pytest.fixture
def asset_controller():
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    return AssetController(tb_url, userfile, passwordfile)

def test_get_default_asset_profile_info(asset_controller):
    # Mocking the tb_client.get_default_asset_profile_info() method
    asset_controller.tb_client.get_default_asset_profile_info = MagicMock(return_value="mocked_result")

    result = asset_controller.get_default_asset_profile_info()

    assert result == "mocked_result"
    # Add additional assertions as needed

def test_create_asset(asset_controller):
    # Mocking the tb_client.save_asset() method
    asset_controller.tb_client.save_asset = MagicMock(return_value="mocked_asset")

    asset_profile_id = "profile_id"
    asset_name = "test_asset"
    customer_obj_id = "customer_id"

    result = asset_controller.create_asset(asset_profile_id, asset_name, customer_obj_id)

    assert result == "mocked_asset"
    # Add additional assertions as needed

def test_create_asset_profile(asset_controller):
    # Mocking the tb_client.save_asset_profile() method
    asset_controller.tb_client.save_asset_profile = MagicMock(return_value="mocked_result")

    profile_name = "test_profile"

    result = asset_controller.create_asset_profile(profile_name)

    assert result == "mocked_result"
    # Add additional assertions as needed

'''def test_check_asset_exists_by_name(asset_controller):
    # Mocking the tb_client.get_tenant_asset_infos() method
    asset_infos = MagicMock()
    asset_infos.data = [{"name": "existing_asset"}, {"name": "another_asset"}]
    asset_controller.tb_client.get_tenant_asset_infos = MagicMock(return_value=asset_infos)

    existing_asset_name = "existing_asset"
    another_asset_name = "non_existing_asset"

    assert asset_controller.check_asset_exists_by_name(existing_asset_name) is True
    assert asset_controller.check_asset_exists_by_name(another_asset_name) is False'''

'''def test_check_asset_profile_exists_by_name(asset_controller):
    # Mocking the tb_client.get_asset_profiles() method
    asset_profiles = MagicMock()
    asset_profiles.data = [{"name": "existing_profile"}, {"name": "another_profile"}]
    asset_controller.tb_client.get_asset_profiles = MagicMock(return_value=asset_profiles)

    existing_profile_name = "existing_profile"
    another_profile_name = "non_existing_profile"

    assert asset_controller.check_asset_profile_exists_by_name(existing_profile_name) is True
    assert asset_controller.check_asset_profile_exists_by_name(another_profile_name) is False'''

'''def test_get_asset_profile_by_name(asset_controller):
    # Mocking the tb_client.get_asset_profiles() method
    asset_profiles = MagicMock()
    asset_profiles.data = [{"name": "existing_profile"}, {"name": "another_profile"}]
    asset_controller.tb_client.get_asset_profiles = MagicMock(return_value=asset_profiles)

    existing_profile_name = "existing_profile"
    another_profile_name = "non_existing_profile"

    result = asset_controller.get_asset_profile_by_name(existing_profile_name)
    assert result["name"] == existing_profile_name

    with pytest.raises(TBWrapperException):
        asset_controller.get_asset_profile_by_name(another_profile_name)'''

def test_save_asset_attributes(asset_controller):
    # Mocking the tb_client.save_entity_attributes_v2() method
    asset_controller.tb_client.save_entity_attributes_v2 = MagicMock(return_value="mocked_result")

    asset_id = "asset_id"
    scope = "scope"
    body = {"attribute": "value"}

    result = asset_controller.save_asset_attributes(asset_id, scope, body)

    assert result == "mocked_result"
    # Add additional assertions as needed

def test_get_tenant_asset(asset_controller):
    # Mocking the tb_client.get_tenant_asset() method
    asset_controller.tb_client.get_tenant_asset = MagicMock(return_value="mocked_asset")

    asset_name = "test_asset"

    result = asset_controller.get_tenant_asset(asset_name)

    assert result == "mocked_asset"
    # Add additional assertions as needed

def test_create_relation(asset_controller):
    # Mocking the tb_client.save_relation() method
    asset_controller.tb_client.save_relation = MagicMock(return_value="mocked_relation")

    from_id = "from_id"
    to_id = "to_id"
    relation_type = "relation_type"

    result = asset_controller.create_relation(from_id, to_id, relation_type)

    assert result == "mocked_relation"
    # Add additional assertions as needed
