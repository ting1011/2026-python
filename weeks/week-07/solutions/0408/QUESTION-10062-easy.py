"""
UVA 10062 更簡易記憶版
用插入法直接模擬，適合理解與手寫。
"""
# 這個方法直接維護一個結果陣列，每次將新牛插入正確位置
# 時間複雜度 O(N^2)，但 N 不大時可用

def restore_cows_easy(order):
    """
    order: 長度 N-1，order[i] 表示第 i+1 頭牛前面有多少頭編號比它小的牛
    回傳: 長度 N，為正確排列的乳牛編號（1~N）
    """
    N = len(order) + 1
    res = []  # 最終排列
    for cow in range(N, 0, -1):
        # 每次將編號 cow 插入到正確位置
        idx = order[cow-2] if cow > 1 else 0
        res.insert(idx, cow)
    res.reverse()  # 反轉得到正確順序
    return res

if __name__ == "__main__":
    # 讀取輸入
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    N = int(lines[0])
    order = list(map(int, lines[1:]))
    ans = restore_cows_easy(order)
    for num in ans:
        print(num)
