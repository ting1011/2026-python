# test_ai.py
# Phase 4: AIStrategy 策略單元測試
# 含繁體中文註解
import unittest
from models import Card, Hand
from ai import AIStrategy

class TestAIStrategy(unittest.TestCase):
    def test_score_play_single(self):
        hand = Hand([Card(3,0), Card(14,3)])
        score = AIStrategy.score_play([Card(14,3)], hand)
        self.assertTrue(isinstance(score, float) or isinstance(score, int))
    def test_score_play_empty_bonus(self):
        hand = Hand([Card(3,0)])
        score = AIStrategy.score_play([Card(3,0)], hand)
        self.assertTrue(score >= 10000)
    def test_score_play_spade_bonus(self):
        hand = Hand([Card(3,0), Card(14,3)])
        score = AIStrategy.score_play([Card(14,3)], hand)
        self.assertTrue(score % 10 >= 5)  # 有♠加分
    def test_select_best_first(self):
        hand = Hand([Card(3,0), Card(14,3)])
        valid = [[Card(3,0)], [Card(14,3)]]
        best = AIStrategy.select_best(valid, hand, is_first=True)
        self.assertEqual(best, [Card(3,0)])
    def test_select_best_greedy(self):
        hand = Hand([Card(3,0), Card(14,3)])
        valid = [[Card(3,0)], [Card(14,3)]]
        best = AIStrategy.select_best(valid, hand)
        self.assertEqual(best, [Card(14,3)])

if __name__ == '__main__':
    unittest.main()
