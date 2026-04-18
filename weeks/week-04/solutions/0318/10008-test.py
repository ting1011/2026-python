"""10008 單元測試

重點：
1. 英文字母大小寫視為相同。
2. 非字母字元（數字、符號、空白）不計入。
3. 排序必須符合「次數降冪、字母升冪」。
"""

import unittest
from importlib import util

ai_spec = util.spec_from_file_location("ai", "10008-ai.py")
ai = util.module_from_spec(ai_spec)
ai_spec.loader.exec_module(ai)

manual_spec = util.spec_from_file_location("manual", "10008-manual.py")
manual = util.module_from_spec(manual_spec)
manual_spec.loader.exec_module(manual)


class TestLetterFrequency(unittest.TestCase):
    """驗證字母統計結果是否正確。"""

    def test_cases(self):
        lines = ["This is a test.", "Count letters!"]
        expected = [
            ("T", 6),
            ("S", 4),
            ("E", 3),
            ("I", 2),
            ("A", 1),
            ("C", 1),
            ("H", 1),
            ("L", 1),
            ("N", 1),
            ("O", 1),
            ("R", 1),
            ("U", 1),
        ]
        self.assertEqual(ai.letter_frequency(lines), expected)
        self.assertEqual(manual.letter_frequency(lines), expected)

    def test_ignore_non_alpha(self):
        """非字母不該影響統計，且大小寫需合併。"""
        lines = ["A1a!", "b_B"]
        expected = [("A", 2), ("B", 2)]
        self.assertEqual(ai.letter_frequency(lines), expected)
        self.assertEqual(manual.letter_frequency(lines), expected)


if __name__ == "__main__":
    unittest.main()
