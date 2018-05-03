import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)  # (1) create a pygame font object
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)  # (2) create a surface with text drawn on it
textRectObj = textSurfaceObj.get_rect()  # (3) create a rect object for the text
textRectObj.center = (200, 150)  # (4) position the rect object

while True:  # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)  # (5) blit the text surface onto the display surface
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()  # (6) call update
