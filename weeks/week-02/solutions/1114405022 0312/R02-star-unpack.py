
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# R2. 解包數量不固定：星號解包（1.2）

# 定義一個函式，丟棄第一個和最後一個元素，只計算中間的平均
def drop_first_last(grades):
    first, *middle, last = grades  # 第一個給 first，最後一個給 last，中間所有元素給 middle（list）
    return sum(middle) / len(middle)  # 回傳中間元素的平均值

# 星號解包可用於不確定長度的序列
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # 前兩個元素分別給 name, email，剩下的都放進 phone_numbers（list）

# 星號也可以放在前面，取得所有前面的元素
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]  # current=3，trailing=[10,8,7,1,9,5,10]
