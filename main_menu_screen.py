import os
import pygame

# my edit : adding the bgm
from pygame import mixer

from globals import *
from save_load_module import save
from screen import Screen
from buttons import TextButton


class MainMenuScreen(Screen):
    def __init__(self, display_surf, logger):
        super(MainMenuScreen, self).__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._background_surf = pygame.image.load(os.path.join(graphics_path, "beyblade_logo.png")).convert_alpha()
        self._background_surf = pygame.transform.scale(self._background_surf, (int(WIDTH / 2), int(HEIGHT / 2)))
        font_size = 32  # text buttons font size
        self._buttons = {}
        self._buttons["play"] = TextButton(logger=self.logger,
                                           width=40, height=15,
                                           centerx=int(WIDTH / 2), centery=HEIGHT - int(HEIGHT / 4),
                                           text="Play", text_color=WHITE, bgd_color=BLACK,
                                           alt_text_color=BRIGHTYELLOW, font_size=font_size)
        self._buttons["quit"] = TextButton(logger=self.logger,
                                           width=40, height=15,
                                           centerx=int(WIDTH / 2),
                                           centery=self._buttons["play"].get_center_posy() + self._buttons[
                                               "play"].get_height() * 3,
                                           text="Quit Game", text_color=WHITE, bgd_color=BLACK,
                                           alt_text_color=BRIGHTYELLOW, font_size=font_size)

        self.reset_played_bbs()  # changes all BB status to not played
        return

    def on_update(self):
        for key, button in self._buttons.items():
            if button.on_update(self._l_mouse_clicked, self._mousex, self._mousey):
                self.on_exit(key)
        return

    def on_render(self):
        # my edit: running the mixer to play the sound
        mixer.init(44100, -16,2,2048)
        mixer.music.load('sounds/bgm.mp3')
        mixer.music.play(-1)
        
        self._display_surf.fill(BLACK)  # clear screen
        self._display_surf.blit(self._background_surf, (int(WIDTH / 4), int(HEIGHT / 8)))
        for button in self._buttons.values():
            button.on_render(self._display_surf)
        super(MainMenuScreen, self).on_render()
        return

    def on_exit(self, key):
        self._running = False
        if key == "play":
            # from battle_screen import BattleScreen
            # self._next_screen = BattleScreen
            from player_selection_screen import PlayerSelectionScreen
            self._next_screen = PlayerSelectionScreen
        elif key == "quit":
            self._next_screen = None
        return

    def reset_played_bbs(self):
        # reset the played BBs list from previous game
        bb_dict = {}
        for bb in BEYBLADES_LIST:
            key = bb + "_played"
            bb_dict[key] = False
        save(bb_dict)
        return

