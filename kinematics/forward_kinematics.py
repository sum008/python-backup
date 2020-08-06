'''
Created on Jun 16, 2020

@author: Sumit
'''
import pygame as p
import math

p.init()
window=(600,600)
display=p.display.set_mode(window)

points=[[300,500],[300,500],[300,500]]

fps=10
run=True
length=50
fix=(300,500)
count=0
while run:
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    
    
    angle1=math.atan2(points[1][1]-points[2][1],points[1][0]-points[2][0])
#     angle1*=57.29
    points[1][0]=points[0][0]+int(length*math.cos(angle1))
    points[1][1]=points[0][1]+int(length*math.sin(angle1))
    
    cur=p.mouse.get_pos()
    angle2=math.atan2(points[2][1]-cur[1],points[2][0]-cur[0])
#     angle2*=57.29
    points[2][0]=points[1][0]+int(length*math.cos(angle2))
    points[2][1]=points[1][1]+int(length*math.sin(angle2))
    
#     print(int(points[1][0]),int(points[1][1]),angle)
    p.draw.line(display, (0,0,0),fix,(int(points[1][0]),int(points[1][1])), 1)
    p.draw.circle(display, (0,0,0), (points[1][0],points[1][1]), 2, 2)
    p.draw.line(display, (0,0,0),(int(points[1][0]),int(points[1][1])),(int(points[2][0]),int(points[2][1])), 1)
        
    p.display.flip()
        
    p.time.Clock().tick(fps)