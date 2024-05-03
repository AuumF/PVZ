import pygame
import sys
from pygame.locals import *

pygame.init()

DS = pygame.display.set_mode( (1280 , 600) )
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DS.fill( (255,255,255) )
    pygame.display.update()