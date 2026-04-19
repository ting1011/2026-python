# R17. 字典子集（1.17）

# 原始股價字典：key 是股票代號、value 是價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 取出價格大於 200 的項目（字典推導式）
p1 = {k: v for k, v in prices.items() if v > 200}

# 先定義目標 key 的集合
tech_names = {'AAPL', 'IBM'}

# 只保留 key 在 tech_names 裡的項目
p2 = {k: v for k, v in prices.items() if k in tech_names}

print('價格 > 200:', p1)
print('科技股子集:', p2)
