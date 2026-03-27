# test_models.py
# Phase 1: Card, Deck, Hand, Player 類別單元測試
# 含繁體中文註解
import unittest
from models import Card, Deck, Hand, Player

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        c = Card(14, 3)
        self.assertEqual(c.rank, 14)
        self.assertEqual(c.suit, 3)
    def test_card_repr_ace(self):
        c = Card(14, 3)
        self.assertEqual(repr(c), '♠A')
    def test_card_repr_three(self):
        c = Card(3, 0)
        self.assertEqual(repr(c), '♣3')
    def test_card_compare_suit(self):
        self.assertTrue(Card(14, 3) > Card(14, 2))
    def test_card_compare_suit_2(self):
        self.assertTrue(Card(14, 2) > Card(14, 1))
    def test_card_compare_suit_3(self):
        self.assertTrue(Card(14, 1) > Card(14, 0))
    def test_card_compare_rank_2(self):
        self.assertTrue(Card(15, 0) > Card(14, 3))
    def test_card_compare_rank_a(self):
        self.assertTrue(Card(14, 0) > Card(13, 3))
    def test_card_compare_equal(self):
        self.assertFalse(Card(14, 3) > Card(14, 3))
    def test_card_sort_key(self):
        c = Card(14, 3)
        self.assertEqual(c.to_sort_key(), (14, 3))

class TestDeck(unittest.TestCase):
    def test_deck_has_52_cards(self):
        d = Deck()
        self.assertEqual(len(d.cards), 52)
    def test_deck_all_unique(self):
        d = Deck()
        self.assertEqual(len(set(d.cards)), 52)
    def test_deck_all_ranks(self):
        d = Deck()
        ranks = set(card.rank for card in d.cards)
        self.assertEqual(ranks, set(range(3, 15+1)))
    def test_deck_all_suits(self):
        d = Deck()
        suits = set(card.suit for card in d.cards)
        self.assertEqual(suits, set(range(4)))
    def test_deck_shuffle(self):
        d = Deck()
        before = d.cards[:]
        d.shuffle()
        self.assertNotEqual(d.cards, before)
    def test_deal_5_cards(self):
        d = Deck()
        dealt = d.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(d.cards), 47)
    def test_deal_multiple(self):
        d = Deck()
        d.deal(5)
        d.deal(3)
        self.assertEqual(len(d.cards), 44)
    def test_deal_exceed(self):
        d = Deck()
        dealt = d.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(d.cards), 0)

class TestHand(unittest.TestCase):
    def test_hand_creation(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(14, 2)])
        self.assertEqual(len(h), 3)
    def test_hand_sort_desc(self):
        h = Hand([Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)])
        h.sort_desc()
        self.assertEqual([repr(c) for c in h], ['♠A', '♥K', '♠3', '♣3'])
    def test_hand_find_3_clubs(self):
        h = Hand([Card(14, 3), Card(3, 0), Card(3, 1)])
        c = h.find_3_clubs()
        self.assertEqual(repr(c), '♣3')
    def test_hand_find_3_clubs_none(self):
        h = Hand([Card(14, 3), Card(3, 1)])
        c = h.find_3_clubs()
        self.assertIsNone(c)
    def test_hand_remove(self):
        h = Hand([Card(3, 0), Card(14, 3)])
        h.remove(Card(3, 0))
        self.assertEqual(len(h), 1)
    def test_hand_remove_not_found(self):
        h = Hand([Card(3, 0)])
        h.remove(Card(14, 3))
        self.assertEqual(len(h), 1)

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        p = Player('AI', True)
        self.assertEqual(p.name, 'AI')
        self.assertTrue(p.is_ai)
        self.assertEqual(p.score, 0)
    def test_take_cards(self):
        p = Player('A')
        cards = [Card(3, 0), Card(14, 3)]
        p.take_cards(cards)
        self.assertEqual(len(p.hand), 2)
    def test_play_cards(self):
        p = Player('A')
        cards = [Card(3, 0), Card(14, 3)]
        p.take_cards(cards)
        played = p.play_cards(Card(3, 0))
        self.assertEqual(len(p.hand), 1)
        self.assertEqual(played, [Card(3, 0)])

if __name__ == '__main__':
    unittest.main()
