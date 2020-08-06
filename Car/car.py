import pygame as p
import vector_
import particle
import math
p.init()
width=600
height=600
display=p.display.set_mode((width,height))
image=p.image.load("car.png")


run=True
velocity=vector_.vector_functions()

bullet1=p.Surface((2,2))
bullet1.fill((255,255,255)) 

x=200
y=200
l=0
position=vector_.vector_functions()
position.create(x, y)

velocity.set_length(l)
position.add_to_xy(velocity)

accelerate = vector_.vector_functions()
accelerate.create(0.6, 0.6)

friction = 0.975

angle=0
image=p.transform.scale(image, (43, 70))
image=p.transform.rotate(image, -270)
acc=0.75
lastangle=angle
move="null"
while run:
    display.fill((0,150,0))
    
    img=p.transform.rotate(image, angle)
    
    getrect=img.get_rect()
    getrect.center=(position.getX()%width,position.getY()%height)
    display.blit(img,getrect)
    
    velocity.set_angle(lastangle)
    position.add_to_xy(velocity)
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
        
    if keys[p.K_RIGHT] and abs(velocity.get_length())>0.75:
        angle=(angle-1)%360
        if move=="r":
            lastangle=math.pi-(angle*0.0174)
        else:
            lastangle=-angle*0.0174
        
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
        velocity.set_length(velocity.get_length()-15)
        lastangle=math.pi-(angle*0.0174)
        move="r"
    if velocity.get_length()<0.75:
        velocity.set_length(0)
    
    velocity.set_length(velocity.get_length()*friction)
    
    print(velocity.get_length())  
    p.display.flip()
    p.time.Clock().tick(120)
