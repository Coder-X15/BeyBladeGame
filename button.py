import pygame
from text import Text


class Button:

    def __init__(self, logger, width, height, center_posx, center_posy, text, text_color, bgd_color):
        self.logger = logger.getChild(__name__)
        self._bgd_color = bgd_color
        if text is not None:
            self._text_obj = Text(text, center_posx, center_posy, text_color, self._bgd_color)
        else:
            self._text_obj = None
            self.rect = pygame.Rect(0, 0, width, height)
            self.rect.center = (center_posx, center_posy)
        return

    def on_render(self, display_surf):
        if self._text_obj is not None:
            self._text_obj.on_render(display_surf)
        else:
            # rect(Surface, color, Rect, width=0) -> Rect
            pygame.draw.rect(self.rect, self._bgd_color, self.rect)

