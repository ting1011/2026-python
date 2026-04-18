"""10035 單元測試

測試目標：
1. 驗證典型案例（有進位、無進位、多次連續進位）。
2. 確保 AI 版與手打版回傳一致。
"""

import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10035-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10035-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)


class TestCarryCount(unittest.TestCase):
    """檢查 carry_count 的核心正確性。"""

    def test_cases(self):
        cases = [
            ((123, 456), 0),
            ((555, 555), 3),
            ((123, 594), 1),
            ((0, 0), 0),
            ((9999, 1), 4),
        ]
        for (a, b), expected in cases:
            self.assertEqual(ai.carry_count(a, b), expected)
            self.assertEqual(manual.carry_count(a, b), expected)


if __name__ == "__main__":
    unittest.main()
