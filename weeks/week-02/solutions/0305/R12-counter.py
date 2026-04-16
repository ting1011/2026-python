
# R12. Counter 統計 + most_common（1.12）
# 本範例說明 collections.Counter 的用法

from collections import Counter

# 1. 統計詞頻
words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)  # 回傳 dict: 單字為 key，出現次數為 value
word_counts.most_common(3)   # 取出現最多的前三個

# 2. 動態更新計數
word_counts.update(['eyes', 'eyes'])  # 將 'eyes' 次數再加 2
