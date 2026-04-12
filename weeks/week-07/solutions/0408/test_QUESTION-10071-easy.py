"""
UVA 10071 -easy 版本單元測試
"""
import unittest
from QUESTION_10071-easy import count_six_tuples_easy

class TestCountSixTuplesEasy(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(count_six_tuples_easy([1,2]), 12)
    def test_small(self):
        self.assertEqual(count_six_tuples_easy([0,1]), 12)
    def test_single(self):
        self.assertEqual(count_six_tuples_easy([3]), 1)

if __name__ == "__main__":
    unittest.main()
