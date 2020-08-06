'''
Created on Jun 18, 2020

@author: Sumit
'''
import pygame as p
import math

p.init()
window=(600,600)
display=p.display.set_mode(window)

points=[[300,300],[350,300],[400,300]]

fps=30
run=True
length=50
fix=(300,300)
count=0
while run:
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    mouse=p.mouse.get_pos()
    
#     t=math.atan2(mouse[1]-fix[1],mouse[0]-fix[0])
#     
#     if fix[0]-2*length>mouse[0] or fix[1]-2*length>mouse[1] or fix[0]+2*length<mouse[0]  or fix[1]+2*length<mouse[1]:
#         
#         ang2=t
#         ang1=ang2
#     else:
        
    mouse=p.mouse.get_pos()
    ang2=math.atan2(mouse[1]-points[2][1], mouse[0]-points[2][0])
    
    points[2][0]=mouse[0]+int(length*math.cos(-ang2))
    points[2][1]=mouse[1]+int(length*math.sin(-ang2))
    
    ang1=math.atan2(points[2][1]-points[1][1], points[2][0]-points[1][0])
    
    points[1][0]=points[2][0]+int(length*math.cos(-ang1))
    points[1][1]=points[2][1]+int(length*math.sin(-ang1))
    
    ang0=math.atan2(points[1][1]-points[0][1], points[1][0]-points[0][0])
    
    points[0][0]=points[1][0]+int(length*math.cos(-ang0))
    points[0][1]=points[1][1]+int(length*math.sin(-ang0))
        
    

    p.draw.line(display, (0,0,0),(points[0][0],points[0][1]),(int(points[1][0]),int(points[1][1])), 1)
    p.draw.circle(display, (0,0,0), (points[1][0],points[1][1]), 4, 4  )
    p.draw.line(display, (0,0,0),(int(points[1][0]),int(points[1][1])),(int(points[2][0]),int(points[2][1])), 1)
        
    p.display.flip()
        
    p.time.Clock().tick(fps)
