def count_six_tuples(S):
"""  # 多行註解：說明本程式用途
UVA 10071 標準解
計算集合 S 中滿足 a+b+c+d+e=f 的六元組數量。
"""  # 多行註解結束
# 由於 S 最多 100 個元素，暴力窮舉五重迴圈計算 a+b+c+d+e，然後檢查 f 是否在 S
# 時間複雜度 O(N^5)，N=100 時約 10^10，不可行。
# 需優化：
# 先計算所有 a+b+c 的和出現次數，再計算 d+e-f 是否能湊出。

from collections import Counter  # 匯入 Counter 用於計數

def count_six_tuples(S):  # 定義計算六元組數量的函式
    """
    S: List[int]，集合 S
    回傳: 滿足 a+b+c+d+e=f 的六元組數量
    """
    N = len(S)  # 取得集合 S 的長度
    sum_abc = Counter()  # 用來記錄所有 a+b+c 的和出現次數
    for a in S:  # 枚舉 a
        for b in S:  # 枚舉 b
            for c in S:  # 枚舉 c
                sum_abc[a+b+c] += 1  # 統計 a+b+c 的和
    ans = 0  # 初始化答案
    for d in S:  # 枚舉 d
        for e in S:  # 枚舉 e
            for f in S:  # 枚舉 f
                ans += sum_abc[d+e-f]  # 若 d+e-f 剛好等於某個 a+b+c，則加總其出現次數
    return ans  # 回傳答案

if __name__ == "__main__":  # 主程式進入點
    N = int(input())  # 讀取集合長度
    S = [int(input()) for _ in range(N)]  # 讀取集合 S
    print(count_six_tuples(S))  # 輸出答案
