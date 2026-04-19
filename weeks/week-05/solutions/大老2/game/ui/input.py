"""Phase 6: Input Handler"""

from typing import List, Dict, Optional, Tuple
import pygame
from ..models import Card
from ..finder import HandFinder
from ..classifier import HandClassifier


class InputHandler:
    """Handle player input"""
    
    def __init__(self, renderer):
        """
        Initialize input handler.
        
        Args:
            renderer: Renderer instance
        """
        self.renderer = renderer
        self.selected_indices: List[int] = []
        self.buttons: Dict[str, pygame.Rect] = {}
    
    def handle_event(self, event: pygame.event.EventType, game) -> bool:
        """
        Handle pygame event.
        
        Args:
            event: Pygame event
            game: Game instance
            
        Returns:
            True if event was handled, False otherwise
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        elif event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        
        return False
    
    def handle_click(self, pos: Tuple[int, int], game) -> bool:
        """
        Handle mouse click.
        
        Args:
            pos: Click position
            game: Game instance
            
        Returns:
            True if handled
        """
        player = game.get_current_player()
        
        if player.is_ai:
            return False
        
        # Check button clicks
        for button_name, button_rect in self.buttons.items():
            if button_rect.collidepoint(pos):
                if button_name == 'play':
                    return self.try_play(game)
                elif button_name == 'pass':
                    game.pass_(player)
                    game.next_turn()
                    return True
        
        # Check card clicks
        hand_y = self.renderer.height - self.renderer.CARD_HEIGHT - 68
        hand_x = 40
        
        card_width_per_card = self.renderer.CARD_WIDTH - self.renderer.CARD_OVERLAP

        # Hit-test from topmost (rightmost) card first to match visual stacking.
        for i in range(len(player.hand) - 1, -1, -1):
            card_x = hand_x + i * card_width_per_card

            # Selected cards are drawn slightly higher.
            y_offset = -12 if i in self.selected_indices else 0

            # In overlapped hands, each card owns only its visible slice,
            # except the last card which keeps full width.
            if i == len(player.hand) - 1:
                hit_width = self.renderer.CARD_WIDTH
            else:
                hit_width = card_width_per_card

            card_rect = pygame.Rect(
                card_x,
                hand_y + y_offset,
                hit_width,
                self.renderer.CARD_HEIGHT,
            )
            
            if card_rect.collidepoint(pos):
                if i in self.selected_indices:
                    self.selected_indices.remove(i)
                else:
                    self.selected_indices.append(i)
                return True
        
        return False
    
    def handle_key(self, key: int, game) -> bool:
        """
        Handle keyboard input.
        
        Args:
            key: Pygame key code
            game: Game instance
            
        Returns:
            True if handled
        """
        player = game.get_current_player()
        
        if player.is_ai:
            return False
        
        if key == pygame.K_RETURN:
            return self.try_play(game)
        elif key == pygame.K_p:
            game.pass_(player)
            game.next_turn()
            return True
        
        return False
    
    def try_play(self, game) -> bool:
        """
        Try to play selected cards.
        
        Args:
            game: Game instance
            
        Returns:
            True if play succeeded
        """
        player = game.get_current_player()
        
        if not self.selected_indices:
            return False
        
        selected_cards = [player.hand[i] for i in self.selected_indices]
        
        if game.play(player, selected_cards):
            self.selected_indices.clear()
            game.next_turn()
            return True
        
        return False
    
    def clear_selection(self) -> None:
        """Clear selected cards"""
        self.selected_indices.clear()
