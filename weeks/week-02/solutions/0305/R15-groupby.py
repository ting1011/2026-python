
# R15. 分組 groupby（1.15）
# 本範例說明 itertools.groupby 分組用法

from itertools import groupby
from operator import itemgetter

# 假設有一組資料，每筆有日期
rows = [
    {'date': '07/01/2012', 'address': '...'},
    {'date': '07/02/2012', 'address': '...'}
]
rows.sort(key=itemgetter('date'))  # 先依分組欄位排序

# 依 date 分組
for date, items in groupby(rows, key=itemgetter('date')):
    for i in items:
        pass  # 這裡可處理每組資料
