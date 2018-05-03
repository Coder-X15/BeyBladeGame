import math
import os
import pygame

from pygame.locals import *

black = 0, 0, 0
graphics_path = "sources\graphics"
WIDTH = 640
HEIGHT = 480
# RESOLUTION = (WIDTH, HEIGHT)
FPS = 30


class Beyblade(object):
    def __init__(self, image, rotation_speed):
        self._image_surf = pygame.image.load(os.path.join(graphics_path, image)).convert_alpha()
        self._image_surf = pygame.transform.scale(self._image_surf, (100, 100))
        self._image_surf_rect = self._image_surf.get_rect(center=(100, 100))
        self._image_surf_orig = self._image_surf
        self._posx, self._posy = 60, 60
        self._speed = (0, 0)
        self._rotation_speed = rotation_speed
        self._image_surf_angle = 0
        return

    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self._image_surf_angle += self._rotation_speed
        self._image_surf = pygame.transform.rotozoom(self._image_surf_orig, self._image_surf_angle, 1)
        # Create a new rect with the center of the old rect.
        self._image_surf_rect = self._image_surf.get_rect(center=self._image_surf_rect.center)

    def move_in_circle(self):
        center_of_rotation_x = WIDTH / 2
        center_of_rotation_y = HEIGHT / 2
        radius = 50
        angle = math.radians(45)
        omega = 0.1  # angular velocity
        self._posx += radius*omega*math.cos(angle + math.pi/2)
        self._posy -= radius*omega*math.sin(angle + math.pi/2)

        print("pos: {},{}".format(self._posx, self._posy))

    def update(self):
        self.rotate()
        self.move_in_circle()
        return

    def render(self, display_surf):
        display_surf.blit(self._image_surf, (self._posx, self._posy))
        return


class CEvent:
    def __init__(self):
        pass

    def on_input_focus(self):
        pass

    def on_input_blur(self):
        pass

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

    def on_mouse_focus(self):
        pass

    def on_mouse_blur(self):
        pass

    def on_mouse_move(self, event):
        pass

    def on_mouse_wheel(self):
        pass

    def on_lbutton_up(self, event):
        pass

    def on_lbutton_down(self, event):
        pass

    def on_rbutton_up(self, event):
        pass

    def on_rbutton_down(self, event):
        pass

    def on_mbutton_up(self, event):
        pass

    def on_mbutton_down(self, event):
        pass

    def on_minimize(self):
        pass

    def on_restore(self):
        pass

    def on_resize(self, event):
        pass

    def on_expose(self):
        pass

    def on_exit(self):
        pass

    def on_user(self, event):
        pass

    def on_joy_axis(self, event):
        pass

    def on_joybutton_up(self, event):
        pass

    def on_joybutton_down(self, event):
        pass

    def on_joy_hat(self, event):
        pass

    def on_joy_ball(self, event):
        pass

    def on_event(self, event):
        print("on_event")
        if event.type == pygame.QUIT:
            self.on_exit()

        elif event.type >= USEREVENT:
            self.on_user(event)

        elif event.type == VIDEOEXPOSE:
            self.on_resize(event)

        elif event.type == KEYUP:
            self.on_key_up(event)

        elif event.type == KEYDOWN:
            self.on_key_down(event)

        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 0:
                self.on_lbutton_up(event)
            elif event.button == 1:
                self.on_mbutton_up(event)
            elif event.button == 2:
                self.on_rbutton_up(event)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 0:
                self.on_lbutton_down(event)
            elif event.button == 1:
                self.on_mbutton_down(event)
            elif event.button == 2:
                self.on_rbutton_down(event)

        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()


class App(CEvent):

    def __init__(self):
        print("__init__")
        self.clock = pygame.time.Clock()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.beyblades_list = []

    def on_init(self):
        print("on_init")
        pygame.init()
        pygame.display.set_caption("MyGame")
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.beyblades_list.append(Beyblade('golden.png', 90))
        self._running = True
        return True

    def on_loop(self):
        print("on_loop")
        for beyblade in self.beyblades_list:
            beyblade.update()
        pass

    def on_render(self):
        print("on_render")
        self._display_surf.fill(black)  # clear screen
        for beyblade in self.beyblades_list:
            beyblade.render(self._display_surf)
        pygame.display.update()
        # pygame.display.flip()
        self.clock.tick(FPS)
        pass

    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        print("on_cleanup")
        pygame.quit()

    def on_execute(self):
        print("on_execute")
        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
