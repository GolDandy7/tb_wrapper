
import pytest
from unittest.mock import patch, mock_open
from tb_rest_client.rest_client_ce import *
from src.ConnectionSingleton import ConnectionSingleton


class TestConnectionSingleton:

    @patch('builtins.open', new_callable=mock_open, read_data='user\npass')
    def test_getConnection(self, mock_file):
        tb_url = 'http://217.76.51.6:9090'
        userfile = 'user.secrets'
        passwordfile = 'pass.secrets'
        singleton = ConnectionSingleton.getInstance(tb_url, userfile, passwordfile)
        assert singleton is not None
        assert singleton.get_client() is not None

    def test_destroyConnection(self):
        ConnectionSingleton.destroyConnection()
        assert ConnectionSingleton.tb_connection is None
