import pygame
from globals import *
from screen import Screen
from main_menu_screen import MainMenuScreen
from my_logger import get_logger


class App(Screen):

    def __init__(self):
        super().__init__(logger=logger)
        # TODO: app shouldn't be a screen, it should call pygame.init() and pygame.quit() and remove it from screen, screen should inherit the surface
        self._main_menu = MainMenuScreen(logger=logger)
        self._main_menu.on_execute()

    def on_init(self):
        super().on_init()
        return True

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(black)  # clear screen
        pygame.display.update()
        # pygame.display.flip()
        # milliseconds = self.clock.tick(FPS)
        # self._playtime += milliseconds / 1000.0
        # text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self._playtime)
        text = "FPS: {0:.2f}".format(self.clock.get_fps())
        pygame.display.set_caption(text)
        pass


if __name__ == "__main__":
    logger = get_logger()
    theApp = App()
    theApp.on_execute()
