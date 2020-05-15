from settings import *
from sprites import *
from test_init import *
from functions import *

def game_loop():
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ESCAPE ):
                running = False
        # Add a new enemy?
            elif event.type == ADDENEMY:
        # Create the new enemy and add it to sprite groups
                new_enemy = SmallFish()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                friends.add(new_cloud)
                all_sprites.add(new_cloud)
            elif event.type == ADDFISH:
                new_fish = Fish()
                friends.add(new_fish)
                all_sprites.add(new_fish)
            elif event.type == ADDBLUE:
                new_fish = BlueFish()
                enemies.add(new_fish)
                all_sprites.add(new_fish)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        # Update enemy position
        enemies.update()
        friends.update()
        missiles.update()
        # Fill the background with white
        screen.fill((100, 80,200))

        for missile in missiles:
            screen.blit(missile.surf,(missile.rect.left+10,missile.rect.top+10))
        for friend in friends:
            screen.blit(friend.surf,friend.rect)
        screen.blit(player.image, (player.rect.left-40,player.rect.top-45))
        for enemy in enemies:
            if isinstance(enemy,BlueFish):
                screen.blit(enemy.image, (enemy.rect.left -50, enemy.rect.top -15))
            else:
                screen.blit(enemy.image,(enemy.rect.left-10,enemy.rect.top-10))
        # Draw all sprites
        #for enemy in all_sprites:
         #   screen.blit(enemy.surf, enemy.rect)
        # Check if any enemies have collided with the player

        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            died_sound.play()
            player.kill()
            crash()
            running = False
            time.sleep(1)
        if pygame.sprite.spritecollideany(player,friends):
            fishtype = type(pygame.sprite.spritecollideany(player,friends)).__name__
            if fishtype == 'Cloud':
                new_fish = Cloud()
            elif fishtype == 'Fish':
                new_fish = Fish()
            friends.add(new_fish)
            all_sprites.add(new_fish)
            #friends.update()
            for friend in friends:
                screen.blit(friend.surf, friend.rect)
        for enemy in enemies:
            if pygame.sprite.spritecollideany(enemy,friends):
                enemy.kill()
                pygame.sprite.spritecollideany(enemy, friends).speed = -8
            if pygame.sprite.spritecollideany(enemy,missiles):
                missile_hit.play()
                enemy.kill()
                pygame.sprite.spritecollideany(enemy, missiles).kill()
        pygame.display.flip()
        time.sleep(.04)
        # Ensure program maintains a rate of 30 frames per second
        #clock.tick(15)

        # Look at every event in the queue