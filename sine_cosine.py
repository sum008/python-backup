import math
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1080, 480))

dot1=pygame.Surface((5,5))
dot1.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

dot2=pygame.Surface((5,5))
dot2.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

dot3=pygame.Surface((5,5))
dot3.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

dot4=pygame.Surface((5,5))
dot4.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

FPSCLOCK = pygame.time.Clock()
count=0.0174
screen.fill((0,0,0))

done =False
while not done:
#     screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
#     pygame.draw.circle(screen, (255,255,255), (100,100), 50, 2)
#     screen.blit(dot,(100,100))
    x1=(50*count)%1080
    y1=math.cos(count)*70+100
    print(math.cos(count)*70)
    screen.blit(dot1,(x1,y1))
    
    x2=(50*count)%1080
    y2=math.sin(count)*70+100
    print(math.cos(count)*70)
    screen.blit(dot2,(x2,y2))
    
    x3=(50*count)%1080
    y3=math.tan(count)*70+100
    print(math.tan(count)*70)
    screen.blit(dot3,(x3,y3))
    
    count=(count+0.01)
    pygame.display.flip()
    FPSCLOCK.tick(120)