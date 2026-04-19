# R19. 轉換+聚合：生成器表達式（1.19）

# 範例 1：用生成器計算平方和，避免先建立中間串列
nums = [1, 2, 3]
print('平方和:', sum(x * x for x in nums))

# 範例 2：先把 tuple 內元素轉成字串，再用逗號串接
s = ('ACME', 50, 123.45)
print('tuple 串接:', ','.join(str(x) for x in s))

# 範例 3：在一組字典中找最小 shares
portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]

# 只回傳最小 shares 的數值
print('最小 shares 值:', min(s['shares'] for s in portfolio))

# 回傳整筆 shares 最小的字典
print('shares 最小的項目:', min(portfolio, key=lambda s: s['shares']))
