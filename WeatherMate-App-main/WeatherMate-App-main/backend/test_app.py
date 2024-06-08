import unittest
from unittest.mock import patch, MagicMock
import sqlite3
import app

class TestApp(unittest.TestCase):

    @patch('app.requests.get')
    @patch('app.conn')
    @patch('app.cursor')
    def test_fetch_weather_data(self, mock_cursor, mock_conn, mock_get):
        # Thiết lập mock cho requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temperature': '25°C', 'humidity': '60%'}
        mock_get.return_value = mock_response
        
        # Kiểm tra fetch_weather_data
        city = 'London'
        data = app.fetch_weather_data(city)
        self.assertIsNotNone(data)
        self.assertEqual(data['temperature'], '25°C')
        self.assertEqual(data['humidity'], '60%')

    @patch('app.conn')
    @patch('app.cursor')
    def test_register_user(self, mock_cursor, mock_conn):
        # Kiểm tra đăng ký người dùng thành công
        mock_cursor.execute.return_value = None
        mock_conn.commit.return_value = None
        self.assertTrue(app.register_user('testuser', 'password', 'test@example.com'))

        # Kiểm tra đăng ký người dùng trùng lặp 
        mock_cursor.execute.side_effect = sqlite3.IntegrityError
        self.assertFalse(app.register_user('testuser', 'password', 'test@example.com'))

    @patch('app.fetch_weather_data')
    @patch('app.store_weather_data')
    def test_update_weather_for_city(self, mock_store_weather_data, mock_fetch_weather_data):
        # Thiết lập mock cho fetch_weather_data
        mock_fetch_weather_data.return_value = {'temperature': '20°C', 'humidity': '70%'}
        
        # Kiểm tra update_weather_for_city
        city = 'New York'
        app.update_weather_for_city(city)
        mock_store_weather_data.assert_called_once_with(city, {'temperature': '20°C', 'humidity': '70%'})

    @patch('app.fetch_weather_data')
    @patch('app.store_weather_data')
    def test_update_weather(self, mock_store_weather_data, mock_fetch_weather_data):
        # Thiết lập mock cho fetch_weather_data
        mock_fetch_weather_data.return_value = {'temperature': '20°C', 'humidity': '70%'}
        
        # Kiểm tra update_weather
        app.update_weather()
        mock_store_weather_data.assert_called()

if __name__ == '__main__':
    unittest.main()