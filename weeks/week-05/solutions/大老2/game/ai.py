"""Phase 4: AI Strategy"""

from typing import List, Optional
from .models import Card, Hand
from .classifier import CardType, HandClassifier


class AIStrategy:
    """AI strategy for choosing plays"""
    
    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8
    }
    
    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5
    
    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        """
        Score a play based on strategy.
        
        Args:
            cards: Cards to play
            hand: Current hand (after removing played cards)
            is_first: Whether this is the first play
            
        Returns:
            Score (higher is better)
        """
        classification = HandClassifier.classify(cards)
        
        if classification is None:
            return -1000
        
        card_type, rank_value, suit_value = classification
        
        # Type score
        type_score = AIStrategy.TYPE_SCORES.get(card_type, 0) * 100
        
        # Rank score
        rank_score = rank_value * 10
        
        # Calculate remaining cards after this play
        remaining = len(hand)
        
        # Remaining bonus
        remaining_bonus = 0
        if remaining == 1:
            remaining_bonus = AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 3:
            remaining_bonus = AIStrategy.NEAR_EMPTY_BONUS
        
        # Spade bonus
        spade_bonus = 0
        for card in cards:
            if card.suit == 3:  # Spade
                spade_bonus += AIStrategy.SPADE_BONUS
        
        total_score = type_score + rank_score + remaining_bonus + spade_bonus
        
        return total_score
    
    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        """
        Select the best play using greedy strategy.
        
        Args:
            valid_plays: List of valid plays
            hand: Current hand
            is_first: Whether this is the first play
            
        Returns:
            Best play or None if no valid plays
        """
        if not valid_plays:
            return None
        
        if is_first:
            # Opening play must include 3♣.
            for play in valid_plays:
                for card in play:
                    if card.rank == 3 and card.suit == 0:
                        return play
            return None
        
        # Score each play
        best_play = None
        best_score = -float('inf')
        
        for play in valid_plays:
            # Create hand after removing played cards
            remaining_hand = Hand([card for card in hand if card not in play])
            
            score = AIStrategy.score_play(play, remaining_hand, is_first)
            
            if score > best_score:
                best_score = score
                best_play = play
        
        return best_play
