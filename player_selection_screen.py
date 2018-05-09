from globals import *
from screen import Screen
from textbutton import *


class PlayerSelectionScreen(Screen):
    def __init__(self, display_surf, logger):
        super(PlayerSelectionScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._beyblades = {}
        self.create_bb_buttons()
        return

    def create_bb_buttons(self):
        centerx_correct = 20

        left_col_centerx = int(WIDTH * 1.0 / 20) + centerx_correct
        right_col_centerx = int(WIDTH * 4.0 / 20) + centerx_correct

        centery_correct = -20

        row_one_centery = int(HEIGHT * 4.0 / 20) + centery_correct
        row_two_centery = int(HEIGHT * 7.5 / 20) + centery_correct
        row_three_centry = int(HEIGHT * 11 / 20) + centery_correct
        row_four_centery = int(HEIGHT * 14.5 / 20) + centery_correct
        row_five_centery = int(HEIGHT * 18 / 20) + centery_correct

        width, height = 80, 80
        pady = 15
        font_size = 20

        # self._beyblades["golden"] = ImageButton(logger=self.logger, width=width, height=height, image="golden.png",
        #                                         centerx=left_col_centerx, centery=row_one_centery)
        # self._beyblades["atomic"] = ImageButton(logger=self.logger, width=width, height=height, image="atomic.png",
        #                                         centerx=right_col_centerx, centery=row_one_centery)
        self._beyblades["golden"] = ImageTextButton(logger=self.logger, width=width, height=height, image="golden.png",
                                                    centerx=left_col_centerx, centery=row_one_centery, pady=pady,
                                                    text="Golden",
                                                    text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["atomic"] = ImageTextButton(logger=self.logger, width=width, height=height, image="atomic.png",
                                                    centerx=right_col_centerx, centery=row_one_centery, pady=pady,
                                                    text="Atomic",
                                                    text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["demon"] = ImageTextButton(logger=self.logger, width=width, height=height, image="demon.png",
                                                   centerx=left_col_centerx, centery=row_two_centery, pady=pady,
                                                   text="Demon",
                                                   text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["fire_spirit"] = ImageTextButton(logger=self.logger, width=width, height=height,
                                                         image="fire_spirit.png",
                                                         centerx=right_col_centerx, centery=row_two_centery, pady=pady,
                                                         text="Fire Spirit",
                                                         text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                                         font_size=font_size)
        self._beyblades["imp"] = ImageTextButton(logger=self.logger, width=width, height=height, image="imp.png",
                                                 centerx=left_col_centerx, centery=row_three_centry, pady=pady,
                                                 text="Imp",
                                                 text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["kraken"] = ImageTextButton(logger=self.logger, width=width, height=height, image="kraken.png",
                                                    centerx=right_col_centerx, centery=row_three_centry, pady=pady,
                                                    text="Kraken",
                                                    text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["medusa"] = ImageTextButton(logger=self.logger, width=width, height=height, image="medusa.png",
                                                    centerx=left_col_centerx, centery=row_four_centery, pady=pady,
                                                    text="Medusa",
                                                    text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["pegasus"] = ImageTextButton(logger=self.logger, width=width, height=height,
                                                     image="pegasus.png",
                                                     centerx=right_col_centerx, centery=row_four_centery, pady=pady,
                                                     text="Pegasus",
                                                     text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["unicorn"] = ImageTextButton(logger=self.logger, width=width, height=height,
                                                     image="unicorn.png",
                                                     centerx=left_col_centerx, centery=row_five_centery, pady=pady,
                                                     text="Unicorn",
                                                     text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._beyblades["valkyrie"] = ImageTextButton(logger=self.logger, width=width, height=height,
                                                      image="valkyrie.png",
                                                      centerx=right_col_centerx, centery=row_five_centery, pady=pady,
                                                      text="Valkyrie",
                                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                                      font_size=font_size)

    def on_update(self):
        for key, image_btn in self._beyblades.items():
            if image_btn.on_update(self._mouse_clicked, self._mousex, self._mousey):
                from save_load_module import save
                save(save_dict={"beyblade": key})
                self.on_exit(key)
        return

    def on_render(self):
        self._display_surf.fill(BLACK)  # clear screen
        for image_btn in self._beyblades.values():
            image_btn.on_render(self._display_surf)
        super(PlayerSelectionScreen, self).on_render()
        return

    def on_exit(self, key):
        self._running = False
        from battle_screen import BattleScreen
        self._next_screen = BattleScreen
        self.logger.info("Player selected {} beyblade".format(key))
