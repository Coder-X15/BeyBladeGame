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
        self._player = player
        self._bb_profile = load_profile(name)

        # load profile
        self._max_hp = self._bb_profile["hp"]
        self._hp = int(self._max_hp)
        self._atk = self._bb_profile["atk"]
        self._def = self._bb_profile["def"]
        self._max_spd = self._bb_profile["spd"]
        self._spd = int(self._max_spd)
        self._max_radius = self.get_max_radius()
        self._radius = self._max_radius
        self._rotation_speed = None

        # BB images
        self._image_surf = None
        self._image_surf_rect = None
        self._image_surf_orig = None

        # parts images that break when the BB loses
        self._wheel_surf = None
        self._wheel_surf_rect = None
        self._spinner_surf = None
        self._spinner_surf_rect = None

        self._image_surf_angle = 0  # initial rotation angle
        if player:
            self._angle_degree = 180
        else:
            self._angle_degree = 0
        self._clockwise = 1

        self.load_image(name+'.png')

        self._attacking = False
        self._evading = False
        self._lost = False  # when BB loses, it breaks and spins out of screen

        # the BB passed through the center while trying to attack, if reached the edge stop the attack
        # self._passed_through_center = False
        self._dx = None  # movement vector towards center
        self._dy = None  # movement vector towards center

        return

    def on_update(self):
        self.rotate()  # BB always rotates
        self._update_radius()  # update radius according to BB action
        self._update_speed()  # return speed to regular values
        self.move_in_circle()  # BB always moves in circle

        # cx = self._image_surf_rect.centerx
        # cy = self._image_surf_rect.centery
        # self._logger.info("Player: {}\tCenter pos: {},{}".format(self._player, cx, cy))
        return

    def on_render(self, display_surf):
        if self._lost:
            # if BB lost render it's broken parts
            display_surf.blit(self._wheel_surf, (self._wheel_surf_rect.left, self._wheel_surf_rect.top))
            display_surf.blit(self._spinner_surf, (self._spinner_surf_rect.left, self._spinner_surf_rect.top))
        display_surf.blit(self._image_surf, (self._image_surf_rect.left, self._image_surf_rect.top))
        return

    def load_image(self, image):
        size_ratio = self._max_hp * 1.0 / MAX_ATTRIBUTE

        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf,
                                                  (int(BB_SIZE * size_ratio), int(BB_SIZE * size_ratio)))
        self._image_surf_rect = self._image_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self._image_surf_orig = self._image_surf

        self._wheel_surf = pygame.image.load(os.path.join(graphics_path, "metal_wheel.png")).convert_alpha()
        self._wheel_surf = pygame.transform.scale(self._wheel_surf,
                                                  (int(BB_SIZE * size_ratio * 0.67), int(BB_SIZE * size_ratio * 0.67)))
        self._wheel_surf_rect = self._wheel_surf.get_rect(center=(WIDTH /2, HEIGHT / 2))

        self._spinner_surf = pygame.image.load(os.path.join(graphics_path, "spinner.png")).convert_alpha()
        self._spinner_surf = pygame.transform.scale(self._image_surf,
                                                    (int(BB_SIZE * size_ratio * 0.5), int(BB_SIZE * size_ratio * 0.5)))
        self._spinner_surf_rect = self._spinner_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
        return

    def rotate(self):
        if self._lost:
            return
        self._image_surf_angle += 15
        self._image_surf = pygame.transform.rotozoom(self._image_surf_orig, self._image_surf_angle, 1)
        # Create a new rect with the center of the old rect.
        self._image_surf_rect = self._image_surf.get_rect(center=self._image_surf_rect.center)
        return

    def move_in_circle(self):
        angle_radians = math.radians(self._angle_degree)

        self._image_surf_rect.centerx = WIDTH / 2 + (self._radius * math.cos(angle_radians))
        self._image_surf_rect.centery = HEIGHT / 2 + (self._radius * math.sin(angle_radians))
        # self._angle_degree += 0.5

        self._angle_degree += self._clockwise * self._spd / MAX_ATTRIBUTE

        if self._lost:
            self._wheel_surf_rect.centerx = self._image_surf_rect.centerx + (self._radius * math.cos(angle_radians + math.pi/4))
            self._wheel_surf_rect.centery = self._image_surf_rect.centery + (self._radius * math.sin(angle_radians + math.pi/4))

            self._spinner_surf_rect.centerx = self._image_surf_rect.centerx + (self._radius * math.cos(angle_radians + math.pi/8))
            self._spinner_surf_rect.centerx = self._image_surf_rect.centerx + (self._radius * math.cos(angle_radians + math.pi/8))
        else:
            self._wheel_surf_rect.center = self._image_surf_rect.center
            self._spinner_surf_rect.center = self._image_surf_rect.center
        return

    def attack(self, opp_centerx, opp_centery):
        self._attacking = True
        self._evading = False
        # self.calc_movement_vector(opp_centerx, opp_centery)
        return

    def _update_radius(self):

        dr = self._spd / MAX_ATTRIBUTE  # calculate delta radius

        if self._lost:
            # when bb loses it spins out of screen
            self._radius += dr * 15
            return

        if self._attacking:
            if self._radius > 0:
                self._radius -= dr
                if abs(self._radius) < 5:
                    self._radius = 0
            elif self._radius == 0:
                self._attacking = False
        elif self._radius < self._max_radius:
            self._radius += dr
        else:
            self._radius = self._max_radius
        return

    def _update_speed(self):

        if self._attacking or self._lost:
            # if attacking keep speed steady
            return
        elif abs(self._spd - self._max_spd) <= 5:
            self._spd = self._max_spd
            self._evading = False
        elif self._spd < self._max_spd:
            self._spd += self._max_spd / MAX_ATTRIBUTE
        elif self._spd > self._max_spd:
            self._spd -= self._max_spd / MAX_ATTRIBUTE
        return

    def evade(self):
        # self._angle_degree += self._clockwise * self._spd * 10.0 / MAX_ATTRIBUTE
        self._spd += self._spd  # double the bb speed for a short duration to evade the enemy
        self._evading = True
        self._attacking = False

    def collided(self, opp_bb):

        opp_attack = opp_bb.get_atk()
        opp_spd = opp_bb.get_spd()

        delta_hp = 0

        if self._attacking:
            self._clockwise = -1 * self._clockwise  # change direction
        elif opp_bb.is_attacking():
            delta_hp = max(10, opp_attack - self._def)

        new_spd = max(10, self._spd - opp_spd)  # speed cannot decrease below 10

        print("Player: {}\tAttacking: {}\t\tATK: {}\tDEF: {}\t\tHP: {}\t*HP: {}\t\tSPD: {}\t*SPD: {}".format(self._player,
                                                                                                             self._attacking,
                                                                                                             self._atk,
                                                                                                             self._def,
                                                                                                             self._hp,
                                                                                                             self._hp - delta_hp,
                                                                                                             self._spd,
                                                                                                             new_spd
                                                                                                             ))
        # self._attacking = False
        self._hp -= delta_hp
        if self._hp < 0:
            self._hp = 0
        self._spd = new_spd
        pass

    def get_radius(self):
        # faster BBs can move with greater radius
        # return self._spd * 1.0 / MAX_ATTRIBUTE * MAX_RADIUS - self._image_surf_rect.width
        # TODO: need to fix this!
        return calc_distance(self._image_surf_rect.centerx, self._image_surf_rect.centery,
                             int(WIDTH/2.0), int(HEIGHT/2.0))

    def get_max_radius(self):
        # returns the maximum radius for the BB
        return self._max_spd * MAX_RADIUS * 1.0 / MAX_ATTRIBUTE
        # return self._max_spd * MAX_RADIUS * 1.0 / MAX_ATTRIBUTE - self._image_surf_rect.width/2

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

    def is_attacking(self):
        return self._attacking

    def unset_attacking(self):
        self._attacking = False

    def unset_evading(self):
        self._evading = False

    def set_lost(self):
        self._lost = True

    def is_out_of_screen(self):
        if self._image_surf_rect.left < 0 or self._image_surf_rect.right > WIDTH:
            return True
        elif self._image_surf_rect.top < 0 or self._image_surf_rect.bottom > HEIGHT:
            return True
        else:
            return False