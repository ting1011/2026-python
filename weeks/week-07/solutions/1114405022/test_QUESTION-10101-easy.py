"""
UVA 10101 -easy 版本單元測試
"""
import unittest
from QUESTION_10101-easy import try_move_easy

class TestTryMoveEasy(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(try_move_easy('9+1=8'), '3+5=8#')
    def test_sample2(self):
        self.assertEqual(try_move_easy('5+3=9'), '6+3=9#')
    def test_no_solution(self):
        self.assertEqual(try_move_easy('1+1=1'), 'No')

if __name__ == "__main__":
    unittest.main()
