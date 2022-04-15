import pygame, sys, os
from time import sleep
from random import randint
from pygame.math import Vector2
from datetime import datetime, timedelta

pygame.init()

# main parameters
grid_size = 40
grid_number = 20
WIDTH, HEIGHT = grid_size*grid_number, grid_size*grid_number
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake Game')
run = True
score = 0
font = pygame.font.SysFont('Cooper Black',grid_size)
game_over_img = pygame.image.load(os.path.join('images','game over.png'))
timer = 0

# necessary colors
bg_color = (175,215,70)
grass_color = (167,209,61)
snake_color = (255,0,0)

# velocity of the snake
clock = pygame.time.Clock()
FPS = 10

# types of food
foods = [
         pygame.transform.scale(pygame.image.load(os.path.join('images','burger.png')),(40,40)),
         pygame.transform.scale(pygame.image.load(os.path.\
            join('images','apple.png')),(40,40)),
         pygame.transform.scale(pygame.image.load(os.path.join('images','rabbit.png')),(40,40)),
         pygame.transform.scale(pygame.image.load(os.path.join('images','cola.png')),(40,40))
         ]

# main function
def draw_grass():
   for i in range(grid_number):
      if i % 2 == 0:
         for j in range(grid_number):
            if j % 2 == 0:
               pygame.draw.rect(screen,grass_color,(i*grid_size,j*grid_size,grid_size,grid_size))
      else:
         for j in range(grid_number):
            if j % 2 != 0:
               pygame.draw.rect(screen,grass_color,(i*grid_size,j*grid_size,grid_size,grid_size))

def show_score(font):
   txt = font.render(f'{score}',True,(0,0,0))
   screen.blit(txt,(WIDTH-40,HEIGHT-40))


# all info about Food
class Food:
   def _init_(self):
      i = randint(0,3)
      self.image = foods[i]
      self.cost = i + 1
      self.set_random_pos()

   def set_random_pos(self):
      self.x = randint(0,grid_number-1)
      self.y = randint(0,grid_number-1)
      self.pos = Vector2(self.x, self.y)
      i = randint(0,3)
      self.image = foods[i]
      self.cost = i + 1

   def draw(self):
      food_rect = pygame.Rect(self.pos.x*grid_size, self.pos.y*grid_size, grid_size, grid_size)
      screen.blit(self.image, food_rect)

# all info about snake
class Snake:
   def _init_(self):
      self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
      self.dx = 1
      self.dy = 0
      self.right, self.left, self.up, self.down = True, False, False, False
   
   def draw(self):
      for cell in self.body:
         pygame.draw.rect(screen,snake_color,(cell.x*grid_size, cell.y*grid_size, grid_size, grid_size))
   
   def move(self):
      global timer
      for i in range(len(self.body)-1,0,-1):
         self.body[i].x = self.body[i-1].x
         self.body[i].y =  self.body[i-1].y

      self.body[0].x += self.dx
      self.body[0].y += self.dy
      timer += 1
      if timer == 30:
         food.set_random_pos()
         timer = 0
      

   def check_fail(self):
      if self.body[0].x < 0 or self.body[0].x > grid_number-1 or self.body[0].y < 0 or self.body[0].y > grid_number-1:
         # 1 case
         self.game_over()
      # 2 case
      for block in self.body[1:]:
         if block == self.body[0]:
            self.game_over()
   
   def game_over(self):
      sleep(1)
      screen.blit(game_over_img,(WIDTH/2-game_over_img.get_width(), HEIGHT-game_over_img.get_height()))
      pygame.quit()
      sys.exit()
      

food = Food()
snake = Snake()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

while run:
   clock.tick(FPS)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
         sys.exit()
      if event.type == screen_update:
         snake.move()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            if snake.dx != -1:
               snake.dx = 1
               snake.dy = 0
         if event.key == pygame.K_LEFT:
            if snake.dx != 1:
               snake.dx = -1
               snake.dy = 0
         if event.key == pygame.K_DOWN:
            if snake.dy != -1:
               snake.dx = 0
               snake.dy = 1
         if event.key == pygame.K_UP:
            if snake.dy != 1:
               snake.dx = 0
               snake.dy = -1

   # main patterns of the game
   screen.fill(bg_color)
   draw_grass()
   show_score(font)

   # drawing the food randomly
   food.draw()

   # drawing the snake body
   snake.draw()

   # check wether the snake-head collides with border or eats itself
   snake.check_fail()

   # check the collision == > eating the food
   if snake.body[0] == food.pos:
      # Randomly generating food with different weights
      score += food.cost

      # Foods which are disappearing after some time(timer)
      timer = 0

      snake.body.append(Vector2(snake.body[len(snake.body)-1].x, snake.body[len(snake.body)-1].y))
      food.set_random_pos()

      # sound of eating food
      pygame.mixer.Sound(os.path.join('music','snake_eat.wav')).play()

      # check again whether the food is appearing on the snake's body
      for block in snake.body[1:]:
         while block == food.pos:
            food.set_random_pos()
   
   pygame.display.update()

pygame.quit()