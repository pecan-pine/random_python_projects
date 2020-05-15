# Simple pygame program
# Import and initialize the pygame lib
from settings import *
from sprites import *
from test_init import *
from functions import *
#from game_loop import *

pygame.mixer.music.load("song.wav")
pygame.mixer.music.play(loops=-1)
# Run until the user aks to quit
game_loop()
# Done! Time to quit.
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
