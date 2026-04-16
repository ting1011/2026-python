
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))
sorted(zip(prices.values(), prices.keys()))

min(prices, key=lambda k: prices[k])  # 回傳 key
# R8. 字典運算：min/max/sorted + zip（1.8）

# 建立一個股票價格字典
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip 將 value, key 配對成 tuple，min/max/sorted 會以 value 為主
min(zip(prices.values(), prices.keys()))    # 取價格最小的 (10.75, 'FB')
max(zip(prices.values(), prices.keys()))    # 取價格最大的 (612.78, 'AAPL')
sorted(zip(prices.values(), prices.keys())) # 依價格排序

# 只取 key，但排序依 value
min(prices, key=lambda k: prices[k])  # 回傳價格最小的 key
