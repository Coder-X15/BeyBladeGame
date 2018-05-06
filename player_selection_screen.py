from globals import *
from screen import Screen
from button import ImageButton


class PlayerSelectionScreen(Screen):
    def __init__(self, display_surf, logger):
        super().__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._beyblades = {"golden": ImageButton(logger=self.logger,
                                                 width=100, height=100, image="golden.png", bgd_color=BRIGHTGREEN,
                                                 center_posx=int(WIDTH/4), center_posy=int(HEIGHT/4))}
        self._beyblades["atomic"] = ImageButton(logger=self.logger,
                                                width=self._beyblades["golden"].get_width(),
                                                height=self._beyblades["golden"].get_height(),
                                                image="atomic.png", bgd_color=BRIGHTGREEN,
                                                center_posx=int(WIDTH*3.0/4), center_posy=int(HEIGHT/4))
        return

    def on_update(self):
        for key, image_btn in self._beyblades.items():
            if image_btn.on_update(self._mouse_clicked, self._mousex, self._mousey):
                self.on_exit(key)
        return

    def on_render(self):
        self._display_surf.fill(BLUE)  # clear screen
        for image_btn in self._beyblades.values():
            image_btn.on_render(self._display_surf)
        super().on_render()
        return

    def on_exit(self, key):
        self._running = False
        self.logger.info("Player selected {} beyblade".format(key))
        return
