import pygame
from globals import *
from beyblade import Beyblade
from screen import Screen


class App(Screen):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.beyblades_list = []

    def on_init(self):
        super().on_init()
        self.beyblades_list.append(Beyblade('golden.png', MEDIUM_SPEED, MEDIUM_SPEED))
        return True

    def on_loop(self):
        print("on_loop")
        for beyblade in self.beyblades_list:
            beyblade.update()
        pass

    def on_render(self):
        print("on_render")
        self._display_surf.fill(black)  # clear screen
        for beyblade in self.beyblades_list:
            beyblade.render(self._display_surf)
        pygame.display.update()
        # pygame.display.flip()
        self.clock.tick(FPS)
        pass


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
