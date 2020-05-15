from settings import *
# Define a Player object by extending pygame.sprite.Sprite

# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("boat.png").convert()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 20))
        self.rect = self.surf.get_rect()
    # Move the sprite based on user keypresses

    def update(self, pressed_keys):
        move_amount = 10
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -move_amount)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, move_amount)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-move_amount, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(move_amount, 0)
        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_H:
            self.rect.bottom = SCREEN_H
# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf = pygame.image.load('cloud.png').convert()
        self.surf = pygame.transform.flip(self.surf,True,False)
        self.surf = pygame.transform.scale(self.surf,(50,50))
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_W + 20, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf = pygame.image.load('fish2.png').convert()
        #self.surf = pygame.transform.flip(self.surf,True,False)
        self.surf = pygame.transform.scale(self.surf,(50,50))
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_W + 20, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )
        self.speed = 5
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("fish.png").convert()
        self.image = pygame.transform.scale(self.image, (50,25))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.Surface((20, 5))
        self.surf.fill((20, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )
        self.speed = random.randint(-20, 20)
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()