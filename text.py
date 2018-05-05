import pygame


class Text:
    def __init__(self, text, center_posx, center_posy, text_color, bgd_color):
        font_obj = pygame.font.Font('freesansbold.ttf', 32)  # (1) create a pygame font object
        self._textSurfaceObj = font_obj.render(text, True, text_color, bgd_color)  # (2) create a surface with text drawn on it
        self._textRectObj = self._textSurfaceObj.get_rect()  # (3) create a rect object for the text
        self._textRectObj.center = (center_posx, center_posy)  # (4) position the rect object

    def on_render(self, display_surf):
        display_surf.blit(self._textSurfaceObj, self._textRectObj)
        return
