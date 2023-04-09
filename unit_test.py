import unittest
from app import multiply, read_file


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_read_file(self):
        filePath = 'winequality-red.csv'
        expected_output = [[6.2, 0.31, 0.23, 8.1, 0.053, 49.0, 92.0, 0.9989, 3.45, 0.36, 8.6, 5.0], [8.0, 0.42, 0.28, 4.7, 0.06,                                                                               15.0, 60.0, 0.9983, 3.24, 0.53, 9.7, 6.0], [7.4, 0.49, 0.33, 7.3, 0.061, 21.0, 83.0, 0.9972, 3.24, 0.7, 9.9, 6.0]]
        result = read_file(filePath)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
