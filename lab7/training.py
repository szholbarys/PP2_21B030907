import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()