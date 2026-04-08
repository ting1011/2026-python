"""
UVA 10093 單元測試
"""
import unittest
from QUESTION_10093 import max_artillery

class TestMaxArtillery(unittest.TestCase):
    def test_sample(self):
        N, M = 3, 3
        grid = ["PPP", "PPP", "PPP"]
        self.assertEqual(max_artillery(N, M, grid), 5)
    def test_with_hill(self):
        N, M = 2, 3
        grid = ["PHP", "PPP"]
        self.assertEqual(max_artillery(N, M, grid), 3)
    def test_all_hill(self):
        N, M = 2, 2
        grid = ["HH", "HH"]
        self.assertEqual(max_artillery(N, M, grid), 0)

if __name__ == "__main__":
    unittest.main()
