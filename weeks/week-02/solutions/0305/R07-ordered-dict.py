
# R7. OrderedDict（1.7）
# 本範例說明 collections.OrderedDict 的用法

from collections import OrderedDict
import json

# 建立有順序的字典
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2  # 依加入順序儲存
json.dumps(d)  # 轉成 JSON 也會保留順序
