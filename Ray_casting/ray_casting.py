'''
Created on Apr 27, 2020

@author: Sumit
'''
import pygame as p
import math 

width=840
height=650
screen = p.display.set_mode((width, height))


point1=(600,200)
point2=(600,400)

source1=(100,300)
source2=(300,300)
fix_source=(700,300)


def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle)*(oldx-cx)-math.sin(angle)*(oldy-cy)
    y=cy+math.sin(angle)*(oldx-cx)+math.cos(angle)*(oldy-cy)
    return (x,y)


angle=0
run=True
while run:
    
    screen.fill((0,0,0))
    

    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
    m_pos=p.mouse.get_pos()        
    angle=math.atan2((m_pos[1]-fix_source[1]), m_pos[0]-fix_source[0])
    
    source2=rot(source1[0], source1[1], fix_source[0], fix_source[1], angle)
    
    p.draw.line(screen, (255,255,255), point1, point2, 2)
    
    x1,y1,x2,y2,x3,y3,x4,y4=map(int ,(source1[0],source1[1],source2[0],source2[1],point1[0],point1[1],point2[0],point2[1]))
    dem=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if dem!=0:
        t=( (x1-x3)*(y3-y4) - (y1-y3)*(x3-x4) ) / dem
        u=- ( (x1-x2)*(y1-y3) - (y1-y2)*(x1-x3) ) / dem
        
        px=x1+t*(x2-x1)
        py=y1+t*(y2-y1)
    #     print(t,u)
        if (u>=0 and u<=1 and t>=0 and t<=1): # ( t>=0 and t<=1 ) or
    #             print(px,py)
            p.draw.circle(screen, (255,155,23), (int(px),int(py)), 5, 5)
            p.draw.line(screen, (255,255,255), source1, (int(px),int(py)), 2)
        else:
            p.draw.line(screen, (255,255,255), source1, source2, 2)
    #             p.draw.circle(screen, (255,155,23), (int(px),int(py)), 5, 5)
    p.display.flip()
    p.time.Clock().tick(60)
    
    
    
    