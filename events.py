import pygame
from pygame.locals import *


class CEvent(object):
    def __init__(self):
        self._mousex = 0
        self._mousey = 0
        self._l_mouse_clicked = False
        self._r_mouse_clicked = True
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
        self._mousex, self._mousey = event.pos
        pass

    def on_mouse_wheel(self):
        pass

    def on_lbutton_up(self, event):
        self._l_mouse_clicked = True
        pass

    def on_lbutton_down(self, event):
        pass

    def on_rbutton_up(self, event):
        self._r_mouse_clicked = True
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

    def on_exit(self, event=None):
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
        if event.type == pygame.QUIT:
            self.on_exit(event)

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
            self._mousex, self._mousey = event.pos
            if event.button == 1:
                self.on_lbutton_up(event)
            elif event.button == 2:
                self.on_mbutton_up(event)
            elif event.button == 3:
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
