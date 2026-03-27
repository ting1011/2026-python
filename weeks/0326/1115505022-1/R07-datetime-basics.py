# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# timedelta 代表兩個時間點的差距，可用於加減日期
# days=2, hours=6 代表 2 天 6 小時
# hours=4.5 代表 4 小時 30 分

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b  # timedelta 可直接相加
print(c.days)  # 2，總共 2 天
print(c.total_seconds() / 3600)  # 58.5，總共 58.5 小時

dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00，日期加 10 天

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89，兩日期相減得到天數

# 閏年自動處理
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（2012 為閏年，2/28~3/1 跨 2 天）
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（2013 為平年，2/28~3/1 跨 1 天）

# ── 3.13 計算指定星期日期 ─────────────────────────────
# WEEKDAYS 列出星期名稱，方便查詢
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# get_previous_byday：取得某日期之前最近的指定星期幾
# dayname: 目標星期名稱
# start: 起始日期，預設為今天
# 回傳：最近的目標星期幾日期

def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    if start is None:
        start = datetime.today()
    day_num = start.weekday()  # 取得起始日期是星期幾（0=Monday）
    target = WEEKDAYS.index(dayname)  # 目標星期幾的索引
    days_ago = (7 + day_num - target) % 7 or 7  # 算出要往前幾天
    return start - timedelta(days=days_ago)  # 回傳結果

base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 2012-08-27，base 之前最近的週一
print(get_previous_byday("Friday", base))  # 2012-08-24，base 之前最近的週五
