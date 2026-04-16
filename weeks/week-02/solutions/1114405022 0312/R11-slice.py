
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
# R11. 命名切片 slice（1.11）

# 假設有一筆固定格式的字串資料
record = '....................100 .......513.25 ..........'
# 用 slice 物件命名欄位位置
SHARES = slice(20, 23)  # 20~22 是 shares
PRICE = slice(31, 37)   # 31~36 是 price
# 取出 shares 與 price，計算總價
cost = int(record[SHARES]) * float(record[PRICE])
