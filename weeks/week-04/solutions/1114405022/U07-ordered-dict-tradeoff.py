
# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）
# 本範例說明 OrderedDict 會記住插入順序，但因此更耗記憶體


from collections import OrderedDict  # 匯入 OrderedDict，保證 key 的插入順序


d = OrderedDict()  # 建立一個空的 OrderedDict
d['foo'] = 1  # 插入 'foo'，值為 1
d['bar'] = 2  # 插入 'bar'，值為 2
# OrderedDict 會記住 key 的插入順序，遍歷時順序固定
# 但為了維持順序，內部需要額外的結構（如雙向鏈結串列），因此比一般 dict 更耗記憶體
