# R18. namedtuple（1.18）

# namedtuple 可以讓 tuple 具備「欄位名稱」，可讀性更高
from collections import namedtuple

# 宣告一個 Subscriber 型別，包含 addr 與 joined 兩個欄位
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立實例後，可以像物件一樣用 .欄位名 存取
sub = Subscriber('jonesy@example.com', '2012-10-19')
print('訂閱者 addr:', sub.addr)

# 另一個 namedtuple 範例：股票資料
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)

# namedtuple 不可變，更新值要用 _replace() 產生新物件
s = s._replace(shares=75)
print('更新後的 Stock:', s)
