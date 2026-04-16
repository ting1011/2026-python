p = (4, 5)
x, y = p
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# R1. 序列解包（1.1）
# 本範例說明 Python 的序列解包（unpacking）語法

# 1. 基本序列解包
p = (4, 5)  # 建立一個二元素 tuple
x, y = p    # 將 tuple 依序解包給 x, y
# x = 4, y = 5

# 2. 多變數解包
data = ['ACME', 50, 91.1, (2012, 12, 21)]  # 包含巢狀 tuple 的 list
name, shares, price, date = data  # 依序解包給四個變數
# name = 'ACME', shares = 50, price = 91.1, date = (2012, 12, 21)

# 3. 巢狀解包
name, shares, price, (year, mon, day) = data  # date 也可直接巢狀解包
# year = 2012, mon = 12, day = 21


# 4. 丟棄不需要的值（用 _ 作為占位符）
_, shares, price, _ = data  # 只取 shares, price，其餘用 _ 忽略

if __name__ == "__main__":
	print("x:", x)
	print("y:", y)
	print("name:", name)
	print("shares:", shares)
	print("price:", price)
	print("date:", date)
	print("year:", year)
	print("mon:", mon)
	print("day:", day)
