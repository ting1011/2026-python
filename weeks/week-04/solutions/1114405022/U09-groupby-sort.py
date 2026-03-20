
# U9. groupby 為何一定要先 sort（1.15）
# 本範例說明 groupby 分組前必須先排序，否則同 key 會被分成多段


from itertools import groupby  # 匯入 groupby，用於分組相鄰且 key 相同的元素
from operator import itemgetter  # 匯入 itemgetter，方便根據字典的 key 取值


rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]  # 每個元素是有 date 欄位的字典


# 沒排序：'07/02/2012' 會被分成兩段，因為 groupby 只分組「連續」的 key
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)  # 這裡 '07/02/2012' 會出現兩次分組


# 排序後：同 date 的元素才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))  # 先根據 date 欄位排序
for k, g in groupby(rows, key=itemgetter('date')):
    list(g)  # 這時每個 date 只會有一個分組
