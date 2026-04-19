"""Phase 5: Game Logic"""

from typing import List, Optional, Tuple
from .models import Card, Deck, Hand, Player
from .classifier import HandClassifier
from .finder import HandFinder
from .ai import AIStrategy


class BigTwoGame:
    """Main game controller for Big Two"""
    
    def __init__(self, player_names: List[str] = None) -> None:
        """
        Initialize game.
        
        Args:
            player_names: List of player names (default: 4 AI players)
        """
        if player_names is None:
            player_names = ['AI_1', 'AI_2', 'AI_3', 'AI_4']
        
        self.deck = Deck()
        self.players: List[Player] = []
        for i, name in enumerate(player_names):
            is_ai = name.startswith('AI_')
            self.players.append(Player(name, is_ai))
        
        self.current_player = 0
        self.last_play: Optional[Tuple[List[Card], int]] = None  # (cards, player_index)
        self.pass_count = 0
        self.winner: Optional[Player] = None
        self.round_number = 0
        self.is_opening_turn = True
    
    def setup(self) -> None:
        """Set up the game: deal cards and find starting player"""
        self.deck = Deck()
        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1
        self.is_opening_turn = True

        for player in self.players:
            player.hand = Hand()

        self.deck.shuffle()
        
        # Deal 13 cards to each player
        for player in self.players:
            cards = self.deck.deal(13)
            player.take_cards(cards)
        
        # Find player with 3♣ to start
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                self.current_player = i
                break
    
    def play(self, player: Player, cards: List[Card]) -> bool:
        """
        Process a play.
        
        Args:
            player: Player making the play
            cards: Cards to play
            
        Returns:
            True if play was valid, False otherwise
        """
        if player not in self.players:
            return False

        if player != self.get_current_player():
            return False

        # All played cards must exist in player's hand.
        for card in cards:
            if card not in player.hand:
                return False
        
        if not self._is_valid_play(cards):
            return False
        
        # Opening play must include 3♣.
        if self.is_opening_turn:
            if not any(c.rank == 3 and c.suit == 0 for c in cards):
                return False
        
        # Remove cards from hand
        player.play_cards(cards)
        
        # Set as last play
        player_idx = self.players.index(player)
        self.last_play = (cards, player_idx)
        self.is_opening_turn = False
        
        # Reset pass count
        self.pass_count = 0
        
        # Check for winner
        if self.check_winner():
            self.winner = player
            return True
        
        return True
    
    def pass_(self, player: Player) -> bool:
        """
        Process a pass.
        
        Args:
            player: Player passing
            
        Returns:
            True if pass was valid, False otherwise
        """
        if player not in self.players:
            return False

        if player != self.get_current_player():
            return False
        
        if self.last_play is None:
            return False
        
        self.pass_count += 1
        
        # Check if round should reset
        self.check_round_reset()
        
        return True
    
    def _is_valid_play(self, cards: List[Card]) -> bool:
        """
        Check if a play is valid.
        
        Args:
            cards: Cards to play
            
        Returns:
            True if valid, False otherwise
        """
        if not cards:
            return False
        
        classification = HandClassifier.classify(cards)
        if classification is None:
            return False

        if self.last_play is None:
            # Leading play: any valid hand (opening-turn 3♣ checked in play()).
            return True

        return HandClassifier.can_play(self.last_play[0], cards)
    
    def check_round_reset(self) -> None:
        """Reset play if 3 players pass in a row"""
        if self.pass_count >= 3 and self.last_play is not None:
            self.last_play = None
            self.pass_count = 0
            self.round_number += 1
    
    def check_winner(self) -> bool:
        """
        Check if any player has won.
        
        Returns:
            True if there's a winner, False otherwise
        """
        current = self.get_current_player()
        if current and len(current.hand) == 0:
            self.winner = current
            return True
        return False
    
    def is_game_over(self) -> bool:
        """Check if game is over"""
        return self.winner is not None
    
    def get_current_player(self) -> Player:
        """Get the current player"""
        return self.players[self.current_player]
    
    def next_turn(self) -> None:
        """Move to next player's turn"""
        self.current_player = (self.current_player + 1) % len(self.players)
    
    def ai_turn(self) -> bool:
        """
        Execute AI turn.
        
        Returns:
            True if AI made a play, False if AI passed
        """
        player = self.get_current_player()
        
        if not player.is_ai:
            return False
        
        # Get valid plays
        valid_plays = HandFinder.get_all_valid_plays_with_opening(
            player.hand,
            self.last_play[0] if self.last_play else None,
            is_opening_turn=self.is_opening_turn,
        )
        
        if not valid_plays:
            # No valid play, must pass
            self.pass_(player)
            return False
        
        # Select best play
        is_first = self.last_play is None
        best_play = AIStrategy.select_best(valid_plays, player.hand, is_first)
        
        if best_play:
            self.play(player, best_play)
            return True
        else:
            self.pass_(player)
            return False
    
    def get_game_state(self) -> dict:
        """Get current game state"""
        return {
            'current_player': self.current_player,
            'round': self.round_number,
            'last_play': self.last_play,
            'pass_count': self.pass_count,
            'winner': self.winner,
            'players': [
                {
                    'name': p.name,
                    'hand_count': len(p.hand),
                    'is_ai': p.is_ai,
                    'score': p.score
                }
                for p in self.players
            ]
        }
