from screen import Screen
from buttons import *
from profile_window import ProfileWindow
from save_load_module import save

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
            "hades_kerbecs": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="hades_kerbecs.png",
                                      centerx=left_col_centerx, centery=row_one_centery, pady=pady,
                                      text="Hades Kerbecs",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "arc_bahamut": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="arc_bahamut.png",
                                      centerx=right_col_centerx, centery=row_one_centery, pady=pady,
                                      text="Arc Bahamut",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "gladiator_bahamut": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="gladiator_bahamut.png",
                                     centerx=left_col_centerx, centery=row_two_centery, pady=pady,
                                     text="Gladiator Bahamut",
                                     text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "phantom_orion": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                           image="phantom_orion.png",
                                           centerx=right_col_centerx, centery=row_two_centery, pady=pady,
                                           text="Phantom Orion",
                                           text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                           font_size=FONT_SIZE),
            "samurai_ifrit": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="samurai_ifrit.png",
                                   centerx=left_col_centerx, centery=row_three_centry, pady=pady,
                                   text="Samurai Ifrit",
                                   text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "pirate_kraken": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="pirate_kraken.png",
                                      centerx=right_col_centerx, centery=row_three_centry, pady=pady,
                                      text="Pirate Kraken",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "pirate_orochi": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT, image="pirate_orochi.png",
                                      centerx=left_col_centerx, centery=row_four_centery, pady=pady,
                                      text="Pirate Orochi",
                                      text_color=WHITE, alt_text_color=BRIGHTYELLOW, font_size=FONT_SIZE),
            "big_bang_pegasus": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                       image="big_bang_pegasus.png",
                                       centerx=right_col_centerx, centery=row_four_centery, pady=pady,
                                       text="Big Bang Pegasus",
                                       text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                       font_size=FONT_SIZE),
            "blitz_striker": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                       image="blitz_striker.png",
                                       centerx=left_col_centerx, centery=row_five_centery, pady=pady,
                                       text="Blitz Striker",
                                       text_color=WHITE, alt_text_color=BRIGHTYELLOW,
                                       font_size=FONT_SIZE),
            "xeno_xcalibur": ImageTextButton(logger=self.logger, width=BB_WIDTH, height=BB_HEIGHT,
                                        image="xeno_xcalibur.png",
                                        centerx=right_col_centerx, centery=row_five_centery, pady=pady,
                                        text="Xeno Xcalibur",
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
            if image_btn.on_update(self._l_mouse_clicked, self._mousex, self._mousey):
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
        if hasattr(key, "type"):
            if key.type is pygame.QUIT:
                return

        if self._selected_beyblade is not None:
            from campaign_screen import CampaignScreen
            self._next_screen = CampaignScreen

            # save selected player BB to savegame file
            from save_load_module import save
            save(save_dict={"player_beyblade": key})

            self.logger.info("Player selected {} beyblade".format(key))
        return
