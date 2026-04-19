# TEST_LOG

## Run 1 (Red)
- 指令:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- 測試摘要:
  - 總數: 9
  - 通過: 8
  - 失敗: 1
- 失敗原因摘要:
  - `test_empty_logs` 失敗，因為 Task 3 空輸入時沒有回傳可預期 top action。
- 修改內容:
  - 在 `summarize_logs()` 補上空輸入回傳 `(none, 0)`。

## Run 2 (Green)
- 指令:
  - `python -m unittest discover -s tests -p "test_*.py" -v`
- 測試摘要:
  - 總數: 9
  - 通過: 9
  - 失敗: 0
- 從失敗到通過的關鍵:
  - 補齊空輸入分支與輸出格式後，邊界測試通過，全部轉綠。
