import pytest
from unittest.mock import Mock, patch
from tb_wrapper.UserController import *
import unittest


def get_env():
    env = dict()
    tb_url = 'http://217.76.51.6:9090'
    userfile = 'user.secrets'
    passwordfile = 'pass.secrets'
    env['tb_url'] = tb_url
    env['userfile'] = userfile
    env['passwordfile'] = passwordfile
    env['user'] = {'additional_info': {'failedLoginAttempts': 0, 'lastLoginTs': 1701852057581},
                   'authority': 'TENANT_ADMIN',
                   'created_time': 1684395767453,
                   'customer_id': {'entity_type': 'CUSTOMER',
                                   'id': '13814000-1dd2-11b2-8080-808080808080'},
                   'email': 'tenant@thingsboard.org',
                   'first_name': None,
                   'id': {'entity_type': 'USER', 'id': '954e94d0-f54f-11ed-91d5-ed8a7accb44b'},
                   'last_name': None,
                   'name': 'tenant@thingsboard.org',
                   'phone': None,
                   'tenant_id': {'entity_type': 'TENANT',
                                 'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}}
    env['tenant_object'] = {'entity_type': 'TENANT',
                            'id': '94cf0490-f54f-11ed-91d5-ed8a7accb44b'}
    env['tenant_id'] = "94cf0490-f54f-11ed-91d5-ed8a7accb44b"
    return env


class TestUserController(unittest.TestCase):

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_actual_user(self, mockClient):
        conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn

        env = get_env()
        conn.get_user.return_value = env['user']

        uc = UserController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = uc.actual_user()
        assert result == env['user']

    def test_get_users_from_customer(self):
        pass

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_get_tenant_id(self, mockClient):
        conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn
        env = get_env()
        mockTenant = Mock()
        mock_id = Mock()
        mock_id.id = env['tenant_id']
        mockTenant.tenant_id = mock_id
        conn.get_user.return_value = mockTenant

        uc = UserController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = uc.actual_user().tenant_id.id

        assert result == env['tenant_id']

    @patch('tb_wrapper.MainController.RestClientCE', autospec=True)
    def test_get_tenant_entity_id(self, mockClient):
        conn = Mock()
        conn.login.return_value = conn
        mockClient.return_value = conn
        env = get_env()
        mockTenant = Mock()
        mockTenant.tenant_id = env['tenant_object']
        conn.get_user.return_value = mockTenant
        uc = UserController(
            tb_url=env['tb_url'], userfile=env['userfile'], passwordfile=env['passwordfile'])
        result = uc.actual_user()
        assert result.tenant_id == env['tenant_object']
