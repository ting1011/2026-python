# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
# 你能解釋：為了維持插入順序，它需要額外結構（因此更耗記憶體）
# 補充說明：
# OrderedDict 會額外維護一個雙向鏈結串列來記錄插入順序，
# 所以比一般 dict 更耗記憶體，但能保證遍歷時順序與插入一致。
