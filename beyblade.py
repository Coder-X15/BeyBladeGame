"""
Beyblade Class

HP: BB's health before it breaks
ATK: BB's damage when hitting an opponent BB
DEF: BB's defense when being hit
SPD: BB's attack speed, how fast can it move in a vector or evade. It can also determine the BB's movement radius
"""


import pygame
from globals import *
from save_load_module import load_profile
from utils import calc_distance
import math
import os


class Beyblade(object):
    def __init__(self, logger, name, player=False):
        self._logger = logger.getChild(name)

        self._name = name
        self._player = True
        self._bb_profile = load_profile(name)

        # load profile
        self._max_hp = self._bb_profile["hp"]
        self._hp = int(self._max_hp)
        self._atk = self._bb_profile["atk"]
        self._def = self._bb_profile["def"]
        self._max_spd = self._bb_profile["spd"]
        self._spd = int(self._max_spd)
        self._rotation_speed = None

        self._image_surf = None
        self._image_surf_rect = None
        self._image_surf_orig = None
        self._image_surf_angle = 0  # initial rotation angle
        if player:
            self._angle_degree = 180
        else:
            self._angle_degree = 0

        self.load_image(name+'.png')
        self._radius = self.get_max_radius()

        self._attacking = False
        self._passed_through_center = False  # the BB passed through the center while trying to attack, if reached the edge stop the attack
        self._dx = None  # movement vector towards center
        self._dy = None  # movement vector towards center
        return

    def on_update(self):
        self.rotate()

        if self.get_radius() > self.get_max_radius():
            # BB reached the edge of the arena
            self._logger.error("actual radius: {} > max radius: {}".format(self.get_radius(), self.get_max_radius()))
            self._attacking = False

        if not self._attacking:
            self.move_in_circle()
        else:
            self.move_in_vector()
        self._logger.info("Player: {}\tCenter pos: {},{}".
                          format(self._player, self._image_surf_rect.centerx, self._image_surf_rect.centery))
        return

    def on_render(self, display_surf):
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        return

    def load_image(self, image):
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        size_ratio = self._max_hp * 1.0 / MAX_ATTRIBUTE
        self._image_surf = pygame.transform.scale(self._image_surf,
                                                  (int(BB_SIZE * size_ratio), int(BB_SIZE * size_ratio)))
        self._image_surf_rect = self._image_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self._image_surf_orig = self._image_surf
        return

    def rotate(self):
        self._image_surf_angle += 15
        self._image_surf = pygame.transform.rotozoom(self._image_surf_orig, self._image_surf_angle, 1)
        # Create a new rect with the center of the old rect.
        self._image_surf_rect = self._image_surf.get_rect(center=self._image_surf_rect.center)
        return

    def move_in_circle(self):
        angle_radians = math.radians(self._angle_degree)

        self._image_surf_rect.centerx = WIDTH / 2 + (self._radius * math.cos(angle_radians))
        self._image_surf_rect.centery = HEIGHT / 2 + (self._radius * math.sin(angle_radians))
        self._angle_degree += 0.5
        return

    def attack(self, opp_centerx, opp_centery):
        self._attacking = True
        self.calc_movement_vector(opp_centerx, opp_centery)
        return

    def calc_movement_vector(self, opp_centerx, opp_centery):
        bb_centerx = self._image_surf_rect.centerx
        bb_centery = self._image_surf_rect.centery
        # g_centerx = int(WIDTH/2.0)
        # g_centery = int(HEIGHT/2.0)

        # self._dx = g_centerx - bb_centerx
        # self._dy = g_centery - bb_centery
        self._dx = opp_centerx - bb_centerx
        self._dy = opp_centery - bb_centery
        return

    def move_in_vector(self):

        bb_centerx = self._image_surf_rect.centerx
        bb_centery = self._image_surf_rect.centery

        dx = int(self._dx * self._spd / MAX_ATTRIBUTE / 80)
        dy = int(self._dy * self._spd / MAX_ATTRIBUTE / 80)

        self._image_surf_rect.centerx = bb_centerx + dx
        self._image_surf_rect.centery = bb_centery + dy

        return

    def _check_passed_through_center(self):
        return self._image_surf_rect.collidepoint(int(WIDTH / 2.0), int(HEIGHT / 2.0))

    def evade(self):
        self._angle_degree += int(self._spd * 1.0 / MAX_ATTRIBUTE)
        return

    def collided(self, opp_attack, opp_spd):
        self._attacking = False
        self._hp -= int(opp_attack * 1.0 * self._def / MAX_ATTRIBUTE)
        self._spd = max(10, self._spd - opp_spd)  # speed cannot decrease below 10
        pass

    def get_radius(self):
        # faster BBs can move with greater radius
        # return self._spd * 1.0 / MAX_ATTRIBUTE * MAX_RADIUS - self._image_surf_rect.width
        # TODO: need to fix this!
        return calc_distance(self._image_surf_rect.centerx, self._image_surf_rect.centery,
                             int(WIDTH/2.0), int(HEIGHT/2.0))

    def get_max_radius(self):
        # returns the maximum radius for the BB
        return self._max_spd * MAX_RADIUS * 1.0 / MAX_ATTRIBUTE - self._image_surf_rect.width

    def get_rect(self):
        return self._image_surf_rect

    def get_hp(self):
        return self._hp

    def get_atk(self):
        return self._atk

    def get_def(self):
        return self._def

    def get_spd(self):
        return self._spd
