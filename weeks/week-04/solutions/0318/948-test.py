"""948 單元測試

測試目標：
1. 驗證 AI 版與手打版函式都能輸出正確 fibonaccimal 字串。
2. 確保兩份程式對同一組測資的結果一致。
"""

import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "948-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "948-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)


class TestFibonaccimalBase(unittest.TestCase):
    """針對 fibonaccimal 轉換函式的核心測試。"""

    def test_cases(self):
        # 覆蓋小值、一般值與較大值，避免只對單一案例過度擬合。
        cases = [
            (1, "1"),
            (2, "10"),
            (3, "100"),
            (4, "101"),
            (10, "10010"),
            (100, "1000010100"),
            (143, "1010101010"),
        ]
        for n, expected in cases:
            self.assertEqual(ai.fibonaccimal_base(n), expected)
            self.assertEqual(manual.fibonaccimal_base(n), expected)


if __name__ == "__main__":
    unittest.main()
