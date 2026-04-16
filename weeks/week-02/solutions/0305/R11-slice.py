
# R11. 命名切片 slice（1.11）
# 本範例說明如何用 slice 物件命名切片，提升可讀性

record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)   # 20~22 為 shares 欄位
PRICE = slice(31, 37)    # 31~36 為 price 欄位
cost = int(record[SHARES]) * float(record[PRICE])  # 取出 shares 與 price 並計算總價
