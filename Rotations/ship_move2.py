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

bullet1=p.Surface((14,3))
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
accelerate.create(0.55, 0.55)
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
        angle=(angle+1)%360
        
    if keys[p.K_RIGHT]:
        angle=(angle-1)%360
        
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
        

#         if abs(cur_bullet.getX()-position.getX())>=150 or abs(cur_bullet.getY()-position.getY())>=150:
        mouse_pos=p.mouse.get_pos()    
        
        if abs(cur_bullet.getX()-mouse_pos[0])<=15 and  abs(cur_bullet.getY()-mouse_pos[1])<=15 :
            list_bullet.remove([cur_bullet,lastangle])

        a=p.Vector2(mouse_pos[0],mouse_pos[1])
        b=p.Vector2(cur_bullet.getX(),cur_bullet.getY())
        an=math.atan2(mouse_pos[1]-cur_bullet.getY(), mouse_pos[0]-cur_bullet.getX())
        
        desired=a-b
        desired=desired.normalize()*5
        
        vel_vec=p.Vector2(cur_bullet.velocity.getX(),cur_bullet.velocity.getY())
        steer=(desired-vel_vec).normalize()*0.036
        
        cur_bullet.velocity.setX(cur_bullet.velocity.getX()+steer[0])
        cur_bullet.velocity.setY(cur_bullet.velocity.getY()+steer[1])
        bullet2=p.transform.rotate(bullet1,-an*57.23)
#         else:
#             bullet2=p.transform.rotate(bullet1,lastangle)
        display.blit(bullet2,(cur_bullet.getX(),cur_bullet.getY()))
        cur_bullet.update()
#         print(pos)
        
        
#     print(velocity.get_length())  
    p.display.flip()
    p.time.Clock().tick(60)
