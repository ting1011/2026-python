
# R13. 字典列表排序 itemgetter（1.13）
# 本範例說明 operator.itemgetter 排序用法

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]
sorted(rows, key=itemgetter('fname'))         # 依 fname 排序
sorted(rows, key=itemgetter('uid'))           # 依 uid 排序
sorted(rows, key=itemgetter('uid', 'fname'))  # 先依 uid，再依 fname 排序
