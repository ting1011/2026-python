"""
UVA 10101 單元測試
"""
import unittest
from QUESTION_10101 import try_move

class TestTryMove(unittest.TestCase):
    def test_sample1(self):
        # 例：9+1=8#，移動一根木棒可變成 3+5=8#
        self.assertEqual(try_move('9+1=8'), '3+5=8#')
    def test_sample2(self):
        # 例：5+3=9#，移動一根木棒可變成 6+3=9#
        self.assertEqual(try_move('5+3=9'), '6+3=9#')
    def test_no_solution(self):
        # 例：1+1=1#，無法移動一根木棒成立
        self.assertEqual(try_move('1+1=1'), 'No')

if __name__ == "__main__":
    unittest.main()
