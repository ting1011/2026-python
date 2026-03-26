# 更簡單的測試程式（無需 pytest）
def run_easy(inputs):
    n, *rest = map(int, inputs.split())
    idx = 0
    result = []
    for _ in range(n):
        r = rest[idx]
        houses = sorted(rest[idx+1:idx+1+r])
        median = houses[r // 2]
        total = sum(abs(h - median) for h in houses)
        result.append(str(total))
        idx += 1 + r
    return "\n".join(result)

# 測試資料
input_data = "2 2 2 4 3 2 4 6"
expected = "2\n4"
assert run_easy(input_data) == expected
print("測試通過！")
