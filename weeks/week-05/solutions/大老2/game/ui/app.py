"""Phase 6: Main Application"""

import pygame
from typing import List
from .render import Renderer
from .input import InputHandler
from ..game import BigTwoGame


class BigTwoApp:
    """Main application for Big Two game"""
    
    def __init__(self, player_names: List[str] = None):
        """
        Initialize application.
        
        Args:
            player_names: List of player names
        """
        pygame.init()
        
        self.width = 960
        self.height = 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Big Two Card Game")
        
        self.renderer = Renderer(self.width, self.height)
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame(player_names)
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 30
    
    def setup(self) -> None:
        """Set up game"""
        self.game.setup()
    
    def handle_events(self) -> None:
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.input_handler.handle_event(event, self.game)
    
    def update(self) -> None:
        """Update game state"""
        if self.game.is_game_over():
            return
        
        player = self.game.get_current_player()
        
        if player.is_ai:
            self.game.ai_turn()
            self.game.next_turn()
    
    def draw(self) -> None:
        """Draw game state"""
        self.renderer.draw_background(self.screen)

        header = self.renderer.font_large.render("BIG TWO", True, self.renderer.COLORS['text'])
        self.screen.blit(header, (30, 20))
        status = self.renderer.font_small.render(
            f"Round {self.game.round_number}   Pass Count: {self.game.pass_count}",
            True,
            self.renderer.COLORS['text']
        )
        self.screen.blit(status, (34, 64))
        
        # Draw players
        player_y = 104
        player_panel_width = 212
        left_margin = 34
        available_width = self.width - left_margin * 2
        step_x = (available_width - player_panel_width) // max(len(self.game.players) - 1, 1)
        for i, player in enumerate(self.game.players):
            is_current = (i == self.game.current_player)
            player_x = left_margin + i * step_x
            
            self.renderer.draw_player_info(
                self.screen, player.name, len(player.hand),
                player_x, player_y,
                is_current=is_current, is_ai=player.is_ai
            )
        
        # Draw last play
        if self.game.last_play:
            cards, player_idx = self.game.last_play
            player_name = self.game.players[player_idx].name
            self.renderer.draw_last_play(self.screen, cards, player_name, 34, 188)
        
        # Draw current player's hand
        player = self.game.get_current_player()
        if not player.is_ai:
            hand_x = 40
            hand_y = self.height - self.renderer.CARD_HEIGHT - 68

            hand_title = self.renderer.font_small.render("Your Hand", True, self.renderer.COLORS['text'])
            self.screen.blit(hand_title, (hand_x, hand_y - 26))

            self.renderer.draw_hand(
                self.screen, player.hand, hand_x, hand_y,
                selected_indices=self.input_handler.selected_indices
            )
            
            # Draw buttons
            button_y = self.height - 54
            play_button = pygame.Rect(self.width - 220, button_y, 82, 36)
            pass_button = pygame.Rect(self.width - 128, button_y, 82, 36)
            
            self.input_handler.buttons = {
                'play': play_button,
                'pass': pass_button
            }
            
            self.renderer.draw_button(self.screen, "Play", play_button)
            self.renderer.draw_button(self.screen, "Pass", pass_button)
        
        # Draw game over message
        if self.game.is_game_over():
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 130))
            self.screen.blit(overlay, (0, 0))
            msg = f"{self.game.winner.name} wins!"
            text = self.renderer.font_large.render(msg, True, (255, 255, 0))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    def run(self) -> None:
        """Main game loop"""
        self.setup()
        
        while self.running and not self.game.is_game_over():
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        # Show final state briefly
        for _ in range(60):
            self.handle_events()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()


def main():
    """Entry point"""
    # Mix of human and AI players
    player_names = ['Player1', 'AI_1', 'AI_2', 'AI_3']
    app = BigTwoApp(player_names)
    app.run()


if __name__ == '__main__':
    main()
