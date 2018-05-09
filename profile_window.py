import pygame
import os
from save_load_module import load_profile
from text import Text
from bars import TextBar
from globals import *


class ProfileWindow:
    def __init__(self, image: str, image_width: int, image_height: int, top: int, left: int, bgd_color):
        self._name = image.split(".png")[0]
        self._profile = load_profile(self._name)
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf, (image_width, image_height))
        self._image_surf_rect = self._image_surf.get_rect(top=top, left=left)

        txt_padx = -int(WIDTH / 20)
        txt_pady = 30
        left = self._image_surf_rect.left
        txt_centerx = left + txt_padx
        txt_centery = self._image_surf_rect.bottom + 3 * txt_pady

        self._name_text = Text(text=self._name.upper().replace("_", " "),
                               center_posx=self._image_surf_rect.centerx,
                               center_posy=self._image_surf_rect.bottom + 2 * txt_pady,
                               text_color=BRIGHTYELLOW, bgd_color=bgd_color, alt_text_color=WHITE, font_size=36)

        hp = self._profile["hp"]
        atk = self._profile["atk"]
        def_val = self._profile["def"]
        spd = self._profile["spd"]

        self._hp_text_bar = TextBar(text="HP", text_centerx=txt_centerx, text_centery=txt_centery + txt_pady,
                                    text_color=WHITE, bgd_text_color=bgd_color, alt_text_color=WHITE, font_size=24,
                                    value=hp, max_value=MAX_ATTRIBUTE, width=image_width, bar_left=left,
                                    bar_color=BRIGHTGREEN, bar_bgd_color=GREEN)
        self._atk_text_bar = TextBar(text="ATK", text_centerx=txt_centerx, text_centery=txt_centery + 3 * txt_pady,
                                     text_color=WHITE, bgd_text_color=bgd_color, alt_text_color=WHITE, font_size=24,
                                     value=atk, max_value=MAX_ATTRIBUTE, width=image_width, bar_left=left,
                                     bar_color=BRIGHTGREEN, bar_bgd_color=GREEN)
        self._def_text_bar = TextBar(text="DEF", text_centerx=txt_centerx, text_centery=txt_centery + 5 * txt_pady,
                                     text_color=WHITE, bgd_text_color=bgd_color, alt_text_color=WHITE, font_size=24,
                                     value=def_val, max_value=MAX_ATTRIBUTE, width=image_width, bar_left=left,
                                     bar_color=BRIGHTGREEN, bar_bgd_color=GREEN)
        self._spd_text_bar = TextBar(text="SPD", text_centerx=txt_centerx, text_centery=txt_centery + 7 * txt_pady,
                                     text_color=WHITE, bgd_text_color=bgd_color, alt_text_color=WHITE, font_size=24,
                                     value=spd, max_value=MAX_ATTRIBUTE, width=image_width, bar_left=left,
                                     bar_color=BRIGHTGREEN, bar_bgd_color=GREEN)

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        self._name_text.on_render(display_surf)
        self._hp_text_bar.on_render(display_surf)
        self._atk_text_bar.on_render(display_surf)
        self._def_text_bar.on_render(display_surf)
        self._spd_text_bar.on_render(display_surf)
        return

    def __str__(self):
        return self._name
