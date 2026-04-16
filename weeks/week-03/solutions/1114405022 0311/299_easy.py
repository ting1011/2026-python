# 299_easy.py
"""
UVA 299 題目：Train Swapping
AI 版（簡單易懂）
繁體中文詳細註解
"""

def train_swapping(trains):
    """
    計算將火車車廂排序所需的交換次數（冒泡排序次數）
    trains: List[int]，每個元素代表一個車廂編號
    回傳：int，交換次數
    """
    count = 0
    arr = trains[:]
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count

if __name__ == "__main__":
    # 範例測試
    print(train_swapping([1, 3, 2]))  # 應輸出 1
    print(train_swapping([4, 3, 2, 1]))  # 應輸出 6
