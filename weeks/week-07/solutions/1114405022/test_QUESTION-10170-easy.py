"""
UVA 10170 -easy 版本單元測試
"""
import unittest
from QUESTION_10170-easy import find_group_easy

class TestFindGroupEasy(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(find_group_easy(3, 12), 6)
    def test_sample2(self):
        self.assertEqual(find_group_easy(4, 9), 5)
    def test_sample3(self):
        self.assertEqual(find_group_easy(4, 4), 4)
    def test_large(self):
        self.assertEqual(find_group_easy(1, 100), 14)

if __name__ == "__main__":
    unittest.main()
