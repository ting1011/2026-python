# R7. OrderedDict（1.7）
# 保持插入順序的字典，適合需要順序的場合

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
json.dumps(d)  # 轉成 JSON 也會保留順序
