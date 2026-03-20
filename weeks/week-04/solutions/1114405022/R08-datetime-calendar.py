
# R08. 日期範圍與字串轉換（3.14–3.15）
# 本範例示範 calendar.monthrange、strptime、strftime 等日期處理技巧


from datetime import datetime, date, timedelta  # 匯入日期時間相關類別
from calendar import monthrange  # 匯入 monthrange，取得每月天數


# ── 3.14 當月日期範圍 ─────────────────────────────────
# 取得某個月的起始與結束日期
def get_month_range(start: date | None = None) -> tuple[date, date]:
    if start is None:
        start = date.today().replace(day=1)  # 預設為本月第一天
    _, days = monthrange(start.year, start.month)  # 取得該月天數
    return start, start + timedelta(days=days)  # 回傳起始日與下個月第一天


first, last = get_month_range(date(2012, 8, 1))
print(first, "~", last - timedelta(days=1))  # 2012-08-01 ~ 2012-08-31，last 減一天才是當月最後一天


# 通用日期迭代生成器，可依 step 產生一連串日期
def date_range(start: datetime, stop: datetime, step: timedelta):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 9, 2), timedelta(hours=6)):
    print(d)  # 2012-09-01 00:00:00 / 06:00 / 12:00 / 18:00


# ── 3.15 字串轉換為日期 ───────────────────────────────
text = "2012-09-20"
dt = datetime.strptime(text, "%Y-%m-%d")  # 由字串轉 datetime
print(dt)  # 2012-09-20 00:00:00
print(datetime.strftime(dt, "%A %B %d, %Y"))  # 轉成指定格式字串 'Thursday September 20, 2012'


# 手動解析（比 strptime 快 7 倍）
def parse_ymd(s: str) -> datetime:
    y, m, d = s.split("-")  # 直接用 split 拆解
    return datetime(int(y), int(m), int(d))  # 組成 datetime


print(parse_ymd("2012-09-20"))  # 2012-09-20 00:00:00
