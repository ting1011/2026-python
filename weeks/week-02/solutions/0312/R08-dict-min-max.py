# R8. 字典運算：min/max/sorted + zip（1.8）

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

 # 以 zip 將 value 與 key 配對，方便同時排序或找最大最小
 min(zip(prices.values(), prices.keys()))  # (10.75, 'FB')
 max(zip(prices.values(), prices.keys()))  # (612.78, 'AAPL')
 sorted(zip(prices.values(), prices.keys()))  # [(10.75, 'FB'), ...]

 # 只回傳 key，但排序依 value
 min(prices, key=lambda k: prices[k])  # 'FB'
