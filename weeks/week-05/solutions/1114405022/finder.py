from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from .classifier import CardType, HandClassifier
from .models import Card, Hand


class HandFinder:
    @staticmethod
    def find_singles(hand: Hand) -> list[list[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> list[list[Card]]:
        by_rank: dict[int, list[Card]] = defaultdict(list)
        for card in hand:
            by_rank[card.rank].append(card)

        pairs: list[list[Card]] = []
        for cards in by_rank.values():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    pairs.append(list(pair))
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> list[list[Card]]:
        by_rank: dict[int, list[Card]] = defaultdict(list)
        for card in hand:
            by_rank[card.rank].append(card)

        triples: list[list[Card]] = []
        for cards in by_rank.values():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    triples.append(list(triple))
        return triples

    @staticmethod
    def find_fives(hand: Hand) -> list[list[Card]]:
        five_types = {
            CardType.STRAIGHT,
            CardType.FLUSH,
            CardType.FULL_HOUSE,
            CardType.FOUR_OF_A_KIND,
            CardType.STRAIGHT_FLUSH,
        }
        results: list[list[Card]] = []
        for combo in combinations(hand, 5):
            play = list(combo)
            info = HandClassifier.classify(play)
            if info and info[0] in five_types:
                results.append(play)
        return results

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> list[Card] | None:
        need = [start_rank + i for i in range(5)]
        if need == [14, 15, 16, 17, 18]:
            return None
        chosen: list[Card] = []
        for rank in need:
            candidates = [c for c in hand if c.rank == rank]
            if not candidates:
                return None
            chosen.append(max(candidates, key=lambda c: c.suit))
        return chosen

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: list[Card] | None) -> list[list[Card]]:
        if not hand:
            return []

        all_plays: list[list[Card]] = []
        all_plays.extend(HandFinder.find_singles(hand))
        all_plays.extend(HandFinder.find_pairs(hand))
        all_plays.extend(HandFinder.find_triples(hand))
        all_plays.extend(HandFinder.find_fives(hand))

        valid = [play for play in all_plays if HandClassifier.can_play(last_play, play)]
        valid.sort(key=lambda play: HandClassifier.classify(play) or (0, 0, 0))
        return valid
