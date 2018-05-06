import pygame
from globals import *
from text import Text
import os


class Button:

    def __init__(self, logger, width, height, center_posx, center_posy, text, text_color, bgd_color, alt_text_color):
        self.logger = logger.getChild(__name__)
        self._text_color = text_color
        self._bgd_color = bgd_color
        self._width = width
        self._height = height
        self._text = text

        if text is not None:
            self._text_obj = Text(text, center_posx, center_posy, text_color, self._bgd_color, alt_text_color)
            self._rect = self._text_obj.get_rect()
        else:
            self._text_obj = None
            self._rect = pygame.Rect(0, 0, width, height)
            self._rect.center = (center_posx, center_posy)
        return

    def __str__(self):
        return self._text

    def on_update(self, clicked, mousex, mousey):
        mouse_floats = self._rect.collidepoint(mousex, mousey)
        self._text_obj.on_update(mouse_floats=mouse_floats)
        if mouse_floats and clicked:
            return True
        else:
            return False

    def on_render(self, display_surf):
        if self._text_obj is not None:
            self._text_obj.on_render(display_surf)
        else:
            # rect(Surface, color, Rect, width=0) -> Rect
            pygame.draw.rect(self._rect, self._bgd_color, self._rect)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_center_posx(self):
        return self._rect.centerx

    def get_center_posy(self):
        return self._rect.centery


class ImageButton:

    def __init__(self, logger, width, height, image, bgd_color, center_posx, center_posy, padx=10, pady=10):
        self.logger = logger.getChild(__name__)
        self._text = image.split('.png')[0]
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf, (width, height))
        self._image_surf_rect = self._image_surf.get_rect(center=(center_posx, center_posy))
        self._bgd_color = bgd_color  # background color for selected image
        self._padx = padx
        self._pady = pady
        self._mouse_floats = False
        return

    def __str__(self):
        return self._text

    def on_update(self, clicked, mousex, mousey):
        self._mouse_floats = self._image_surf_rect.collidepoint(mousex, mousey)
        if self._mouse_floats and clicked:
            return True
        else:
            return False

    def on_render(self, display_surf):
        if self._mouse_floats:
            bgd_rect = pygame.Rect(0, 0, self.get_width() + self._padx, self.get_height()+self._pady)
            bgd_rect.center = self._image_surf_rect.center
            pygame.draw.rect(display_surf, self._bgd_color, bgd_rect)
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))

    def get_width(self):
        return self._image_surf_rect.width

    def get_height(self):
        return self._image_surf_rect.height

    def get_center_posx(self):
        return self._image_surf_rect.centerx

    def get_center_posy(self):
        return self._image_surf_rect.centery
