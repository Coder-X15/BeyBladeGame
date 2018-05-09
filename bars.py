import pygame


def calc_relative_width(max_value, value, width):
    relative_width = int(value * 1.0 / max_value * width)
    return relative_width


class Bar:
    def __init__(self, value: int, max_value: int, width: int, height: int, left: int, top: int,
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

