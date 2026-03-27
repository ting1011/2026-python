# test_game.py
# Phase 5: BigTwoGame 遊戲流程單元測試
# 含繁體中文註解
import unittest
from models import Card, Hand, Player
from game import BigTwoGame

class TestGameInit(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
    def test_game_has_4_players(self):
        self.assertEqual(len(self.game.players), 4)
    def test_each_player_13_cards(self):
        for p in self.game.players:
            self.assertEqual(len(p.hand), 13)
    def test_total_cards_distributed(self):
        total = sum(len(p.hand) for p in self.game.players)
        self.assertEqual(total, 52)
    def test_first_player_has_3_clubs(self):
        first = self.game.players[self.game.current_player]
        self.assertTrue(any(c.rank==3 and c.suit==0 for c in first.hand))
    def test_one_human_three_ai(self):
        ai_count = sum(1 for p in self.game.players if p.is_ai)
        self.assertEqual(ai_count, 3)

class TestPlayFlow(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
    def test_play_removes_cards(self):
        p = self.game.players[self.game.current_player]
        card = p.hand[0]
        before = len(p.hand)
        self.game.play([card])
        self.assertEqual(len(p.hand), before-1)
    def test_play_sets_last_play(self):
        p = self.game.players[self.game.current_player]
        card = p.hand[0]
        self.game.play([card])
        self.assertEqual(self.game.last_play, [card])
    def test_invalid_play(self):
        p = self.game.players[self.game.current_player]
        card = Card(99, 9)  # 不存在的牌
        result = self.game.play([card])
        self.assertFalse(result)
    def test_pass_increments(self):
        before = self.game.pass_count
        self.game.pass_turn()
        self.assertEqual(self.game.pass_count, before+1)

class TestRound(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
    def test_three_passes_resets(self):
        self.game.pass_count = 2
        self.game.pass_turn()
        self.assertEqual(self.game.last_play, None)
    def test_turn_rotates(self):
        before = self.game.current_player
        self.game.next_turn()
        self.assertEqual(self.game.current_player, (before+1)%4)

class TestWin(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
    def test_detect_winner(self):
        p = self.game.players[0]
        p.hand.clear()
        winner = self.game.check_winner()
        self.assertEqual(winner, p)
    def test_no_winner_yet(self):
        winner = self.game.check_winner()
        self.assertIsNone(winner)
    def test_game_ends(self):
        p = self.game.players[0]
        p.hand.clear()
        self.game.check_winner()
        self.assertTrue(self.game.is_game_over)

if __name__ == '__main__':
    unittest.main()
