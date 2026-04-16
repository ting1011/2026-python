# 10035 題目測試程式
# 測試 carry_count 函式（AI 版與手打版）
# 繁體中文註解
import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10035-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10035-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)

class TestCarryCount(unittest.TestCase):
    def test_cases(self):
        cases = [
            ((123, 456), 0),
            ((555, 555), 3),
            ((123, 594), 1),
            ((0, 0), 0),
        ]
        for (a, b), expected in cases:
            self.assertEqual(ai.carry_count(a, b), expected)
            self.assertEqual(manual.carry_count(a, b), expected)

if __name__ == "__main__":
    unittest.main()
