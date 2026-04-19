"""Phase 3: Hand Finder"""

from typing import List, Optional
from itertools import combinations
from .models import Card, Hand
from .classifier import HandClassifier


class HandFinder:
    """Find valid plays from a hand"""
    
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        """
        Find all single card plays.
        
        Args:
            hand: Player's hand
            
        Returns:
            List of single card plays
        """
        return [[card] for card in hand]
    
    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        """
        Find all pair plays.
        
        Args:
            hand: Player's hand
            
        Returns:
            List of pair plays
        """
        pairs = []
        from collections import Counter
        rank_groups = {}
        
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    pairs.append(list(pair))
        
        return pairs
    
    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        """
        Find all triple plays.
        
        Args:
            hand: Player's hand
            
        Returns:
            List of triple plays
        """
        triples = []
        rank_groups = {}
        
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    triples.append(list(triple))
        
        return triples
    
    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        """
        Find a straight starting from specified rank.
        
        Args:
            hand: Player's hand
            start_rank: Starting rank
            
        Returns:
            List of 5 cards forming straight or None
        """
        # Create a map of cards by rank
        rank_map = {}
        for card in hand:
            if card.rank not in rank_map:
                rank_map[card.rank] = []
            rank_map[card.rank].append(card)
        
        # Try to build straight
        straight = []
        current_rank = start_rank
        
        # Special case: A-2-3-4-5
        if start_rank == 3:
            needed_ranks = [3, 4, 5, 14, 15]  # 3-4-5-A-2
        else:
            # Normal straight
            needed_ranks = list(range(current_rank, current_rank + 5))
            # Check if all ranks are valid (3-15)
            if any(r < 3 or r > 15 for r in needed_ranks):
                return None
        
        # Try to pick one card from each needed rank
        for rank in needed_ranks:
            if rank in rank_map and rank_map[rank]:
                straight.append(rank_map[rank].pop(0))
            else:
                return None
        
        # Restore rank_map
        for card in straight:
            if card.rank not in rank_map:
                rank_map[card.rank] = []
            rank_map[card.rank].append(card)
        
        return straight if len(straight) == 5 else None
    
    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        """
        Find all 5-card plays (straight, flush, full house, etc).
        
        Args:
            hand: Player's hand
            
        Returns:
            List of 5-card plays
        """
        fives = []
        
        # Get all 5-card combinations
        for combo in combinations(hand, 5):
            cards = list(combo)
            classification = HandClassifier.classify(cards)
            
            if classification is not None:
                fives.append(cards)
        
        return fives
    
    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        """
        Get all valid plays from hand.
        
        Args:
            hand: Player's hand
            last_play: The last play (None if first turn)
            
        Returns:
            List of valid plays
        """
        return HandFinder.get_all_valid_plays_with_opening(hand, last_play, is_opening_turn=False)

    @staticmethod
    def get_all_valid_plays_with_opening(
        hand: Hand,
        last_play: Optional[List[Card]],
        is_opening_turn: bool = False,
    ) -> List[List[Card]]:
        """
        Get all valid plays from hand with opening-turn awareness.

        Args:
            hand: Player's hand
            last_play: The last play on table
            is_opening_turn: True only for the very first play of the game

        Returns:
            List of valid plays
        """
        valid_plays = []

        # Leading turn (table empty)
        if last_play is None:
            all_plays = []
            all_plays.extend(HandFinder.find_singles(hand))
            all_plays.extend(HandFinder.find_pairs(hand))
            all_plays.extend(HandFinder.find_triples(hand))
            all_plays.extend(HandFinder.find_fives(hand))

            if is_opening_turn:
                for play in all_plays:
                    if any(card.rank == 3 and card.suit == 0 for card in play):
                        valid_plays.append(play)
                return valid_plays

            return all_plays
        
        # Find all possible plays by type
        all_plays = []
        
        last_class = HandClassifier.classify(last_play)
        if last_class is None:
            return []
        
        last_type = last_class[0]
        
        # Get plays of same type and count
        if last_type == 1:  # Single
            all_plays = HandFinder.find_singles(hand)
        elif last_type == 2:  # Pair
            all_plays = HandFinder.find_pairs(hand)
        elif last_type == 3:  # Triple
            all_plays = HandFinder.find_triples(hand)
        elif last_type == 4 or last_type == 5 or last_type == 6 or last_type == 7 or last_type == 8:  # 5-card hands
            all_plays = HandFinder.find_fives(hand)
        
        # Filter by valid plays
        for play in all_plays:
            if HandClassifier.can_play(last_play, play):
                valid_plays.append(play)
        
        return valid_plays
