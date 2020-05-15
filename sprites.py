from settings import *
# Define a Player object by extending pygame.sprite.Sprite

# The surface drawn on the screen is now an attribute of 'player'
all_sprites = pygame.sprite.Group()
player = pygame.sprite.Group()
food = pygame.sprite.Group()

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.speed= 50
        self.life = 100
        self.surfsize = 20
        self.surfcolor = (200,200,100)
        self.surf = pygame.Surface((self.surfsize,self.surfsize))
        self.surf.fill(self.surfcolor)
        self.rect = self.surf.get_rect()
        self.xdir = self.speed
        self.ydir = 0
    def update(self, pressed_keys):
        self.surf = pygame.Surface((self.surfsize,self.surfsize))
        self.surf.fill(self.surfcolor)
        if self.speed >= 11 and self.surfsize >= 20:
            self.speed = self.speed-1
        elif self.surfsize >= 20:
            self.surfsize = self.surfsize - 1
        else:
            self.surfsize = 20
            self.surfcolor=(200, 200, 100)
            self.life = self.life - 1
        if self.life <= 0:
            self.kill()
        self.rect.move_ip(self.xdir,self.ydir)
        if pressed_keys[K_UP]:
            self.xdir = 0
            self.ydir = -self.speed
        if pressed_keys[K_DOWN]:
            self.xdir = 0
            self.ydir = self.speed
        if pressed_keys[K_LEFT]:
            self.xdir = -self.speed
            self.ydir = 0
        if pressed_keys[K_RIGHT]:
            self.xdir = self.speed
            self.ydir = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.life = 100
        self.surf = pygame.Surface((20,20))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    def update(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.kill()
'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("boat.png").convert()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255, 255, 20))
        self.rect = self.surf.get_rect()

    def fire_missile(self):
        new_missile = Missile(self.rect.left,self.rect.top)
        missiles.add(new_missile)
        all_sprites.add(new_missile)
        missile_sound.play()


    # Move the sprite based on user keypresses

    def update(self, pressed_keys):
        move_amount = 5
        if pressed_keys[SPACE]:
            self.fire_missile()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -move_amount)
            #move_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, move_amount)
            #move_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-move_amount, 0)
            #move_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(move_amount, 0)
            #move_sound.play()
        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_W:
            self.rect.right = SCREEN_W

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_H:
            self.rect.bottom = SCREEN_H
#the class friend is for fishes that it doesn't matter if you hit
class Friend(pygame.sprite.Sprite):
    def __init__(self,picture):
        super(Friend, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf = pygame.image.load(picture).convert()
        self.surf = pygame.transform.flip(self.surf,True,False)
        self.surf = pygame.transform.scale(self.surf,(50,50))
        self.surf.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_W + 20, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )
        self.speed = random.randint(5, 8)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            '''