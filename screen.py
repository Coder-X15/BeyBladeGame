import pygame
from globals import *
from events import CEvent


class Screen(CEvent):

    def __init__(self, logger=None):
        assert(logger is None, 'logger == None!')
        self.logger = logger.getChild(__name__)
        super().__init__()
        self.logger.info("__init__")
        self.clock = pygame.time.Clock()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = WIDTH, HEIGHT
        return

    def on_init(self):
        self.logger.info("on_init")
        pygame.init()
        # pygame.display.set_caption("MyGame")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        return True

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(black)  # clear screen
        pygame.display.update()
        # pygame.display.flip()
        self.clock.tick(FPS)
        pass

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        self.logger.info("on_cleanup")
        pygame.quit()
        exit()

    def on_execute(self):
        self.logger.info("on_execute")
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()
