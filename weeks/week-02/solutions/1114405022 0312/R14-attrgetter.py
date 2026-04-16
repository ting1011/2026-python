
from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))
# R14. 物件排序 attrgetter（1.14）

from operator import attrgetter  # 匯入 attrgetter

# 定義一個 User 類別
class User:
    def __init__(self, user_id):
        self.user_id = user_id  # 設定 user_id 屬性

# 建立 User 物件的列表
users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))  # 依 user_id 屬性排序
