import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Import hàm từ manage.py
import manage

class TestManage(unittest.TestCase):

    @patch('manage.os.environ.setdefault')
    @patch('manage.sys.argv', ['manage.py', 'test_command'])
    @patch('manage.execute_from_command_line')
    def test_main(self, mock_execute, mock_argv, mock_setdefault):
        # Kiểm tra xem os.environ.setdefault được gọi với đúng đối số
        manage.main()
        mock_setdefault.assert_called_once_with('DJANGO_SETTINGS_MODULE', 'backend_django.settings')

        # Kiểm tra xem execute_from_command_line được gọi với đúng đối số
        mock_execute.assert_called_once_with(['manage.py', 'test_command'])

    @patch('manage.os.environ.setdefault')
    @patch('manage.sys.argv', ['manage.py', 'test_command'])
    @patch('manage.execute_from_command_line')
    def test_manage_import(self, mock_execute, mock_argv, mock_setdefault):
        # Kiểm tra việc import manage.py
        self.assertIsNotNone(manage)

if __name__ == '__main__':
    unittest.main()