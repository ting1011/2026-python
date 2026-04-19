# U9. groupby 為何一定要先 sort（1.15）

from itertools import groupby
from operator import itemgetter

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 沒排序：07/02 會被分成兩段（因為 groupby 只看「連續」）
print('未排序 groupby:')
for k, g in groupby(rows, key=itemgetter('date')):
    # 這裡轉 list 只是為了觸發迭代並觀察該組內容
    print('  ', k, list(g))

# 排序後：同 date 才會連在一起，分組才正確
rows.sort(key=itemgetter('date'))
print('排序後 groupby:')
for k, g in groupby(rows, key=itemgetter('date')):
    # 排序後可得到我們直覺上的「同日期一組」
    print('  ', k, list(g))
