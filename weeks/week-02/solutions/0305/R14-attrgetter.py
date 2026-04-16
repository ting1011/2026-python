
# R14. 物件排序 attrgetter（1.14）
# 本範例說明 operator.attrgetter 排序物件用法

from operator import attrgetter

# 定義一個 User 類別
class User:
    def __init__(self, user_id):
        self.user_id = user_id

# 建立 User 物件列表
users = [User(23), User(3), User(99)]
sorted(users, key=attrgetter('user_id'))  # 依 user_id 排序
