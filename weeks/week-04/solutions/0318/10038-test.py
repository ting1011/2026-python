# 10038 題目測試程式
# 測試 is_jolly 函式（AI 版與手打版）
# 繁體中文註解
import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10038-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10038-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)

class TestIsJolly(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([1, 4, 2, 3], True),
            ([1, 4, 2, -1, 6], False),
            ([11, 7, 4, 2, 1, 6], False),
            ([1], True),
        ]
        for nums, expected in cases:
            self.assertEqual(ai.is_jolly(nums), expected)
            self.assertEqual(manual.is_jolly(nums), expected)

if __name__ == "__main__":
    unittest.main()
