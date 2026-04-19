# TEST_CASES

## Case 1: N + L = W
- 輸入: 方向 `N`，命令 `L`
- 預期: `W`
- 實際: `W`
- 結果: PASS
- 對應測試: `test_n_plus_l_equals_w`

## Case 2: N + R = E
- 輸入: 方向 `N`，命令 `R`
- 預期: `E`
- 實際: `E`
- 結果: PASS
- 對應測試: `test_n_plus_r_equals_e`

## Case 3: 連續四次 R 回原方向
- 輸入: `N` + `RRRR`
- 預期: `N`
- 實際: `N`
- 結果: PASS
- 對應測試: `test_four_right_turns_back_to_origin_direction`

## Case 4: 邊界往外 F 會 LOST
- 輸入: 地圖 5x3，機器人 `(0,3,N)`，命令 `F`
- 預期: `LOST`，座標仍 `(0,3)`
- 實際: 符合
- 結果: PASS
- 對應測試: `test_forward_out_of_bounds_lost`

## Case 5: 邊界內移動不會 LOST
- 輸入: 地圖 5x3，機器人 `(1,1,N)`，命令 `F`
- 預期: `(1,2,N)` 且 ALIVE
- 實際: 符合
- 結果: PASS
- 對應測試: `test_forward_inside_bounds_not_lost`

## Case 6: 第一台越界留下 scent
- 輸入: `(0,3,N)` 執行 `F`
- 預期: scent 含 `(0,3,N)`
- 實際: 符合
- 結果: PASS
- 對應測試: `test_first_lost_leaves_scent`

## Case 7: 第二台同位同向忽略危險 F
- 輸入: 第二台 `(0,3,N)` 執行 `F`
- 預期: 不 LOST，位置不變
- 實際: 符合
- 結果: PASS
- 對應測試: `test_second_robot_ignores_same_dangerous_forward`

## Case 8: 同格不同向不共用 scent
- 輸入: `(0,3,E)` 執行 `F`
- 預期: 可移到 `(1,3)`
- 實際: 符合
- 結果: PASS
- 對應測試: `test_same_cell_different_direction_not_shared`

## Case 9: LOST 後停止後續命令
- 輸入: `(0,3,N)` + `FRFFLF`
- 預期: 一失足即停，方向保持 `N`
- 實際: 符合
- 結果: PASS
- 對應測試: `test_lost_robot_stops_following_commands`

## Case 10: 非法命令 X
- 輸入: 命令 `X`
- 預期: 拋出 `ValueError`
- 實際: 拋出 `ValueError`
- 結果: PASS
- 對應測試: `test_invalid_command_raises_error`
