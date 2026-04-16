

# R2. 解包數量不固定：星號解包（1.2）
# 本範例說明 Python 星號（*）解包語法

# 1. 星號解包用於變數數量不固定的情境
def drop_first_last(grades):
    first, *middle, last = grades  # 第一個給 first，最後一個給 last，中間全部給 middle（list）
    return sum(middle) / len(middle)  # 計算中間成績的平均

# 2. 星號解包 tuple
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # 前兩個分別給 name, email，剩下全部給 phone_numbers（list）


# 3. 星號解包 list
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]  # 最後一個給 current，其餘全部給 trailing

if __name__ == "__main__":
    grades = [80, 90, 70, 60, 100]
    print("drop_first_last 平均:", drop_first_last(grades))
    print("name:", name)
    print("email:", email)
    print("phone_numbers:", phone_numbers)
    print("trailing:", trailing)
    print("current:", current)
