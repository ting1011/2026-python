from __future__ import annotations

import random
from typing import Iterable


class Card:
    """Single playing card used in Big Two."""

    RANK_STR = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A",
        15: "2",
    }
    SUIT_STR = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        rank_text = self.RANK_STR.get(self.rank, str(self.rank))
        return f"{self.SUIT_STR[self.suit]}{rank_text}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: "Card") -> bool:
        return (self.rank, self.suit) < (other.rank, other.suit)

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)


class Deck:
    """52-card deck for Big Two."""

    def __init__(self):
        self.cards = self._create_cards()

    def _create_cards(self) -> list[Card]:
        return [Card(rank, suit) for rank in range(3, 16) for suit in range(4)]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self, n: int) -> list[Card]:
        n = max(0, min(n, len(self.cards)))
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    """Player hand with helper methods."""

    def __init__(self, cards: Iterable[Card] | None = None):
        super().__init__(cards or [])

    def sort_desc(self) -> None:
        self.sort(key=lambda c: (c.rank, c.suit), reverse=True)

    def find_3_clubs(self) -> Card | None:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards):
        if isinstance(cards, Card):
            cards_to_remove = [cards]
        else:
            cards_to_remove = list(cards)
        for card in cards_to_remove:
            if card in self:
                super().remove(card)


class Player:
    """Game player."""

    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: Iterable[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: Iterable[Card]) -> list[Card]:
        played = list(cards)
        self.hand.remove(played)
        return played
