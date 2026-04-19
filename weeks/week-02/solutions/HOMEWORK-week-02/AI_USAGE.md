# AI_USAGE

## 1) 我問了哪些問題
- Task 1 如何在不破壞順序下做去重？
- Task 2 多條件排序 key 應該怎麼寫最清楚？
- Task 3 如何在 action 次數同分時做穩定且可預期的輸出？
- unittest 測試如何覆蓋正常、邊界、反例？

## 2) 我採用的 AI 建議
- Task 1 使用 `seen` 集合 + `out` 串列做保序去重。
- Task 2 用 `sorted(..., key=lambda s: (-score, age, name))`。
- Task 3 用 `Counter` 做雙重統計，再用排序輸出。

## 3) 我拒絕的 AI 建議
- 拒絕「Task 1 直接用 `list(set(nums))`」: 會破壞第一次出現順序。
- 拒絕「Task 2 手寫冒泡排序」: 作業要求必須用 `sorted(key=...)`。

## 4) 一個 AI 可能誤導但我修正的案例
- 誤導點: AI 最初對 Task 3 空輸入建議輸出空字串，會讓格式不一致且難測試。
- 修正: 我改成固定輸出 `top_action: none 0`，測試與輸出格式都更穩定。
