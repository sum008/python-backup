'''
Created on Jun 14, 2020

@author: Sumit
'''
import pygame as p
import ball
from random import randint
import math
import time
from datetime import datetime as dt
p.init()

width=600
height=600
display=p.display.set_mode((width,height))
r=2
n=30
length=10
fps=120
x=100
y=10
g=0.3
f=1
wind=0.1
mass=1.5
ball_lis=[]
for i in range(0,n):
    b=[]
    x=200
    for j in range(0,n):
        ball1=ball.ball()
        ball1.create(x,y,x,y,mass,g,f,wind)
        b.append(ball1)
        x+=length
    ball_lis.append(b)
    y+=length
    
    
def distance(dx,dy):
    return math.sqrt(dx**2+dy**2)

def draw_ball(ball_lis):
    
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
            p.draw.circle(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), r, 1)
            
            if j<len(ball_lis)-1:
                p.draw.line(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), (int(ball_lis[i][j+1].get_x()),int(ball_lis[i][j+1].get_y())), 1)
            
            if i<len(ball_lis)-1:
                p.draw.line(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), (int(ball_lis[i+1][j].get_x()),int(ball_lis[i+1][j].get_y())), 1)
    
def reposition(ball_lis):
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
            
            ball1=ball_lis[i][j]
            
            if j<len(ball_lis)-1:
                
                ball2=ball_lis[i][j+1]
                
                dx=ball1.get_x()-ball2.get_x()
                dy=ball1.get_y()-ball2.get_y()
                
                d=distance(dx,dy)
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball2.set_x(ball2.get_x()-offsetx)
                ball2.set_y(ball2.get_y()-offsety)
                
                ball1.set_x(ball1.get_x()+offsetx)
                ball1.set_y(ball1.get_y()+offsety)
                
                
            if j>0:
                
                ball2=ball_lis[i][j-1]
                
                dx=ball1.get_x()-ball2.get_x()
                dy=ball1.get_y()-ball2.get_y()
                
                d=distance(dx,dy)
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball2.set_x(ball2.get_x()-offsetx)
                ball2.set_y(ball2.get_y()-offsety)
                
                ball1.set_x(ball1.get_x()+offsetx)
                ball1.set_y(ball1.get_y()+offsety)
                
            if i>0:
                ball2=ball_lis[i-1][j]
                
                dx=ball1.get_x()-ball2.get_x()
                dy=ball1.get_y()-ball2.get_y()
                
                d=distance(dx,dy)
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball2.set_x(ball2.get_x()-offsetx)
                ball2.set_y(ball2.get_y()-offsety)
                
                ball1.set_x(ball1.get_x()+offsetx)
                ball1.set_y(ball1.get_y()+offsety)
                
            if i<len(ball_lis)-1:
                ball2=ball_lis[i+1][j]
                
                dx=ball1.get_x()-ball2.get_x()
                dy=ball1.get_y()-ball2.get_y()
                
                d=distance(dx,dy)
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball2.set_x(ball2.get_x()-offsetx)
                ball2.set_y(ball2.get_y()-offsety)
                
                ball1.set_x(ball1.get_x()+offsetx)
                ball1.set_y(ball1.get_y()+offsety)
                

run=True
mouse_button_is_pressed=False
prev=int(time.clock())
count=0
c=0
a=0
b=0
pos=[]
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
    
    mouse_press=p.mouse.get_pressed()
#     print(mouse_press[0])
    
    if mouse_press[0]==0:
        mouse_button_is_pressed=False
        c=0
        
    if mouse_press[0]==1 and mouse_button_is_pressed==False:
        mouse_button_is_pressed=True
        pos=p.mouse.get_pos()
        d=1000
        c=1
        for i in range(0,len(ball_lis)):
            for j in range(0,len(ball_lis)):
                if distance(pos[0]-ball_lis[i][j].get_x(),pos[1]-ball_lis[i][j].get_y())<d:
                    d=distance(pos[0]-ball_lis[i][j].get_x(),pos[1]-ball_lis[i][j].get_y())
                    a=i
                    b=j
                     
#         ball_lis[a][b].set_ox(ball_lis[a][b].get_x())
#         ball_lis[a][b].set_oy(ball_lis[a][b].get_y())
#         print(a,b)
    if mouse_button_is_pressed==True:
        pos=p.mouse.get_pos()
        ball_lis[a][b].set_x(pos[0])
        ball_lis[a][b].set_y(pos[1])
    
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
            
            if i!=a and j!=b:
                vx=ball_lis[i][j].get_x()-ball_lis[i][j].get_ox()
                vy=ball_lis[i][j].get_y()-ball_lis[i][j].get_oy()
                
                ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
                ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
                
                ball_lis[i][j].set_x(ball_lis[i][j].get_x()+vx)
                ball_lis[i][j].set_y(ball_lis[i][j].get_y()+vy)
    #             ball_lis[i][j].apply_g()
                ball_lis[i][j].apply_wind()

    for i in range(3):
        reposition(ball_lis) 
    
    draw_ball(ball_lis)            
    p.display.flip()
        
    p.time.Clock().tick(fps)