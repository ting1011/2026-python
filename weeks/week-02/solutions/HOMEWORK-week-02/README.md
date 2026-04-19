# Week 02 Homework - HOMEWORK-week-02

## 1) 完成題目清單
- Task 1: Sequence Clean
- Task 2: Student Ranking
- Task 3: Log Summary

## 2) 執行方式
- Python 版本: Python 3.10+

程式執行指令:
- `python task1_sequence_clean.py`
- `python task2_student_ranking.py`
- `python task3_log_summary.py`

測試執行指令:
- `python -m unittest discover -s tests -p "test_*.py" -v`

## 3) 資料結構選擇理由
- Task 1: 使用 `list` 保存順序，搭配 `set` 做 O(1) 查找，達到保序去重。
- Task 2: 使用 tuple `(name, score, age)` 表示單筆學生資料，直接以 `sorted(key=...)` 實作多條件排序。
- Task 3: 使用 `Counter` 統計使用者次數與 action 次數，程式短且可讀性高。

## 4) 1 個錯誤與修正方式
- 錯誤: 一開始 Task 2 只用 `score` 排序，沒有處理同分 tie-break。
- 修正: 改成 `key=lambda s: (-s[1], s[2], s[0])`，依序處理分數、年齡、名字。

## 5) Red -> Green -> Refactor 摘要
- Task 1:
  - Red: 先寫 `test_dedupe_order`，初版誤用 set 造成順序錯誤。
  - Green: 改成 `seen + out` 流程後通過。
  - Refactor: 把解析、去重、格式化拆成函式，讓主流程更清楚。
- Task 2:
  - Red: `test_tie_break_name` 失敗，顯示 tie-break 不完整。
  - Green: 補齊三段排序規則後測試全綠。
  - Refactor: 抽出 `rank_students()`，I/O 與排序邏輯分離。
- Task 3:
  - Red: 空輸入時 top action 沒有定義，`test_empty_logs` 失敗。
  - Green: 定義空輸入回傳 `(none, 0)`。
  - Refactor: 先做統計再做排序輸出，結構更容易維護。
