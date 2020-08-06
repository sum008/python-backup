import pygame as p
import vector_
import particle
import math
p.init()
width=600
height=600
display=p.display.set_mode((width,height))
image=p.image.load("ship.png")
image=p.transform.scale(image, (40, 70))
run=True
velocity=vector_.vector_functions()

bullet1=p.Surface((10,2))
bullet1.set_colorkey((0,0,0))
bullet1.fill((255,255,255)) 
# bullet1=p.image.load("mi.jpg")

x=200
y=200
l=0
position=vector_.vector_functions()
position.create(x, y)

velocity.set_length(l)
position.add_to_xy(velocity)

accelerate = vector_.vector_functions()
accelerate.create(0.6, 0.6)
angle=0
image=p.transform.rotate(image, -90)
list_bullet=[]
lastangle=angle

while run:
    display.fill((0,0,0))
    
    img=p.transform.rotate(image, angle)
    
    getrect=img.get_rect()
    getrect.center=(position.getX(),position.getY())
    display.blit(img,getrect)
    
    position.create(position.getX()%width , position.getY()%height)
    velocity.set_angle(-(angle)*0.01745)
    position.add_to_xy(velocity)
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
        if event.type==p.KEYDOWN:
            if event.key==32:
                lastangle=angle
                bullet=particle.particle()
                bullet.create(position.getX()+22*math.cos(-(angle)*0.01745), position.getY()+22*math.sin(-(angle)*0.01745), -(angle)*0.01745, velocity.get_length()*2+3, 0, 0, 0)
                list_bullet.append([bullet,lastangle])
                
    keys=p.key.get_pressed()
           
    if keys[p.K_LEFT]:
        angle=(angle+2)%360
        
    if keys[p.K_RIGHT]:
        angle=(angle-2)%360
        
    if keys[p.K_UP]:
        accelerate.set_angle(-(angle)*0.01745)
        velocity.add_to_xy(accelerate)
        
    if keys[p.K_DOWN] and velocity.get_length()>0.75:
        accelerate.set_angle(-(angle)*0.01745)
        velocity.subtract_from_xy(accelerate)
    elif velocity.get_length()<0.75:
        velocity.set_length(0)
    
#     if keys[p.K_SPACE]:    
#         bullet=particle.particle()
#         bullet.create(position.getX()+22*math.cos(-(angle)*0.01745), position.getY()+22*math.sin(-(angle)*0.01745), -(angle)*0.01745, velocity.get_length()*2+6, 0, 0, 0)
#         list_bullet.append(bullet)
                
    for cur_bullet,lastangle in list_bullet:
        
        if cur_bullet.getX()>width or cur_bullet.getX()<0 or cur_bullet.getY()>height or cur_bullet.getY()<0:
            list_bullet.remove([cur_bullet,lastangle])
#         if abs(cur_bullet.getX()-position.getX())>=150 or abs(cur_bullet.getY()-position.getY())>=150:
        pos=p.mouse.get_pos()    
        a=math.atan2(pos[1]-cur_bullet.getY(), pos[0]-cur_bullet.getX())
        cur_bullet.velocity.set_angle(a)
        bullet2=p.transform.rotate(bullet1,-a*57.29)
#         else:
#             bullet2=p.transform.rotate(bullet1,lastangle)
        display.blit(bullet2,(cur_bullet.getX(),cur_bullet.getY()))
        cur_bullet.update()
#         print(pos)
        
        
#     print(velocity.get_length())  
    p.display.flip()
    p.time.Clock().tick(60)
