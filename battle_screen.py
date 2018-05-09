from screen import Screen
from globals import *
from beyblade import Beyblade
from save_load_module import load


class BattleScreen(Screen):
    def __init__(self, display_surf, logger):
        super(BattleScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self.beyblades_list = []
        image = load(key="beyblade") + '.png'
        self.beyblades_list.append(Beyblade(logger=self.logger,
                                            image=image,
                                            rotation_speed=MEDIUM_SPEED,
                                            movement_speed=MEDIUM_SPEED))

    def on_update(self):
        for beyblade in self.beyblades_list:
            beyblade.on_update()
        pass

    def on_render(self):
        self._display_surf.fill(BLACK)  # clear screen
        for beyblade in self.beyblades_list:
            beyblade.on_render(self._display_surf)
        super(BattleScreen, self).on_render()

    def on_exit(self, key=None):
        self._running = False
        # from main_menu_screen import MainMenuScreen
        # self._next_screen = MainMenuScreen
