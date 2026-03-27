# test_classifier.py
# Phase 2: HandClassifier 牌型分類單元測試
# 含繁體中文註解
import unittest
from models import Card, Hand
from classifier import HandClassifier, CardType

class TestCardTypeEnum(unittest.TestCase):
    def test_cardtype_values(self):
        # 測試 CardType 列舉值
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)

class TestSingleClassify(unittest.TestCase):
    def test_classify_single_ace(self):
        h = Hand([Card(14, 3)])
        self.assertEqual(HandClassifier.classify(h), (CardType.SINGLE, 14, 3))
    def test_classify_single_two(self):
        h = Hand([Card(15, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.SINGLE, 15, 0))
    def test_classify_single_three(self):
        h = Hand([Card(3, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.SINGLE, 3, 0))

class TestPairClassify(unittest.TestCase):
    def test_classify_pair(self):
        h = Hand([Card(14, 3), Card(14, 2)])
        self.assertEqual(HandClassifier.classify(h), (CardType.PAIR, 14, 0))
    def test_classify_pair_diff_rank(self):
        h = Hand([Card(14, 3), Card(13, 3)])
        self.assertIsNone(HandClassifier.classify(h))
    def test_classify_pair_from_three(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])
        # 取前兩張
        self.assertEqual(HandClassifier.classify(Hand(h[:2])), (CardType.PAIR, 14, 0))

class TestTripleClassify(unittest.TestCase):
    def test_classify_triple(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(HandClassifier.classify(h), (CardType.TRIPLE, 14, 0))
    def test_classify_triple_not_enough(self):
        h = Hand([Card(14, 3), Card(14, 2)])
        self.assertIsNone(HandClassifier.classify(h))

class TestFiveCardClassify(unittest.TestCase):
    def test_classify_straight(self):
        h = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.STRAIGHT, 7, 0))
    def test_classify_straight_ace_low(self):
        h = Hand([Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.STRAIGHT, 5, 0))
    def test_classify_flush(self):
        h = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.FLUSH, 11, 0))
    def test_classify_full_house(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 1)])
        self.assertEqual(HandClassifier.classify(h), (CardType.FULL_HOUSE, 14, 0))
    def test_classify_four_of_a_kind(self):
        h = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)])
        self.assertEqual(HandClassifier.classify(h), (CardType.FOUR_OF_A_KIND, 14, 0))
    def test_classify_straight_flush(self):
        h = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)])
        self.assertEqual(HandClassifier.classify(h), (CardType.STRAIGHT_FLUSH, 7, 0))

class TestHandCompare(unittest.TestCase):
    def test_compare_single_rank(self):
        c1 = Hand([Card(14, 3)])
        c2 = Hand([Card(13, 3)])
        self.assertEqual(HandClassifier.compare(c1, c2), 1)
    def test_compare_single_suit(self):
        c1 = Hand([Card(14, 3)])
        c2 = Hand([Card(14, 2)])
        self.assertEqual(HandClassifier.compare(c1, c2), 1)

if __name__ == '__main__':
    unittest.main()
