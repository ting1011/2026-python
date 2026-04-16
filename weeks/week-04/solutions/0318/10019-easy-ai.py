# UVA 10019: Funny Encryption Method（簡易版）
# 中文詳細註解

def count_ones(n):
    b1 = bin(n).count('1')
    b2 = sum(bin(int(d)).count('1') for d in str(n))
    return b1, b2

# 測試
if __name__ == "__main__":
    print(count_ones(265))  # (5, 5)
