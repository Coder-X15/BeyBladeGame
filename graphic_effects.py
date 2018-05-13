import pygame

GRADIENT_UP = 1
GRADIENT_DOWN = -1


def draw_vertical_gradient_box(display_surface, width, height, left, top, color, direction, alpha_levels):
    rect_height = int(height / alpha_levels)
    alpha_step = int(255.0 / alpha_levels)
    alphas_list = range(0, 256, alpha_step)
    if direction == GRADIENT_DOWN:
        alphas_list = list(reversed(alphas_list))

    for i in range(len(alphas_list)):
        s = pygame.Surface((width, rect_height))
        rect_top = top + rect_height * i

        rect_alpha = alphas_list[i]

        s.set_alpha(rect_alpha)
        s.fill(color)
        display_surface.blit(s, (left, rect_top))

        # pygame.draw.rect(display_surface, color, rect)
    return


class FadeInBox:
    def __init__(self, width, height, top, left, color, alpha_levels):
        self._rect = pygame.Rect((left, top), (width, height))
        self._surface = pygame.Surface((width, height))
        self._color = color
        alpha_step = int(255.0 / alpha_levels)
        self._alpha_list = range(0, 256, alpha_step)
        self._alpha_index = 0
        return

    def on_update(self):
        alpha = self._alpha_list[self._alpha_index]
        self._surface.set_alpha(255 - alpha)
        self._surface.fill(self._color)
        if self._alpha_index < len(self._alpha_list) - 1:
            self._alpha_index += 1
            return False
        elif self._alpha_index == len(self._alpha_list) - 1:
            return True

    def on_render(self, display_surf):
        left = self._rect.left
        top = self._rect.top
        display_surf.blit(self._surface, (left, top))
        return
