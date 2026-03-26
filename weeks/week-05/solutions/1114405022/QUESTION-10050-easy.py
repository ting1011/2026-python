# UVA 10050 - 簡單解法
# 題目：計算在一段天數內，有多少天會被至少一個政黨罷工
# 解法：用集合記錄所有罷工日，排除每7天的假日
n = int(input())
for _ in range(n):
    days = int(input())
    p = int(input())
    parties = [int(input()) for _ in range(p)]
    hartals = set()
    for h in parties:
        hartals.update(i for i in range(h, days+1, h) if i % 7 != 6 and i % 7 != 0)
    print(len(hartals))
