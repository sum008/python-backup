import pygame as p
import vector_
import math
p.init()
width=600
height=600
display=p.display.set_mode((width,height))
image=p.image.load("car.png")


run=True
velocity=vector_.vector_functions()


x=200
y=200
l=0
position=vector_.vector_functions()
position.create(x, y)

velocity.set_length(l)
position.add_to_xy(velocity)

accelerate = vector_.vector_functions()
accelerate.create(0.6, 0.6)

friction = 0.98

angle=0
image=p.transform.scale(image, (30, 55))
image=p.transform.rotate(image, -270)
acc=0.5
deacc=3
lastangle=angle
move="null"
last_dir="null"
while run:
    display.fill((0,150,0))
    
    angle_rot = velocity.get_angle()
    img=p.transform.rotate(image, angle)
    
    getrect=img.get_rect()
    
    getrect.center=(position.getX()%width,position.getY()%height)
    display.blit(img,getrect)
    
    velocity.set_angle(lastangle)
    b=p.Vector2(0,0)
    a=p.Vector2(velocity.getX(),velocity.getY())
    if last_dir=="r":
        b=p.Vector2(velocity.getX()+100,velocity.getY()+100)
    elif last_dir=="l":
        b=p.Vector2(velocity.getX()-100,velocity.getY()-100)
    c=a-b
    
    if c[0]!=0 or c[1]!=0:
        c=c.normalize()*0.9
    print(c)
    vel2=vector_.vector_functions()
    vel2.create(velocity.getX()+c[0], velocity.getY()+c[1])
    position.add_to_xy(vel2)
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
     
    keys=p.key.get_pressed()
           
    if keys[p.K_LEFT] and abs(velocity.get_length())>0.75:
        angle=(angle+1)%360
        lastangle=-angle*0.0174
        if move=="r":
            lastangle=math.pi-(angle*0.0174)
        else:
            lastangle=-angle*0.0174
        last_dir="l"
    if keys[p.K_RIGHT] and abs(velocity.get_length())>0.75:
        angle=(angle-1)%360
        if move=="r":
            lastangle=math.pi-(angle*0.0174)
        else:
            lastangle=-angle*0.0174
        last_dir="r"
    if keys[p.K_UP]: #Accelerate
        if(velocity.get_length()<10):
            velocity.set_length(velocity.get_length()+acc)
        lastangle=-angle*0.0174
        move="null"
#     if keys[p.K_DOWN] and velocity.get_length()>0.75: #Brakes
#         velocity.set_length(velocity.get_length()-acc)
#         lastangle=-(angle*0.0174)
#         move="null"
    if keys[p.K_DOWN]:# and velocity.get_length()<=0:
        
        velocity.set_length(velocity.get_length()-deacc)
        lastangle=math.pi-(angle*0.0174)
        move="r"
    if velocity.get_length()<0.5:
        velocity.set_length(0)
        last_dir="null"
    
    
    velocity.set_length(velocity.get_length()*friction)
    
    print(position.getX(),angle,getrect)  
    p.display.flip()
    p.time.Clock().tick(60)
