"""Stage 2 — 搜尋正確性測試骨架

規格:search.py 的 linear_search / binary_search / set_search 必須
  1. 一律不可修改傳入的 data(測試要驗)
  2. 回傳型別「不一致」,共用測試時要小心:
       - linear_search(data, target) -> int   找到回 index,找不到回 -1
       - binary_search(data, target) -> int   找到回 index,找不到回 -1
       - set_search(data, target)    -> bool  回傳是否存在
  3. binary_search 的前提是 data 已排序;收到未排序 data 的行為,
     自己定義並在 docstring 寫清楚,測試也要對得上你的定義

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。
  因為回傳型別不同,subTest 裡要把「找到/找不到」轉成可比較的共同判準
  (例:linear/binary 看 index 是否 >= 0,set 看 bool)——怎麼轉自己想。

待辦:
  1. 自己打提示詞跟 AI 討論,補齊測試——一般案例、edge case(空 list?重複值?
     目標不存在?)、「不可修改傳入 data」都要覆蓋;AI 給的齊不齊,自己驗收
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage2 搜尋正確性測試"
  4. 寫 search.py,全綠後 commit: "feat: stage2 實作三種搜尋"
"""

import copy
import unittest

from search import linear_search, binary_search, set_search

SEARCH_FUNCTIONS = [linear_search, binary_search, set_search]


def _found(search_func, data, target):
    """轉換回傳值為共同判準：found → True, not found → False"""
    result = search_func(data, target)
    if search_func is set_search:
        return result
    return result >= 0


class TestSearchFunctions(unittest.TestCase):

    def test_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                self.assertTrue(_found(func, data, 1))
                self.assertTrue(_found(func, data, 5))
                self.assertTrue(_found(func, data, 9))

    def test_not_found_cases(self):
        data = [1, 3, 5, 7, 9]
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                self.assertFalse(_found(func, data, 0))
                self.assertFalse(_found(func, data, 4))
                self.assertFalse(_found(func, data, 10))

    def test_empty_list(self):
        data = []
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                self.assertFalse(_found(func, data, 1))

    def test_input_not_mutated(self):
        data = [3, 1, 4, 1, 5]
        original = copy.deepcopy(data)
        for func in SEARCH_FUNCTIONS:
            with self.subTest(func=func.__name__):
                func(data, 4)
                self.assertEqual(data, original)


if __name__ == "__main__":
    unittest.main()
