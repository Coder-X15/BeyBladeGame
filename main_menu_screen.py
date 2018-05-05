import os
import pygame
from screen import Screen
from globals import *


class MainMenuScreen(Screen):
    def __init__(self, logger):
        super().__init__(logger=logger.getChild(__name__))
        self._background_surf = None

    def on_init(self):
        super().on_init()
        self._background_surf = pygame.image.load(os.path.join(graphics_path, "beyblade_logo.png")).convert_alpha()
        self._background_surf = pygame.transform.scale(self._background_surf, (WIDTH, HEIGHT))
        return True

    def on_loop(self):
        pass

    def on_render(self):
        # self._display_surf.fill(black)  # clear screen
        self._display_surf.blit(self._background_surf, (0, 0))
        pygame.display.update()
        # pygame.display.flip()
        pass
