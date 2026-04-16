# R1. 序列解包（1.1）
# 將序列（如 tuple、list）中的元素直接對應到多個變數，讓程式更簡潔易讀

p = (4, 5)
x, y = p  # x=4, y=5，將 tuple 兩個元素分別賦值給 x, y

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data  # 對應多個變數
name, shares, price, (year, mon, day) = data  # 巢狀解包，date 會再拆成 year, mon, day

# 丟棄不需要的值（用 _ 佔位，代表這個值不會用到）
_, shares, price, _ = data
