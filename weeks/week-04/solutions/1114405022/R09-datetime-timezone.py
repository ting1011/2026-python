
# R09. 時區操作（3.16）
# 本範例示範 zoneinfo（Python 3.9+，取代 pytz）進行時區處理


from datetime import datetime, timedelta  # 匯入 datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones  # 匯入時區相關類別


utc = ZoneInfo("UTC")  # UTC 時區
central = ZoneInfo("America/Chicago")  # 芝加哥時區
taipei = ZoneInfo("Asia/Taipei")  # 台北時區


# 建立帶時區的 datetime 物件
d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00，含時區資訊


# 轉換時區
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 轉成印度加爾各答時區
print(d.astimezone(taipei))  # 轉成台北時區


# 取得當前 UTC 時間
now_utc = datetime.now(tz=utc)
print(now_utc)


# 最佳實踐：內部用 UTC，輸出時再轉本地時區
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 轉成芝加哥時區


# 查詢國家時區
tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']
