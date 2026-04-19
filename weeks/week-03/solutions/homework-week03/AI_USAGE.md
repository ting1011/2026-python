# AI_USAGE

## 我問 AI 的問題
1. scent 為什麼要記錄 `(x, y, dir)` 而不是只記 `(x, y)`？
2. 如何把核心邏輯與 pygame 畫面解耦，讓測試可以純跑邏輯？
3. LOST 後應該在哪一層停止指令（單步函式還是批次執行）？
4. 非法指令建議忽略還是丟例外？

## 我採用的建議與原因
- 採用 `(x, y, dir)` 作為 scent key，符合 UVA 118 規則，避免錯誤共享。
- 採用 `robot_core.py` / `robot_game.py` 分離，讓測試不依賴 pygame。
- 採用 `ValueError` 處理非法指令，測試能明確驗證錯誤。

## 我拒絕的建議與原因
- 拒絕「非法指令直接忽略」：會讓錯誤輸入默默被吞掉，不利除錯。
- 拒絕「把 scent 放在 Robot 內」：scent 是全域世界規則，不屬於單一機器人。

## 一個 AI 建議不完整、我自行修正的案例
- 不完整建議：只在 `execute_command()` 判斷 LOST，但沒處理批次指令的中斷。
- 我的修正：在 `execute_commands()` 加入 `if robot.lost: break`，保證 LOST 後不再執行後續命令。
