
# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 本範例示範多種過濾資料的方法，包括列表推導式、生成器、filter、compress


mylist = [1, 4, -5, 10]  # 一個整數列表
[n for n in mylist if n > 0]  # 使用列表推導式，過濾出大於 0 的元素，結果為 [1, 4, 10]
pos = (n for n in mylist if n > 0)  # 使用生成器表達式，產生大於 0 的元素（惰性運算）


values = ['1', '2', '-3', '-', 'N/A']  # 一個字串列表，內容可能不是數字


def is_int(val):
    try:
        int(val); return True  # 嘗試將 val 轉為整數，成功則回傳 True
    except ValueError:
        return False  # 轉換失敗（如 '-' 或 'N/A'），回傳 False


list(filter(is_int, values))  # 用 filter 過濾出可以轉成整數的字串，結果為 ['1', '2', '-3']


from itertools import compress  # 匯入 compress，可根據布林條件壓縮序列
addresses = ['a1', 'a2', 'a3']  # 地址列表
counts = [0, 3, 10]  # 對應每個地址的數值
more5 = [n > 5 for n in counts]  # 產生布林列表，表示 counts 中哪些值大於 5，結果為 [False, False, True]
list(compress(addresses, more5))  # 只保留 more5 對應為 True 的地址，結果為 ['a3']
