# test_299.py
"""
UVA 299 題目：Train Swapping
單元測試程式
繁體中文詳細註解
"""

import unittest
from 299_handwrite import train_swapping

class TestTrainSwapping(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(train_swapping([1, 3, 2]), 1)
    def test_example2(self):
        self.assertEqual(train_swapping([4, 3, 2, 1]), 6)
    def test_sorted(self):
        self.assertEqual(train_swapping([1, 2, 3, 4]), 0)
    def test_reverse(self):
        self.assertEqual(train_swapping([5, 4, 3, 2, 1]), 10)

if __name__ == "__main__":
    unittest.main()
