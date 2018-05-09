import pygame
import os
from save_load_module import load_profile
from text import Text
from globals import *


class ProfileWindow:
    def __init__(self, image: str, image_width: int, image_height: int, top: int, left: int, bgd_color):
        self._name = image.split(".png")[0]
        self._profile = load_profile(self._name)
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf, (image_width, image_height))
        self._image_surf_rect = self._image_surf.get_rect(top=top, left=left)

        txt_padx = -int(WIDTH/20)
        txt_pady = 30
        left = self._image_surf_rect.left
        txt_centerx = left + txt_padx
        txt_centery = self._image_surf_rect.bottom + 3*txt_pady

        self._name_text = Text(text=self._name.upper().replace("_", " "),
                               center_posx=self._image_surf_rect.centerx,
                               center_posy=self._image_surf_rect.bottom+2*txt_pady,
                               text_color=BRIGHTYELLOW, bgd_color=bgd_color, alt_text_color=WHITE, font_size=36)
        self._hp_text = Text(text="HP", center_posx=txt_centerx, center_posy=txt_centery + txt_pady,
                             text_color=WHITE, bgd_color=bgd_color, alt_text_color=WHITE, font_size=24)
        self._atk_text = Text(text="ATK", center_posx=txt_centerx, center_posy=txt_centery + 3 * txt_pady,
                              text_color=WHITE, bgd_color=bgd_color, alt_text_color=WHITE, font_size=24)
        self._def_text = Text(text="DEF", center_posx=txt_centerx, center_posy=txt_centery + 5 * txt_pady,
                              text_color=WHITE, bgd_color=bgd_color, alt_text_color=WHITE, font_size=24)
        self._spd_text = Text(text="SPD", center_posx=txt_centerx, center_posy=txt_centery + 7 * txt_pady,
                              text_color=WHITE, bgd_color=bgd_color, alt_text_color=WHITE, font_size=24)

        bar_height = int(self._hp_text.get_rect().height)

        hp = self._profile["hp"]
        hp_bar_width = int(hp*1.0/100*image_width)
        hp_bar_top = self._hp_text.get_rect().top

        self._hp_rect = pygame.Rect(left, hp_bar_top, hp_bar_width, bar_height)

        atk = self._profile["atk"]
        atk_bar_width = int(atk * 1.0 / 100 * image_width)
        atk_bar_top = self._atk_text.get_rect().top
        self._atk_rect = pygame.Rect(left, atk_bar_top, atk_bar_width, bar_height)

        def_val = self._profile["def"]
        def_bar_width = int(def_val * 1.0 / 100 * image_width)
        def_bar_top = self._def_text.get_rect().top
        self._def_rect = pygame.Rect(left, def_bar_top, def_bar_width, bar_height)

        spd = self._profile["spd"]
        spd_bar_width = int(spd * 1.0 / 100 * image_width)
        spd_bar_top = self._spd_text.get_rect().top
        self._spd_rect = pygame.Rect(left, spd_bar_top, spd_bar_width, bar_height)

    def __str__(self):
        return self._name

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        self._name_text.on_render(display_surf)
        self._hp_text.on_render(display_surf)
        self._atk_text.on_render(display_surf)
        self._def_text.on_render(display_surf)
        self._spd_text.on_render(display_surf)
        pygame.draw.rect(display_surf, BRIGHTGREEN, self._hp_rect)
        pygame.draw.rect(display_surf, BRIGHTGREEN, self._atk_rect)
        pygame.draw.rect(display_surf, BRIGHTGREEN, self._def_rect)
        pygame.draw.rect(display_surf, BRIGHTGREEN, self._spd_rect)
        return
