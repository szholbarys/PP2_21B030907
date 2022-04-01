import pygame
import datetime
pygame.init()

clock = pygame.time.Clock()
screen=pygame.display.set_mode((780,795))

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)

working=True

hold = datetime.datetime.now()
now_minute=int(hold.strftime("%M"))
now_sec=int(hold.strftime("%S"))

sec_angle,angle=0,0

sec_hand=pygame.image.load(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\lefthand1.png')
image=pygame.image.load(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\back.png')
hand=pygame.image.load(r'C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab7\righthand1.png')


sec_hand=pygame.transform.scale(sec_hand,(400,250))
hand=pygame.transform.scale(hand,(450,300))
print(sec_hand.get_width(), sec_hand.get_height())
print(hand.get_width(), sec_hand.get_height())
print(image.get_width(), sec_hand.get_height())
w,h=hand.get_size()
k,l=sec_hand.get_size()
angle-=((5*now_sec*1.2)-54)
sec_angle-=((1.2*5*now_minute)+61)
count_min=1
print(now_minute,now_sec)
pos = ((screen.get_width()/2), (screen.get_height()/2)-5)
black=(0,0,0)
while working:
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            working =False
    screen.fill(0)
    screen.blit(image,(0,0))
    blitRotate(screen, hand, pos, (w/2, h/2), angle)
    blitRotate(screen, sec_hand, pos, (k/2, l/2), sec_angle)
    pygame.draw.circle(screen,black,((screen.get_width()/2), (screen.get_height()/2)),16)
    angle-=1.2
    sec_angle-=0.02
    pygame.display.flip()
    clock.tick(5)