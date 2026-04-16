# UVA 10035: Primary Arithmetic（簡易版）
# 中文詳細註解

def carry_count(a, b):
    a = str(a)[::-1]
    b = str(b)[::-1]
    carry = 0
    cnt = 0
    for i in range(max(len(a), len(b))):
        d1 = int(a[i]) if i < len(a) else 0
        d2 = int(b[i]) if i < len(b) else 0
        if d1 + d2 + carry >= 10:
            carry = 1
            cnt += 1
        else:
            carry = 0
    return cnt

# 測試
if __name__ == "__main__":
    print(carry_count(555, 555))  # 3
