#Imports
from turtle import Screen
import pygame, sys
from pygame.locals import *
import random, time
import os
#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SPEED = 5
SCORE = 0
COINS = 0
LEVEL = 0
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (167,20,20))
score_font1 = pygame.font.SysFont("comicsansms", 40)

background = pygame.image.load(os.path.join("images", "AnimatedStreet.png"))

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

def Your_score1(SCORE):
    value = score_font1.render("Your Score: " + str(SCORE), True, (66,145,51))
    DISPLAYSURF.blit(value, [70, 250])

def Your_coins1(COINS):
    value = score_font1.render("Your Coins: " + str(COINS), True, (66,145,51))
    DISPLAYSURF.blit(value, [70, 300])
def Your_level1(LEVEL):
    value = score_font1.render("Your Level: " + str(LEVEL), True, (66,145,51))
    DISPLAYSURF.blit(value, [70, 350])

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("images", "enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class food(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("images", "coin.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
       # global SCORE
        self.rect.move_ip(0,COIN_SPEED)
        if (self.rect.bottom > 600):
          #  SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def appear(self): 
        self.rect.top = 0 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),  random.randint(0, 100)) 
class food2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image =  pygame.transform.scale(pygame.image.load(os.path.join('images','dollarr.png')),(50,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
       # global SCORE
        self.rect.move_ip(0,COIN_SPEED)
        if (self.rect.bottom > 600):
          #  SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def appear(self): 
        self.rect.top = 0 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40),  random.randint(0, 100)) 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(os.path.join("images", "player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top < SCREEN_HEIGHT:        
              if pressed_keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:        
              if pressed_keys[K_DOWN]:
                  self.rect.move_ip(0, 5)         

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = food()
D1 = food2()

#Creating Sprites Groups
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group() 
dollar = pygame.sprite.Group() 
all_sprites = pygame.sprite.Group()

enemies.add(E1)  
player.add(P1)  
coins.add(C1) 
dollar.add(D1)

all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(D1)

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if COINS >= 5 and COINS < 10:
          SPEED = 7
          LEVEL = 1
        if COINS >= 10 and COINS < 15:
          SPEED = 9
          LEVEL = 2
        if COINS >= 20 and COINS < 25:
          SPEED = 11
        if COINS >= 30:
          SPEED = 15
          LEVEL = 3



    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score: " +str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coins = font_small.render("Coin: " +str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (150,10))
    levels = font_small.render("Level: " +str(LEVEL), True, BLACK)
    DISPLAYSURF.blit(levels, (270,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(os.path.join('music', 'crash.wav')).play()
          time.sleep(1)
                   
          DISPLAYSURF.fill((14,236,255))
          DISPLAYSURF.blit(game_over, (30,150))
          
          Your_score1(SCORE)
          Your_coins1(COINS)
          Your_level1(LEVEL)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(3)
          pygame.quit()
          sys.exit() 
    #coins collection             
    if pygame.sprite.spritecollideany(C1, player): # coin --> 1 coin is earned 
        #pygame.mixer.Sound.play('coin.wav')
        COINS += 1 
        C1.appear() 
    if pygame.sprite.spritecollideany(D1, player): # dollar --> 1 coin is earned 
        #pygame.mixer.Sound.play('coin.wav')
        COINS += 2 
        D1.appear()            
    pygame.display.update()
    FramePerSec.tick(FPS)
