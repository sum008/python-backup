'''
Created on Apr 30, 2020

@author: Sumit
'''
import pygame as p
import math

p.init()
width=600
height=600
display=p.display.set_mode((width,height))
font=p.font.SysFont(None, 30)

run=True
i=0
k=1
m=1
dt=0.1
xp=1
yp=1
v=0
x=0
y=0
while run:
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    ax=-(k/m)*x
    ay=-(k/m)*y        
    if i==0:
        xp=2*x-xp+ax*dt**2
        yp=2*x-yp+ay*dt**2
        x=xp
        y=yp
        i+=1
    else:
        
        xp=2*x-xp+ax*dt**2
        yp=2*x-yp+ay*dt**2
        x=xp
        y=yp
        
    print(x,y,ax,ay)
    p.draw.circle(display, (0,0,0), (int(x),int(y)), 13, 13)
    p.display.flip()
    p.time.Clock().tick(30)
#     dt+=0.1
    
        
        