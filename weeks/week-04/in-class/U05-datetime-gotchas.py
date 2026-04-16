
"""
U05. 日期時間的陷阱（3.12–3.15）
本檔案示範：
1. timedelta 不能直接加月份
2. 如何正確加一個月
3. strptime 效能問題與手動解析
"""

import timeit
import calendar
from datetime import datetime, timedelta


# ── timedelta 不支援月份（3.12）──────────────────────
# datetime/timedelta 不能直接加月份
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument



# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:
        year += 1
        month = 1

    # 取得目標月份的天數，並把日期限制在該月最後一天
    _, days_in_target_month = calendar.monthrange(year, month)
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)



# 範例：加一個月，遇到月底自動調整
print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23


# ── strptime 效能問題（3.15）─────────────────────────
# 產生大量日期字串
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]



# 用 strptime 解析日期字串
def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")



# 手動 split 解析日期字串，效能較佳
def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))



# 驗證兩種解析方式結果一致
assert use_strptime("2012-09-20") == use_manual("2012-09-20")


# 效能比較：strptime 與手動 split
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
