
# R18. namedtuple（1.18）
# 本範例示範如何使用 namedtuple 建立具名欄位的不可變資料結構


from collections import namedtuple  # 匯入 namedtuple，方便建立具名欄位的 tuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])  # 定義一個 Subscriber 類型，有 addr 和 joined 兩個欄位
sub = Subscriber('jonesy@example.com', '2012-10-19')  # 建立 Subscriber 實例
sub.addr  # 取出 addr 欄位的值，結果為 'jonesy@example.com'


Stock = namedtuple('Stock', ['name', 'shares', 'price'])  # 定義一個 Stock 類型，有 name、shares、price 三個欄位
s = Stock('ACME', 100, 123.45)  # 建立 Stock 實例
s = s._replace(shares=75)  # 用 _replace 建立 shares 欄位被修改的新 Stock 實例（原本的 s 不會被改變）
