"""
UVA 10101 標準解
七段顯示器木棒移動，檢查移動一根木棒後等式是否成立。
"""
# 先建立 0~9 的七段顯示器 bitmask 對照表
# 對每個數字的每一根木棒嘗試移動到其他數字，檢查移動後的等式是否成立

SEGMENTS = [0x7E,0x30,0x6D,0x79,0x33,0x5B,0x5F,0x70,0x7F,0x7B]  # 0~9
# 每個數字的七段顯示器 bitmask
#  a
# f b
#  g
# e c
#  d
# bit順序: gfedcba

# 預先計算所有一根木棒移動能變成的數字對
MOVE_MAP = {}
for i in range(10):
    for j in range(10):
        if i==j: continue
        diff = SEGMENTS[i]^SEGMENTS[j]
        # 只允許一根木棒移動: 兩個位元不同且一個1->0,一個0->1
        if bin(diff).count('1')==2:
            if bin(SEGMENTS[i]&diff).count('1')==1 and bin(SEGMENTS[j]&diff).count('1')==1:
                MOVE_MAP.setdefault(i,set()).add(j)

import re

def parse_expr(expr):
    # 解析數字與運算符
    tokens = re.findall(r'-?\d+|[+=-]', expr)
    return tokens

def eval_expr(tokens):
    # 計算等式左右兩邊的值
    eq = tokens.index('=')
    left = tokens[:eq]
    right = tokens[eq+1:]
    def calc(side):
        s = 0
        op = 1
        for t in side:
            if t=='+': op=1
            elif t=='-': op=-1
            else: s += op*int(t)
        return s
    return calc(left)==calc(right)

def try_move(expr):
    # 對每個數字的每一位嘗試移動
    tokens = parse_expr(expr)
    for idx, t in enumerate(tokens):
        if not t.lstrip('-').isdigit(): continue
        num = t.lstrip('-')
        sign = '-' if t.startswith('-') else ''
        for i, d in enumerate(num):
            d0 = int(d)
            for d1 in MOVE_MAP.get(d0, []):
                if d1==d0: continue
                new_num = num[:i]+str(d1)+num[i+1:]
                new_token = sign+new_num
                new_tokens = tokens[:idx]+[new_token]+tokens[idx+1:]
                if eval_expr(new_tokens):
                    # 重組字串
                    out = ''
                    j = 0
                    for tok in tokens:
                        if j==idx:
                            out += new_token
                        else:
                            out += tok
                        j += 1
                    return out+'#'
    return 'No'

if __name__ == "__main__":
    import sys
    line = sys.stdin.readline().strip()
    expr = line[:line.index('#')]
    print(try_move(expr))
