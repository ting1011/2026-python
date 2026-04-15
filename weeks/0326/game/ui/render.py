# ui/render.py
# Phase 6: GUI 渲染器
# 含繁體中文註解
import pygame

class Renderer:
    COLORS = {
        'background': (45,45,45),
        'card_back': (74,144,217),
        'spade_club': (255,255,255),
        'heart_diamond': (231,76,60),
        'player': (46,204,113),
        'ai': (149,165,166),
        'selected': (241,196,15),
        'button': (52,152,219)
    }
    CARD_WIDTH = 60
    CARD_HEIGHT = 90

    def draw_card(self, screen, card, x, y, selected=False):
        # 畫單張牌
        color = self.COLORS['selected'] if selected else self.COLORS['card_back']
        pygame.draw.rect(screen, color, (x, y, self.CARD_WIDTH, self.CARD_HEIGHT))
        # ...可加上數字/花色顯示...

    def draw_hand(self, screen, hand, x, y, selected_indices):
        # 畫手牌
        for i, card in enumerate(hand):
            self.draw_card(screen, card, x + i*30, y, i in selected_indices)

    def draw_player(self, screen, player, x, y, is_current):
        # 畫玩家名稱
        color = self.COLORS['player'] if is_current else self.COLORS['ai']
        # ...畫名字...

    def draw_last_play(self, screen, cards, player_name, x, y):
        # 畫上家出牌
        # ...畫牌...
        pass

    def draw_buttons(self, screen, buttons, x, y):
        # 畫按鈕
        # ...畫按鈕...
        pass
