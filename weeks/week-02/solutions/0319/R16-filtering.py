# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 原始數列：同時包含正數與負數
mylist = [1, 4, -5, 10]

# 串列推導式：立即產生「所有正數」的新串列
print('正數(串列推導式):', [n for n in mylist if n > 0])

# 生成器表達式：延遲計算，逐個產生正數
pos = (n for n in mylist if n > 0)
print('正數(生成器):', list(pos))

# 這組資料包含可轉成整數與不可轉換的字串
values = ['1', '2', '-3', '-', 'N/A']

# 自訂過濾條件：能成功 int() 就回傳 True
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter() 依條件函式保留元素，再轉成 list 觀察結果
print('可轉 int 的字串:', list(filter(is_int, values)))

# compress(data, selectors)：根據布林遮罩挑出對應元素
from itertools import compress
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 先建立條件遮罩：True 的位置會被保留
more5 = [n > 5 for n in counts]
print('count > 5 的地址:', list(compress(addresses, more5)))
