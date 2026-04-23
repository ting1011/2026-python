from __future__ import annotations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class AIStrategy:
    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8,
    }

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def _is_first_turn_play(cards: list[Card]) -> bool:
        return len(cards) == 1 and cards[0].rank == 3 and cards[0].suit == 0

    @staticmethod
    def score_play(cards: list[Card], hand: Hand, is_first: bool = False) -> float:
        info = HandClassifier.classify(cards)
        if info is None:
            return float("-inf")

        if is_first and not AIStrategy._is_first_turn_play(cards):
            return float("-inf")

        card_type, major_rank, major_suit = info
        score = AIStrategy.TYPE_SCORES[card_type] * 100 + major_rank * 10 + major_suit

        remain = len(hand) - len(cards)
        if remain == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remain <= 3:
            score += AIStrategy.NEAR_EMPTY_BONUS

        score += sum(AIStrategy.SPADE_BONUS for c in cards if c.suit == 3)
        return float(score)

    @staticmethod
    def select_best(
        valid_plays: list[list[Card]], hand: Hand, is_first: bool = False
    ) -> list[Card] | None:
        if not valid_plays:
            return None

        plays = valid_plays
        if is_first:
            plays = [p for p in valid_plays if AIStrategy._is_first_turn_play(p)]
            if not plays:
                return None

        def key(play: list[Card]):
            info = HandClassifier.classify(play) or (0, 0, 0)
            return (
                AIStrategy.score_play(play, hand, is_first=is_first),
                len(play),
                info[0],
                info[1],
                info[2],
            )

        return max(plays, key=key)
