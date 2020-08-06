import math
import pygame
import random
pygame.init()
print(random.random()/(random.randint(1,10)))
screen = pygame.display.set_mode((1080, 480))

dot1=pygame.Surface((1,1))
dot1.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))


FPSCLOCK = pygame.time.Clock()
count=0
screen.fill((0,0,0))
xr=0.1
yr=0.1


xangle=0.1
yangle=0.1

xangle1=-0.1
yangle1=-0.1

a=500
b=250

done =False
while not done:
#     screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    x1=math.cos(yangle)*xr+500
    y1=math.sin(yangle)*yr+200
    
    
    print(x1,y1)
    screen.blit(dot1,(x1,y1))
    
    x1=math.cos(yangle1)*xr+500
    y1=math.sin(yangle1)*yr+200
    
    screen.blit(dot1,(x1,y1))
    
    xr+=0.1
    yr+=0.1
#     screen.blit(dot1,(500,250))
    
    xangle=(xangle+0.1)
    yangle=(yangle+0.1)
    
    xangle1=(xangle1-0.1)
    yangle1=(yangle1-0.1)
    
    pygame.display.flip()
    FPSCLOCK.tick(120)