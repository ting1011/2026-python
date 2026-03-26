# 更簡單的測試程式（無需 pytest）
def run_easy(inputs):
    lines = inputs.strip().split('\n')
    n = int(lines[0])
    idx = 1
    result = []
    for _ in range(n):
        days = int(lines[idx])
        p = int(lines[idx+1])
        parties = [int(lines[idx+2+i]) for i in range(p)]
        hartals = set()
        for h in parties:
            hartals.update(i for i in range(h, days+1, h) if i % 7 != 6 and i % 7 != 0)
        result.append(str(len(hartals)))
        idx += 2 + p
    return "\n".join(result)

# 測試資料
input_data = "1\n14\n3\n3\n4\n8"
expected = "5"
assert run_easy(input_data) == expected
print("測試通過！")
