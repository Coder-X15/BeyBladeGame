from screen import Screen
from globals import *
from beyblade import Beyblade


class BattleScreen(Screen):
    def __init__(self, display_surf, logger):
        super().__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self.beyblades_list = []
        self.beyblades_list.append(Beyblade(logger=self.logger,
                                            image='golden.png',
                                            rotation_speed=MEDIUM_SPEED,
                                            movement_speed=MEDIUM_SPEED))

    def on_update(self):
        for beyblade in self.beyblades_list:
            beyblade.update()
        pass

    def on_render(self):
        self._display_surf.fill(black)  # clear screen
        for beyblade in self.beyblades_list:
            beyblade.render(self._display_surf)
        super().on_render()

    def on_exit(self):
        self._running = False
        # from main_menu_screen import MainMenuScreen
        # self._next_screen = MainMenuScreen
