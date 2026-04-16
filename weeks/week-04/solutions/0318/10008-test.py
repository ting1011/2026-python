# 10008 題目測試程式
# 測試 letter_frequency 函式（AI 版與手打版）
# 繁體中文註解
import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10008-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10008-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)

class TestLetterFrequency(unittest.TestCase):
    def test_cases(self):
        lines = ["This is a test.", "Count letters!"]
        expected = [('T', 4), ('E', 3), ('S', 3), ('I', 2), ('C', 1), ('H', 1), ('L', 1), ('N', 1), ('O', 1), ('R', 1), ('U', 1)]
        self.assertEqual(ai.letter_frequency(lines), expected)
        self.assertEqual(manual.letter_frequency(lines), expected)

if __name__ == "__main__":
    unittest.main()
