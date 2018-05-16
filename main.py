"""
Pygame based Beyblade game

Created By: Roy Mainer roymainer@gmail.com

Version: 1.0
Date: 10.5.18
"""


import pygame
from globals import *
from my_logger import get_logger
from profiler import create_profiles

from main_menu_screen import MainMenuScreen
from player_selection_screen import PlayerSelectionScreen
from campaign_screen import CampaignScreen
from battle_screen import BattleScreen


class App:

    def __init__(self):
        self.logger = logger
        logger.info("__init__")
        pygame.init()
        create_profiles()
        self._display_surf = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        # self._active_screen = MainMenuScreen(display_surf=self._display_surf, logger=logger)
        # self._active_screen = PlayerSelectionScreen(display_surf=self._display_surf, logger=logger)
        # self._active_screen = CampaignScreen(self._display_surf, logger)
        self._active_screen = BattleScreen(self._display_surf, self.logger)
        self._running = True

    def on_cleanup(self):
        self.logger.info("on_cleanup")
        pygame.quit()

    def on_execute(self):
        self.logger.info("on_execute")

        while self._running:
            next_active_screen = self._active_screen.on_execute()
            if next_active_screen is not None:
                self._active_screen = next_active_screen(self._display_surf, self.logger)
            else:
                self._running = False

        self.on_cleanup()


if __name__ == "__main__":
    logger = get_logger()
    theApp = App()
    theApp.on_execute()
