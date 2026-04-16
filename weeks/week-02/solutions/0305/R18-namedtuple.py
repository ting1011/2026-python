
# R18. namedtuple（1.18）
# 本範例說明 collections.namedtuple 的用法

from collections import namedtuple

# 1. 定義具名 tuple 型別
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')  # 可用屬性存取欄位
sub.addr  # 'jonesy@example.com'

# 2. 股票資訊範例
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)  # 產生 shares 改為 75 的新物件
