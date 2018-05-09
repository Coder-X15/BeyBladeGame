import pygame
from globals import *
from text import Text
import os


class Button(object):
    def __init__(self, logger, width, height, centerx, centery):
        self.logger = logger.getChild(__name__)
        self._width = width
        self._height = height
        self._centerx = centerx
        self._centery = centery
        self._text = ""
        # self._mouse_floats = False
        return

    def __str__(self):
        return self._text

    def on_render(self, display_surf):
        pass

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_center_posx(self):
        return self._centerx

    def get_center_posy(self):
        return self._centery


class TextButton(Button):

    def __init__(self, logger, width, height, centerx, centery, text, text_color, bgd_color, alt_text_color, font_size):
        super(TextButton, self).__init__(logger=logger, width=width, height=height, centerx=centerx, centery=centery)
        self._text_color = text_color
        self._bgd_color = bgd_color
        self._text = text

        self._text_obj = Text(text, centerx, centery, text_color, self._bgd_color, alt_text_color, font_size)
        return

    def on_update(self, clicked, mousex, mousey):
        rect = self._text_obj.get_rect()
        mouse_floats = rect.collidepoint(mousex, mousey)
        self._text_obj.on_update(mouse_floats=mouse_floats)
        if mouse_floats and clicked:
            return True
        else:
            return False

    def on_render(self, display_surf):
        self._text_obj.on_render(display_surf)
        return


class ImageButton(Button):

    def __init__(self, logger, width, height, image, centerx, centery):
        super(ImageButton, self).__init__(logger=logger, width=width, height=height, centerx=centerx, centery=centery)
        self._text = image.split('.png')[0]

        # original button image
        self._image_surf_orig = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf_orig = pygame.transform.smoothscale(self._image_surf_orig, (width, height))
        self._image_surf_orig_rect = self._image_surf_orig.get_rect(center=(centerx, centery))

        # large button image for when the mouse floats over the button
        self._image_surf_large = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf_large = pygame.transform.smoothscale(self._image_surf_large, (width+5, height+5))
        self._image_surf_large_rect = self._image_surf_large.get_rect(center=(centerx, centery))

        self._image_surf = self._image_surf_orig
        self._image_surf_rect = self._image_surf_orig_rect

        return

    def __str__(self):
        return self._text

    def on_update(self, clicked, mousex, mousey):
        mouse_floats = self._image_surf_rect.collidepoint(mousex, mousey)
        if mouse_floats:
            self._image_surf = self._image_surf_large
            self._image_surf_rect = self._image_surf_large_rect
            if clicked:
                return True
            else:
                return False
        else:
            self._image_surf = self._image_surf_orig
            self._image_surf_rect = self._image_surf_orig_rect
        return False

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        return


class ImageTextButton(Button):

    def __init__(self, logger, width, height, image, centerx, centery, pady, text, text_color, alt_text_color, font_size):
        super(ImageTextButton, self).__init__(logger=logger, width=width, height=height,
                                              centerx=centerx, centery=centery)
        self._text = text
        self._text_color = text_color

        # original button image
        self._image_surf_orig = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf_orig = pygame.transform.smoothscale(self._image_surf_orig, (width, height))
        self._image_surf_orig_rect = self._image_surf_orig.get_rect(center=(centerx, centery))

        # large button image for when the mouse floats over the button
        self._image_surf_large = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf_large = pygame.transform.smoothscale(self._image_surf_large, (width + 5, height + 5))
        self._image_surf_large_rect = self._image_surf_large.get_rect(center=(centerx, centery))

        self._image_surf = self._image_surf_orig
        self._image_surf_rect = self._image_surf_orig_rect

        pady = pady  # the distance between the image and the text

        self._text_obj = Text(text=text, center_posx=centerx, center_posy=centery + height/2 + pady,
                              text_color=text_color, bgd_color=None, alt_text_color=alt_text_color, font_size=font_size)

        self._mouse_floats = False
        return

    def on_collide(self, mousex, mousey):
        text_rect = self._text_obj.get_rect()
        return self._image_surf_rect.collidepoint(mousex, mousey) | text_rect.collidepoint(mousex, mousey)

    def on_update(self, clicked, mousex, mousey):
        mouse_floats = self.on_collide(mousex, mousey)
        self._text_obj.on_update(mouse_floats=mouse_floats)
        if mouse_floats:
            self._image_surf = self._image_surf_large
            self._image_surf_rect = self._image_surf_large_rect
            if clicked:
                return True
            else:
                return False
        else:
            self._image_surf = self._image_surf_orig
            self._image_surf_rect = self._image_surf_orig_rect
        return False

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        self._text_obj.on_render(display_surf)