# 272_easy.py
"""
UVA 272 題目：TEX Quotes
AI 版（簡單易懂）
繁體中文詳細註解
"""

def tex_quotes(text: str) -> str:
    """
    將輸入的文字中的雙引號（"）依照 TEX Quotes 規則轉換：
    - 第一個 " 轉成 ``
    - 第二個 " 轉成 ''
    - 依此類推交替
    """
    result = []  # 用來儲存轉換後的字元
    open_quote = True  # 標記目前遇到的是開頭還是結尾的引號
    for ch in text:
        if ch == '"':
            if open_quote:
                result.append('``')  # 開頭引號
            else:
                result.append("''")  # 結尾引號
            open_quote = not open_quote  # 交替狀態
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    # 範例測試
    sample = '"To be or not to be," quoth the Bard. "That is the question."'
    print(tex_quotes(sample))
