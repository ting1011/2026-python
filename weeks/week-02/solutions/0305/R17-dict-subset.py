
# R17. 字典子集（1.17）
# 本範例說明字典推導式過濾子集

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}
p1 = {k: v for k, v in prices.items() if v > 200}  # 取價格大於 200 的項目

tech_names = {'AAPL', 'IBM'}
p2 = {k: v for k, v in prices.items() if k in tech_names}  # 只取科技股
