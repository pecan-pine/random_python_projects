from settings import *
#from sprites import *

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#title at top of window
pygame.display.set_caption('Snake')

#setup a clock
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy

ADDFOOD = pygame.USEREVENT + 1
pygame.time.set_timer(ADDFOOD, 1000)
ADDBLUE = pygame.USEREVENT+4
pygame.time.set_timer(ADDBLUE,500)
ADDCLOUD = pygame.USEREVENT+2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDFISH = pygame.USEREVENT+3
pygame.time.set_timer(ADDFISH,1000)
# Instantiate player. Right now, this is just a rectangle.

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (200,100)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()