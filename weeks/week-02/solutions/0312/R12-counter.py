# R12. Counter 統計 + most_common（1.12）
# 用 Counter 統計元素出現次數，可快速取得最常見元素

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)  # 統計每個單字出現次數
word_counts.most_common(3)    # 出現最多的前三個

word_counts.update(['eyes', 'eyes'])  # 動態更新計數
