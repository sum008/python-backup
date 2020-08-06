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
n=20
length=10
fps=120
x=100
y=10
g=2
f=1
wind=2
mass=1.5
ball_lis=[]
for i in range(0,n):
    b=[]
    x=200
    for j in range(0,n):
        ox=0
        oy=0
        ball1=ball.ball()
        ball1.create(x,y,ox,oy,mass,g,f,wind)
        b.append(ball1)
        x+=length
    ball_lis.append(b)
    y+=length
    
    
def distance(x1,x2,y1,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    return math.sqrt(x**2+y**2)

def draw_ball(ball_lis):
    
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
#             p.draw.circle(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), r, 1)
            
            if j<len(ball_lis)-1:
                p.draw.line(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), (int(ball_lis[i][j+1].get_x()),int(ball_lis[i][j+1].get_y())), 1)
            
            if i<len(ball_lis)-1:
                p.draw.line(display, (0,0,0), (int(ball_lis[i][j].get_x()),int(ball_lis[i][j].get_y())), (int(ball_lis[i+1][j].get_x()),int(ball_lis[i+1][j].get_y())), 1)
    
#     p.draw.circle(display, (0,0,0), (int(ball_lis[len(ball_lis)-1].get_x()),int(ball_lis[len(ball_lis)-1].get_y())), r, 1) 

    
def reposition(ball_lis):
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
            
            if j<len(ball_lis)-1:
                dx=ball_lis[i][j].get_x()-ball_lis[i][j+1].get_x()
                dy=ball_lis[i][j].get_y()-ball_lis[i][j+1].get_y()
                
                d=distance(ball_lis[i][j+1].get_x(),ball_lis[i][j].get_x(),ball_lis[i][j+1].get_y(),ball_lis[i][j].get_y())
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
                ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
                
                ball_lis[i][j+1].set_ox(ball_lis[i][j+1].get_x())
                ball_lis[i][j+1].set_oy(ball_lis[i][j+1].get_y())
                
                ball_lis[i][j+1].set_x(ball_lis[i][j+1].get_x()-offsetx)
                ball_lis[i][j+1].set_y(ball_lis[i][j+1].get_y()-offsety)
                
                ball_lis[i][j].set_x(ball_lis[i][j].get_x()+offsetx)
                ball_lis[i][j].set_y(ball_lis[i][j].get_y()+offsety)
                
                
            if j>0:
                dx=ball_lis[i][j].get_x()-ball_lis[i][j-1].get_x()
                dy=ball_lis[i][j].get_y()-ball_lis[i][j-1].get_y()
                
                d=distance(ball_lis[i][j-1].get_x(),ball_lis[i][j].get_x(),ball_lis[i][j-1].get_y(),ball_lis[i][j].get_y())
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
                ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
                
                ball_lis[i][j-1].set_ox(ball_lis[i][j-1].get_x())
                ball_lis[i][j-1].set_oy(ball_lis[i][j-1].get_y())
                
                ball_lis[i][j-1].set_x(ball_lis[i][j-1].get_x()-offsetx)
                ball_lis[i][j-1].set_y(ball_lis[i][j-1].get_y()-offsety)
                
                ball_lis[i][j].set_x(ball_lis[i][j].get_x()+offsetx)
                ball_lis[i][j].set_y(ball_lis[i][j].get_y()+offsety)
                
                
            
            if i>0:
                dx=ball_lis[i][j].get_x()-ball_lis[i-1][j].get_x()
                dy=ball_lis[i][j].get_y()-ball_lis[i-1][j].get_y()
                
                d=distance(ball_lis[i-1][j].get_x(),ball_lis[i][j].get_x(),ball_lis[i-1][j].get_y(),ball_lis[i][j].get_y())
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
                ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
                
                ball_lis[i-1][j].set_ox(ball_lis[i-1][j].get_x())
                ball_lis[i-1][j].set_oy(ball_lis[i-1][j].get_y())
                
                ball_lis[i-1][j].set_x(ball_lis[i-1][j].get_x()-offsetx)
                ball_lis[i-1][j].set_y(ball_lis[i-1][j].get_y()-offsety)
                
                ball_lis[i][j].set_x(ball_lis[i][j].get_x()+offsetx)
                ball_lis[i][j].set_y(ball_lis[i][j].get_y()+offsety)
                
            if i<len(ball_lis)-1:
                dx=ball_lis[i][j].get_x()-ball_lis[i+1][j].get_x()
                dy=ball_lis[i][j].get_y()-ball_lis[i+1][j].get_y()
                
                d=distance(ball_lis[i+1][j].get_x(),ball_lis[i][j].get_x(),ball_lis[i+1][j].get_y(),ball_lis[i][j].get_y())
                diff=length-d
                percent_change=diff/d/2
    #             print(percent_change,d,diff)
                offsetx=dx*percent_change
                offsety=dy*percent_change
                
                ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
                ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
                
                ball_lis[i+1][j].set_ox(ball_lis[i+1][j].get_x())
                ball_lis[i+1][j].set_oy(ball_lis[i+1][j].get_y())
                
                ball_lis[i+1][j].set_x(ball_lis[i+1][j].get_x()-offsetx)
                ball_lis[i+1][j].set_y(ball_lis[i+1][j].get_y()-offsety)
                
                ball_lis[i][j].set_x(ball_lis[i][j].get_x()+offsetx)
                ball_lis[i][j].set_y(ball_lis[i][j].get_y()+offsety)
                

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
        a=n//2
        b=n//2
#         for i in range(0,len(ball_lis)):
#             for i in range(0,len(ball_lis)):
#                 if distance(pos[0],ball_lis[i][j].get_x(),pos[1],ball_lis[i][j].get_y())<d:
#                     d=distance(pos[0],ball_lis[i][j].get_x(),pos[1],ball_lis[i][j].get_y())
#                     a=i
#                     b=j
#                     
        ball_lis[a][b].set_ox(ball_lis[a][b].get_x())
        ball_lis[a][b].set_oy(ball_lis[a][b].get_y())
         
        ball_lis[a][b].set_x(pos[0])
        ball_lis[a][b].set_y(pos[1])
    
        
    reposition(ball_lis) 
    reposition(ball_lis) 
    
    for i in range(0,len(ball_lis)):
        for j in range(0,len(ball_lis)):
            vx=ball_lis[i][j].get_x()-ball_lis[i][j].get_ox()
            vy=ball_lis[i][j].get_y()-ball_lis[i][j].get_oy()
            
            ball_lis[i][j].set_ox(ball_lis[i][j].get_x())
            ball_lis[i][j].set_oy(ball_lis[i][j].get_y())
            
            ball_lis[i][j].set_x(ball_lis[i][j].get_x()+vx)
            ball_lis[i][j].set_y(ball_lis[i][j].get_y()+vy)
            ball_lis[i][j].apply_g()
#             ball_lis[i][j].apply_wind()
    
    draw_ball(ball_lis)            
    p.display.flip()
        
    p.time.Clock().tick(fps)