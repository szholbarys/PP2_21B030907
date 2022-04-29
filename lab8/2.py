import pygame, sys, os
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# main parameters
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Car_collison game!')
clock = pygame.time.Clock()
FPS = 60

# car size and speed
car_width, car_length = 40, 80
speed = 5

# score counter
score = 0

# all fonts
font = pygame.font.SysFont('Calibri',60)
font_score = pygame.font.SysFont('Calibri',20)
go = pygame.image.load(os.path.join('image','ramadan.png'))

# background фон
bg = pygame.image.load(os.path.join('image','street.png'))

# game music
pygame.mixer.music.load(os.path.join('music','background.wav'))
pygame.mixer.music.play(-1)

# player info
class Player(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load(os.path.join('image','player.png'))
      self.rect = self.image.get_rect()
      self.rect.center = (WIDTH/2 - car_width/2, HEIGHT - car_length)
   
   def move(self):
      pressed = pygame.key.get_pressed()
      if self.rect.left > 0:
         if pressed[K_LEFT]:
            self.rect.move_ip(-10,0)
      if self.rect.right < WIDTH:
         if pressed[K_RIGHT]:
            self.rect.move_ip(10,0)

# enemies info
class Enemy(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load(os.path.join('image','enemy.png'))
      self.rect = self.image.get_rect()
      self.rect.center = (randint(car_width,WIDTH-car_width),0)
   
   def move(self):
      global score
      self.rect.move_ip(0,speed)
      if self.rect.top > HEIGHT:
         self.rect.top = 0
         self.rect.center = (randint(30,370),0)
         score += 1

# Coin info
coin_cnt = 0
font_coin = pygame.font.SysFont('Calibri', 20)

class Coin(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.transform.scale(pygame.image.load(os.path.join('image','burger.png')),(50,40))
      self.rect = self.image.get_rect()
      self.rect.center = (randint(50,WIDTH-50),0)
   
   def move(self):
      self.rect.move_ip(0,3)
      if self.rect.top > HEIGHT:
         self.rect.top = 0
         self.rect.center = (randint(50,WIDTH-50),0)

   def disappear(self):
      self.rect.top = 0
      self.rect.center = (randint(40,WIDTH-50),0)

# represent both player and enemies, also coins
p1 = Player()
e1 = Enemy()
c1 = Coin()

# Sprites
enemies = pygame.sprite.Group()
enemies.add(e1)

all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c1)

coins = pygame.sprite.Group()
coins.add(c1)

# my event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 5000)

while True:

   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

      if event.type == inc_speed:
         speed += 0.5

   screen.blit(bg,(0,0))

   # show the score on the screen(right top corner)
   show = font_score.render(f'P:{str(score)}',True,black)
   screen.blit(show,(WIDTH-38,20))
      
   #Moves and Re-draws all Sprites
   for entity in all_sprites:
      screen.blit(entity.image, entity.rect)
      entity.move()
   
   # collision with coins or collectin coins
   coin_show = font_coin.render(f'$:{str(coin_cnt)}', True, black)
   screen.blit(coin_show,(WIDTH-38,50))

   if pygame.sprite.spritecollideany(p1,coins):
      c1.disappear()
      pygame.mixer.Sound(os.path.join('music','collect.wav')).play()
      coin_cnt += 1

   # collison with enemies
   if pygame.sprite.spritecollideany(p1,enemies):
   # losing the game
    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return

        go = pg.image.load("ranadan.png")
        self.screen.blit(go,(0,0))
     

      pygame.mixer.music.stop()
      pygame.mixer.Sound(os.path.join('music','crash.wav')).play()

      # 1
      screen.blit(game_over,(35,250))

      # 2
      font = pygame.font.SysFont('Calibri',30)
      total = font.render(f'Total score: {str(score)}',True, black)
      screen.blit(total,(100,350))

      # 3
      font = pygame.font.SysFont('Calibri',30)
      total = font.render(f'Total money: {str(coin_cnt)}',True,black)
      screen.blit(total,(100,400))

      pygame.display.update()

      for entity in all_sprites:
         entity.kill()
      sleep(2)
      pygame.quit()
      sys.exit()

   pygame.display.update()