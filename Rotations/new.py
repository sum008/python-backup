import pygame as p
import math
import particle
import vector_
p.init()

display=p.display.set_mode((1080,400))
point=p.Surface((50,50))
point.fill((205,25,111))

bullet1=p.Surface((10,2))
bullet1.set_colorkey((0,0,0))
bullet1.fill((255,255,255))


line=p.Surface((50,2))
line.set_colorkey((0,0,0))
line.fill((0,153,250))


px=500
py=350

cx=px
cy=py
x=cx+25
y=cy
angle=0
bx=x
by=y
curangle=0
g=0.3
v=11
bullet=particle.particle()
bullet.create(bx, by, curangle, 0, 0, 0, 0.99)

point1=particle.particle()
point1.create(px, py, 0, 0, 10, 0, 0.99)

accelerateX=vector_.vector_functions()
accelerateX.create(0.2, 0)

run=True

an=curangle
display.fill((0,0,0))
b=0
pe=0

lastkey="null"
while run:
    display.fill((0,0,0))
    an=curangle
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False        
            
    keys=p.key.get_pressed()
    if keys[p.K_UP]:
        point1.velocity.add_to_xy(accelerateX)
        bullet.velocity.add_to_xy(accelerateX)

    if keys[p.K_DOWN] :
        point1.velocity.subtract_from_xy(accelerateX)
        bullet.velocity.subtract_from_xy(accelerateX)
        
    if keys[p.K_LEFT]:
        display.fill((0,0,0))
        angle=(angle+1)%360
        
        b=25*math.cos(angle/57.296)
        pe=25*math.sin(angle/57.296)
        
        curangle=math.atan2(pe, b)
        
        bullet.position.setX(point1.position.getX()+b)
        bullet.position.setY(point1.position.getY()-pe)
        bullet.velocity.set_length(0)
        bullet.gravity.set_length(0)
        lastkey="l"
        print(angle,curangle)
         
    if keys[p.K_RIGHT]:
        display.fill((0,0,0))
        angle=(angle-1)%360
        
        b=25*math.cos(angle/57.296)
        pe=25*math.sin(angle/57.296)
        
        curangle=math.atan2(pe, b)
        bullet.position.setX(point1.position.getX()+b)
        bullet.position.setY(point1.position.getY()-pe)
        bullet.velocity.set_length(0)
        bullet.gravity.set_length(0)
        lastkey="r"
        print(angle,curangle)
    if keys[p.K_SPACE]:
        if abs(point1.velocity.get_length())==0:
            bullet.velocity.set_length(0)
        bullet.position.setX(point1.position.getX()+b)
        bullet.position.setY(point1.position.getY()-pe)
        
        bullet.velocity.set_length(v)
        bullet.velocity.set_angle(-curangle)
        bullet.gravity.set_length(g)
        bullet.gravity.set_angle(math.pi/2)
        lastkey="s"
        
    if abs(point1.velocity.get_length())<0.1:
            point1.velocity.set_length(0)
                
    if lastkey=="l" or lastkey=="r":
        an=curangle 
    elif lastkey=="s":
        an=-bullet.velocity.get_angle()  
        
    bul=p.transform.rotate(bullet1, an*57.2958)
    getrect=bul.get_rect()
    getrect.center=(bullet.getX(),bullet.getY())
    an=-bullet.velocity.get_angle()
    
    
    line1=p.transform.rotate(line, angle)
    getrect1=line1.get_rect()
    getrect1.center=(point1.getX(),point1.getY())
    display.blit(line1,getrect1)
    display.blit(point,(point1.getX(),point1.getY()))
    display.blit(bul,getrect)
    
    
    
    p.display.flip()
    bullet.drag_overall()
    bullet.update()
    point1.update()
    
    point1.drag_overall()
    
    p.time.Clock().tick(60)
    
    