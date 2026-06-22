"""Stage 1 — @timeit 裝飾器測試骨架

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時(float 秒)append 到 f.records
  4. f.last_elapsed = 本次 repeat 的平均耗時
  5. 裝飾器內不准 print
  6. repeat < 1 → raise ValueError(用 raise,不准 assert)

待辦:
  1. 自己打提示詞跟 AI 討論,補齊下面的測試(可再加);規格每條都要有覆蓋
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage1 timeit 裝飾器測試"
  4. 寫 timing.py,全綠後 commit: "feat: stage1 實作 timeit 裝飾器"
"""

import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):

    def test_returns_original_result(self):
        @timeit()
        def add(a, b):
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        @timeit()
        def sample_func(x):
            """docstring"""
            return x

        self.assertEqual(sample_func.__name__, "sample_func")
        self.assertEqual(sample_func.__doc__, "docstring")

    def test_repeat_records_and_average(self):
        @timeit(repeat=5)
        def add(a, b):
            return a + b

        add(1, 2)
        self.assertEqual(len(add.records), 5)
        self.assertIsInstance(add.last_elapsed, float)
        self.assertGreater(add.last_elapsed, 0)

        add(3, 4)
        self.assertEqual(len(add.records), 10)

    def test_repeat_below_one_raises_valueerror(self):
        for invalid in (0, -1, -100):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):
                    @timeit(repeat=invalid)
                    def f():
                        pass


if __name__ == "__main__":
    unittest.main()
