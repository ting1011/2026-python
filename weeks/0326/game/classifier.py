# classifier.py
# Phase 2: HandClassifier 牌型分類實作
# 含繁體中文註解
from enum import IntEnum
from typing import List, Optional, Tuple
from models import Card, Hand

class CardType(IntEnum):
    SINGLE = 1        # 單張
    PAIR = 2          # 對子
    TRIPLE = 3        # 三條
    STRAIGHT = 4      # 順子
    FLUSH = 5         # 同花
    FULL_HOUSE = 6    # 葫蘆
    FOUR_OF_A_KIND = 7 # 四條
    STRAIGHT_FLUSH = 8 # 同花順

class HandClassifier:
    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        # 檢查是否為順子，需處理 A-2-3-4-5
        ranks = sorted(set(ranks))
        if len(ranks) != 5:
            return False
        # 一般順子
        if ranks[-1] - ranks[0] == 4:
            return True
        # 特殊：A-2-3-4-5
        if set(ranks) == {15, 3, 4, 5, 14}:
            return True
        return False

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        # 檢查是否為同花
        return len(set(suits)) == 1

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        n = len(cards)
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        rank_count = {r: ranks.count(r) for r in set(ranks)}
        # 單張
        if n == 1:
            return (CardType.SINGLE, ranks[0], suits[0])
        # 對子
        if n == 2 and len(rank_count) == 1:
            return (CardType.PAIR, ranks[0], 0)
        # 三條
        if n == 3 and len(rank_count) == 1:
            return (CardType.TRIPLE, ranks[0], 0)
        # 五張
        if n == 5:
            is_flush = HandClassifier._is_flush(suits)
            is_straight = HandClassifier._is_straight(ranks)
            if is_flush and is_straight:
                return (CardType.STRAIGHT_FLUSH, max(ranks), 0)
            if 4 in rank_count.values():
                for r, cnt in rank_count.items():
                    if cnt == 4:
                        return (CardType.FOUR_OF_A_KIND, r, 0)
            if sorted(rank_count.values()) == [2, 3]:
                for r, cnt in rank_count.items():
                    if cnt == 3:
                        return (CardType.FULL_HOUSE, r, 0)
            if is_flush:
                return (CardType.FLUSH, max(ranks), 0)
            if is_straight:
                return (CardType.STRAIGHT, max(ranks), 0)
        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        # 比較兩手牌大小
        t1 = HandClassifier.classify(play1)
        t2 = HandClassifier.classify(play2)
        if t1 is None or t2 is None:
            return 0
        # 先比牌型
        if t1[0] != t2[0]:
            return 1 if t1[0] > t2[0] else -1
        # 再比數字
        if t1[1] != t2[1]:
            return 1 if t1[1] > t2[1] else -1
        # 再比花色
        if t1[2] != t2[2]:
            return 1 if t1[2] > t2[2] else -1
        return 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        # 第一回合只能出3♣
        if last_play is None:
            return any(c.rank == 3 and c.suit == 0 for c in cards)
        # 需能大於上一手
        return HandClassifier.compare(cards, last_play) == 1
