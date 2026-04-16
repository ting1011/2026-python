
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
# R10. 去重且保序（1.10）

# 去除重複元素，並保留原本順序
def dedupe(items):
    seen = set()  # 用來記錄已出現過的元素
    for item in items:
        if item not in seen:
            yield item  # 第一次出現才回傳
            seen.add(item)

# 可自訂 key 來判斷重複
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 若有 key 則用 key(item) 判斷
        if val not in seen:
            yield item
            seen.add(val)
