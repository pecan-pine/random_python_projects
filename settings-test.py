import pygame, time,random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE as ESCAPE,
    K_SPACE as SPACE,
    KEYDOWN,
    QUIT,
)


#SCREEN WIDTH AND HEIGHT
SCREEN_W = 1500
SCREEN_H = 1000

#sounds
pygame.mixer.init()
move_sound = pygame.mixer.Sound('motor2.wav')
missile_sound = pygame.mixer.Sound('missile.wav')    #'horn2.wav')
missile_hit = pygame.mixer.Sound('missile_hit.wav')
died_sound = pygame.mixer.Sound('died.wav')