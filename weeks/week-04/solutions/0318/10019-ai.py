# UVA 10019: Funny Encryption Method
# 中文註解版

def count_ones(n):
    # 十進位轉二進位後 1 的個數
    b1 = bin(n).count('1')
    # 十進位每一位數字轉成 4 位二進位後 1 的個數
    b2 = sum(bin(int(d)).count('1') for d in str(n))
    return b1, b2

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        b1, b2 = count_ones(n)
        print(f"{b1} {b2}")
