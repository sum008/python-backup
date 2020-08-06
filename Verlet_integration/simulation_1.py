'''
Created on May 1, 2020

@author: Sumit
'''
import pygame as p
import ball
from random import randint
import math
import time
p.init()

width=600
height=600
display=p.display.set_mode((width,height))
r=15
n=50
wind=2
ball_lis=[]
for i in range(0,n):
    x=randint(r,width-r)
    y=randint(r,height-r)
    ox=x-randint(1,10)
    oy=y-randint(1,10)
    g=randint(1,5)/10
    f=0.998
#     print(x,y,ox,oy)
    ball1=ball.ball()
    ball1.create(x,y,ox,oy,1,g,f,wind)
    ball_lis.append(ball1)

def distance(x1,x2,y1,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    return math.sqrt(x**2+y**2)

prev=int(time.clock())
count=0

run=True
while run:
    
    count+=1
    cl=int(time.clock())
    
    if prev!=cl:
        print("FPS : "+ str(count//abs(prev-cl)))
        count=0
        prev=int(time.clock())
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    for ball in ball_lis:
        x=ball.get_x()
        y=ball.get_y()
        ox=ball.get_ox()
        oy=ball.get_oy()
        
        vx=x-ox
        vy=y-oy 
        
#         print(x,y,ox,oy,vx,vy)
        ball.set_ox(x)
        ball.set_oy(y)
    
        x+=vx
        y+=vy
        
        ball.set_x(x)
        ball.set_y(y)
        
        if x+r>=width:
            x=width-r
            ball.set_x(x)
#             ox=x+vx
            ball.set_ox(x+vx)
        elif x-r<=0:
            x=r
            ball.set_x(x)
#             ox=x+vx
            ball.set_ox(x+vx)
        elif y+r>=height:
            y=height-r
            ball.set_y(y)
#             oy=y+vy
            ball.set_oy(y+vy)
        elif y-r<=0:
            y=r
            ball.set_y(y)
#             oy=y+vy
            ball.set_oy(y+vy) 
        ball.apply_g() 
        ball.apply_friction()   
        
#         ball.remove_friction()

#         for ball1 in ball_lis:
#             if not ball1==ball:
#                 x1=ball1.get_x()
#                 y1=ball1.get_y()
#                  
#                 d=distance(x, x1, y, y1)
# #                 print(d)
#                 if d<=5:
# #                     print("Sd")
#                     ox1=ball1.get_ox()
#                     oy1=ball1.get_oy()
#                     ox=ball.get_ox()
#                     oy=ball.get_oy()
#                      
#                     ball1.set_x(x)
#                     ball1.set_y(y)
#                     ball1.set_ox(ox)
#                     ball1.set_oy(oy)
#                      
#                     ball.set_x(x1)
#                     ball.set_y(y1)
#                     ball.set_ox(ox1)
#                     ball.set_oy(oy1)
        p.draw.circle(display, (0,0,0), (int(ball.get_x()),int(ball.get_y())), r, 1)
                 
    p.display.flip()
        
    p.time.Clock().tick(60)