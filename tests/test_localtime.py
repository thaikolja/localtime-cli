import unittest
from unittest.mock import patch, mock_open
from localtime import load_api_key, APIKeyError


class TestLocalTime(unittest.TestCase):

    @patch('localtime.os.path.isfile', return_value=True)
    @patch('localtime.loadfile', return_value={'API_KEY': 'test_api_key'})
    def test_api_key_from_env_file(self, mock_loadfile, mock_isfile):
        self.assertEqual(load_api_key(), 'test_api_key')

    @patch('localtime.os.path.isfile', side_effect=[False, True])
    @patch('builtins.open', new_callable=mock_open, read_data='export API_KEY="test_api_key"')
    def test_api_key_from_bashrc(self, mock_open, mock_isfile):
        self.assertEqual(load_api_key(), 'test_api_key')

    @patch('localtime.os.path.isfile', return_value=False)
    @patch('localtime.os.environ.get', return_value='test_api_key')
    def test_api_key_from_env_var(self, mock_get, mock_isfile):
        self.assertEqual(load_api_key(), 'test_api_key')

    @patch('localtime.os.path.isfile', return_value=False)
    @patch('localtime.os.environ.get', return_value=None)
    def test_api_key_not_found(self, mock_get, mock_isfile):
        with self.assertRaises(APIKeyError):
            load_api_key()


if __name__ == '__main__':
    unittest.main()
