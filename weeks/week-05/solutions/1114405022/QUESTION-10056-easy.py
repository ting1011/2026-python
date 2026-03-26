# UVA 10056 - 簡單解法
# 題目：機率計算問題
# 解法：直接套用機率公式
while True:
    try:
        n, p, i = map(float, input().split())
        if p == 0:
            print("0.0000")
            continue
        prob = (1-p)**(i-1) * p / (1-(1-p)**n)
        print(f"{prob:.4f}")
    except EOFError:
        break
