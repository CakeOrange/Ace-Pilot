"""Author: Cheng Gao
   Date: May 4, 2015
   Description: This is the main game loop of our super breakout game.
   Press Space to start and use arrow keys to control the direction of the 
   paddle.
"""
# I - IMPORT AND INITIALIZE
import pygame
import mySprites
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))


def main():
    '''This function defines the 'mainline logic' for our Super Break-Out game.'''

    # DISPLAY
    pygame.display.set_caption("Ace Pilot v1.0")

    # ENTITIES

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # load game background music
    pygame.mixer.music.load(
        "music/bgm.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    is_shield_on = False  # (not finishing with shield)
    player = mySprites.Player(screen, is_shield_on)

    # player initial score and health
    player_score = mySprites.ScoreKeeper(screen)
    player_health = mySprites.PlayerHealth(screen)
    # enemy missiles initial speed
    missile_speed = 5

    # load two images as game background
    sky = mySprites.Background(screen)
    sky2 = mySprites.Background2(screen)

    # assigan player's x, y speed
    player_xspeed = 5
    player_yspeed = -5
    laser_sound = pygame.mixer.Sound("sound effects/laser.ogg")
    laser_sound.set_volume(0.5)
    enemy_explosion_sound = pygame.mixer.Sound("sound effects/explode.ogg")
    enemy_explosion_sound.set_volume(0.5)

    # put the sprites into group
    otherGroup = pygame.sprite.Group(player_score, player_health)
    aircraftGroup = pygame.sprite.Group(player)
    enemyGroup = pygame.sprite.Group(mySprites.Enemy(screen))
    playermissileGroup = pygame.sprite.Group()
    enemymissileGroup = pygame.sprite.Group()
    backgroundGroup = pygame.sprite.Group(sky, sky2)
    enemyHitPlayerGroup = pygame.sprite.Group()
    missileHitPlayerGroup = pygame.sprite.Group()
    potionGroup = pygame.sprite.Group()

    # load gameover image
    gameover = pygame.image.load("images/gameover1.gif")
    gameover = gameover.convert()

    # Action

    # Assign
    keepGoing = True
    clock = pygame.time.Clock()
    counter_for_spawning_enemy = 0  # a time counter used to spawn enemy
    # a time counter used to increase enemy missile speed
    counter_for_enemy_missile_speed = 0
    fire_cooldown = 20  # missile cooldown time
    fire = False  # determine if the player is firing missiles

    # Loop
    while keepGoing:
        clock.tick(30)
        counter_for_spawning_enemy += 1
        counter_for_enemy_missile_speed += 1

    # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_direction((-player_xspeed, 0))
                elif event.key == pygame.K_RIGHT:
                    player.change_direction((player_xspeed, 0))
                elif event.key == pygame.K_UP:
                    player.change_direction((0, -player_yspeed))
                elif event.key == pygame.K_DOWN:
                    player.change_direction((0, player_yspeed))
                elif event.key == pygame.K_SPACE:
                    fire = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    player.change_direction((0, 0))
                if event.key == pygame.K_SPACE:
                    fire = False
        # player is firing missiles
        if fire:
            if fire_cooldown == 0:
                playermissileGroup.add(mySprites.PlayerMissile(
                    screen, player.current_position()))
                laser_sound.play()
                fire_cooldown = 20

        # set a fire cooldown time so that the missile will not be casted too fast
        if fire_cooldown != 0:
            fire_cooldown -= 1

        # spawn enemy
        if counter_for_spawning_enemy == 50:
            enemyGroup.add(mySprites.Enemy(screen))
            counter_for_spawning_enemy = 0

        # enemy missile speed increases as time goes by
        if counter_for_enemy_missile_speed == 1000:
            if missile_speed != 15:
                missile_speed += 2
                counter_for_enemy_missile_speed = 0
            if missile_speed == 15:
                missile_speed += 0

        # check if player's missiles hit enemies
        for missile in playermissileGroup:
            collide_enemy = pygame.sprite.spritecollide(
                missile, enemyGroup, True)
            for enemy in collide_enemy:
                enemy_explosion_sound.play()
                player_score.player_scored()
                enemyHitPlayerGroup.add(mySprites.EnemyHitPlayer(
                    screen, enemy.current_position()))
                missile.kill()
                # the player will have a chance to earn a potion as reward every time
                # the player killed an enemy
                potion_reward = random.randint(1, 11)
                if potion_reward == 1:
                    potionGroup.add(mySprites.Potion(
                        screen, enemy.current_position()))

        # check if potion hit the player
        potion_hit_player = pygame.sprite.spritecollide(
            player, potionGroup, True)
        for potion in potion_hit_player:
            player_health.health_increase()

        # check if enemies hit the player
        enemy_hit_player = pygame.sprite.spritecollide(
            player, enemyGroup, True)
        for enemy2 in enemy_hit_player:
            enemy_explosion_sound.play()
            player_health.health_decrease()
            enemyHitPlayerGroup.add(mySprites.EnemyHitPlayer(
                screen, enemy2.current_position()))

        # enemies fire missiles
        for enemy3 in enemyGroup:
            enemy_missile_fire = random.randint(1, 30)
            if enemy_missile_fire == 1:
                enemymissileGroup.add(mySprites.EnemyMissile(
                    screen, enemy3.current_position(), missile_speed))

        # check if enemies' missiles hit the player
        emissle_hit_player = pygame.sprite.spritecollide(
            player, enemymissileGroup, True)
        for emissile in emissle_hit_player:
            enemy_explosion_sound.play()
            missileHitPlayerGroup.add(mySprites.MissleHitPlayer(
                screen, emissile.current_position()))
            player_health.health_decrease()

        # check if the player's health reaches 0
        if player_health.game_over():
            pygame.mixer.music.fadeout(2000)
            keepGoing = False

        backgroundGroup.clear(screen, background)
        playermissileGroup.clear(screen, background)
        aircraftGroup.clear(screen, background)
        otherGroup.clear(screen, background)
        enemyGroup.clear(screen, background)
        enemyHitPlayerGroup.clear(screen, background)
        enemymissileGroup.clear(screen, background)
        missileHitPlayerGroup.clear(screen, background)
        potionGroup.clear(screen, background)

        backgroundGroup.update()
        playermissileGroup.update()
        aircraftGroup.update()
        otherGroup.update()
        enemyGroup.update()
        enemyHitPlayerGroup.update()
        enemymissileGroup.update()
        missileHitPlayerGroup.update()
        potionGroup.update()

        backgroundGroup.draw(screen)
        playermissileGroup.draw(screen)
        aircraftGroup.draw(screen)
        otherGroup.draw(screen)
        enemyGroup.draw(screen)
        enemyHitPlayerGroup.draw(screen)
        enemymissileGroup.draw(screen)
        missileHitPlayerGroup.draw(screen)
        potionGroup.draw(screen)

        pygame.display.flip()

    screen.blit(gameover, (0, 0))
    pygame.display.flip()
    pygame.time.delay(2500)
    pygame.quit()


main()