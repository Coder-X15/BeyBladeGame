import os
import pygame
from globals import *
from screen import Screen
from button import Button


class MainMenuScreen(Screen):
    def __init__(self, display_surf, logger):
        super().__init__(display_surf=display_surf, logger=logger.getChild(__name__))
        self._background_surf = pygame.image.load(os.path.join(graphics_path, "beyblade_logo.png")).convert_alpha()
        self._background_surf = pygame.transform.scale(self._background_surf, (int(WIDTH/2), int(HEIGHT/2)))
        self._buttons = {"play": Button(logger=self.logger,
                                        width=40, height=15,
                                        center_posx=int(WIDTH/2), center_posy=HEIGHT - int(HEIGHT/4),
                                        text="Play", text_color=WHITE, bgd_color=BLACK, alt_text_color=YELLOW)}
        self._buttons["quit"] = Button(logger=self.logger,
                                       width=40, height=15,
                                       center_posx=int(WIDTH/2),
                                       center_posy=self._buttons["play"].get_center_posy()+self._buttons["play"].get_height()*3,
                                       text="Quit Game", text_color=WHITE, bgd_color=BLACK, alt_text_color=YELLOW)

    def on_update(self):
        for key, button in self._buttons.items():
            if button.on_update(self._mouse_clicked, self._mousex, self._mousey):
                self.on_exit(key)
        return

    def on_render(self):
        self._display_surf.fill(BLACK)  # clear screen
        self._display_surf.blit(self._background_surf, (int(WIDTH/4), int(HEIGHT/8)))
        for button in self._buttons.values():
            button.on_render(self._display_surf)
        super().on_render()
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
