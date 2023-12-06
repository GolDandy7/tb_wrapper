import pytest
from unittest.mock import patch, mock_open
from tb_wrapper.MainController import MainController


class TestMainController:

    @patch('builtins.open', new_callable=mock_open, read_data='user\npass')
    def test_MainController(self, mock_file):
        pass

    def test_logout(self):
        pass
