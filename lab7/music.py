import pygame 
import random
pygame.init()

l = [
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes - Wonder.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes - It Will Be Okay.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes & Justin Bieber - Monster.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes, Tainy - Summer Of Love.mp3'
    ]

colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255), (200, 0, 100), (70, 70, 70), (0, 0, 255)]
im = pygame.image.load(r"shawn.jpg")
screen = pygame.display.set_mode((850, 450))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

do = False
val = 0.05
print(l[0])
pos = 0
pygame.mixer.music.load(l[pos])
pygame.mixer.music.play()
pygame.mixer.music.queue(l[random.randrange(0, 5)])
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if pos <= 4:
                pos+=1
            else:
                pos = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if pos >= 1:
                pos-=1
            else:
                pos = 5
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            val+=0.05
            pygame.mixer.music.set_volume(val)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            val-=0.05
            pygame.mixer.music.set_volume(val)
  
    screen.blit(im, (0, 0))

    clock.tick(10)
    
    pygame.display.flip()
pygame.quit()
