# R13. 字典列表排序 itemgetter（1.13）
# 用 itemgetter 取出字典指定欄位，做排序

from operator import itemgetter

rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依 fname 排序
sorted(rows, key=itemgetter('fname'))
# 依 uid 排序
sorted(rows, key=itemgetter('uid'))
# 依 uid、fname 排序
sorted(rows, key=itemgetter('uid', 'fname'))
