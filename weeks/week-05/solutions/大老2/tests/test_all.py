"""Tests for Big Two Game"""

import unittest
from game.models import Card, Deck, Hand, Player
from game.classifier import CardType, HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class TestCard(unittest.TestCase):
    """Test Card class"""
    
    def test_card_creation(self):
        """Test card creation"""
        card = Card(14, 3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)
    
    def test_card_repr_ace(self):
        """Test ace representation"""
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")
    
    def test_card_repr_three(self):
        """Test 3 representation"""
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")
    
    def test_card_compare_suit(self):
        """Test suit comparison"""
        card1 = Card(14, 3)
        card2 = Card(14, 2)
        self.assertTrue(card1 > card2)
    
    def test_card_compare_rank(self):
        """Test rank comparison"""
        card1 = Card(15, 0)
        card2 = Card(14, 3)
        self.assertTrue(card1 > card2)
    
    def test_card_equality(self):
        """Test card equality"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(card1, card2)
    
    def test_card_hash(self):
        """Test card hash"""
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertEqual(hash(card1), hash(card2))


class TestDeck(unittest.TestCase):
    """Test Deck class"""
    
    def test_deck_has_52_cards(self):
        """Test deck initialization"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
    
    def test_deck_all_unique(self):
        """Test all cards are unique"""
        deck = Deck()
        unique_cards = set(deck.cards)
        self.assertEqual(len(unique_cards), 52)
    
    def test_deck_deal(self):
        """Test dealing cards"""
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)
    
    def test_deck_shuffle(self):
        """Test shuffle"""
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        # Very unlikely to shuffle to same order
        self.assertNotEqual(deck1.cards, deck2.cards)


class TestHand(unittest.TestCase):
    """Test Hand class"""
    
    def test_hand_creation(self):
        """Test hand creation"""
        cards = [Card(3, 0), Card(4, 1), Card(5, 2)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)
    
    def test_hand_find_3_clubs(self):
        """Test finding 3♣"""
        cards = [Card(14, 3), Card(3, 0), Card(5, 2)]
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)
        self.assertEqual(three_clubs.rank, 3)
        self.assertEqual(three_clubs.suit, 0)
    
    def test_hand_find_3_clubs_not_found(self):
        """Test 3♣ not found"""
        cards = [Card(14, 3), Card(5, 2)]
        hand = Hand(cards)
        three_clubs = hand.find_3_clubs()
        self.assertIsNone(three_clubs)
    
    def test_hand_remove(self):
        """Test removing cards"""
        cards = [Card(14, 3), Card(3, 0), Card(5, 2)]
        hand = Hand(cards)
        hand.remove([Card(3, 0)])
        self.assertEqual(len(hand), 2)


class TestClassifier(unittest.TestCase):
    """Test HandClassifier"""
    
    def test_classify_single(self):
        """Test single card classification"""
        cards = [Card(14, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
    
    def test_classify_pair(self):
        """Test pair classification"""
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)
    
    def test_classify_triple(self):
        """Test triple classification"""
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)
    
    def test_classify_straight(self):
        """Test straight classification"""
        cards = [Card(5, 0), Card(6, 1), Card(7, 2), Card(8, 3), Card(9, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
    
    def test_classify_flush(self):
        """Test flush classification"""
        cards = [Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(13, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FLUSH)


class TestPlayer(unittest.TestCase):
    """Test Player class"""
    
    def test_player_creation(self):
        """Test player creation"""
        player = Player("Player1")
        self.assertEqual(player.name, "Player1")
        self.assertFalse(player.is_ai)
    
    def test_player_ai(self):
        """Test AI player"""
        player = Player("AI_1", is_ai=True)
        self.assertTrue(player.is_ai)
    
    def test_player_take_cards(self):
        """Test taking cards"""
        player = Player("Player1")
        cards = [Card(3, 0), Card(5, 1)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)
    
    def test_player_play_cards(self):
        """Test playing cards"""
        player = Player("Player1")
        cards = [Card(3, 0), Card(5, 1), Card(7, 2)]
        player.take_cards(cards)
        played = player.play_cards([Card(5, 1)])
        self.assertEqual(len(player.hand), 2)
        self.assertEqual(len(played), 1)


class TestFinder(unittest.TestCase):
    """Test HandFinder"""
    
    def test_find_singles(self):
        """Test finding singles"""
        hand = Hand([Card(3, 0), Card(5, 1), Card(7, 2)])
        singles = HandFinder.find_singles(hand)
        self.assertEqual(len(singles), 3)
    
    def test_find_pairs(self):
        """Test finding pairs"""
        hand = Hand([Card(3, 0), Card(3, 1), Card(5, 2)])
        pairs = HandFinder.find_pairs(hand)
        self.assertEqual(len(pairs), 1)


class TestAI(unittest.TestCase):
    """Test AIStrategy"""
    
    def test_score_play(self):
        """Test scoring a play"""
        cards = [Card(14, 3)]
        hand = Hand([Card(5, 1), Card(7, 2)])
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, 0)
    
    def test_select_best(self):
        """Test selecting best play"""
        plays = [[Card(5, 0)], [Card(7, 1)]]
        hand = Hand([Card(14, 3)])
        best = AIStrategy.select_best(plays, hand)
        self.assertIsNotNone(best)


if __name__ == '__main__':
    unittest.main()
