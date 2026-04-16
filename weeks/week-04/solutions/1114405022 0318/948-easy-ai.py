# UVA 948: Fibonaccimal Base（簡易版）
# 中文詳細註解

def fibonaccimal_base(n):
    fibs = [1, 2]
    # 產生所有不超過 n 的費波那契數
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    res = []
    # 由大到小檢查每個費波那契數
    for f in reversed(fibs):
        if n >= f:
            res.append('1')  # 需要這個費波那契數
            n -= f
        else:
            res.append('0')  # 不需要
    return ''.join(res).lstrip('0')

# 測試
if __name__ == "__main__":
    print(fibonaccimal_base(100))  # 應輸出 100010010
