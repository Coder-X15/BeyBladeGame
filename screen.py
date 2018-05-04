import pygame
from globals import *
from events import CEvent


class Screen(CEvent):

    def __init__(self):
        super().__init__()
        print("__init__")
        self.clock = pygame.time.Clock()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = WIDTH, HEIGHT
        return

    def on_init(self):
        print("on_init")
        pygame.init()
        pygame.display.set_caption("MyGame")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        return True

    def on_loop(self):
        print("on_loop")
        pass

    def on_render(self):
        print("on_render")
        self._display_surf.fill(black)  # clear screen
        pygame.display.update()
        # pygame.display.flip()
        self.clock.tick(FPS)
        pass

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        print("on_cleanup")
        pygame.quit()

    def on_execute(self):
        print("on_execute")
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()
