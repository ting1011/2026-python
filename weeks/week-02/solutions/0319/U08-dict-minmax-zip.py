# U8. 字典最值為何常用 zip(values, keys)（1.8）

# key 是商品代號，value 是價格
prices = {'A': 2.0, 'B': 1.0}

# 直接 min(prices) 比的是 key（字母序）
print('min(prices) =', min(prices))  # 回傳 key 的最小值（字母序）

# 只看 values 雖能拿到最小價格，但會失去對應 key
print('min(prices.values()) =', min(prices.values()))   # 回傳最小 value，但你不知道是哪個 key

# zip 後會形成 (value, key) 配對，可一次拿到價格與對應代號
print('min(zip(values, keys)) =', min(zip(prices.values(), prices.keys())))
# 回傳 (最小value, 對應key)，一次拿到兩者
