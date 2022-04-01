import pygame 
import random
from pygame import mixer

mixer.init()
pygame.init()

shawn = pygame.image.load(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\shawn.jpg')
shawns_songs = [
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes - Wonder.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes - It Will Be Okay.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes & Justin Bieber - Monster.mp3',
    r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\Shawn Mendes, Tainy - Summer Of Love.mp3'
]

screen = pygame.display.set_mode((1200, 800))
done = False

loc = 0
volume = 0.1

pygame.mixer.music.load(shawns_songs[loc])
pygame.mixer.music.play()
pygame.mixer.music.queue(shawns_songs[random.randrange(0, 7)])

while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.KEYDOWN:
          if i.key == pygame.K_SPACE:
               pygame.mixer.music.pause()
            if i.key == pygame.K_RSHIFT:
               pygame.mixer.music.unpause()
            if i.key == pygame.K_LEFT:
                if loc >= 1:
                   loc -= 1:
                else:
                   loc = 6
                pygame.mixer.music.stop()
                pygame.mixer.music.load(shawna_songs[loc])
                pygame.mixer.music.play()
            if i.key == pygame.K_RIGHT:
                if loc <= 6:
                   loc += 1
                else:
                   loc = 0    
                pygame.mixer.music.stop()
                pygame.mixer.music.load(shawna_songs[loc])
                pygame.mixer.music.play()
            if i.key == pygame.K_DOWN:
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)
            screen.blit(shawn, (0, 0))
            pygame.display.flip()

        pygame.mixer.music.queue(shawns_songs[random.randrange(0, 7)])
        pygame.quit()    