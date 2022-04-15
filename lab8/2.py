from operator import truediv
import random
import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

photo = pygame.image.load('road.png')

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DISPLAYSURF.blit(photo , (0 , 0))

pygame.display.update()


def check(n):
    if n % 10 == 0:
        return True
    return False


class Enemy(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


    def move(self):
        n = 8
        if check == True:
            n += 5
        self.rect.move_ip(0, n)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(95, 305), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 



class Coin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 7)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(95, 305), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin2(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 6)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(95, 305), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
        self.cnt = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()


cnt = 0
count = 0

coins = pygame.sprite.Group()
coins.add(C1)

coins2 = pygame.sprite.Group()
coins2.add(C2)

enemys = pygame.sprite.Group()
enemys.add(E1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if pygame.sprite.spritecollideany(P1 , coins):
        count += 1
        C1.rect.center = (random.randint(95, 305), 0)

    if pygame.sprite.spritecollideany(P1 , coins2):
        count += 1
        C2.rect.center = (random.randint(95, 305), 0)

    if pygame.sprite.spritecollideany(P1, enemys):
        cnt += 1


    if cnt >= 1:
        font = pygame.font.Font(None, 80)
        text1 = font.render('game over' , True , (0 , 0 , 255))
        DISPLAYSURF.fill((255 , 0 , 0))
        DISPLAYSURF.blit(text1, [40, 250])
    else:
        P1.update()
        check(count)
        E1.move()
        C1.move()   
        C2.move()

        DISPLAYSURF.blit(photo , (0 , 0))


        font2 = pygame.font.Font(None, 60)
        text2 = font2.render(f'Coins : {count}' , True , (255 , 255 , 0))
        DISPLAYSURF.blit(text2, [0 , 0])

        P1.draw(DISPLAYSURF)
        E1.draw(DISPLAYSURF)
        C1.draw(DISPLAYSURF)
        C2.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()