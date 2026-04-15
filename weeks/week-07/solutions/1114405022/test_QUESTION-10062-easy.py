"""  # 檔案開頭的多行註解，說明用途
UVA 10062 -easy 版本單元測試
"""  # 多行註解結束
import unittest  # 匯入 Python 標準單元測試模組
from QUESTION_10062-easy import restore_cows_easy  # 匯入要測試的函式

# 定義一個測試類別，繼承自 unittest.TestCase
class TestRestoreCowsEasy(unittest.TestCase):
    def test_sample(self):  # 測試範例案例
        self.assertEqual(restore_cows_easy([0,1,2,3]), [1,2,3,4,5])  # 驗證輸入 [0,1,2,3] 應得 [1,2,3,4,5]
    def test_reverse(self):  # 測試完全反向的情況
        self.assertEqual(restore_cows_easy([0,0,0,0]), [5,4,3,2,1])  # 驗證輸入 [0,0,0,0] 應得 [5,4,3,2,1]
    def test_random(self):  # 測試隨機排列的情況
        self.assertEqual(restore_cows_easy([0,1,1,0]), [2,4,5,1,3])  # 驗證輸入 [0,1,1,0] 應得 [2,4,5,1,3]

if __name__ == "__main__":  # 主程式進入點
    unittest.main()  # 執行所有單元測試
