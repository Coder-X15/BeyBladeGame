from screen import Screen
from buttons import *
from profile_window import ProfileWindow

# Constants
centerx_correct = 20
left_col_centerx = int(WIDTH * 1.0 / 20) + centerx_correct
right_col_centerx = int(WIDTH * 4.0 / 20) + centerx_correct

centery_correct = -20

row_one_centery = int(HEIGHT * 4.0 / 20) + centery_correct
row_two_centery = int(HEIGHT * 7.5 / 20) + centery_correct
row_three_centry = int(HEIGHT * 11 / 20) + centery_correct
row_four_centery = int(HEIGHT * 14.5 / 20) + centery_correct
row_five_centery = int(HEIGHT * 18 / 20) + centery_correct

BB_WIDTH, BB_HEIGHT = 80, 80
pady = 15
FONT_SIZE = 20

PROFILE_IMAGE_WIDTH = int(WIDTH / 4)
PROFILE_IMAGE_HEIGHT = int(WIDTH / 4)

PROFILE_IMAGE_LEFT = int(WIDTH * 10.0 / 20)
PROFILE_IMAGE_TOP = int(HEIGHT * 2.0 / 20)
BACKGROUND_COLOR = BLACK


class PlayerSelectionScreen(Screen):
    def __init__(self, display_surf, logger):
        super(PlayerSelectionScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._title = self.create_title()
        self._beyblades = self.create_bb_buttons()
        self._profiles = self.create_bb_profiles()
        self._active_profile = None
        self._selected_beyblade = None
        return

    def create_title(self):
        centerx = int((left_col_centerx + right_col_centerx) / 2)
        centery = row_one_centery + 4 * centery_correct
        text_obj = Text(text="Select Beyblade", center_posx=centerx, center_posy=centery,
                        text_color=WHITE, bgd_color=BACKGROUND_COLOR, alt_text_color=WHITE, font_size=32)
        return text_obj

    def create_bb_buttons(self):

        # self._beyblades["golden"] = ImageButton(logger=self.logger, width=width, height=height, image="golden.png",
        #                                         centerx=left_col_centerx, centery=row_one_centery)
        # self._beyblades["atomic"] = ImageButton(logger=self.logger, width=width, height=height, image="atomic.png",
        #                                         centerx=right_col_centerx, centery=row_one_centery)
        beyblades_dict = {
            "golden": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="golden.png",
                                      centerx=left_col_centerx, centery=row_one_centery, pady=pady,
                                      text="Golden",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "atomic": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="atomic.png",
                                      centerx=right_col_centerx, centery=row_one_centery, pady=pady,
                                      text="Atomic",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "demon": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="demon.png",
                                     centerx=left_col_centerx, centery=row_two_centery, pady=pady,
                                     text="Demon",
                                     text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "fire_spirit": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                           image="fire_spirit.png",
                                           centerx=right_col_centerx, centery=row_two_centery, pady=pady,
                                           text="Fire Spirit",
                                           text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                           font_size=FONT_SIZE),
            "imp": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="imp.png",
                                   centerx=left_col_centerx, centery=row_three_centry, pady=pady,
                                   text="Imp",
                                   text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "kraken": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="kraken.png",
                                      centerx=right_col_centerx, centery=row_three_centry, pady=pady,
                                      text="Kraken",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "medusa": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="medusa.png",
                                      centerx=left_col_centerx, centery=row_four_centery, pady=pady,
                                      text="Medusa",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "pegasus": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                       image="pegasus.png",
                                       centerx=right_col_centerx, centery=row_four_centery, pady=pady,
                                       text="Pegasus",
                                       text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                       font_size=FONT_SIZE),
            "unicorn": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                       image="unicorn.png",
                                       centerx=left_col_centerx, centery=row_five_centery, pady=pady,
                                       text="Unicorn",
                                       text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                       font_size=FONT_SIZE),
            "valkyrie": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                        image="valkyrie.png",
                                        centerx=right_col_centerx, centery=row_five_centery, pady=pady,
                                        text="Valkyrie",
                                        text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                        font_size=FONT_SIZE)}
        return beyblades_dict

    def create_bb_profiles(self):
        profiles_dict = {}

        for bb in BEYBLADES_LIST:
            image = bb + ".png"
            profiles_dict[bb] = ProfileWindow(image=image,
                                              image_width=PROFILE_IMAGE_WIDTH, image_height=PROFILE_IMAGE_HEIGHT,
                                              top=PROFILE_IMAGE_TOP, left=PROFILE_IMAGE_LEFT,
                                              bgd_color=BACKGROUND_COLOR)
        return profiles_dict

    def on_update(self):
        for key, image_btn in self._beyblades.items():
            if image_btn.on_update(self._mouse_clicked, self._mousex, self._mousey):
                from save_load_module import save
                save(save_dict={"beyblade": key})
                self._selected_beyblade = key
                self.on_exit(key)

            if image_btn.on_collide(mousex=self._mousex, mousey=self._mousey):
                if key in self._profiles.keys():
                    self._active_profile = self._profiles[key]
                    return
            else:
                self._active_profile = None
        return

    def on_render(self):
        self._display_surf.fill(BACKGROUND_COLOR)  # clear screen
        self._title.on_render(self._display_surf)
        for image_btn in self._beyblades.values():
            image_btn.on_render(self._display_surf)
        if self._active_profile is not None:
            self._active_profile.on_render(self._display_surf)
        super(PlayerSelectionScreen, self).on_render()
        return

    def on_exit(self, key):
        self._running = False
        if self._selected_beyblade is not None:
            from battle_screen import BattleScreen
            self._next_screen = BattleScreen
            self.logger.info("Player selected {} beyblade".format(key))
