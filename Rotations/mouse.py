import pygame as p
import math

p.init()

display=p.display.set_mode((400,400))
point=p.Surface((30,5))
point.set_colorkey((255,255,255))
point.fill((0,0,0))


dot=p.Surface((3,3))
dot.fill((0,0,0))

angle=0
display.fill((255,255,255))
pos=0

cx=200
cy=200

x=cx+100
y=cy

angle1=0.5
def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle*(0.01745))*(oldx-cx)-math.sin(angle*(0.01745))*(oldy-cy)
    y=cy+math.sin(angle*(0.01745))*(oldx-cx)+math.cos(angle*(0.01745))*(oldy-cy)
    return [x,y]

run=True
while run:
    
    display.fill((255,255,255))
    point_=p.transform.rotate(point, -angle*57.29)
    getrect=point_.get_rect()
    getrect.center=(x,y)
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
        
        if event.type==p.MOUSEMOTION:
            pos = p.mouse.get_pos()
            
            print(pos[0],pos[1])
            
    angle=math.atan2(pos[1]-getrect[1], pos[0]-getrect[0])
    
    p.draw.rect(display, (120,88,19), getrect, 1)
    
    display.blit(point_,getrect)
    
    display.blit(dot,(cx,cy))
#     a=rot(cx,cy,x,y,angle1)
#     x=a[0]
#     y=a[1]
    
    p.display.flip()
    p.time.Clock().tick(120)
            