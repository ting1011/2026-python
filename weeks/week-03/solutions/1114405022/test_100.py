# 測試程式（含中文註解）
import unittest
from 100_easy import max_cycle_length

class TestUVA100(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(max_cycle_length(1, 10), 20)
        self.assertEqual(max_cycle_length(100, 200), 125)
        self.assertEqual(max_cycle_length(201, 210), 89)
        self.assertEqual(max_cycle_length(900, 1000), 174)

if __name__ == "__main__":
    unittest.main()
