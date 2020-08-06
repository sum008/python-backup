import pygame
from random import randint
import math

pygame.init()
displayGame = pygame.display.set_mode((400, 400))
displayGame.fill((25, 200, 150)) 
pygame.display.set_caption("mhh")
clock = pygame.time.Clock()
crashed=True
x=1
y=50
width=25
height=25
velocity=0.05
food_x=0
food_y=0
food_width=25
food_height=25
food=False
while crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed=False
#     while count<=200:
#         pygame.draw.circle(displayGame, (0,0,255), (200,200), count)
#         pygame.display.update() 
#         time.sleep(0.01)
#         count+=1
#     while count>1:
#         pygame.draw.circle(displayGame, (50,100,255), (200,200), count, 1)
#         pygame.display.update() 
#         time.sleep(0.01)
#         count-=1
    if food==False:
        print("dfdsfsdfsd")
        food_x=randint(10,300)
        food_y=randint(10,300)
#         while food_x==x or food_y==y:
#             food_x=randint(10,300)
#             food_y=randint(10,300)
        pygame.display.update()
        food=True
         
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=velocity
    elif keys[pygame.K_RIGHT]:
        x+=velocity
    elif keys[pygame.K_UP]:
        y-=velocity
    elif keys[pygame.K_DOWN]:
        y+=velocity
    displayGame.fill((25, 200, 150)) 
    pygame.draw.rect(displayGame, (10,50,200), (food_x,food_y,food_width,food_height))
    pygame.draw.rect(displayGame, (0,0,255), (math.floor(x)%400,math.floor(y)%400,width,height))
    pygame.display.update()
    
    if math.floor(x)==food_x and math.floor(y)==food_y:
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        width+=food_width
        food=False
    print(math.floor(x),math.floor(y),food_x,food_y)
#     if x<=0 or x>=375:
#         crashed=False
    
            


        
    