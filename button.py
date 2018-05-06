import pygame
from text import Text


class Button:

    def __init__(self, logger, width, height, center_posx, center_posy, text, text_color, bgd_color, alt_text_color):
        self.logger = logger.getChild(__name__)
        self._text_color = text_color
        self._bgd_color = bgd_color
        self._width = width
        self._height = height
        self._center_posx = center_posx
        self._center_posy = center_posy

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
        return self._center_posx

    def get_center_posy(self):
        return self._center_posy