# 490_easy.py
"""
UVA 490 題目：Rotating Sentences
AI 版（簡單易懂）
繁體中文詳細註解
"""

def rotate_sentences(lines):
    """
    將多行字串順時針旋轉 90 度
    lines: List[str]，每行一個字串
    回傳：List[str]，旋轉後的結果
    """
    if not lines:
        return []
    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines]
    rotated = []
    for i in range(max_len):
        new_line = ''.join(row[i] for row in reversed(padded))
        rotated.append(new_line)
    return rotated

if __name__ == "__main__":
    # 範例測試
    input_lines = [
        "Hello World!",
        "This is a test.",
        "Rotate me!"
    ]
    for line in rotate_sentences(input_lines):
        print(line)
