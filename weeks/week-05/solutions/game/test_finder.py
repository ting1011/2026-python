# test_finder.py
# Phase 3: HandFinder 牌型搜尋單元測試
# 含繁體中文註解
import unittest
from models import Card, Hand
from finder import HandFinder

class TestFindSingles(unittest.TestCase):
    def test_find_singles(self):
        hand = Hand([Card(14,3), Card(13,2), Card(3,0)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)  # 3個單張
    def test_find_singles_empty(self):
        hand = Hand([])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 0)

class TestFindPairs(unittest.TestCase):
    def test_find_pairs_one(self):
        hand = Hand([Card(14,3), Card(14,2), Card(3,0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)
    def test_find_pairs_two(self):
        hand = Hand([Card(14,3), Card(14,2), Card(13,3), Card(13,0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 2)
    def test_find_pairs_none(self):
        hand = Hand([Card(14,3), Card(13,2), Card(3,0)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 0)

class TestFindTriples(unittest.TestCase):
    def test_find_triples_one(self):
        hand = Hand([Card(14,3), Card(14,2), Card(14,1), Card(3,0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)
    def test_find_triples_with_extra(self):
        hand = Hand([Card(14,3), Card(14,2), Card(14,1), Card(13,3), Card(13,0)])
        triples = HandFinder.find_triples(hand)
        self.assertEqual(len(triples), 1)

class TestFindFiveCardTypes(unittest.TestCase):
    def test_find_straight(self):
        hand = Hand([Card(3,0), Card(4,1), Card(5,2), Card(6,3), Card(7,0)])
        straights = HandFinder.find_straights(hand)
        self.assertTrue(any([set([3,4,5,6,7]) == set(c.rank for c in s) for s in straights]))
    def test_find_flush(self):
        hand = Hand([Card(3,0), Card(5,0), Card(7,0), Card(9,0), Card(11,0)])
        flushes = HandFinder.find_flushes(hand)
        self.assertTrue(any([all(c.suit==0 for c in f) for f in flushes]))
    def test_find_full_house(self):
        hand = Hand([Card(14,3), Card(14,2), Card(14,1), Card(15,0), Card(15,1)])
        full_houses = HandFinder.find_full_houses(hand)
        self.assertTrue(len(full_houses) > 0)
    def test_find_four_of_a_kind(self):
        hand = Hand([Card(14,3), Card(14,2), Card(14,1), Card(14,0), Card(3,1)])
        fours = HandFinder.find_four_of_a_kind(hand)
        self.assertTrue(len(fours) > 0)
    def test_find_straight_flush(self):
        hand = Hand([Card(3,0), Card(4,0), Card(5,0), Card(6,0), Card(7,0)])
        straight_flushes = HandFinder.find_straight_flushes(hand)
        self.assertTrue(len(straight_flushes) > 0)

class TestValidPlays(unittest.TestCase):
    def test_first_turn(self):
        hand = Hand([Card(3,0), Card(14,3)])
        valid = HandFinder.valid_plays(hand, last_play=None)
        self.assertTrue(any(Card(3,0) in v for v in valid))
    def test_with_last_single(self):
        hand = Hand([Card(5,0), Card(14,3)])
        last = Hand([Card(5,2)])
        valid = HandFinder.valid_plays(hand, last_play=last)
        self.assertTrue(all(len(v)==1 for v in valid))
    def test_with_last_pair(self):
        hand = Hand([Card(5,0), Card(5,1), Card(14,3)])
        last = Hand([Card(5,2), Card(5,3)])
        valid = HandFinder.valid_plays(hand, last_play=last)
        self.assertTrue(all(len(v)==2 for v in valid))
    def test_no_valid(self):
        hand = Hand([Card(3,0)])
        last = Hand([Card(15,3)])
        valid = HandFinder.valid_plays(hand, last_play=last)
        self.assertEqual(len(valid), 0)

if __name__ == '__main__':
    unittest.main()
