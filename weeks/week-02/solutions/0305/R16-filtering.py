def is_int(val):

# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 本範例說明多種過濾資料的方式

mylist = [1, 4, -5, 10]
[n for n in mylist if n > 0]  # 推導式過濾正數
pos = (n for n in mylist if n > 0)  # 產生器表達式

values = ['1', '2', '-3', '-', 'N/A']

# 判斷字串是否可轉為 int
def is_int(val):
    try:
        int(val); return True
    except ValueError:
        return False

list(filter(is_int, values))  # 用 filter 過濾可轉 int 的字串

from itertools import compress
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]  # 產生布林遮罩
list(compress(addresses, more5))  # 只保留 counts > 5 的地址
