import pygame
from globals import *
from events import CEvent


class Screen(CEvent):

    def __init__(self, display_surf=None, logger=None):
        assert(display_surf is not None), 'display_surf == None!'
        assert (logger is not None), 'logger == None!'
        self.logger = logger.getChild(__name__)
        self.logger.info("__init__")

        self._display_surf = display_surf
        self.clock = pygame.time.Clock()
        self._running = True
        self._next_screen = None
        return

    def on_update(self):
        pass

    def on_render(self):
        pygame.display.update()
        # pygame.display.flip()
        milliseconds = self.clock.tick(FPS)
        # self._playtime += milliseconds / 1000.0
        # text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(self.clock.get_fps(), self._playtime)
        text = "FPS: {0:.2f}".format(self.clock.get_fps())
        pygame.display.set_caption(text)
        pass

    def on_exit(self):
        self._running = False

    def on_execute(self):
        self.logger.info("on_execute")
        self.mouse_clicked = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_update()
            self.on_render()

        return self._next_screen
