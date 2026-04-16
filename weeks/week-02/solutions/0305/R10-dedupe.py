def dedupe(items):
def dedupe2(items, key=None):

# R10. 去重且保序（1.10）
# 本範例說明如何去除重複元素並保留原順序

def dedupe(items):
    seen = set()  # 用 set 記錄已出現過的元素
    for item in items:
        if item not in seen:
            yield item  # 首次出現才產生
            seen.add(item)

# 進階：可指定 key 進行去重
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)  # 依 key 決定去重依據
        if val not in seen:
            yield item
            seen.add(val)
