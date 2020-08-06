'''
Created on Jun 14, 2020

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
r=2
n=100
length=2
fps=120
x=300
y=10
g=0.2
mass=1
f=1
wind=2
ball_lis=[]

    
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
        if d!=0:
            diff=length-d
            percent_change=diff/d/2
    #         print(percent_change,d,diff)
            offsetx=dx*percent_change
            offsety=dy*percent_change
            if i!=0:
                ball_lis[i].set_x(ball_lis[i].get_x()+offsetx)
                ball_lis[i].set_y(ball_lis[i].get_y()+offsety)
            if (i+1)!=len(ball_lis)-1:
                ball_lis[i+1].set_x(ball_lis[i+1].get_x()-offsetx)
                ball_lis[i+1].set_y(ball_lis[i+1].get_y()-offsety)
        
 
 
prev=int(time.clock())
count=0
       
posy=0
run=True
pressed=False
while run:
    
    count+=1
    cl=int(time.clock())
    
    if prev!=cl:
        print(count//abs(prev-cl))
        count=0
        prev=int(time.clock())
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    mouse_press=p.mouse.get_pressed()
    
    if pressed==False:
        click=p.mouse.get_pressed()
        if click[0]==1:
            posy=p.mouse.get_pos()[1]
            ball1=ball.ball()
            ball1.create(100,posy,100,posy,mass,g,f,wind)
            ball_lis.append(ball1)
            
            for i in range(1,n-1):
                ball1=ball.ball()
                ball1.create(x,y,x,y,mass,g,f,wind)
                ball_lis.append(ball1)
                x+=length
            ball1=ball.ball()
            ball1.create(550,posy,550,posy,mass,g,f,wind)
            ball_lis.append(ball1)
            pressed=True
            
    if pressed==True:
        
        draw_ball(ball_lis) 
        
#         click=p.mouse.get_pressed()
#         if click[0]==1:
#         pos=p.mouse.get_pos()
        ball_lis[0].set_x(100)
        ball_lis[0].set_y(posy)
#         
        ball_lis[n-1].set_x(550)
        ball_lis[n-1].set_y(posy)
        
        mouse_press=p.mouse.get_pressed()
        if mouse_press[0]==1:
            pos=p.mouse.get_pos()
            d=1000
            index=0
            for i in range(1,len(ball_lis)-1):
                if distance(pos[0],ball_lis[i].get_x(),pos[1],ball_lis[i].get_y())<d:
                    d=distance(pos[0],ball_lis[i].get_x(),pos[1],ball_lis[i].get_y())
                    index=i
#             ball_lis[index].set_ox(ball_lis[index].get_x())
#             ball_lis[index].set_oy(ball_lis[index].get_y())
            
            ball_lis[index].set_x(pos[0])
            ball_lis[index].set_y(pos[1])
        
        for i in range(1,len(ball_lis)-2):
            
            vx=ball_lis[i].get_x()-ball_lis[i].get_ox()
            vy=ball_lis[i].get_y()-ball_lis[i].get_oy()
            
            ball_lis[i].set_ox(ball_lis[i].get_x())
            ball_lis[i].set_oy(ball_lis[i].get_y())
            
            ball_lis[i].set_x(ball_lis[i].get_x()+vx)
            ball_lis[i].set_y(ball_lis[i].get_y()+vy)
        
            ball_lis[i].apply_g()
    #         ball_lis[i].apply_wind()
        for count in range(55):
            reposition(ball_lis) 
                   
    p.display.flip()
        
    p.time.Clock().tick(fps)