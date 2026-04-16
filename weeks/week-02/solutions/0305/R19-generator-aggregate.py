
# R19. 轉換+聚合：生成器表達式（1.19）
# 本範例說明生成器表達式的聚合運算

nums = [1, 2, 3]
sum(x * x for x in nums)  # 計算平方和

s = ('ACME', 50, 123.45)
','.join(str(x) for x in s)  # 將 tuple 轉成字串並用逗號串接

portfolio = [{'name': 'AOL', 'shares': 20}, {'name': 'YHOO', 'shares': 75}]
min(s['shares'] for s in portfolio)  # 取 shares 最小值
min(portfolio, key=lambda s: s['shares'])  # 取 shares 最小的物件
