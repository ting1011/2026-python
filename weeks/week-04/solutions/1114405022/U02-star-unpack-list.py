
# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
# 本範例說明星號（*）解包可以處理不定長資料，且結果一定是 list


record = ('Dave', 'dave@example.com')  # 一個只有兩個元素的 tuple
name, email, *phones = record  # 用 *phones 接收剩下的元素，這裡沒有多的元素，phones 會是空 list
# phones == []  仍是 list，無論有沒有多的元素，*變數 都會是 list 型態
