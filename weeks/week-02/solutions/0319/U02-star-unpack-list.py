# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 只有姓名與 email，沒有電話號碼
record = ('Dave', 'dave@example.com')

# *phones 會接住「剩下所有元素」，即使沒有也會得到空 list
name, email, *phones = record
# phones == []  仍是 list
print('name =', name)
print('email =', email)
print('phones =', phones)
