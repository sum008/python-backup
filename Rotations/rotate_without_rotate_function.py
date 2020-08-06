# import sys
# import pygame
# pygame.init()
# 
# screen = pygame.display.set_mode((640, 480))
# FPSCLOCK = pygame.time.Clock()
# RED = pygame.Color("red")
# startpoint = pygame.math.Vector2(320, 240)
# endpoint = pygame.math.Vector2(170, 0)
# angle = 0
# done = False
# 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
# 
#     import sys
import math
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

dot=pygame.Surface((5,5))
dot.fill((25,154,26))
FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
angle = 0
done = False
cx=250
cy=250
x=cx+100
y=cy+100
while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    t=pygame.draw.line(screen, RED, (cx,cy), (x,y), 2)
    pygame.draw.rect(screen, (120,88,19), t, 1)
    print(t,cx,cy)
    
    keys=pygame.key.get_pressed()
             
    if keys[pygame.K_LEFT]:
        
        angle=1
        xold=x
        x=cx+math.cos(angle*(0.01745))*(xold-cx)-math.sin(angle*(0.01745))*(y-cy)
        y=cy+math.sin(angle*(0.01745))*(xold-cx)+math.cos(angle*(0.01745))*(y-cy)
    elif keys[pygame.K_RIGHT]:
        angle=-1
        xold=x
        x=cx+math.cos(angle*(0.01745))*(xold-cx)-math.sin(angle*(0.01745))*(y-cy)
        y=cy+math.sin(angle*(0.01745))*(xold-cx)+math.cos(angle*(0.01745))*(y-cy)
    
    
#     xold=x
#     x=cx+math.cos(angle*(0.01745))*(xold-cx)-math.sin(angle*(0.01745))*(y-cy)
#     y=cy+math.sin(angle*(0.01745))*(xold-cx)+math.cos(angle*(0.01745))*(y-cy)

#     print(x,y)
#     angle=(angle+1)
    pygame.display.flip()
    FPSCLOCK.tick(120)
    
