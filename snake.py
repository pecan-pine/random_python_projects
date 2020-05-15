# Simple pygame program
# Import and initialize the pygame lib
from settings import *
from init import *
from sprites import *
#from game_loop import *


# Create the scree object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Run until the user aks to quit
running = True
snake = Snake()
player.add(snake)
all_sprites.add(snake)
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click te window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        elif event.type == ADDFOOD:
            new_food = Food()
            food.add(new_food)
            all_sprites.add(new_food)
    pressed_keys = pygame.key.get_pressed()
    screen.fill((100, 100, 200))
    player.update(pressed_keys)
    food.update()
    screen.blit(snake.surf, snake.rect)
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)
    if pygame.sprite.spritecollideany(snake, food):
        pygame.sprite.spritecollideany(snake, food).kill()
        snake.life = snake.life + 10
        snake.surfsize = snake.surfsize+10
        snake.surfcolor = (200,0,0)
    if len(player) == 0:
        screen.fill((100, 100, 200))
    message_display("life:"+str(snake.life))
    pygame.display.flip()
    #clock.tick(30)
    time.sleep(.05)
    # Look at every event in the queue
# Done! Time to quit.
pygame.quit()