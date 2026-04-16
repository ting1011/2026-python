# 10019 題目測試程式
# 測試 count_ones 函式（AI 版與手打版）
# 繁體中文註解
import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10019-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10019-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)

class TestCountOnes(unittest.TestCase):
    def test_cases(self):
        cases = [
            (265, (5, 5)),
            (111, (6, 3)),
            (1234, (5, 5)),
        ]
        for n, expected in cases:
            self.assertEqual(ai.count_ones(n), expected)
            self.assertEqual(manual.count_ones(n), expected)

if __name__ == "__main__":
    unittest.main()
