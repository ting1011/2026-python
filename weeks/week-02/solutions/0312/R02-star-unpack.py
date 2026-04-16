# R2. 解包數量不固定：星號解包（1.2）
# 使用 * 來接收多餘的元素，讓函式能處理不定長度的序列

def drop_first_last(grades):
    first, *middle, last = grades  # middle 會是中間所有元素的 list
    return sum(middle) / len(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record  # phone_numbers 會是 tuple 其餘元素

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]  # trailing 取得前面所有元素
