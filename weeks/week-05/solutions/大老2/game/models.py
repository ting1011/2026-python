"""Phase 1: Data Models - Card, Deck, Hand, Player"""

from typing import List, Optional, Tuple
import random


class Card:
    """Playing card with rank and suit"""
    
    # Class attributes for card representation
    RANK_NAMES = {
        3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'
    }
    
    SUIT_SYMBOLS = {
        0: '♣', 1: '♦', 2: '♥', 3: '♠'
    }
    
    def __init__(self, rank: int, suit: int) -> None:
        """
        Initialize a card.
        
        Args:
            rank: int (3-14, where 14=A, 15=2)
            suit: int (0=♣, 1=♦, 2=♥, 3=♠)
        """
        self.rank = rank
        self.suit = suit
    
    def __repr__(self) -> str:
        """Return string representation in format: ♠A"""
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_NAMES[self.rank]}"
    
    def __eq__(self, other: 'Card') -> bool:
        """Check if two cards are equal"""
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other: 'Card') -> bool:
        """Compare cards: first by rank (descending in game logic), then by suit (ascending)"""
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit
    
    def __hash__(self) -> int:
        """Return hash value"""
        return hash((self.rank, self.suit))
    
    def to_sort_key(self) -> Tuple[int, int]:
        """Return tuple for sorting"""
        return (self.rank, self.suit)


class Deck:
    """Deck of 52 playing cards"""
    
    def __init__(self) -> None:
        """Initialize deck with 52 cards"""
        self.cards: List[Card] = self._create_cards()
    
    def _create_cards(self) -> List[Card]:
        """Create all 52 cards"""
        cards = []
        for suit in range(4):
            for rank in range(3, 16):  # rank: 3-15 (3 to 2)
                cards.append(Card(rank, suit))
        return cards
    
    def shuffle(self) -> None:
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def deal(self, n: int) -> List[Card]:
        """
        Deal n cards from the deck.
        
        Args:
            n: Number of cards to deal
            
        Returns:
            List of cards dealt (may be less than n if deck has fewer cards)
        """
        dealt = []
        for _ in range(min(n, len(self.cards))):
            dealt.append(self.cards.pop(0))
        return dealt


class Hand(list):
    """Player's hand of cards (inherits from list)"""
    
    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        """
        Initialize hand.
        
        Args:
            cards: List of cards (optional)
        """
        if cards is None:
            cards = []
        super().__init__(cards)
    
    def sort_desc(self) -> None:
        """Sort hand by rank (descending), then by suit (ascending)"""
        # In game logic: 2 > A > K > ... > 3
        # So we need to convert ranks to game order first
        game_rank_order = {15: 14, 14: 13, 13: 12, 12: 11, 11: 10, 10: 9, 9: 8, 8: 7, 7: 6, 6: 5, 5: 4, 4: 3, 3: 2}
        self.sort(key=lambda card: (-game_rank_order[card.rank], card.suit))
    
    def find_3_clubs(self) -> Optional[Card]:
        """Find and return 3♣ (rank=3, suit=0)"""
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None
    
    def remove(self, cards: List[Card]) -> None:
        """
        Remove specified cards from hand.
        
        Args:
            cards: List of cards to remove
        """
        for card in cards:
            if card in self:
                list.remove(self, card)


class Player:
    """Game player"""
    
    def __init__(self, name: str, is_ai: bool = False) -> None:
        """
        Initialize player.
        
        Args:
            name: Player name
            is_ai: Whether this is an AI player
        """
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    
    def take_cards(self, cards: List[Card]) -> None:
        """
        Add cards to player's hand.
        
        Args:
            cards: List of cards to add
        """
        self.hand.extend(cards)
    
    def play_cards(self, cards: List[Card]) -> List[Card]:
        """
        Play (remove) cards from hand.
        
        Args:
            cards: Cards to play
            
        Returns:
            The cards played
        """
        self.hand.remove(cards)
        return cards
