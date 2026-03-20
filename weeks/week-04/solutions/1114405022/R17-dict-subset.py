
# R17. 字典子集（1.17）
# 本範例示範如何用字典推導式過濾出子集


prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}  # 股票名稱對應價格的字典

# 用字典推導式，過濾出價格大於 200 的項目，結果為 {'AAPL': 612.78, 'IBM': 205.55}
p1 = {k: v for k, v in prices.items() if v > 200}


tech_names = {'AAPL', 'IBM'}  # 只關心的科技股名稱集合

# 用字典推導式，過濾出名稱在 tech_names 集合中的項目，結果為 {'AAPL': 612.78, 'IBM': 205.55}
p2 = {k: v for k, v in prices.items() if k in tech_names}
