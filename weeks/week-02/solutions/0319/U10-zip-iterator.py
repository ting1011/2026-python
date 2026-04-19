# U10. zip 為何只能用一次（1.8）

prices = {'A': 2.0, 'B': 1.0}

# zip 產生的是迭代器（lazy object），不是可重複讀取的序列
z = zip(prices.values(), prices.keys())

print('第一次 min(z):', min(z))  # OK（第一次取用，會消耗掉迭代器）
# max(z)  # 會失敗：因為 z 已經被消耗完
print('第二次 list(z):', list(z))  # 已被消耗，結果會是空串列
