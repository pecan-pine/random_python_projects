from settings import *
# Define a Player object by extending pygame.sprite.Sprite

# The surface drawn on the screen is now an attribute of 'player'
enemies = pygame.sprite.Group()
friends = pygame.sprite.Group()
missiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


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
class Cloud(Friend):
    def __init__(self,picture = 'cloud.png'):
        super(Cloud,self).__init__(picture)
class Fish(Friend):
    def __init__(self, picture='fish2.png'):
        super(Fish, self).__init__(picture)
        self.surf = pygame.transform.flip(self.surf, True, False)
class Enemy(pygame.sprite.Sprite):
    def __init__(self,picture):
        super(Enemy, self).__init__()
        self.speed = random.randint(1, 10)
        self.image = pygame.image.load(picture).convert()
        self.image = pygame.transform.scale(self.image, (50,25))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.surf = pygame.Surface((20, 15))
        self.surf.fill((20, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_W+20, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
class SmallFish(Enemy):
    def __init__(self, picture='fish.png'):
        super(SmallFish, self).__init__(picture)
        '''
        self.speed = random.randint(-10,10)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_W + 100),
                random.randint(0, SCREEN_H),
            )
        )'''
class BlueFish(Enemy):
    def __init__(self,picture='bluefish.png'):
        super(BlueFish,self).__init__(picture)
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.surf = pygame.Surface((20, 15))
class Missile(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos):
        super(Missile, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 20))
        self.rect = self.surf.get_rect(center=(xpos,ypos))
        self.speed = 20

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_W:
            self.kill()
