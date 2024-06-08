import unittest
import pandas as pd
from personalized_weather_alerts import train_model, predict
from unittest.mock import MagicMock, patch

class TestPersonalizedWeatherAlerts(unittest.TestCase):

    @patch('personalized_weather_alerts.RandomForestClassifier')
    def test_train_model(self, mock_random_forest):
        # Dữ liệu mẫu cho việc kiểm thử
        weather_data = pd.DataFrame({
            'user_id': [1, 2, 3],
            'temperature': [20, 25, 30],
            'humidity': [50, 55, 60],
            'wind_speed': [10, 12, 15]
        })

        user_preferences = pd.DataFrame({
            'user_id': [1, 2, 3],
            'preference_1': [0, 1, 0],
            'preference_2': [1, 0, 1],
            'alert_needed': [0, 1, 0]
        })

        # Giả lập cho RandomForestClassifier
        mock_model_instance = MagicMock()
        mock_random_forest.return_value = mock_model_instance

        # Gọi hàm train_model
        model = train_model(weather_data, user_preferences)

        # Kiểm tra xem RandomForestClassifier được gọi đúng cách
        mock_random_forest.assert_called_once()
        mock_model_instance.fit.assert_called_once()

    def test_predict(self):
        # Dữ liệu mẫu cho việc kiểm thử
        weather_data = pd.DataFrame({
            'user_id': [1, 2, 3],
            'temperature': [20, 25, 30],
            'humidity': [50, 55, 60],
            'wind_speed': [10, 12, 15]
        })

        user_preferences = pd.DataFrame({
            'user_id': [1, 2, 3],
            'preference_1': [0, 1, 0],
            'preference_2': [1, 0, 1],
            'alert_needed': [0, 1, 0]
        })

        # Mô hình giả lập
        mock_model = MagicMock()

        # Gọi hàm predict
        predictions = predict(mock_model, weather_data, user_preferences)

        # Kiểm tra xem dữ liệu đầu ra có đúng định dạng không
        self.assertTrue(isinstance(predictions, pd.DataFrame))

if __name__ == '__main__':
    unittest.main()