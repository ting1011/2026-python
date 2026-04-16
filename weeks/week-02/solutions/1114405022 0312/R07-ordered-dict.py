
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
json.dumps(d)
# R7. OrderedDict（1.7）

from collections import OrderedDict  # 匯入 OrderedDict
import json  # 匯入 json 模組

# 建立一個有順序的字典
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2  # 依序加入 foo, bar
json.dumps(d)  # 轉成 json 字串時會保留順序
