# finder.py
# Phase 3: HandFinder 牌型搜尋實作
# 含繁體中文註解
from itertools import combinations
from typing import List, Optional
from models import Card, Hand
from classifier import HandClassifier

class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        # 回傳所有單張
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        # 找所有對子
        pairs = []
        rank_groups = {}
        for card in hand:
            rank_groups.setdefault(card.rank, []).append(card)
        for group in rank_groups.values():
            if len(group) >= 2:
                for comb in combinations(group, 2):
                    pairs.append(list(comb))
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        # 找所有三條
        triples = []
        rank_groups = {}
        for card in hand:
            rank_groups.setdefault(card.rank, []).append(card)
        for group in rank_groups.values():
            if len(group) >= 3:
                for comb in combinations(group, 3):
                    triples.append(list(comb))
        return triples

    @staticmethod
    def find_straights(hand: Hand) -> List[List[Card]]:
        # 找所有順子（含 A-2-3-4-5）
        cards = sorted(hand, key=lambda c: (c.rank, c.suit))
        unique = {(c.rank, c.suit): c for c in cards}.values()
        ranks = sorted(set(c.rank for c in unique))
        straights = []
        for i in range(len(ranks) - 4):
            seq = ranks[i:i+5]
            if seq[-1] - seq[0] == 4:
                straight = [next(c for c in unique if c.rank == r) for r in seq]
                straights.append(straight)
        # 處理 A-2-3-4-5
        if set([15, 14, 3, 4, 5]).issubset(ranks):
            straight = [next(c for c in unique if c.rank == r) for r in [15, 14, 3, 4, 5]]
            straights.append(straight)
        return straights

    @staticmethod
    def find_flushes(hand: Hand) -> List[List[Card]]:
        # 找所有同花
        suit_groups = {}
        for card in hand:
            suit_groups.setdefault(card.suit, []).append(card)
        flushes = []
        for group in suit_groups.values():
            if len(group) >= 5:
                for comb in combinations(group, 5):
                    flushes.append(list(comb))
        return flushes

    @staticmethod
    def find_full_houses(hand: Hand) -> List[List[Card]]:
        # 找所有葫蘆（三條+對子）
        triples = HandFinder.find_triples(hand)
        pairs = HandFinder.find_pairs(hand)
        full_houses = []
        for t in triples:
            for p in pairs:
                if t[0].rank != p[0].rank:
                    full_houses.append(t + p)
        return full_houses

    @staticmethod
    def find_four_of_a_kind(hand: Hand) -> List[List[Card]]:
        # 找所有四條
        fours = []
        rank_groups = {}
        for card in hand:
            rank_groups.setdefault(card.rank, []).append(card)
        for group in rank_groups.values():
            if len(group) >= 4:
                for comb in combinations(group, 4):
                    # 加一張其他牌
                    rest = [c for c in hand if c.rank != comb[0].rank]
                    if rest:
                        for r in rest:
                            fours.append(list(comb) + [r])
        return fours

    @staticmethod
    def find_straight_flushes(hand: Hand) -> List[List[Card]]:
        # 找所有同花順
        flushes = HandFinder.find_flushes(hand)
        straight_flushes = []
        for f in flushes:
            if HandClassifier._is_straight([c.rank for c in f]):
                straight_flushes.append(f)
        return straight_flushes

    @staticmethod
    def valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        # 根據上家牌型，回傳所有合法出牌
        valid = []
        if last_play is None:
            # 第一回合只能出3♣
            for c in hand:
                if c.rank == 3 and c.suit == 0:
                    valid.append([c])
            return valid
        n = len(last_play)
        if n == 1:
            valid = HandFinder.find_singles(hand)
        elif n == 2:
            valid = HandFinder.find_pairs(hand)
        elif n == 3:
            valid = HandFinder.find_triples(hand)
        elif n == 5:
            valid = (HandFinder.find_straights(hand) +
                     HandFinder.find_flushes(hand) +
                     HandFinder.find_full_houses(hand) +
                     HandFinder.find_four_of_a_kind(hand) +
                     HandFinder.find_straight_flushes(hand))
        # 過濾掉不能大於上家的
        valid = [v for v in valid if HandClassifier.compare(v, last_play) == 1]
        return valid
