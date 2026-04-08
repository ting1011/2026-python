"""
UVA 10101 更簡易記憶版
暴力嘗試每個數字的每一根木棒移動到其他數字，僅適合理解題意與小型測資。
"""
# 這個方法直接枚舉所有數字的每一位，嘗試所有一根木棒移動的可能，並檢查等式是否成立
# 適合理解題意與小型資料測試
SEGMENTS = [0x7E,0x30,0x6D,0x79,0x33,0x5B,0x5F,0x70,0x7F,0x7B]
MOVE_MAP = {}
for i in range(10):
    for j in range(10):
        if i==j: continue
        diff = SEGMENTS[i]^SEGMENTS[j]
        if bin(diff).count('1')==2:
            if bin(SEGMENTS[i]&diff).count('1')==1 and bin(SEGMENTS[j]&diff).count('1')==1:
                MOVE_MAP.setdefault(i,set()).add(j)
import re

def try_move_easy(expr):
    tokens = re.findall(r'-?\d+|[+=-]', expr)
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
                eq = new_tokens.index('=')
                left = new_tokens[:eq]
                right = new_tokens[eq+1:]
                def calc(side):
                    s = 0
                    op = 1
                    for t in side:
                        if t=='+': op=1
                        elif t=='-': op=-1
                        else: s += op*int(t)
                    return s
                if calc(left)==calc(right):
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
    print(try_move_easy(expr))
