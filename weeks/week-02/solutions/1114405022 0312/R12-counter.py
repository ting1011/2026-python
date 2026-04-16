
from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)
word_counts.most_common(3)

word_counts.update(['eyes', 'eyes'])
# R12. Counter 統計 + most_common（1.12）

from collections import Counter  # 匯入 Counter

# 統計單字出現次數
words = ['look', 'into', 'my', 'eyes', 'look']
word_counts = Counter(words)  # 得到每個單字的出現次數
word_counts.most_common(3)    # 取出出現最多的前三個單字

# 可以再更新計數
word_counts.update(['eyes', 'eyes'])  # 'eyes' 次數會再加 2
