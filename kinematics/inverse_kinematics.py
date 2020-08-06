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

fps=30
run=True
length=50
fix=(300,500)
count=0
while run:
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    mouse=p.mouse.get_pos()
    
    angle=math.atan2(mouse[1]-fix[1], mouse[0]-fix[0])
    
    if fix[0]-2*length>mouse[0] or fix[1]-2*length>mouse[1] or fix[0]+2*length<mouse[0]  or fix[1]+2*length<mouse[1]:
        
        angle1=angle
        angle2=0
        
        points[1][0]=fix[0]+int(length*math.cos(angle1))
        points[1][1]=fix[1]+int(length*math.sin(angle1))
    
        points[2][0]=points[1][0]+int(length*math.cos(angle2+angle1))
        points[2][1]=points[1][1]+int(length*math.sin(angle2+angle1))
    
    else:
        l=math.sqrt((mouse[0]-fix[0])**2+(mouse[1]-fix[1])**2)
    
        x=(l*l-2*length**2)/(2*length*length)
#       
        try:
            angle2=math.acos(x)
        except:
            pass
        angle1=math.atan2(mouse[1]-fix[1],mouse[0]-fix[0])-math.atan2((length*math.sin(angle2)),(length+length*math.cos(angle2)))
        
        points[1][0]=fix[0]+int(length*math.cos(angle1))
        points[1][1]=fix[1]+int(length*math.sin(angle1))
    
        points[2][0]=points[1][0]+int(length*math.cos(angle2+angle1))
        points[2][1]=points[1][1]+int(length*math.sin(angle2+angle1))
    
    
    p.draw.line(display, (0,0,0),fix,(int(points[1][0]),int(points[1][1])), 1)
    p.draw.circle(display, (0,0,0), (points[1][0],points[1][1]), 4, 4  )
    p.draw.line(display, (0,0,0),(int(points[1][0]),int(points[1][1])),(int(points[2][0]),int(points[2][1])), 1)
        
    p.display.flip()
        
    p.time.Clock().tick(fps)