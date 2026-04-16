
p = (4, 5)
x, y = p

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
_, shares, price, _ = data
# R1. 序列解包（1.1）

# 將一個 tuple 直接解包給兩個變數
p = (4, 5)  # p 是一個二元素的 tuple
x, y = p    # x=4, y=5，將 p 的值依序賦給 x, y

# 將 list 依序解包給多個變數
data = ['ACME', 50, 91.1, (2012, 12, 21)]  # data 是一個 list，最後一個元素是 tuple
name, shares, price, date = data  # 依序解包給四個變數，date 會是 (2012, 12, 21)

# 巢狀解包，將最後一個 tuple 也展開
name, shares, price, (year, mon, day) = data  # year=2012, mon=12, day=21

# 丟棄不需要的值（用 _ 佔位，表示這個值不要）
_, shares, price, _ = data  # 只取 shares, price，其餘丟棄
