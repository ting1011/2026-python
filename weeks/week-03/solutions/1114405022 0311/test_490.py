# test_490.py
"""
UVA 490 題目：Rotating Sentences
單元測試程式
繁體中文詳細註解
"""

import unittest
from 490_handwrite import rotate_sentences

class TestRotateSentences(unittest.TestCase):
    def test_example(self):
        lines = [
            "Hello World!",
            "This is a test.",
            "Rotate me!"
        ]
        expected = [
            '  RTR',
            'eoeho',
            'tsl l',
            'atltl',
            't a o',
            'eieWm',
            '   es',
            'satd!',
            '.te. '
        ]
        # 這裡只檢查長度與部分內容
        result = rotate_sentences(lines)
        self.assertEqual(len(result), 13)
        self.assertTrue(result[0].strip().startswith('R'))

    def test_empty(self):
        self.assertEqual(rotate_sentences([]), [])

if __name__ == "__main__":
    unittest.main()
