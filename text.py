import pygame


class Text:
    def __init__(self, text, center_posx, center_posy, text_color, bgd_color, alt_text_color, font_size=32):
        self._text = text
        self._center_posx = center_posx
        self._center_posy = center_posy
        self._text_color = text_color
        self._bgd_color = bgd_color
        self._alt_text_color = alt_text_color
        self._font_size = font_size
        self._font_obj = pygame.font.Font('freesansbold.ttf', font_size)  # (1) create a pygame font object
        self._textSurfaceObj = self._font_obj.render(self._text, True, self._text_color, self._bgd_color)
        self._textRectObj = self._textSurfaceObj.get_rect()  # (3) create a rect object for the text
        self._textRectObj.center = (self._center_posx, self._center_posy)  # (4) position the rect object
        return

    def on_render(self, display_surf):
        display_surf.blit(self._textSurfaceObj, self._textRectObj)
        return

    def on_update(self, mouse_floats):
        if mouse_floats:  # if mouse cursor is over the text button
            # (2) create a surface with text drawn on it
            self._textSurfaceObj = self._font_obj.render(self._text, True, self._alt_text_color, self._bgd_color)
        else:
            self._textSurfaceObj = self._font_obj.render(self._text, True, self._text_color, self._bgd_color)

        # self._textRectObj = self._textSurfaceObj.get_rect()  # (3) create a rect object for the text
        # self._textRectObj.center = (self._center_posx, self._center_posy)  # (4) position the rect object
        return

    def get_rect(self):
        return self._textRectObj
