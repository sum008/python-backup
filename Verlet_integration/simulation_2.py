'''
Created on Jun 13, 2020

@author: Sumit
'''
import pygame as p
import ball
from random import randint
import math

p.init()

width=600
height=600
display=p.display.set_mode((width,height))
r=2
n=50
length=5
fps=120
x=300
y=10
g=1
f=1
wind=2
ball_lis=[]
for i in range(0,n):
    ox=0
    oy=0
    mass=2
    ball1=ball.ball()
    ball1.create(x,y,ox,oy,mass,g,f,wind)
    ball_lis.append(ball1)
    y+=length
    
def distance(x1,x2,y1,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    return math.sqrt(x**2+y**2)

def draw_ball(ball_lis):
    
    for i in range(0,len(ball_lis)-1):
     
        p.draw.circle(display, (0,0,0), (int(ball_lis[i].get_x()),int(ball_lis[i].get_y())), r, 1)
        p.draw.line(display, (0,0,0), (int(ball_lis[i].get_x()),int(ball_lis[i].get_y())), (int(ball_lis[i+1].get_x()),int(ball_lis[i+1].get_y())), 1)
    
    p.draw.circle(display, (0,0,0), (int(ball_lis[len(ball_lis)-1].get_x()),int(ball_lis[len(ball_lis)-1].get_y())), r, 1) 
    
count=0
    
def reposition(ball_lis):
    for i in range(0,len(ball_lis)-1):
    
        dx=ball_lis[i].get_x()-ball_lis[i+1].get_x()
        dy=ball_lis[i].get_y()-ball_lis[i+1].get_y()
        
        d=distance(ball_lis[i+1].get_x(),ball_lis[i].get_x(),ball_lis[i+1].get_y(),ball_lis[i].get_y())
        diff=length-d
        percent_change=diff/d/2
#         print(percent_change,d,diff)
        offsetx=dx*percent_change
        offsety=dy*percent_change
        
        if i>-1:
            ball_lis[i].set_ox(ball_lis[i].get_x())
            ball_lis[i].set_oy(ball_lis[i].get_y())
             
            ball_lis[i].set_x(ball_lis[i].get_x()+offsetx)
            ball_lis[i].set_y(ball_lis[i].get_y()+offsety)
        
        ball_lis[i+1].set_ox(ball_lis[i+1].get_x())
        ball_lis[i+1].set_oy(ball_lis[i+1].get_y())
        
        ball_lis[i+1].set_x(ball_lis[i+1].get_x()-offsetx)
        ball_lis[i+1].set_y(ball_lis[i+1].get_y()-offsety)
        
        

run=True
while run:
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    mouse_press=p.mouse.get_pressed()
    if mouse_press[0]==1:
        pos=p.mouse.get_pos()
        d=1000
        index=len(ball_lis)-1
#         for i in range(0,len(ball_lis)):
#             if distance(pos[0],ball_lis[i].get_x(),pos[1],ball_lis[i].get_y())<d:
#                 d=distance(pos[0],ball_lis[i].get_x(),pos[1],ball_lis[i].get_y())
#                 index=i
        ball_lis[index].set_ox(ball_lis[index].get_x())
        ball_lis[index].set_oy(ball_lis[index].get_y())
        
        ball_lis[index].set_x(pos[0])
        ball_lis[index].set_y(pos[1])
    
        
    reposition(ball_lis) 
    reposition(ball_lis) 
#     reposition(ball_lis) 
#     reposition(ball_lis) 
#     reposition(ball_lis) 
#     reposition(ball_lis) 
    
    for i in range(0,len(ball_lis)):
        
        vx=ball_lis[i].get_x()-ball_lis[i].get_ox()
        vy=ball_lis[i].get_y()-ball_lis[i].get_oy()
        
        ball_lis[i].set_ox(ball_lis[i].get_x())
        ball_lis[i].set_oy(ball_lis[i].get_y())
        
        ball_lis[i].set_x(ball_lis[i].get_x()+vx)
        ball_lis[i].set_y(ball_lis[i].get_y()+vy)
    
#         ball_lis[i].apply_g()
#         ball_lis[i].apply_wind()

    
    
    draw_ball(ball_lis)            
    p.display.flip()
        
    p.time.Clock().tick(fps)