# 計劃測試

def test_max():
    nums = [1, 5, 3, 9, 2]
    assert max(nums) == 9

def test_reverse():
    s = "hello"
    assert s[::-1] == "olleh"

if __name__ == "__main__":
    test_max()
    test_reverse()
    print("所有測試通過！")
