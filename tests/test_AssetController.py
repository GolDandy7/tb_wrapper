from tb_wrapper.AssetController import *
import unittest
from unittest.mock import Mock, patch
import json


def get_env():
    env = dict()
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    env['tb_url'] = tb_url
    env['userfile'] = userfile
    env['passwordfile'] = passwordfile
    env['default_profile_info'] = {'default_dashboard_id': None,
                                   'id': {'entity_type': 'ASSET_PROFILE',
                                          'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                                   'image': None,
                                   'name': 'default',
                                   'tenant_id': {'entity_type': 'TENANT',
                                                 'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}}
    env["saved_asset"] = {'additional_info': None,
                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                               'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                          'created_time': 1701358904645,
                          'customer_id': {'entity_type': 'CUSTOMER',
                                          'id': '9567e930-f54f-11ed-91d5-ed8a7accb44b'},
                          'id': {'entity_type': 'ASSET', 'id': 'f6f91750-8f96-11ee-8034-97ab8762f59b'},
                          'label': None,
                          'name': 'Test',
                          'tenant_id': {'entity_type': 'TENANT',
                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                          'type': 'default'}
    env['asset'] = {'additional_info': None,
                    'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                         'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                    'created_time': None,
                    'customer_id': {'entity_type': 'CUSTOMER',
                                    'id': '9567e930-f54f-11ed-91d5-ed8a7accb44b'},
                    'id': None,
                    'label': None,
                    'name': 'Test',
                    'tenant_id': None,
                    'type': None}
    env['tenant_asset_info'] = {'data': [{'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '40a42a10-f551-11ed-b21a-bd6762728fed'},
                                          'asset_profile_name': 'TbServiceQueue',
                                          'created_time': 1684396484407,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '13814000-1dd2-11b2-8080-808080808080'},
                                          'customer_is_public': False,
                                          'customer_title': None,
                                          'id': {'entity_type': 'ASSET',
                                                 'id': '40a51470-f551-11ed-b21a-bd6762728fed'},
                                          'label': None,
                                          'name': 'Main_1e6c3fadf7fd',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'TbServiceQueue'},
                                         {'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '40a42a10-f551-11ed-b21a-bd6762728fed'},
                                          'asset_profile_name': 'TbServiceQueue',
                                          'created_time': 1697188221187,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '13814000-1dd2-11b2-8080-808080808080'},
                                          'customer_is_public': False,
                                          'customer_title': None,
                                          'id': {'entity_type': 'ASSET',
                                                 'id': '55e9c530-69a8-11ee-8bf0-899ee6c3e465'},
                                          'label': None,
                                          'name': 'Main_3fa1eb5663cb',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'TbServiceQueue'},
                                         {'additional_info': {'description': ''},
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '69869dd0-8946-11ee-9593-fbf738de8bd6'},
                                          'asset_profile_name': 'MWProfile',
                                          'created_time': 1700664623748,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '9567e930-f54f-11ed-91d5-ed8a7accb44b'},
                                          'customer_is_public': False,
                                          'customer_title': 'Customer C',
                                          'id': {'entity_type': 'ASSET',
                                                 'id': '774f8440-8946-11ee-9593-fbf738de8bd6'},
                                          'label': None,
                                          'name': 'MW',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'MWProfile'},
                                         {'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '40a42a10-f551-11ed-b21a-bd6762728fed'},
                                          'asset_profile_name': 'TbServiceQueue',
                                          'created_time': 1701437798522,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '13814000-1dd2-11b2-8080-808080808080'},
                                          'customer_is_public': False,
                                          'customer_title': None,
                                          'id': {'entity_type': 'ASSET',
                                                 'id': 'a7635da0-904e-11ee-878c-31ea2d675701'},
                                          'label': None,
                                          'name': 'Main_eace3141b04c',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'TbServiceQueue'},
                                         {'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                                          'asset_profile_name': 'default',
                                          'created_time': 1697547454337,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '13814000-1dd2-11b2-8080-808080808080'},
                                          'customer_is_public': False,
                                          'customer_title': None,
                                          'id': {'entity_type': 'ASSET',
                                                 'id': 'bd8e5f10-6cec-11ee-8bf0-899ee6c3e465'},
                                          'label': None,
                                          'name': 'FUNCTIONS',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'default'},
                                         {'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                                          'asset_profile_name': 'default',
                                          'created_time': 1697205661069,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '13814000-1dd2-11b2-8080-808080808080'},
                                          'customer_is_public': False,
                                          'customer_title': None,
                                          'id': {'entity_type': 'ASSET',
                                                 'id': 'f0e493d0-69d0-11ee-8bf0-899ee6c3e465'},
                                          'label': None,
                                          'name': 'ZOE ML SECTION',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'default'},
                                         {'additional_info': None,
                                          'asset_profile_id': {'entity_type': 'ASSET_PROFILE',
                                                               'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                                          'asset_profile_name': 'default',
                                          'created_time': 1701358904645,
                                          'customer_id': {'entity_type': 'CUSTOMER',
                                                          'id': '9567e930-f54f-11ed-91d5-ed8a7accb44b'},
                                          'customer_is_public': False,
                                          'customer_title': 'Customer C',
                                          'id': {'entity_type': 'ASSET',
                                                 'id': 'f6f91750-8f96-11ee-8034-97ab8762f59b'},
                                          'label': None,
                                          'name': 'Test',
                                          'tenant_id': {'entity_type': 'TENANT',
                                                        'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'},
                                          'type': 'default'}],
                                'has_next': False,
                                'total_elements': 7,
                                'total_pages': 1}
    env['tenant_profile_info'] = {'data': [{'created_time': 1684396484401,
                                            'default': False,
                                            'default_dashboard_id': None,
                                            'default_edge_rule_chain_id': None,
                                            'default_queue_name': None,
                                            'default_rule_chain_id': None,
                                            'description': 'Default asset profile',
                                            'id': {'entity_type': 'ASSET_PROFILE',
                                                   'id': '40a42a10-f551-11ed-b21a-bd6762728fed'},
                                            'image': None,
                                            'name': 'TbServiceQueue',
                                            'tenant_id': {'entity_type': 'TENANT',
                                                          'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}},
                                           {'created_time': 1700664600621,
                                            'default': False,
                                            'default_dashboard_id': None,
                                            'default_edge_rule_chain_id': None,
                                            'default_queue_name': None,
                                            'default_rule_chain_id': None,
                                            'description': None,
                                            'id': {'entity_type': 'ASSET_PROFILE',
                                                   'id': '69869dd0-8946-11ee-9593-fbf738de8bd6'},
                                            'image': None,
                                            'name': 'MWProfile',
                                            'tenant_id': {'entity_type': 'TENANT',
                                                          'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}},
                                           {'created_time': 1684395766762,
                                            'default': True,
                                            'default_dashboard_id': None,
                                            'default_edge_rule_chain_id': None,
                                            'default_queue_name': None,
                                            'default_rule_chain_id': None,
                                            'description': 'Default asset profile',
                                            'id': {'entity_type': 'ASSET_PROFILE',
                                                   'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'},
                                            'image': None,
                                            'name': 'default',
                                            'tenant_id': {'entity_type': 'TENANT',
                                                          'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}}],
                                  'has_next': False,
                                  'total_elements': 3,
                                  'total_pages': 1}
    env['asset_profile'] = {'created_time': None,
                            'default': None,
                            'default_dashboard_id': None,
                            'default_edge_rule_chain_id': None,
                            'default_queue_name': None,
                            'default_rule_chain_id': None,
                            'description': 'profile_name',
                            'id': None,
                            'image': None,
                            'name': 'profile_name',
                            'tenant_id': {'entity_type': 'TENANT',
                                          'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}}
    env['saved_asset_profile'] = {'created_time': 1701689295340,
                                  'default': False,
                                  'default_dashboard_id': None,
                                  'default_edge_rule_chain_id': None,
                                  'default_queue_name': None,
                                  'default_rule_chain_id': None,
                                  'description': 'profile_name',
                                  'id': {'entity_type': 'ASSET_PROFILE',
                                         'id': '372c52c0-9298-11ee-878c-31ea2d675701'},
                                  'image': None,
                                  'name': 'profile_name',
                                  'tenant_id': {'entity_type': 'TENANT',
                                                'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}}

    return env


class TestAssetController(unittest.TestCase):

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_get_default_profile_info(self, mockConn):

        conn = Mock()
        conn.login.return_value = conn
        mockConn.return_value = conn

        env = get_env()
        response_default_profile_info = env['default_profile_info']
        conn.get_default_asset_profile_info.return_value = response_default_profile_info
        asset_controller = AssetController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])

        result = asset_controller.get_default_asset_profile_info()
        assert result == response_default_profile_info

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_get_default_profile_info_exists_conn(self, mockConn):

        conn = Mock()
        conn.login.return_value = conn
        mockConn.return_value = conn

        env = get_env()
        response_default_profile_info = env['default_profile_info']
        conn.get_default_asset_profile_info.return_value = response_default_profile_info

        asset_controller = AssetController(connection=conn)
        result = asset_controller.get_default_asset_profile_info()
        assert result == response_default_profile_info

    @patch('tb_wrapper.AssetController.Asset', autospec=True)
    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_create_asset(self, mockClient, mockAsset):

        conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn

        asset_name = "Test"
        assetProfileID = {'entity_type': 'ASSET_PROFILE',
                                         'id': '94e524a0-f54f-11ed-91d5-ed8a7accb44b'}
        customerID = {'entity_type': 'CUSTOMER',
                      'id': '9567e930-f54f-11ed-91d5-ed8a7accb44b'}
        env = get_env()
        conn.save_asset.return_value = env['saved_asset']
        mockAsset.return_value = env['asset']
        ac = AssetController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = ac.create_asset(
            asset_profile_id=assetProfileID, asset_name=asset_name, customer_obj_id=customerID)

        conn.save_asset.assert_called_once_with(env['asset'])
        mockAsset.assert_called_once_with(
            name=asset_name, asset_profile_id=assetProfileID, customer_id=customerID)
        assert result == env['saved_asset']

    @patch('tb_wrapper.AssetController.AssetProfile')
    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_create_asset_profile(self, mockClient, mockAssetProfile):

        conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn
        conn.get_user.tenant_id = "{'entity_type': 'TENANT','id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}"
        env = get_env()
        asset_profile_name = "profile_name"
        tenant_id = {'entity_type': 'TENANT',
                     'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}
        mockAssetProfile.return_value = env['asset_profile']
        conn.save_asset_profile.return_value = env['saved_asset_profile']

        ac = AssetController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = ac.create_asset_profile(asset_profile_name)

        assert result == env['saved_asset_profile']

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_exists_asset_by_name(self, mockClient):
        pass
        '''conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn

        env = get_env()
        alarm_name = "ZOE ML SECTION"
        conn.get_tenant_asset_infos.return_value = env['tenant_asset_info']

        mockProfile = Mock()
        mockProfile.return_value
        
        ac = AssetController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = ac.check_asset_exists_by_name(alarm_name)

        assert result == True'''

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_exists_profile_asset_by_name(self, mockClient):
        pass
