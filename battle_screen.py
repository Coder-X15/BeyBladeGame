from screen import Screen
from globals import *

class BattleScreen(Screen):
    def __init__(self):
        super().__init__()


    def on_init(self):
        super().on_init()

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
