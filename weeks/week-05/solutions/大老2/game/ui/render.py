"""Phase 6: Rendering Module"""

from typing import List, Tuple, Dict, Optional
from pathlib import Path
import pygame
from ..models import Card


class Renderer:
    """Renderer for Big Two game UI"""
    
    COLORS = {
        'bg_top': (20, 56, 77),
        'bg_bottom': (9, 28, 41),
        'panel': (13, 39, 55),
        'panel_border': (61, 115, 140),
        'panel_soft': (22, 61, 80),
        'card_front': (248, 245, 236),
        'card_back': (30, 125, 167),
        'card_back_line': (98, 181, 218),
        'text_dark': (24, 27, 31),
        'spade_club': (24, 27, 31),
        'heart_diamond': (182, 44, 44),
        'player': (76, 221, 138),
        'ai': (170, 186, 196),
        'selected': (242, 195, 61),
        'button_play': (34, 146, 98),
        'button_pass': (198, 95, 67),
        'button_text': (245, 248, 250),
        'text': (236, 242, 247),
    }
    
    CARD_WIDTH = 72
    CARD_HEIGHT = 108
    CARD_OVERLAP = 42
    QUALITY_SCALE = 2

    RANK_NAMES = {
        3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
        10: "10", 11: "J", 12: "Q", 13: "K", 14: "A", 15: "2"
    }

    SPRITE_COL_BY_RANK = {
        14: 0,  # A
        15: 1,  # 2
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11,
        13: 12,
    }
    
    def __init__(self, width: int = 1200, height: int = 800):
        """
        Initialize renderer.
        
        Args:
            width: Screen width
            height: Screen height
        """
        self.width = width
        self.height = height
        self.font_large = pygame.font.SysFont("georgia", 42, bold=True)
        self.font_medium = pygame.font.SysFont("trebuchetms", 24, bold=True)
        self.font_small = pygame.font.SysFont("trebuchetms", 18)
        self.font_card_rank = pygame.font.SysFont("trebuchetms", 28, bold=True)
        self.card_sheet: Optional[pygame.Surface] = None
        self.card_sheet_cols = 13
        self.card_sheet_rows = 5
        self.card_sheet_cell_w = 0
        self.card_sheet_cell_h = 0
        self.card_back_sprite: Optional[pygame.Surface] = None
        self.scaled_sprite_cache: Dict[Tuple[int, int, int], pygame.Surface] = {}
        self.vector_card_cache: Dict[Tuple[int, int, int], pygame.Surface] = {}
        self._load_card_sheet()

    def _load_card_sheet(self) -> None:
        """Load optional card sprite sheet from assets/cards.png."""
        base = Path(__file__).resolve().parents[2]
        candidate_paths = [
            base / "assets" / "cards.png",
            base / "assets" / "cards.jpg",
            base / "assets" / "cards.jpeg",
            base / "assets" / "cards.webp",
            base / "assets" / "playing-cards.png",
        ]

        for path in candidate_paths:
            if not path.exists():
                continue
            try:
                sheet = pygame.image.load(str(path)).convert_alpha()
                self.card_sheet = sheet
                self.card_sheet_cell_w = max(sheet.get_width() // self.card_sheet_cols, 1)
                self.card_sheet_cell_h = max(sheet.get_height() // self.card_sheet_rows, 1)

                # Prefer a dedicated back card from row 5 col 3 if present.
                back_row = min(4, self.card_sheet_rows - 1)
                back_col = min(2, self.card_sheet_cols - 1)
                self.card_back_sprite = self._sheet_cell(back_col, back_row)
                return
            except pygame.error:
                self.card_sheet = None
                self.card_back_sprite = None

    def _sheet_cell(self, col: int, row: int) -> Optional[pygame.Surface]:
        """Extract one cell image from sprite sheet."""
        if self.card_sheet is None:
            return None
        x = col * self.card_sheet_cell_w
        y = row * self.card_sheet_cell_h
        if x + self.card_sheet_cell_w > self.card_sheet.get_width() or y + self.card_sheet_cell_h > self.card_sheet.get_height():
            return None
        rect = pygame.Rect(x, y, self.card_sheet_cell_w, self.card_sheet_cell_h)
        return self.card_sheet.subsurface(rect).copy()

    def _get_card_sprite(self, card: Card) -> Optional[pygame.Surface]:
        """Map game card rank/suit to sprite sheet position."""
        if self.card_sheet is None:
            return None
        col = self.SPRITE_COL_BY_RANK.get(card.rank)
        if col is None:
            return None
        # Sheet order: clubs, diamonds, hearts, spades.
        row = card.suit
        return self._sheet_cell(col, row)

    def _scale_sprite(self, sprite: pygame.Surface, cache_key: Tuple[int, int, int]) -> pygame.Surface:
        """Scale sprite once and reuse it to keep quality stable and rendering smooth."""
        cached = self.scaled_sprite_cache.get(cache_key)
        if cached is not None:
            return cached

        # Two-stage upscale yields cleaner edges when source sprite is small.
        if sprite.get_width() < self.CARD_WIDTH or sprite.get_height() < self.CARD_HEIGHT:
            enlarged = pygame.transform.smoothscale(
                sprite,
                (self.CARD_WIDTH * self.QUALITY_SCALE, self.CARD_HEIGHT * self.QUALITY_SCALE),
            )
            scaled = pygame.transform.smoothscale(enlarged, (self.CARD_WIDTH, self.CARD_HEIGHT))
        else:
            scaled = pygame.transform.smoothscale(sprite, (self.CARD_WIDTH, self.CARD_HEIGHT))

        self.scaled_sprite_cache[cache_key] = scaled
        return scaled

    def _vector_card_surface(self, card: Card, faceup: bool) -> pygame.Surface:
        """Render vector card at higher internal resolution and scale down for sharper output."""
        cache_key = (card.rank, card.suit, 1 if faceup else 0)
        cached = self.vector_card_cache.get(cache_key)
        if cached is not None:
            return cached

        w = self.CARD_WIDTH * self.QUALITY_SCALE
        h = self.CARD_HEIGHT * self.QUALITY_SCALE
        hs = pygame.Surface((w, h), pygame.SRCALPHA)
        rect = pygame.Rect(0, 0, w, h)
        radius = max(8 * self.QUALITY_SCALE, 2)

        if not faceup:
            pygame.draw.rect(hs, self.COLORS['card_back'], rect, border_radius=radius)
            pygame.draw.rect(hs, self.COLORS['text'], rect, 2 * self.QUALITY_SCALE, border_radius=radius)
            spacing = max(6 * self.QUALITY_SCALE, 4)
            for line_x in range(8 * self.QUALITY_SCALE, w - 6 * self.QUALITY_SCALE, spacing):
                pygame.draw.line(
                    hs,
                    self.COLORS['card_back_line'],
                    (line_x, 6 * self.QUALITY_SCALE),
                    (line_x - 8 * self.QUALITY_SCALE, h - 6 * self.QUALITY_SCALE),
                    max(self.QUALITY_SCALE, 1),
                )
        else:
            pygame.draw.rect(hs, self.COLORS['card_front'], rect, border_radius=radius)
            pygame.draw.rect(hs, self.COLORS['text_dark'], rect, 2 * self.QUALITY_SCALE, border_radius=radius)

            if card.suit in [0, 3]:
                text_color = self.COLORS['spade_club']
            else:
                text_color = self.COLORS['heart_diamond']

            rank_text = self.RANK_NAMES.get(card.rank, "?")
            font_rank = pygame.font.SysFont("trebuchetms", 28 * self.QUALITY_SCALE, bold=True)
            rank_surface = font_rank.render(rank_text, True, text_color)
            hs.blit(rank_surface, (6 * self.QUALITY_SCALE, 4 * self.QUALITY_SCALE))

            corner_suit_size = max((self.CARD_WIDTH // 9) * self.QUALITY_SCALE, 5)
            self._draw_suit_icon(
                hs,
                card.suit,
                (14 * self.QUALITY_SCALE, 36 * self.QUALITY_SCALE),
                corner_suit_size,
                text_color,
            )

            center_suit_size = max((self.CARD_WIDTH // 5) * self.QUALITY_SCALE, 10)
            self._draw_suit_icon(
                hs,
                card.suit,
                (w // 2, (h // 2) + 12 * self.QUALITY_SCALE),
                center_suit_size,
                text_color,
            )

        final_surface = pygame.transform.smoothscale(hs, (self.CARD_WIDTH, self.CARD_HEIGHT))
        self.vector_card_cache[cache_key] = final_surface
        return final_surface

    def _draw_suit_icon(
        self,
        surface: pygame.Surface,
        suit: int,
        center: Tuple[int, int],
        size: int,
        color: Tuple[int, int, int],
    ) -> None:
        """Draw suit icon with vector shapes so symbols always appear."""
        cx, cy = center

        if suit == 1:  # Diamond
            points = [
                (cx, cy - size),
                (cx + size, cy),
                (cx, cy + size),
                (cx - size, cy),
            ]
            pygame.draw.polygon(surface, color, points)
            return

        if suit == 2:  # Heart
            radius = max(size // 2, 2)
            pygame.draw.circle(surface, color, (cx - radius, cy - radius), radius)
            pygame.draw.circle(surface, color, (cx + radius, cy - radius), radius)
            points = [
                (cx - size, cy - radius // 2),
                (cx + size, cy - radius // 2),
                (cx, cy + size),
            ]
            pygame.draw.polygon(surface, color, points)
            return

        if suit == 0:  # Club
            radius = max(size // 2, 2)
            pygame.draw.circle(surface, color, (cx, cy - radius), radius)
            pygame.draw.circle(surface, color, (cx - radius, cy + radius // 2), radius)
            pygame.draw.circle(surface, color, (cx + radius, cy + radius // 2), radius)
            pygame.draw.rect(surface, color, (cx - max(size // 6, 1), cy + radius, max(size // 3, 2), size))
            return

        # Spade
        radius = max(size // 2, 2)
        pygame.draw.circle(surface, color, (cx - radius, cy), radius)
        pygame.draw.circle(surface, color, (cx + radius, cy), radius)
        points = [
            (cx - size, cy + radius // 2),
            (cx + size, cy + radius // 2),
            (cx, cy - size),
        ]
        pygame.draw.polygon(surface, color, points)
        pygame.draw.rect(surface, color, (cx - max(size // 6, 1), cy + radius, max(size // 3, 2), size))

    def draw_background(self, surface: pygame.Surface) -> None:
        """Draw atmospheric gradient background with subtle table rails."""
        for y in range(self.height):
            ratio = y / max(self.height - 1, 1)
            r = int(self.COLORS['bg_top'][0] * (1 - ratio) + self.COLORS['bg_bottom'][0] * ratio)
            g = int(self.COLORS['bg_top'][1] * (1 - ratio) + self.COLORS['bg_bottom'][1] * ratio)
            b = int(self.COLORS['bg_top'][2] * (1 - ratio) + self.COLORS['bg_bottom'][2] * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (self.width, y))

        table_rect = pygame.Rect(30, 95, self.width - 60, self.height - 240)
        table_shadow = table_rect.move(0, 4)
        pygame.draw.rect(surface, (4, 17, 24), table_shadow, border_radius=26)
        pygame.draw.rect(surface, self.COLORS['panel'], table_rect, border_radius=26)
        pygame.draw.rect(surface, self.COLORS['panel_border'], table_rect, 2, border_radius=26)

        # Decorative rails to make the table look less flat.
        pygame.draw.ellipse(surface, self.COLORS['panel_soft'], (52, 114, self.width - 104, 26), 2)
        pygame.draw.ellipse(surface, self.COLORS['panel_soft'], (64, self.height - 180, self.width - 128, 22), 2)
    
    def draw_card(self, surface: pygame.Surface, card: Card, x: int, y: int, 
                  selected: bool = False, faceup: bool = True) -> None:
        """
        Draw a card on surface.
        
        Args:
            surface: Pygame surface
            card: Card to draw
            x: X position
            y: Y position
            selected: Whether card is selected
            faceup: Whether to show face (True) or back (False)
        """
        y_offset = -12 if selected else 0
        rect = pygame.Rect(x, y + y_offset, self.CARD_WIDTH, self.CARD_HEIGHT)
        shadow_rect = rect.move(2, 4)
        pygame.draw.rect(surface, (18, 18, 18), shadow_rect, border_radius=8)

        if self.card_sheet is not None:
            if faceup:
                sprite = self._get_card_sprite(card)
            else:
                sprite = self.card_back_sprite

            if sprite is not None:
                if faceup:
                    cache_key = (card.rank, card.suit, 1)
                else:
                    cache_key = (0, 0, 0)
                scaled = self._scale_sprite(sprite, cache_key)
                surface.blit(scaled, rect.topleft)
                if selected:
                    pygame.draw.rect(surface, self.COLORS['selected'], rect, 3, border_radius=8)
                return
        
        if not faceup:
            vector = self._vector_card_surface(card, False)
            surface.blit(vector, rect.topleft)
        else:
            vector = self._vector_card_surface(card, True)
            surface.blit(vector, rect.topleft)
        
        # Draw selection highlight
        if selected:
            pygame.draw.rect(surface, self.COLORS['selected'], rect, 3, border_radius=8)
    
    def draw_hand(self, surface: pygame.Surface, cards: List[Card], x: int, y: int,
                  selected_indices: List[int] = None) -> None:
        """
        Draw player's hand with overlapping cards.
        
        Args:
            surface: Pygame surface
            cards: Cards to draw
            x: X position (leftmost)
            y: Y position
            selected_indices: Indices of selected cards
        """
        if selected_indices is None:
            selected_indices = []
        
        card_width_per_card = self.CARD_WIDTH - self.CARD_OVERLAP
        
        for i, card in enumerate(cards):
            card_x = x + i * card_width_per_card
            card_y = y
            
            is_selected = i in selected_indices
            self.draw_card(surface, card, card_x, card_y, selected=is_selected, faceup=True)
    
    def draw_player_info(self, surface: pygame.Surface, name: str, hand_count: int,
                        x: int, y: int, is_current: bool = False, is_ai: bool = False) -> None:
        """
        Draw player information.
        
        Args:
            surface: Pygame surface
            name: Player name
            hand_count: Number of cards in hand
            x: X position
            y: Y position
            is_current: Whether this is current player
            is_ai: Whether this is AI player
        """
        panel = pygame.Rect(x, y, 212, 50)
        pygame.draw.rect(surface, (4, 18, 28), panel.move(0, 2), border_radius=12)
        pygame.draw.rect(surface, (7, 27, 40), panel, border_radius=12)
        pygame.draw.rect(surface, self.COLORS['panel_border'], panel, 2, border_radius=12)

        color = self.COLORS['player'] if not is_ai else self.COLORS['ai']
        if is_current:
            pygame.draw.circle(surface, self.COLORS['selected'], (x + 20, y + 28), 8)
        
        # Draw text
        role = "AI" if is_ai else "YOU"
        text = f"{name}  [{role}]  {hand_count} cards"
        text_surf = self.font_small.render(text, True, color)
        surface.blit(text_surf, (x + 34, y + 17))
    
    def draw_last_play(self, surface: pygame.Surface, cards: List[Card], 
                       player_name: str, x: int, y: int) -> None:
        """
        Draw the last play.
        
        Args:
            surface: Pygame surface
            cards: Cards from last play
            player_name: Name of player who made play
            x: X position
            y: Y position
        """
        panel_width = max(250, 24 + len(cards) * (self.CARD_WIDTH + 10))
        panel_height = self.CARD_HEIGHT + 56
        panel = pygame.Rect(x, y, panel_width, panel_height)
        pygame.draw.rect(surface, (4, 18, 28), panel.move(0, 3), border_radius=14)
        pygame.draw.rect(surface, (7, 27, 40), panel, border_radius=14)
        pygame.draw.rect(surface, self.COLORS['panel_border'], panel, 2, border_radius=14)

        title = self.font_small.render(f"Last Play: {player_name}", True, self.COLORS['text'])
        surface.blit(title, (x + 12, y + 10))
        
        # Draw cards
        for i, card in enumerate(cards):
            self.draw_card(surface, card, x + 12 + i * (self.CARD_WIDTH + 10), y + 42, faceup=True)
    
    def draw_button(self, surface: pygame.Surface, text: str, rect: pygame.Rect,
                   enabled: bool = True) -> None:
        """
        Draw a button.
        
        Args:
            surface: Pygame surface
            text: Button text
            rect: Button rectangle
            enabled: Whether button is enabled
        """
        if enabled:
            color = self.COLORS['button_play'] if text.lower() == 'play' else self.COLORS['button_pass']
        else:
            color = self.COLORS['ai']
        pygame.draw.rect(surface, (12, 22, 30), rect.move(0, 2), border_radius=10)
        pygame.draw.rect(surface, color, rect, border_radius=10)
        pygame.draw.rect(surface, self.COLORS['text'], rect, 2, border_radius=10)
        
        text_surf = self.font_medium.render(text, True, self.COLORS['button_text'])
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)
