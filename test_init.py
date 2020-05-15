from settings import *
from sprites import *

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Lost at Sea')

#setup a clock
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 100)
ADDBLUE = pygame.USEREVENT+4
pygame.time.set_timer(ADDBLUE,500)
ADDCLOUD = pygame.USEREVENT+2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDFISH = pygame.USEREVENT+3
pygame.time.set_timer(ADDFISH,1000)
# Instantiate player. Right now, this is just a rectangle.

