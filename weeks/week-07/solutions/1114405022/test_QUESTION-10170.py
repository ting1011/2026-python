"""
UVA 10170 單元測試
"""
import unittest
from QUESTION_10170 import find_group

class TestFindGroup(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(find_group(3, 12), 6)
    def test_sample2(self):
        self.assertEqual(find_group(4, 9), 5)
    def test_sample3(self):
        self.assertEqual(find_group(4, 4), 4)
    def test_large(self):
        self.assertEqual(find_group(1, 100), 14)

if __name__ == "__main__":
    unittest.main()
