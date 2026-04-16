# 272_handwrite.py
"""
UVA 272 題目：TEX Quotes
手打版（依 AI 版抄寫）
繁體中文詳細註解
"""

def tex_quotes(text: str) -> str:
    """
    將輸入的文字中的雙引號（"）依照 TEX Quotes 規則轉換：
    - 第一個 " 轉成 ``
    - 第二個 " 轉成 ''
    - 依此類推交替
    """
    result = []
    open_quote = True
    for ch in text:
        if ch == '"':
            if open_quote:
                result.append('``')
            else:
                result.append("''")
            open_quote = not open_quote
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    # 範例測試
    sample = '"To be or not to be," quoth the Bard. "That is the question."'
    print(tex_quotes(sample))
