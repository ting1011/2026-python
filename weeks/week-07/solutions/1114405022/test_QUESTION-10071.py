"""
UVA 10071 單元測試
"""
import unittest
from QUESTION_10071 import count_six_tuples

class TestCountSixTuples(unittest.TestCase):
    def test_sample(self):
        # S = [1, 2]
        # 1+1+1+1+1=1, 1+1+1+1+2=2, ...
        # 手算所有組合
        self.assertEqual(count_six_tuples([1,2]), 12)
    def test_small(self):
        # S = [0, 1]
        self.assertEqual(count_six_tuples([0,1]), 12)
    def test_single(self):
        # S = [3]
        self.assertEqual(count_six_tuples([3]), 1)  # 3+3+3+3+3=3

if __name__ == "__main__":
    unittest.main()
