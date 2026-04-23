from __future__ import annotations

from collections import Counter
from enum import IntEnum

from .models import Card


class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    @staticmethod
    def _is_straight(ranks: list[int]) -> bool:
        unique = sorted(set(ranks))
        if len(unique) != 5:
            return False
        if unique == [3, 4, 5, 14, 15]:
            return True
        return unique[-1] - unique[0] == 4 and all(
            unique[i] + 1 == unique[i + 1] for i in range(4)
        )

    @staticmethod
    def _is_flush(suits: list[int]) -> bool:
        return len(set(suits)) == 1

    @staticmethod
    def _straight_major(cards: list[Card]) -> tuple[int, int]:
        ranks = sorted(card.rank for card in cards)
        if ranks == [3, 4, 5, 14, 15]:
            candidates = [c for c in cards if c.rank == 5]
            best = max(candidates, key=lambda c: c.suit)
            return (5, best.suit)
        best = max(cards, key=lambda c: (c.rank, c.suit))
        return (best.rank, best.suit)

    @staticmethod
    def classify(cards: list[Card]):
        n = len(cards)
        if n == 0:
            return None

        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_counter = Counter(ranks)

        if n == 1:
            c = cards[0]
            return (CardType.SINGLE, c.rank, c.suit)

        if n == 2 and len(rank_counter) == 1:
            return (CardType.PAIR, cards[0].rank, max(suits))

        if n == 3 and len(rank_counter) == 1:
            return (CardType.TRIPLE, cards[0].rank, max(suits))

        if n != 5:
            return None

        is_flush = HandClassifier._is_flush(suits)
        is_straight = HandClassifier._is_straight(ranks)

        if is_flush and is_straight:
            major_rank, major_suit = HandClassifier._straight_major(cards)
            return (CardType.STRAIGHT_FLUSH, major_rank, major_suit)

        count_values = sorted(rank_counter.values(), reverse=True)
        if count_values == [4, 1]:
            four_rank = max(rank for rank, cnt in rank_counter.items() if cnt == 4)
            four_suit = max(c.suit for c in cards if c.rank == four_rank)
            return (CardType.FOUR_OF_A_KIND, four_rank, four_suit)

        if count_values == [3, 2]:
            triple_rank = max(rank for rank, cnt in rank_counter.items() if cnt == 3)
            triple_suit = max(c.suit for c in cards if c.rank == triple_rank)
            return (CardType.FULL_HOUSE, triple_rank, triple_suit)

        if is_flush:
            best = max(cards, key=lambda c: (c.rank, c.suit))
            return (CardType.FLUSH, best.rank, best.suit)

        if is_straight:
            major_rank, major_suit = HandClassifier._straight_major(cards)
            return (CardType.STRAIGHT, major_rank, major_suit)

        return None

    @staticmethod
    def compare(play1: list[Card], play2: list[Card]) -> int:
        c1 = HandClassifier.classify(play1)
        c2 = HandClassifier.classify(play2)

        if c1 is None and c2 is None:
            return 0
        if c1 is None:
            return -1
        if c2 is None:
            return 1

        if c1[0] != c2[0]:
            return 1 if c1[0] > c2[0] else -1

        if c1[1] != c2[1]:
            return 1 if c1[1] > c2[1] else -1

        if c1[2] != c2[2]:
            return 1 if c1[2] > c2[2] else -1

        return 0

    @staticmethod
    def can_play(last_play: list[Card] | None, cards: list[Card]) -> bool:
        current = HandClassifier.classify(cards)
        if current is None:
            return False

        if last_play is None:
            return len(cards) == 1 and cards[0].rank == 3 and cards[0].suit == 0

        prev = HandClassifier.classify(last_play)
        if prev is None:
            return False

        if len(cards) != len(last_play):
            return False

        return HandClassifier.compare(cards, last_play) == 1
