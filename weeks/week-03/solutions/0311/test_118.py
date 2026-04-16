# 測試程式（含中文註解）
import unittest
from 118_easy import move_robot

class TestUVA118(unittest.TestCase):
    def test_sample(self):
        grid = (5, 3)
        lost_set = set()
        # 測試範例一
        x, y, dir, lost = move_robot('RFRFRFRF', 1, 1, 'E', grid, lost_set)
        self.assertEqual((x, y, dir, lost), (1, 1, 'E', False))
        # 測試範例二
        lost_set.clear()
        x, y, dir, lost = move_robot('FRRFLLFFRRFLL', 3, 2, 'N', grid, lost_set)
        self.assertEqual((x, y, dir, lost), (3, 3, 'N', True))
        # 測試範例三
        lost_set.clear()
        x, y, dir, lost = move_robot('LLFFFLFLFL', 0, 3, 'W', grid, lost_set)
        self.assertEqual((x, y, dir, lost), (2, 3, 'S', False))

if __name__ == "__main__":
    unittest.main()
