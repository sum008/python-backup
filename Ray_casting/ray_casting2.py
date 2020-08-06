'''
Created on Apr 27, 2020

@author: Sumit
'''

import pygame as p
import math 
from random import randint
from numpy import Infinity

width=650
height=650
screen = p.display.set_mode((width, height))

pointa=[]
pointb=[]
for _ in range(0,5):
    pointa.append([randint(10,width-10),randint(10,height-10)])
    pointb.append([randint(10,width-10),randint(10,height-10)])

source1=(100,300)
fix_source=(100,300)


def distance(x1,x2,y1,y2):
        x=abs(x1-x2)
        y=abs(y1-y2)
        return math.sqrt(x**2+y**2)
    
def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle)*(oldx-cx)-math.sin(angle)*(oldy-cy)
    y=cy+math.sin(angle)*(oldx-cx)+math.cos(angle)*(oldy-cy)
    return (x,y)

def point_to_center(cx,cy,px,py):
    
    angle=math.atan2(cy-py, cx-px)
    return angle*57.2958

offset=200
angle1=0
run=True
while run:
    screen.fill((5,5,5))
    
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
    keys=p.key.get_pressed()        
    if keys[p.K_w]:
        angle1-=5
    elif keys[p.K_s]:
        angle1+=5
    elif keys[p.K_a]:
        offset-=5
    elif keys[p.K_d]:
        offset+=5
    m_pos=p.mouse.get_pos() 
    anglez=int(point_to_center(width//2, height//2, m_pos[0], m_pos[1]))+1
    print(anglez,m_pos[0],m_pos[1])
#     print(180-abs(anglez))
#       
#     s=angle1//2
#     e=angle1//2
#     print(s,e)
    source=[]
#     angle=math.atan2((m_pos[1]-fix_source[1]), m_pos[0]-fix_source[0])
    for angle in range(angle1,90+angle1):
    
        x=rot(m_pos[0],m_pos[1],m_pos[0]+offset,m_pos[1],(angle)*0.0174533)
        y=x[1]
        x=x[0]
        source.append([x,y])
    
    for source2 in source: 
        prevx=0
        prevy=0 
        prev=Infinity
        for point1,point2 in zip(pointa,pointb):
            p.draw.line(screen, (255,255,255), point1, point2, 2)
            x1,y1,x2,y2,x3,y3,x4,y4=map(int ,(m_pos[0],m_pos[1],source2[0],source2[1],point1[0],point1[1],point2[0],point2[1]))
            dem=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
            if dem!=0:
                t=( (x1-x3)*(y3-y4) - (y1-y3)*(x3-x4) ) / dem
                u=- ( (x1-x2)*(y1-y3) - (y1-y2)*(x1-x3) ) / dem
                
                if (t>0 and t<1 and u<1 and u>0): # ( t>=0 and t<=1 ) or
                    px=x1+t*(x2-x1)
                    py=y1+t*(y2-y1)
#                     print(px,py)
                    d=distance(m_pos[0], px, m_pos[1], py)
                    if d<prev:
                        prev=d
                        prevx=px
                        prevy=py
                        
        if prevx!=0 and prevy!=0:
            
            c=(255,255,255)
            p.draw.circle(screen, (255,155,23), (int(prevx),int(prevy)), 3, 3)
            p.draw.line(screen, c, (m_pos[0],m_pos[1]), (int(prevx),int(prevy)), 3)
        else:
            p.draw.line(screen, (255,255,255,1), (m_pos[0],m_pos[1]), source2, 3)
        
    p.display.flip()
    p.time.Clock().tick(60)