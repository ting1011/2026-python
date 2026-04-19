# Week 03 - Robot Lost (homework-week03)

## 功能清單
- 核心規則：L / R / F、LOST、scent（`robot_core.py`）
- 視覺互動：pygame 格子、機器人、scent、鍵盤控制（`robot_game.py`）
- 狀態控制：新機器人（N）、清除 scent（C）

## 執行方式
- Python 3.10+
- 安裝 pygame：`python -m pip install pygame`
- 啟動遊戲：`python robot_game.py`

## 測試方式
- 指令：`python -m unittest test_robot_core.py test_robot_scent.py -v`
- 目前測試共 10 個，覆蓋旋轉、越界、scent、非法指令。

## 資料結構選擇理由
- 使用 `set[tuple[int,int,str]]` 存 scent，查找 O(1)，適合判斷危險前進是否應忽略。
- 使用 `Robot` dataclass 存狀態，欄位清楚可讀，測試好寫。
- 使用 `World` 物件集中地圖邊界與 scent，避免畫面程式直接碰核心判定。

## 我踩到的一個 bug 與修正
- bug：最初版本在 LOST 後仍繼續執行後續指令，造成方向被改變。
- 修正：在 `execute_commands()` 每步後檢查 `robot.lost`，一旦 LOST 立即 `break`。

## 操作鍵
- `L` / `R` / `F`：執行一步
- `N`：新機器人（保留 scent）
- `C`：清除 scent
- `ESC`：離開

## 重播說明
- 目前提供命令歷史列（HUD 的 `History`），可回看操作序列。
- 若要輸出 GIF，可沿用你 week-02 的 `make_circle_replay.py` 方式加上逐幀輸出。
