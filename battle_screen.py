import pygame
from screen import Screen
from globals import *
from beyblade import Beyblade


class BattleScreen(Screen):
    def __init__(self, logger):
        super().__init__(logger=logger.getChild(__name__))
        self.beyblades_list = []

    def on_init(self):
        super().on_init()
        self.beyblades_list.append(Beyblade('golden.png', MEDIUM_SPEED, MEDIUM_SPEED))

    def on_loop(self):
        for beyblade in self.beyblades_list:
            beyblade.update()
        pass

    def on_render(self):
        self._display_surf.fill(black)  # clear screen
        for beyblade in self.beyblades_list:
            beyblade.render(self._display_surf)
        pygame.display.update()
        # pygame.display.flip()
        milliseconds = self.clock.tick(FPS)
        self._playtime += milliseconds / 1000.0
        text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self._playtime)
        pygame.display.set_caption(text)
        pass
