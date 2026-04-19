"""Phase 2: Hand Classification"""

from enum import IntEnum
from typing import List, Optional, Tuple
from collections import Counter
from .models import Card


class CardType(IntEnum):
    """Card hand types"""
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    """Classify and compare card hands"""
    
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        """
        Check if ranks form a straight.
        
        Args:
            ranks: List of 5 ranks
            
        Returns:
            True if straight, False otherwise
        """
        if len(ranks) != 5:
            return False
        
        sorted_ranks = sorted(ranks)
        
        # Check normal straight
        if sorted_ranks[-1] - sorted_ranks[0] == 4 and len(set(sorted_ranks)) == 5:
            return True
        
        # Check special case: A-2-3-4-5 (ranks: 14-15-3-4-5)
        if set(sorted_ranks) == {3, 4, 5, 14, 15}:
            return True
        
        return False
    
    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        """
        Check if all cards have the same suit.
        
        Args:
            suits: List of suits
            
        Returns:
            True if flush, False otherwise
        """
        return len(set(suits)) == 1
    
    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        """
        Classify a hand of cards.
        
        Args:
            cards: List of cards to classify
            
        Returns:
            Tuple of (CardType, rank_value, suit_value) or None if not classifiable
        """
        n = len(cards)
        
        if n == 0:
            return None
        
        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        rank_counts = Counter(ranks)
        
        # Single card
        if n == 1:
            return (CardType.SINGLE, ranks[0], suits[0])
        
        # Pair
        if n == 2:
            if len(set(ranks)) == 1:
                return (CardType.PAIR, ranks[0], max(suits))
            return None
        
        # Triple
        if n == 3:
            if len(set(ranks)) == 1:
                return (CardType.TRIPLE, ranks[0], max(suits))
            return None
        
        # Five cards
        if n == 5:
            is_flush = HandClassifier._is_flush(suits)
            is_straight = HandClassifier._is_straight(ranks)
            
            # Straight Flush
            if is_straight and is_flush:
                max_rank = max(ranks)
                # Special case: A-2-3-4-5
                if set(ranks) == {3, 4, 5, 14, 15}:
                    max_rank = 5  # In this case, 5 is the high card
                return (CardType.STRAIGHT_FLUSH, max_rank, suits[0])
            
            # Four of a kind
            if 4 in rank_counts.values():
                quad_rank = [r for r, c in rank_counts.items() if c == 4][0]
                kicker = [r for r, c in rank_counts.items() if c == 1][0]
                return (CardType.FOUR_OF_A_KIND, quad_rank, max(suits))
            
            # Full House (3 + 2)
            if 3 in rank_counts.values() and 2 in rank_counts.values():
                triple_rank = [r for r, c in rank_counts.items() if c == 3][0]
                pair_rank = [r for r, c in rank_counts.items() if c == 2][0]
                return (CardType.FULL_HOUSE, triple_rank, max(suits))
            
            # Flush
            if is_flush:
                max_rank = max(ranks)
                return (CardType.FLUSH, max_rank, suits[0])
            
            # Straight
            if is_straight:
                max_rank = max(ranks)
                # Special case: A-2-3-4-5
                if set(ranks) == {3, 4, 5, 14, 15}:
                    max_rank = 5
                return (CardType.STRAIGHT, max_rank, max(suits))
        
        return None
    
    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        """
        Compare two plays.
        
        Args:
            play1: First play
            play2: Second play
            
        Returns:
            1 if play1 > play2, -1 if play2 > play1, 0 if tie
        """
        class1 = HandClassifier.classify(play1)
        class2 = HandClassifier.classify(play2)
        
        if class1 is None and class2 is None:
            return 0
        if class1 is None:
            return -1
        if class2 is None:
            return 1
        
        type1, rank1, suit1 = class1
        type2, rank2, suit2 = class2
        
        # Different card types
        if type1 != type2:
            return 1 if type1 > type2 else -1
        
        # Same type, compare rank
        if rank1 != rank2:
            return 1 if rank1 > rank2 else -1
        
        # Same rank, compare suit
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1
        
        return 0
    
    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        """
        Check if cards can be played.
        
        Args:
            last_play: The last play (None if first turn)
            cards: Cards to play
            
        Returns:
            True if valid play, False otherwise
        """
        # No table play yet: any valid classified hand can lead.
        if last_play is None:
            return HandClassifier.classify(cards) is not None
        
        # Classify both hands
        last_class = HandClassifier.classify(last_play)
        curr_class = HandClassifier.classify(cards)
        
        if curr_class is None:
            return False
        if last_class is None:
            return False
        
        # Must be same type and same count
        if len(cards) != len(last_play):
            return False
        
        if last_class[0] != curr_class[0]:
            return False
        
        # Must be better
        return HandClassifier.compare(cards, last_play) > 0
