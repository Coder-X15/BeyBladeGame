import random
import pygame
import os
from screen import Screen
from globals import *
from beyblade import Beyblade
from save_load_module import load


class BattleScreen(Screen):
    def __init__(self, display_surf, logger):
        super(BattleScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._background_surf = self.load_arena()
        self.beyblades_list = []
        image = load(key="beyblade") + '.png'
        self.beyblades_list.append(Beyblade(logger=self.logger, image=image))
        self.beyblades_list.append(Beyblade(self.logger, random.choice(BEYBLADES_LIST)+'.png'))
        return

    def load_arena(self):
        background_surf = pygame.image.load(os.path.join(graphics_path, "blue_arena.png")).convert_alpha()
        min_dim = min(WIDTH, HEIGHT)
        background_surf = pygame.transform.scale(background_surf, (min_dim, min_dim))
        return background_surf

    def on_update(self):
        for beyblade in self.beyblades_list:
            beyblade.on_update()
        pass

    def on_render(self):
        bgd_left = int(int(WIDTH / 2.0) - min(WIDTH, HEIGHT)/2.0)
        self._display_surf.blit(self._background_surf, (bgd_left, 0))
        for beyblade in self.beyblades_list:
            beyblade.on_render(self._display_surf)
        super(BattleScreen, self).on_render()

    def on_exit(self, key=None):
        self._running = False
        # from main_menu_screen import MainMenuScreen
        # self._next_screen = MainMenuScreen
