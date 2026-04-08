"""
UVA 10062 -easy 版本單元測試
"""
import unittest
from QUESTION_10062-easy import restore_cows_easy

class TestRestoreCowsEasy(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(restore_cows_easy([0,1,2,3]), [1,2,3,4,5])
    def test_reverse(self):
        self.assertEqual(restore_cows_easy([0,0,0,0]), [5,4,3,2,1])
    def test_random(self):
        self.assertEqual(restore_cows_easy([0,1,1,0]), [2,4,5,1,3])

if __name__ == "__main__":
    unittest.main()
