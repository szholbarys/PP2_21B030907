import pygame

pygame.init()


size = weight , height = (610, 710)
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Red Ball")


x = y = 0
speed = 20
do = False
clock = pygame.time.Clock()


while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
           
                 
    press = pygame.key.get_pressed()
    if press[pygame.K_UP]:
        if y >= 20:
                y += (-1 * speed)
    if press[pygame.K_DOWN]:
        if y <= height - 60:
                y += speed
    if press[pygame.K_LEFT]:
        if x >= 20:
                x += (-1 * speed)
    if press[pygame.K_RIGHT]:
        if x <= weight - 60:
                x += speed 
          
                
    screen.fill((255, 255, 255))
    clock.tick(30)
    pygame.draw.ellipse(screen, ((255, 0, 0)), (x, y, 50, 50))
    pygame.display.flip()
     
pygame.quit()