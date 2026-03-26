# UVA 10055 - 簡單解法
# 題目：計算兩個整數的差的絕對值
# 解法：直接輸出 abs(a-b)
def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(abs(a-b))
        except EOFError:
            break

if __name__ == "__main__":
    main()
