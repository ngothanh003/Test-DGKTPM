import unittest
import pandas as pd
from weather_pattern_analysis import analyze_weather_patterns

class TestWeatherPatternAnalysis(unittest.TestCase):

    def setUp(self):
        # Dữ liệu thời tiết mẫu để kiểm thử
        self.weather_data = pd.DataFrame({
            'nhiệt_độ': [20, 25, 30, 18, 22, 28, 32, 15],
            'độ_ẩm': [50, 55, 60, 45, 48, 52, 58, 42],
            'tốc_độ_gió': [10, 12, 15, 8, 11, 13, 16, 7]
        })

    def test_analyze_weather_patterns(self):
        # Kiểm tra xem hàm trả về một DataFrame với cột 'cluster' mới hay không
        results = analyze_weather_patterns(self.weather_data)
        self.assertTrue('cluster' in results.columns)

        # Kiểm tra xem số lượng cluster có đúng với giá trị đã chỉ định hay không
        self.assertEqual(len(results['cluster'].unique()), 5)

if __name__ == '__main__':
    unittest.main()