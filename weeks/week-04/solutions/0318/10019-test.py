"""10019 單元測試

測試重點：
1. 驗證 b1 為十進位 n 的二進位 1 的數量。
2. 驗證 b2 為 int(str(n), 16) 的二進位 1 的數量。
"""

import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10019-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10019-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)


class TestCountOnes(unittest.TestCase):
    """檢查兩種計算方式的結果是否與題意一致。"""

    def test_cases(self):
        cases = [
            (265, (3, 5)),
            (111, (6, 3)),
            (1234, (5, 5)),
            (10, (2, 1)),
        ]
        for n, expected in cases:
            self.assertEqual(ai.count_ones(n), expected)
            self.assertEqual(manual.count_ones(n), expected)


if __name__ == "__main__":
    unittest.main()
