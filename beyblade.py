import pygame
from globals import *
import math
import os


class Beyblade(object):
    def __init__(self, logger, image, rotation_speed, movement_speed):
        assert(logger is not None), "Beyblade object got not logger!"
        self.logger = logger.getChild(__name__)
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf, (100, 100))
        self._image_surf_rect = self._image_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self._image_surf_orig = self._image_surf
        self._posx, self._posy = 0, 0  # position of objects top left
        self._center_of_rotation_x = WIDTH / 2
        self._center_of_rotation_y = HEIGHT / 2
        self._radius = 50
        self._angle_degree = 0
        self._rotation_speed = rotation_speed
        self._rotation_counter = 1
        self._movement_speed = movement_speed
        self._movement_counter = 1
        self._image_surf_angle = 0
        return

    def rotate(self):
        def do_rotate():
            if (self._rotation_counter % self._rotation_speed) == 0:
                self._rotation_counter = 1
                self.logger.info ("rotate")
                return True
            else:
                self._rotation_counter += 1
                self.logger.info ("dont rotate")
                return False

        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        if not do_rotate():
            return

        self._image_surf_angle += 90
        if self._image_surf_angle % 360 == 0:
            self._image_surf_angle = 0
        self._image_surf = pygame.transform.rotozoom(self._image_surf_orig, self._image_surf_angle, 1)
        # Create a new rect with the center of the old rect.
        self._image_surf_rect = self._image_surf.get_rect(center=self._image_surf_rect.center)
        return

    def do_move(self):
        if (self._movement_counter % self._movement_speed) == 0:
            self._movement_counter = 1
            return True
        else:
            self._movement_counter += 1
            return False

    def move_in_circle(self):
        if not self.do_move():
            return

        angle_radians = math.radians(self._angle_degree)
        # omega = 0.1  # angular velocity
        # self._posx = radius*omega*math.cos(angle + math.pi/2)
        # self._posy = radius*omega*math.sin(angle + math.pi/2)

        self._image_surf_rect.centerx = self._center_of_rotation_x + (self._radius * math.cos(angle_radians))
        self._image_surf_rect.centery = self._center_of_rotation_y + (self._radius * math.sin(angle_radians))
        self._angle_degree += 5
        self._angle_degree = self._angle_degree % 360
        return

    def on_update(self):
        self.rotate()
        self.move_in_circle()
        self.logger.info("Center pos: {},{}".format(self._image_surf_rect.centerx, self._image_surf_rect.centery))
        return

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        return
