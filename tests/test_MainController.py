import pytest
from unittest.mock import patch, mock_open
from tb_wrapper.ConnectionSingleton import ConnectionSingleton
from tb_wrapper.MainController import MainController

class TestMainController:

    @patch('builtins.open', new_callable=mock_open, read_data='user\npass')
    def test_MainController(self, mock_file):

        tb_url = 'http://217.76.51.6:9090'
        userfile = 'user.secrets'
        passwordfile = 'pass.secrets'
        controller = MainController(tb_url, userfile, passwordfile)
        assert controller is not None
        assert controller.tb_client is not None

    def test_logout(self):
        
        tb_url = 'http://217.76.51.6:9090'
        userfile = 'user.secrets'
        passwordfile = 'pass.secrets'
        controller = MainController(tb_url, userfile, passwordfile)
        controller.logout()
        assert controller.tb_client is None
        assert ConnectionSingleton.tb_connection is None

