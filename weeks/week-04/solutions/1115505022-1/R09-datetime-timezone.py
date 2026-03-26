# R09. 時區操作（3.16）
# zoneinfo（Python 3.9+）取代 pytz

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 建立時區物件
utc = ZoneInfo("UTC")  # 世界標準時間
central = ZoneInfo("America/Chicago")  # 美國中部時區
taipei = ZoneInfo("Asia/Taipei")  # 台北時區

# 建立帶時區的 datetime
# tzinfo 參數指定時區，datetime 物件就會帶有時區資訊
# 這樣的 datetime 可直接做時區轉換

d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print("原始時間（美國中部）:", d)  # 2012-12-21 09:30:00-06:00

# 轉換時區
# astimezone() 可將 datetime 轉換到其他時區
print("轉換到印度時區:", d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print("轉換到台北時區:", d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間
now_utc = datetime.now(tz=utc)
print("目前 UTC 時間:", now_utc)

# 最佳實踐：內部用 UTC，輸出再轉本地
# 系統內部統一用 UTC 儲存，顯示時再轉換成當地時區
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print("UTC 轉美國中部:", utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# 查詢國家時區
# available_timezones() 會回傳所有支援的時區名稱
# 可用 list comprehension 過濾出含有 'Taipei' 的時區

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print("台灣相關時區:", tw_zones)  # ['Asia/Taipei']
