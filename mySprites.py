import pygame
import random
# Generate a screen, and we will use it on our designing too
screen = pygame.Surface((780, 540))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, is_shield_on):
        # initialize the attributes of the sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(("images/aircraft.gif"))
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # put the player at the bottom center of the screen
        self.rect.center = (screen.get_width()/2, screen.get_height()-110)

        self.__dx = 0
        self.__dy = 0
        # to keep track of the screen surface and it will be needed in other methods
        self.__screen = screen
        self.__is_shield_on = is_shield_on

    def change_direction(self, xy_speed):
        # assign x,y speed for player
        self.__dx, self.__dy = xy_speed

    def current_position(self):
        # return the player's current left and top sides
        return self.rect.center

    def update(self):
        # reposition the sprite
        if self.__is_shield_on == False:
            if((self.rect.left > 0) and (self.__dx < 0)) or \
              ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)):
                self.rect.left += self.__dx * 2

            if ((self.rect.top > 0) and (self.__dy > 0)) or\
               ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
                self.rect.top -= self.__dy * 2
        if self.__is_shield_on == True:
            if((self.rect.left > 70) and (self.__dx < 0)) or \
              ((self.rect.right < self.__screen.get_width() - 70) and (self.__dx > 0)):
                self.rect.left += self.__dx * 2

            if ((self.rect.top > 50) and (self.__dy > 0)) or\
               ((self.rect.bottom < self.__screen.get_height() - 50) and (self.__dy < 0)):
                self.rect.top -= self.__dy * 2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        # initialize the attributes of the sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(("images/enemy.gif"))
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        # put the player at the bottom center of the screen
        self.rect.center = (random.randrange(
            100, screen.get_width(), 100), random.randrange(-600, 0, 100))
        self.__dy = random.randrange(1, 3)
        self.__dx = random.randrange(1, 3)
        # to keep track of the screen surface and it will be needed in other methods
        self.__screen = screen

    def current_position(self):
        return self.rect.midbottom

    def update(self):
        if self.rect.left < 0 or self.rect.right > screen.get_width()+10:
            self.__dx = -self.__dx

        if self.rect.top == self.__screen.get_height():
            self.kill()
        self.rect.left += self.__dx

        self.rect.top += self.__dy


class EnemyMissile(pygame.sprite.Sprite):
    def __init__(self, screen, enemy_current_positon, missile_speed):
        # initialize the attributes of the sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy_bullet.gif")
        self.image.set_colorkey((0, 0, 0))
        self.image = self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.center = enemy_current_positon
        # put the player at the bottom center of the screen

        self.__dy = missile_speed
        # to keep track of the screen surface and it will be needed in other methods
        self.__screen = screen

    def current_position(self):
        return self.rect.midbottom

    def update(self):
        if int(self.rect.top) > 780 or int(self.rect.top) < 0:
            self.kill()
        self.rect.top += self.__dy


class MissleHitPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(("images/player_explosion1.gif"))
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.counter = 0
        self.maxcount = 32
        self.__position = position

    def update(self):
        # combine the images into an animation by using a time counter
        self.counter += 1
        if self.counter == 2:
            self.image = pygame.image.load(
                ("images/player_explosion2.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 4:
            self.image = pygame.image.load(
                ("images/player_explosion3.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 6:
            self.image = pygame.image.load(
                ("images/player_explosion4.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 8:
            self.image = pygame.image.load(
                ("images/player_explosion5.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 10:
            self.image = pygame.image.load(
                ("images/player_explosion6.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 12:
            self.image = pygame.image.load(
                ("images/player_explosion7.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 14:
            self.image = pygame.image.load(
                ("images/player_explosion8.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 16:
            self.image = pygame.image.load(
                ("images/player_explosion9.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 18:
            self.image = pygame.image.load(
                ("images/player_explosion10.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 20:
            self.image = pygame.image.load(
                ("images/player_explosion11.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 22:
            self.image = pygame.image.load(
                ("images/player_explosion12.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 24:
            self.image = pygame.image.load(
                ("images/player_explosion13.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 26:
            self.image = pygame.image.load(
                ("images/player_explosion14.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 28:
            self.image = pygame.image.load(
                ("images/player_explosion15.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 30:
            self.image = pygame.image.load(
                ("images/player_explosion16.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == self.maxcount:
            self.kill()


class EnemyHitPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(("images/explosion1.gif"))
        self.image = self.image.convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.counter = 0
        self.maxcount = 24
        self.__position = position

    def update(self):
        # combine the images into an animation by using a time counter
        self.counter += 1
        if self.counter == 2:
            self.image = pygame.image.load(("images/explosion2.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 4:
            self.image = pygame.image.load(("images/explosion3.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 6:
            self.image = pygame.image.load(("images/explosion4.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 8:
            self.image = pygame.image.load(("images/explosion5.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 10:
            self.image = pygame.image.load(("images/explosion6.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 12:
            self.image = pygame.image.load(("images/explosion7.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 14:
            self.image = pygame.image.load(("images/explosion8.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 16:
            self.image = pygame.image.load(("images/explosion9.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 18:
            self.image = pygame.image.load(("images/explosion10.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 20:
            self.image = pygame.image.load(("images/explosion11.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == 22:
            self.image = pygame.image.load(("images/explosion12.gif"))
            self.image = self.image.convert()
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.center = self.__position
        elif self.counter == self.maxcount:
            self.kill()


class PlayerMissile(pygame.sprite.Sprite):
    def __init__(self, screen, player_current_positon):
        # initialize the attributes of the sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/Sprite_Bullets.gif")
        self.image.set_colorkey((0, 0, 0))
        self.image = self.image.convert()

        self.rect = self.image.get_rect()
        self.__x, self.__y = player_current_positon
        self.rect.center = (self.__x - 1, self.__y - 65)
        # put the player at the bottom center of the screen

        self.__dy = 5
        # to keep track of the screen surface and it will be needed in other methods
        self.__screen = screen

    def update(self):
        if self.rect.top < 1:
            self.kill()
        self.rect.top -= self.__dy


class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/sky.gif")
        self.image = self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.dy = 5
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1200:
            self.reset()

    def reset(self):
        self.rect.top = 0


class Background2(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/sky.gif")
        self.image = self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, -600)
        self.dy = 5
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 600:
            self.reset()

    def reset(self):
        self.rect.top = -600


class ScoreKeeper(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.__font = pygame.font.Font("04B_30__.ttf", 28)
        self.__score = 0

    def player_scored(self):
        '''This method decreases the user's life by 1'''
        self.__score += 10

    def game_over(self):
        '''This method is called when the player's life become 0'''
        if self.__score == 1000:
            return 1

    def update(self):
        '''This method will be called automatically to display 
        the current score at the left top of the game window.'''
        score = "SCORE: %d" % (self.__score)
        self.image = self.__font.render(score, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, 30)


class PlayerHealth(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.__font = pygame.font.Font("04B_30__.ttf", 28)
        self.__health = 100

    def health_decrease(self):
        '''This method decreases the user's life by 10'''
        self.__health -= 10

    def health_increase(self):
        '''This method increases the user's life by 10'''
        self.__health += 10

    def game_over(self):
        '''This method is called when the player's life become 0'''
        if self.__health == 0:
            return 1

    def update(self):
        '''This method will be called automatically to display 
        the current score at the left top of the game window.'''
        health = "Health: %d" % (self.__health)
        self.image = self.__font.render(health, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (130, 30)


class Shield(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/shield.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.__dx = 0
        self.__dy = 0
        self.__screen = screen
        self.__counter = 0
        self.__maxcount = 3000

    def change_direction(self, xy_speed):
        # assign x,y speed for player
        self.__dx, self.__dy = xy_speed

    def update(self):
        # reposition the sprite
        if((self.rect.left > 0) and (self.__dx < 0)) or \
          ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)):
            self.rect.left += self.__dx * 2

        if ((self.rect.top > 0) and (self.__dy > 0)) or\
                ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy * 2


class Potion(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/potion.gif")
        self.image = self.image.convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.__dy = 5
        self.__screen = screen

    def update(self):
        self.rect.bottom += self.__dy
        if self.rect.top > self.__screen.get_height():
            self.kill()