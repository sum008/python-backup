import pygame as p
import math
import particle
import vector_
p.init()

display=p.display.set_mode((1080,400))
point=p.Surface((50,50))
point.fill((205,25,111))

bullet1=p.Surface((16,2))
bullet1.set_colorkey((0,0,0))
bullet1.fill((42,193,198))
px=500
py=350

cx=px
cy=py
x=cx+50
y=cy
angle=0
bx=x
by=y
curangle=0
g=0.3
v=11
bullet=particle.particle()
bullet.create(bx, by, curangle, 0, 0, 0, 0.99)

run=True

an=curangle
display.fill((0,0,0))


def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle*(0.01745))*(oldx-cx)-math.sin(angle*(0.01745))*(oldy-cy)
    y=cy+math.sin(angle*(0.01745))*(oldx-cx)+math.cos(angle*(0.01745))*(oldy-cy)
    return [x,y]

lastkey="null"
while run:
    display.fill((0,0,0))
    an=curangle
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False        
            
    keys=p.key.get_pressed()
        
    if keys[p.K_LEFT]:
        display.fill((0,0,0))
        angle=(angle-1)%360
        a=rot(cx, cy, x, y, angle)
        x=a[0]
        y=a[1]
        bx=x
        by=y
        pe=400-50-y
        b=x-500
        curangle=math.atan2(pe, b)
        bullet.position.setX(bx)
        bullet.position.setY(by)
        bullet.velocity.set_length(0)
        bullet.gravity.set_length(0)
        lastkey="l"
        
         
    if keys[p.K_RIGHT]:
        display.fill((0,0,0))
        angle=(angle+1)%360
        a=rot(cx, cy, x, y, angle)
        x=a[0]
        y=a[1]
        bx=x
        by=y
        pe=400-50-y
        b=x-500
        count=0
        curangle=math.atan2(pe, b)
        bullet.position.setX(bx)
        bullet.position.setY(by)
        bullet.velocity.set_length(0)
        bullet.gravity.set_length(0)
        lastkey="r"
    if keys[p.K_SPACE]:
        
        bullet.position.setX(bx)
        bullet.position.setY(by)
        
        bullet.velocity.set_length(v)
        bullet.velocity.set_angle(-curangle)
        bullet.gravity.set_length(g)
        bullet.gravity.set_angle(math.pi/2)
        lastkey="s"
        
                
    if lastkey=="l" or lastkey=="r":
        an=curangle 
    elif lastkey=="s":
        an=-bullet.velocity.get_angle()  
        
    bul=p.transform.rotate(bullet1, an*57.2958)
    getrect=bul.get_rect()
    getrect.center=(bullet.getX(),bullet.getY())
#     an=-bullet.velocity.get_angle()
    
    display.blit(point,(cx,cy))
    display.blit(bul,getrect)
    
    p.draw.line(display, (203,25,14),(cx,cy), (x,y), 4)
    p.display.flip()
    bullet.drag_overall()
    bullet.update()
    angle=0
    p.time.Clock().tick(60)