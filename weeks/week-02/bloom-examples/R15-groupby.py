
# R15. 分組 groupby（1.15）
# 本範例示範如何用 groupby 依據字典中的某個欄位（如日期）進行分組


from itertools import groupby  # 匯入 groupby，用於分組相鄰且 key 相同的元素
from operator import itemgetter  # 匯入 itemgetter，方便根據字典的 key 取值


# 範例資料，每個元素都是一個字典，包含 'date' 和 'address' 欄位
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'}
]

# 先根據 'date' 欄位排序，groupby 只能分組相鄰且 key 相同的元素
rows.sort(key=itemgetter('date'))

# 用 groupby 依據 'date' 欄位分組
for date, items in groupby(rows, key=itemgetter('date')):
    # date 是目前分組的日期
    # items 是一個 iterator，包含所有 date 相同的元素
    for i in items:
        # 這裡可以對每個分組內的元素進行處理
        pass
