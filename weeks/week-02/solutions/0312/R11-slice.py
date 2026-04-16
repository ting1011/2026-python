# R11. 命名切片 slice（1.11）
# 用 slice 物件讓切片更易讀

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)  # 20~22 為 shares
PRICE = slice(31, 37)   # 31~36 為 price
cost = int(record[SHARES]) * float(record[PRICE])
