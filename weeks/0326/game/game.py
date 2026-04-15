# game.py
# Phase 5: BigTwoGame 遊戲流程控制
# 含繁體中文註解
from typing import List, Optional, Tuple
from models import Deck, Player, Card
from classifier import HandClassifier

class BigTwoGame:
    def __init__(self, player_names: List[str]):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 1

    def setup(self) -> None:
        self.deck.shuffle()
        # 發13張牌給每位玩家
        for i, player in enumerate(self.players):
            player.take_cards(self.deck.deal(13))
            player.hand.sort_desc()
        # 找3♣決定先手
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                self.current_player = i
                break
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1

    def play(self, player: Player, cards: List[Card]) -> bool:
        if not self._is_valid_play(cards):
            return False
        player.play_cards(cards)
        self.last_play = (cards, player.name)
        self.pass_count = 0
        self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        self.pass_count += 1
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def _is_valid_play(self, cards: List[Card]) -> bool:
        if self.last_play is None:
            return HandClassifier.can_play(None, cards)
        return HandClassifier.can_play(self.last_play[0], cards)

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    def check_winner(self) -> Optional[Player]:
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]
