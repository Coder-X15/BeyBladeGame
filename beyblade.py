import pygame
from globals import *
from save_load_module import load_profile
import math
import os


class Beyblade(object):
    def __init__(self, logger, image):
        self._name = image.split(".png")[0]
        self._logger = logger.getChild(self._name)

        self._max_hp = None
        self._atk = None
        self._def = None
        self._spd = None
        self._max_spd = None
        self._rotation_speed = None
        self._radius = None

        self._image_surf = None
        self._image_surf_rect = None
        self._image_surf_orig = None
        self._image_surf_angle = 0  # initial rotation angle
        self._movement_counter = 1
        # self._rotation_counter = 0
        self._angle_degree = 0

        self.get_profile()
        self.load_image(image)
        self._radius = self.get_radius()

    def get_profile(self):
        profile_dict = load_profile(self._name)
        self._max_hp = profile_dict["hp"]
        self._atk = profile_dict["atk"]
        self._def = profile_dict["def"]
        self._max_spd = profile_dict["spd"]
        self._spd = int(self._max_spd)
        return

    def load_image(self, image):
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        size_ratio = self._max_hp * 1.0 / MAX_ATTRIBUTE
        self._image_surf = pygame.transform.scale(self._image_surf,
                                                  (int(BB_SIZE * size_ratio), int(BB_SIZE * size_ratio)))
        self._image_surf_rect = self._image_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self._image_surf_orig = self._image_surf
        return

    def get_radius(self):
        return self._spd * 1.0 / MAX_ATTRIBUTE * MAX_RADIUS - self._image_surf_rect.width  # faster BBs can move with greater radius

    def rotate(self):
        # def do_rotate():
        #     if (self._rotation_counter % self._rotation_speed) == 0:
        #         self._rotation_counter = 1
        #         self._logger.info("rotate")
        #         return True
        #     else:
        #         self._rotation_counter += 1
        #         self._logger.info("dont rotate")
        #         return False
        #
        # """Rotate the image of the sprite around its center."""
        # if not do_rotate():
        #     return

        self._image_surf_angle += 15
        self._image_surf = pygame.transform.rotozoom(self._image_surf_orig, self._image_surf_angle, 1)
        # Create a new rect with the center of the old rect.
        self._image_surf_rect = self._image_surf.get_rect(center=self._image_surf_rect.center)
        return

    def do_move(self):
        if (self._movement_counter % self._spd) == 0:
            self._movement_counter = 1
            return True
        else:
            self._movement_counter += 1
            return False

    def move_in_circle(self):
        # if not self.do_move():
        #     return

        angle_radians = math.radians(self._angle_degree)

        # centerx = center_of_rotationx + radius * cos(theta)
        # centery = center_of_rotationy + radius * sin(theta)
        self._image_surf_rect.centerx = WIDTH / 2 + (self._radius * math.cos(angle_radians))
        self._image_surf_rect.centery = HEIGHT / 2 + (self._radius * math.sin(angle_radians))
        self._angle_degree += 0.5
        # self._angle_degree = self._angle_degree % 360
        return

    def on_update(self):
        self.rotate()
        self.move_in_circle()
        # self._logger.info("Center pos: {},{}".format(self._image_surf_rect.centerx, self._image_surf_rect.centery))
        return

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        return
