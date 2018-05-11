import pygame
from text import Text


def calc_relative_width(max_value, value, width):
    relative_width = int(value * 1.0 / max_value * width)
    return relative_width


class Bar(object):
    def __init__(self, value, max_value, width, height, left, top,
                 color, bgd_bar_color=None):
        self._value = value
        self._max_value = max_value,
        self._max_width = width
        self._color = color
        self._bgd_bar_color = None

        relative_width = calc_relative_width(max_value, value, width)
        self._bar_rect = pygame.Rect(left, top, relative_width, height)

        if bgd_bar_color is not None:
            self._bgd_bar_color = bgd_bar_color
            self._bgd_bar_rect = pygame.Rect(left, top, width, height)

        return

    def on_update(self, new_value):
        self._value = new_value
        left = self._bgd_bar_rect.left
        top = self._bgd_bar_rect.top
        height = self._bgd_bar_rect.height
        width = self._bgd_bar_rect.width
        relative_width = calc_relative_width(self._max_value, self._value, width)
        self._bar_rect = pygame.Rect(left, top, relative_width, height)
        return

    def on_render(self, display_surf):
        if self._bgd_bar_color is not None:
            pygame.draw.rect(display_surf, self._bgd_bar_color, self._bgd_bar_rect)
        pygame.draw.rect(display_surf, self._color, self._bar_rect)
        return


class TextBar(Bar):
    def __init__(self, text, text_centerx, text_centery, text_color, bgd_text_color, alt_text_color, font_size,
                 value, max_value, width, bar_left, bar_color, bar_bgd_color):
        self._text = text
        self._text_obj = Text(text, text_centerx, text_centery, text_color, bgd_text_color, alt_text_color, font_size)

        bar_height = self._text_obj.get_rect().height
        # left = self._text_obj. get_rect().right + 10
        bar_top = self._text_obj.get_rect().top

        super(TextBar, self).__init__(value, max_value, width, bar_height, bar_left, bar_top, bar_color, bar_bgd_color)

        return

    def on_render(self, display_surf):
        super(TextBar, self).on_render(display_surf)
        self._text_obj.on_render(display_surf)
        return

