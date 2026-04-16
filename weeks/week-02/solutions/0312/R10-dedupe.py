# R10. 去重且保序（1.10）
# 用生成器函式去除重複元素，且保留原本順序

def dedupe(items):
    seen = set()  # 用來記錄已出現過的元素
    for item in items:
        if item not in seen:
            yield item  # 只產生沒出現過的
            seen.add(item)

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 可自訂判斷重複的依據
        if val not in seen:
            yield item
            seen.add(val)
