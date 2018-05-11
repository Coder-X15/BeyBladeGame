import pygame

GRADIENT_UP = 1
GRADIENT_DOWN = -1


def draw_vertical_gradient_box(display_surface, width, height, left, top, color, direction, levels):
    rect_height = int(height / levels)
    alpha_step = int(255.0 / levels)
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

    return

