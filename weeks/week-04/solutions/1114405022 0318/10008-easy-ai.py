# UVA 10008: What's Cryptanalysis?（簡易版）
# 中文詳細註解

def letter_frequency(lines):
    freq = {}
    for line in lines:
        for c in line:
            if c.isalpha():
                c = c.upper()
                freq[c] = freq.get(c, 0) + 1
    # 依照出現次數（多到少），再依字母排序
    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return result

# 測試
if __name__ == "__main__":
    print(letter_frequency(["This is a test.", "Count letters!"]))
