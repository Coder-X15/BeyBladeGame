import os
from random import shuffle
from graphic_effects import *
from types import *

import pygame

from globals import *
from screen import Screen

BB_WIDTH, BB_HEIGHT = 80, 80


def shuffle_bb_list(player_bb):
    assert type(player_bb) is StringType, "player is not a name string!"
    rnd_bb_list = [i for i in BEYBLADES_LIST]  # copy the list
    rnd_bb_list.remove(player_bb)
    shuffle(rnd_bb_list)  # shuffle works in place and returns None
    return rnd_bb_list


class CampaignScreen(Screen):
    def __init__(self, display_surf, logger, player_bb):
        super(CampaignScreen, self).__init__(display_surf=display_surf, logger=logger)
        self._player_bb = player_bb
        self._rival_bb_dict = self.get_bb_dict()

    def get_bb_dict(self):
        rival_bb_list = shuffle_bb_list(self._player_bb)
        bb_dict = {}
        centerx = int(WIDTH/2.0) + int(BB_WIDTH/2.0)
        for bb in rival_bb_list:
            centery = HEIGHT - int(BB_HEIGHT / 2.0) - BB_HEIGHT * rival_bb_list.index(bb)
            image = bb + ".png"
            image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
            image_surf = pygame.transform.smoothscale(image_surf, (BB_WIDTH, BB_HEIGHT))
            image_surf_rect = image_surf.get_rect(center=(centerx, centery))
            bb_dict[bb] = {"image": image_surf,
                           "rect": image_surf_rect,
                           "played": False}
        return bb_dict

    def on_render(self):

        g_left = None
        self._display_surf.fill(BLACK)

        for bb in self._rival_bb_dict.values():
            image = bb["image"]
            left = bb["rect"].left
            if g_left is None:
                g_left = left
            top = bb["rect"].top

            self._display_surf.blit(image, (left, top))
        draw_vertical_gradient_box(self._display_surf, BB_WIDTH, BB_HEIGHT * 3, g_left, 0, BLACK, GRADIENT_DOWN, 20)  # top gradient
        draw_vertical_gradient_box(self._display_surf, BB_WIDTH, BB_HEIGHT * 3, g_left, HEIGHT - BB_HEIGHT * 3, BLACK, GRADIENT_UP, 20)
        super(CampaignScreen, self).on_render()
        return




