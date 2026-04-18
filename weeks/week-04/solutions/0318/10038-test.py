"""10038 單元測試

測試重點：
1. 一般 Jolly 與 Not jolly 範例。
2. 單一元素序列（邊界條件）。
3. 確保 AI 與手打版本都符合題意。
"""

import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10038-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10038-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)


class TestIsJolly(unittest.TestCase):
    """驗證 Jolly 判斷邏輯。"""

    def test_cases(self):
        cases = [
            ([1, 4, 2, 3], True),
            ([1, 4, 2, -1, 6], False),
            ([11, 7, 4, 2, 1, 6], True),
            ([1], True),
            ([1, 1], False),
        ]
        for nums, expected in cases:
            self.assertEqual(ai.is_jolly(nums), expected)
            self.assertEqual(manual.is_jolly(nums), expected)


if __name__ == "__main__":
    unittest.main()
