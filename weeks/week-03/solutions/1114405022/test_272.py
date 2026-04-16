# test_272.py
"""
UVA 272 題目：TEX Quotes
單元測試程式
繁體中文詳細註解
"""

import unittest
from 272_handwrite import tex_quotes

class TestTexQuotes(unittest.TestCase):
    def test_example(self):
        # 測試範例
        text = '"To be or not to be," quoth the Bard. "That is the question."'
        expected = '``To be or not to be,\'\' quoth the Bard. ``That is the question.\'\''
        self.assertEqual(tex_quotes(text), expected)

    def test_no_quotes(self):
        # 沒有雙引號的情況
        self.assertEqual(tex_quotes('Hello World!'), 'Hello World!')

    def test_multiple_quotes(self):
        # 多組雙引號
        text = '"A" "B" "C"'
        expected = '``A\'\' ``B\'\' ``C\'\''
        self.assertEqual(tex_quotes(text), expected)

if __name__ == "__main__":
    unittest.main()
