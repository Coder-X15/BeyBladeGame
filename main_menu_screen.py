import os
import pygame
from screen import Screen
from globals import *


class MainMenuScreen(Screen):
    def __init__(self, display_surf, logger):
        super().__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._background_surf = pygame.image.load(os.path.join(graphics_path, "beyblade_logo.png")).convert_alpha()
        self._background_surf = pygame.transform.scale(self._background_surf, (WIDTH, HEIGHT))

    def on_update(self):
        pass

    def on_render(self):
        # self._display_surf.fill(black)  # clear screen
        self._display_surf.blit(self._background_surf, (0, 0))
        super().on_render()

    def on_exit(self):
        self._running = False
        from battle_screen import BattleScreen
        self._next_screen = BattleScreen
