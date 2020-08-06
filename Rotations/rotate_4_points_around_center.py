import pygame as p
import math
p.init()

display=p.display.set_mode((400,400))
point=p.Surface((5,5))
point.fill((255,255,255))
# point.set_colorkey((0,0,0))
# point.fill((255,255,255))
# point=p.image.load("Spaceship (4).png")
angle=0
run=True
display.fill((0,0,0))

def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle*(0.01745))*(oldx-cx)-math.sin(angle*(0.01745))*(oldy-cy)
    y=cy+math.sin(angle*(0.01745))*(oldx-cx)+math.cos(angle*(0.01745))*(oldy-cy)
    return [x,y]

offset=100

cx=200
cy=200

ax=cx-offset
ay=cy-offset

bx=cx+offset
by=cy-offset

c_x=cx+offset
c_y=cy+offset

dx=cx-offset
dy=cy+offset

while run:
    display.fill((0,0,0))
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
#     p.draw.rect(display, (120,88,19), (100,100,50,50), 1)
    
    a=rot(cx,cy,ax,ay,angle)
    print(a[0],a[1])
    display.blit(point,(a[0],a[1]))
    ax=a[0]
    ay=a[1]
    
    b=rot(cx,cy,bx,by,angle)
    print(b[0],b[1])
    display.blit(point,(b[0],b[1]))
    bx=b[0]
    by=b[1]
    
    c=rot(cx,cy,c_x,c_y,angle)
    print(c[0],c[1])
    display.blit(point,(c[0],c[1]))
    c_x=c[0]
    c_y=c[1]
    
    d=rot(cx,cy,dx,dy,angle)
    print(d[0],d[1])
    display.blit(point,(d[0],d[1]))
    dx=d[0]
    dy=d[1]
    
    p.draw.line(display, (25,55,200), (ax,ay), (bx,by), 5)
    p.draw.line(display, (99,11,255), (bx,by), (c_x,c_y), 5)
    p.draw.line(display, (119,58,36), (c_x,c_y), (dx,dy), 5)
    p.draw.line(display, (187,5,69), (dx,dy), (ax,ay), 5)
    keys=p.key.get_pressed()
              
    if keys[p.K_LEFT]:
        angle=(angle-1)%360
        
        a=rot(cx,cy,ax,ay,angle)
        print(a[0],a[1])
        display.blit(point,(a[0],a[1]))
        ax=a[0]
        ay=a[1]
        
        b=rot(cx,cy,bx,by,angle)
        print(b[0],b[1])
        display.blit(point,(b[0],b[1]))
        bx=b[0]
        by=b[1]
        
        c=rot(cx,cy,c_x,c_y,angle)
        print(c[0],c[1])
        display.blit(point,(c[0],c[1]))
        c_x=c[0]
        c_y=c[1]
        
        d=rot(cx,cy,dx,dy,angle)
        print(d[0],d[1])
        display.blit(point,(d[0],d[1]))
        dx=d[0]
        dy=d[1]
        
        p.draw.line(display, (255,255,255), (ax,ay), (bx,by), 5)
        p.draw.line(display, (255,255,255), (bx,by), (c_x,c_y), 5)
        p.draw.line(display, (255,255,255), (c_x,c_y), (dx,dy), 5)
        p.draw.line(display, (255,255,255), (dx,dy), (ax,ay), 5)
          
    if keys[p.K_RIGHT]:
        angle=(angle+1)%360
        
        a=rot(cx,cy,ax,ay,angle)
        print(a[0],a[1])
        display.blit(point,(a[0],a[1]))
        ax=a[0]
        ay=a[1]
        
        b=rot(cx,cy,bx,by,angle)
        print(b[0],b[1])
        display.blit(point,(b[0],b[1]))
        bx=b[0]
        by=b[1]
        
        c=rot(cx,cy,c_x,c_y,angle)
        print(c[0],c[1])
        display.blit(point,(c[0],c[1]))
        c_x=c[0]
        c_y=c[1]
        
        d=rot(cx,cy,dx,dy,angle)
        print(d[0],d[1])
        display.blit(point,(d[0],d[1]))
        dx=d[0]
        dy=d[1]
        
        p.draw.line(display, (255,255,255), (ax,ay), (bx,by), 5)
        p.draw.line(display, (255,255,255), (bx,by), (c_x,c_y), 5)
        p.draw.line(display, (255,255,255), (c_x,c_y), (dx,dy), 5)
        p.draw.line(display, (255,255,255), (dx,dy), (ax,ay), 5)
    angle=0
    p.display.flip()
    p.time.Clock().tick(60)
    
    