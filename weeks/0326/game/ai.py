# ai.py
# Phase 4: AI 策略實作
# 含繁體中文註解
from typing import List, Optional
from models import Card, Hand
from classifier import HandClassifier, CardType

class AIStrategy:
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
        t = HandClassifier.classify(cards)
        if t is None:
            return -float('inf')
        type_score = AIStrategy.TYPE_SCORES.get(t[0], 0)
        num_score = t[1]
        left = len(hand) - len(cards)
        bonus = 0
        if left == 0:
            bonus += AIStrategy.EMPTY_HAND_BONUS
        elif left <= 3:
            bonus += AIStrategy.NEAR_EMPTY_BONUS
        bonus += sum(AIStrategy.SPADE_BONUS for c in cards if c.suit == 3)
        return type_score * 100 + num_score * 10 + bonus

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        if is_first:
            for play in valid_plays:
                if any(c.rank == 3 and c.suit == 0 for c in play):
                    return play
            return None
        best = None
        best_score = -float('inf')
        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best = play
        return best
