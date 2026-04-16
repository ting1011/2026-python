
# R8. 字典運算：min/max/sorted + zip（1.8）
# 本範例說明如何用 zip 對字典做 min/max/sorted 運算

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# 1. 用 zip 將 value 與 key 配對
min(zip(prices.values(), prices.keys()))    # 取最小 value 與對應 key
max(zip(prices.values(), prices.keys()))    # 取最大 value 與對應 key
sorted(zip(prices.values(), prices.keys())) # 依 value 排序

# 2. 直接用 key 參數找最小值的 key
min(prices, key=lambda k: prices[k])  # 回傳 value 最小的 key
