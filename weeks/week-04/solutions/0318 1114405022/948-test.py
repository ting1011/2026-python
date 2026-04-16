# 948 題目測試程式
# 測試 fibonaccimal_base 函式（AI 版與手打版）
# 繁體中文註解
import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "948-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "948-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)

class TestFibonaccimalBase(unittest.TestCase):
    def test_cases(self):
        # 測試資料：數字與其費波那契表示
        cases = [
            (1, "1"),
            (2, "10"),
            (3, "100"),
            (4, "101"),
            (10, "10010"),
            (100, "100010010"),
            (143, "1000100000"),
        ]
        for n, expected in cases:
            self.assertEqual(ai.fibonaccimal_base(n), expected)
            self.assertEqual(manual.fibonaccimal_base(n), expected)

if __name__ == "__main__":
    unittest.main()
