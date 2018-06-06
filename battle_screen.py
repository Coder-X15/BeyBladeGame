import os
import math
import pygame

from bars import TextBar
from beyblade import Beyblade
from globals import *
from save_load_module import load
from screen import Screen

BGD_COLOR = BLUE


class BattleScreen(Screen):
    def __init__(self, display_surf, logger):
        super(BattleScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._background_surf = self.load_arena()

        player_name = load(key="player_beyblade")
        opp_name = load(key="opp_beyblade")

        self._player_bb = Beyblade(logger=self.logger, name=player_name, player=True)
        self._opp_bb = Beyblade(self.logger, name=opp_name, player=False)

        self._player_hp_txt_bar = None
        self._player_spd_txt_bar = None
        self._opp_hp_txt_bar = None
        self._opp_spd_txt_bar = None

        self.create_bars()  # create HP & SPD bars

        return

    def create_bars(self):
        player_hp_txt_cntrx = int(WIDTH / 20.0)
        player_hp_txt_cntry = int(HEIGHT / 20.0)
        player_hp = self._player_bb.get_hp()
        player_spd = self._player_bb.get_spd()
        player_bar_left = int(WIDTH * 1.0 / 9)
        opp_hp_txt_cntrx = int(WIDTH * 19.0/20)
        opp_hp = self._opp_bb.get_hp()
        opp_spd = self._opp_bb.get_spd()
        opp_bar_left = int(WIDTH * 5.0 / 9)
        bars_width = int(WIDTH * 3.0 / 9)

        self._player_hp_txt_bar = TextBar(text="HP",
                                          text_centerx=player_hp_txt_cntrx, text_centery=player_hp_txt_cntry,
                                          text_color=WHITE, bgd_text_color=BGD_COLOR, alt_text_color=WHITE, font_size=32,
                                          value=player_hp, max_value=player_hp,
                                          width=bars_width, bar_left=player_bar_left,
                                          bar_color=BRIGHTYELLOW, bar_bgd_color=RED)

        height = self._player_hp_txt_bar.get_height()

        self._player_spd_txt_bar = TextBar(text="SPD",
                                           text_centerx=player_hp_txt_cntrx, text_centery=player_hp_txt_cntry + height,
                                           text_color=WHITE, bgd_text_color=BGD_COLOR, alt_text_color=WHITE, font_size=32,
                                           value=player_spd, max_value=player_spd,
                                           width=int(WIDTH * 3.0 / 9), bar_left=int(WIDTH * 1.0 / 9),
                                           bar_color=BRIGHTBLUE, bar_bgd_color=BLUE)

        self._opp_hp_txt_bar = TextBar(text="HP",
                                            text_centerx=opp_hp_txt_cntrx, text_centery=player_hp_txt_cntry,
                                            text_color=WHITE, bgd_text_color=BGD_COLOR, alt_text_color=WHITE, font_size=32,
                                            value=opp_hp, max_value=opp_hp,
                                            width=bars_width, bar_left=opp_bar_left,
                                            bar_color=BRIGHTYELLOW, bar_bgd_color=RED)

        self._opp_spd_txt_bar = TextBar(text="SPD",
                                             text_centerx=opp_hp_txt_cntrx, text_centery=player_hp_txt_cntry+height,
                                             text_color=WHITE, bgd_text_color=BGD_COLOR, alt_text_color=WHITE, font_size=32,
                                             value=opp_spd, max_value=opp_spd,
                                             width=bars_width, bar_left=opp_bar_left,
                                             bar_color=BRIGHTBLUE, bar_bgd_color=BLUE)
        return

    def load_arena(self):
        background_surf = pygame.image.load(os.path.join(graphics_path, "rings_arena.png")).convert_alpha()
        min_dim = min(WIDTH, HEIGHT)
        background_surf = pygame.transform.scale(background_surf, (min_dim, min_dim))
        return background_surf

    def on_update(self):

        if self._l_mouse_clicked:
            # TODO: player BB should decrease it's speed to shorten it's radius
            opp_rect = self._opp_bb.get_rect()
            self._player_bb.attack(opp_rect.centerx, opp_rect.centery)
            self._l_mouse_clicked = False  # return to default value till next click

        elif self._r_mouse_clicked:
            # TODO: player BB should increase it's movement speed to evade the opponents BB
            self._player_bb.evade()
            self._r_mouse_clicked = False  # return to default value till next click

        self._player_bb.on_update()
        self._player_hp_txt_bar.on_update(self._player_bb.get_hp())
        self._player_spd_txt_bar.on_update(self._player_bb.get_spd())

        self._opp_bb.on_update()
        self._opp_hp_txt_bar.on_update(self._opp_bb.get_hp())
        self._opp_spd_txt_bar.on_update(self._opp_bb.get_spd())

        if self._check_collision():
            self.logger.info("Collision!")
            self._player_bb.collided(opp_attack=self._opp_bb.get_atk(), opp_spd=self._opp_bb.get_spd())
            self._opp_bb.collided(opp_attack=self._player_bb.get_atk(), opp_spd=self._player_bb.get_spd())

        if self._player_bb.get_hp() <= 0:
            self.logger.info("Player Lost!")
            self.on_exit(key="Player Lost!")
        elif self._opp_bb.get_hp() <= 0:
            self.logger.info("Player Won!")
            self.on_exit(key="Player Won!")

        return

    def on_render(self):
        self._display_surf.fill(BGD_COLOR)
        bgd_left = int(int(WIDTH / 2.0) - min(WIDTH, HEIGHT) / 2.0)
        self._display_surf.blit(self._background_surf, (bgd_left, 0))

        self._player_bb.on_render(self._display_surf)
        self._player_hp_txt_bar.on_render(self._display_surf)
        self._player_spd_txt_bar.on_render(self._display_surf)

        self._opp_bb.on_render(self._display_surf)
        self._opp_hp_txt_bar.on_render(self._display_surf)
        self._opp_spd_txt_bar.on_render(self._display_surf)

        super(BattleScreen, self).on_render()
        return

    def on_exit(self, key=None):
        self._running = False
        # from main_menu_screen import MainMenuScreen
        # self._next_screen = MainMenuScreen

    def _check_collision(self):
        player_bb_rect = self._player_bb.get_rect()
        player_bb_centerx = player_bb_rect.centerx
        player_bb_centery = player_bb_rect.centery
        player_bb_radius = int(player_bb_rect.height / 3.0)

        opp_bb_rect = self._opp_bb.get_rect()
        opp_bb_centerx = opp_bb_rect.centerx
        opp_bb_centery = opp_bb_rect.centery
        opp_bb_radius = int(opp_bb_rect.height / 3.0)

        radius_sum = player_bb_radius + opp_bb_radius
        delta_x = abs(player_bb_centerx-opp_bb_centerx)
        delta_y = abs(player_bb_centery - opp_bb_centery)
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distance <= radius_sum:
            return True
        else:
            return False
