# TEST_CASES

## Case 1: Task 1 正常輸入
- 對應測試: `tests/test_task1.py::test_normal_case`
- 輸入: `5 3 5 2 9 2 8 3 1`
- 預期輸出:
  - `dedupe: 5 3 2 9 8 1`
  - `asc: 1 2 2 3 3 5 5 8 9`
  - `desc: 9 8 5 5 3 3 2 2 1`
  - `evens: 2 2 8`
- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: 去重改用保序方式，不用 set 直接輸出。

## Case 2: Task 1 邊界（空輸入）
- 對應測試: `tests/test_task1.py::test_empty_input`
- 輸入: 空字串
- 預期輸出: 四行都為空序列標籤
- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: `parse_numbers` 先判斷空字串。

## Case 3: Task 2 同分排序
- 對應測試: `tests/test_task2.py::test_tie_break_name`
- 輸入: `(c,88,19) (a,88,19) (b,88,19)`
- 預期輸出: `a, b, c`
- 實際輸出: `a, b, c`
- 結果: PASS
- 關鍵修改點: key 加入 name 當第三層排序。

## Case 4: Task 3 反例（空紀錄）
- 對應測試: `tests/test_task3.py::test_empty_logs`
- 輸入: `m = 0`
- 預期輸出:
  - 無使用者行
  - `top_action: none 0`
- 實際輸出: 與預期一致
- 結果: PASS
- 關鍵修改點: 空 Counter 時回傳 `(none, 0)`。

## Case 5: Task 3 最容易出錯（top action 同分）
- 對應測試: `tests/test_task3.py::test_top_action_tie`
- 輸入:
  - `u1 x`
  - `u2 y`
- 預期輸出: `top_action: x 1`（同分採字母序）
- 實際輸出: `top_action: x 1`
- 結果: PASS
- 關鍵修改點: top action 用 `(-count, action)` 排序規則。
