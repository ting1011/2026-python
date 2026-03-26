# models.py
# Phase 1: Card, Deck, Hand, Player 類別實作
# 含繁體中文註解
import random

# 花色符號對應
SUITS = ['♣', '♦', '♥', '♠']
RANKS = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

class Card:
    """撲克牌物件，包含點數與花色"""
    def __init__(self, rank, suit):
        self.rank = rank  # 3-14, 14=A, 15=2
        self.suit = suit  # 0=♣,1=♦,2=♥,3=♠
    def __repr__(self):
        # 以花色+點數顯示
        rank_str = RANKS.get(self.rank, str(self.rank))
        return f"{SUITS[self.suit]}{rank_str}"
    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)
    def __lt__(self, other):
        # 先比點數，再比花色
        return (self.rank, self.suit) < (other.rank, other.suit)
    def __hash__(self):
        return hash((self.rank, self.suit))
    def to_sort_key(self):
        return (self.rank, self.suit)

class Deck:
    """一副 52 張牌的牌組"""
    def __init__(self):
        self.cards = self._create_cards()
    def _create_cards(self):
        # 產生 3~15 點數、4 種花色的 52 張牌
        return [Card(rank, suit) for rank in range(3, 15+1) for suit in range(4)]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, n):
        # 發 n 張牌，若不足則全部發完
        n = min(n, len(self.cards))
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt

class Hand(list):
    """手牌，繼承自 list"""
    def __init__(self, cards=None):
        super().__init__(cards or [])
    def sort_desc(self):
        # 依照點數大到小，花色小到大排序
        self.sort(key=lambda c: (-c.rank, c.suit))
    def find_3_clubs(self):
        # 找 3♣
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None
    def remove(self, cards):
        # 移除指定的牌（可單張或多張）
        if isinstance(cards, Card):
            cards = [cards]
        for card in cards:
            if card in self:
                super().remove(card)

class Player:
    """玩家物件"""
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0
    def take_cards(self, cards):
        # 拿牌到手牌
        self.hand.extend(cards)
    def play_cards(self, cards):
        # 出牌，從手牌移除
        self.hand.remove(cards)
        return cards
