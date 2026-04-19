# TEST_LOG

## Run 1 (Red)
- 指令: `python -m unittest test_robot_core.py test_robot_scent.py -v`
- 測試數: 10
- 通過: 9
- 失敗: 1
- 問題: LOST 後仍繼續執行後續命令，導致方向被改動。
- 修改: 在 `execute_commands()` 中，當 `robot.lost` 時立即中斷迴圈。

## Run 2 (Green)
- 指令: `python -m unittest test_robot_core.py test_robot_scent.py -v`
- 測試數: 10
- 通過: 10
- 失敗: 0
- 結論: 旋轉、越界、scent、非法指令都通過。
