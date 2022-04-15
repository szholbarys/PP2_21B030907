from random import randint
import pygame, sys
from time import sleep
import os

pygame.init()

# main parameters
WIDTH, HEIGHT = 700,700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake Game')
run = True
mode = True

# colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
green = (0,255,0)

# velocity oh the snake
clock = pygame.time.Clock()
FPS = 10

# movement of the snake
radius = 10
block = 5
dx, dy = block, 0
body = [[radius+20,radius+80+200],[0,0],[0,0],[0,0],[0,0]]

border_width = 20

# the end of the game
game_over = pygame.transform.scale(pygame.image.load(os.path.join(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab8\image\game_over.jpg')),(WIDTH,HEIGHT))

score = pygame.transform.scale(pygame.image.load(os.path.join(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab8\image\score.png')),(200,100))
cnt_score = 0

level = pygame.transform.scale(pygame.image.load(os.path.join(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab8\image\level.gif')),(200,120))
cnt_level = 1

# pattern for counting score and level
pattern_width, pattern_height = WIDTH, 200

# functions for food
def own_round(value,base=5):
   return base * round(value/5)

def set_random_food():
   return own_round(randint(20+radius,WIDTH-20-radius)), own_round(randint(20+radius+pattern_height,HEIGHT-20-radius))

food_x, food_y = set_random_food()

while run:
   clock.tick(FPS)
   
   if mode == True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               dx = block
               dy = 0
            if event.key == pygame.K_LEFT:
               dx = -block
               dy = 0
            if event.key == pygame.K_DOWN:
               dy = block
               dx = 0
            if event.key == pygame.K_UP:
               dy = -block
               dx = 0

   # snake movement
   for i in range(len(body)-1,0,-1):
      body[i][0] = body[i-1][0]
      body[i][1] = body[i-1][1]

   body[0][0] += dx
   body[0][1] += dy

   screen.fill(white)

   # food
   pygame.draw.rect(screen,green,(food_x,food_y,15,15))

   # eating the food
   if abs(food_x - body[0][0]) <= radius and abs(food_y - body[0][1]) <= radius:
      food_x, food_y = set_random_food()
      body.append([body[0][0],body[0][1]])
      FPS += 1 # increase the speed
      cnt_score += 1 # increase the score
      if cnt_score % 7 == 0:
         cnt_level += 1
      if cnt_level >= 5:
         FPS -= 0.5

   # border
   pygame.draw.rect(screen,black,(0,0,20,HEIGHT))
   pygame.draw.rect(screen,black,(0,150,WIDTH,20))
   pygame.draw.rect(screen,black,(0,HEIGHT-20,WIDTH,20))
   pygame.draw.rect(screen,black,(WIDTH-20,0,20,HEIGHT))
   
   for i,(x,y) in enumerate(body):
      pygame.draw.circle(screen,red,(x,y),radius)

   # check and show results after losing
   if body[0][0] > WIDTH-20-radius or body[0][0]<20+radius or body[0][1]>HEIGHT-20-radius or body[0][1]<20+radius+150:
      mode = False
      dx,dy = 0,0
      screen.blit(game_over,(0,0))

   # score image, counting the score, showing the score 
   screen.blit(score,(20,20))
   font = pygame.font.SysFont('Comic Sans MS', 50)
   text = font.render(str(cnt_score), False, black)
   screen.blit(text,(200+50,30))

   # level image, couting the level, showing the score
   screen.blit(level,(350,15))
   font = pygame.font.SysFont('Comic Sans MS',50)
   text = font.render(str(cnt_level), False, red)
   screen.blit(text,(350+200,30))

   pygame.display.update()

pygame.quit()