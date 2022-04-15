import pygame
import random
import time

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color = GREEN

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game by Zholbarys')
clock = pygame.time.Clock()

body = [[100,100], [0,0], [0,0]]
block = 15
dy, dx = block , 0

def own_round(value, base = 15):
    return base * round(value / 15)

def set_random_position():
    return own_round(random.randint(0, 500)), own_round(random.randint(0, 500))

foodx, foody = set_random_position()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = block
                dy = 0
            if event.key == pygame.K_LEFT:
                dx = -block
                dy = 0
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = block
            if event.key == pygame.K_UP:
                dx = 0
                dy = -block    
            if event.key == pygame.K_SPACE:
                body.append([0, 0])
                foodx, foody = set_random_position()

# movement of the snake
for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0]
    body[i][1] = body[i - 1][1]

# changes snake's head position
body[0][0] += dx
body[0][1] += dy

if body[0][0] > 500:
    body[0][0] = 0

screen.fill(BLACK)


# # draw food
# pygame.draw.rect(screen, BLUE, (foodx, foody, 15, 10))

# # draw snake
# for i, (x, y) in enumerate(body):
#     if i == 0:
#         color = RED
#     else:
#         color = GREEN
#     pygame.draw.rect(screen , color, (x , y, 15, 10))

  # Draw food
  pygame.draw.circle(screen, BLUE, (foodx, foody), 15)

  # Draw snake
  for i, (x, y) in enumerate(body):
    color = RED if i == 0 else GREEN
    pygame.draw.circle(screen, color, (x, y), 15)

pygame.display.flip() 

clock.tick(5)