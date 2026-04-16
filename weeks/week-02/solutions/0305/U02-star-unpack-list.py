
# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
# 本範例說明星號解包即使沒東西也會得到空 list

record = ('Dave', 'dave@example.com')
name, email, *phones = record  # phones 會是 list，即使沒資料也是空 list
# phones == []  仍是 list
