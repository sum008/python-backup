import pygame as p
import vector_
import particle
import math
import random
p.init()
width=600
height=600
display=p.display.set_mode((width,height))
font=p.font.SysFont(None, 30)

object=vector_.vector_functions()
object.create(200,200)
velocity=vector_.vector_functions()
velocity.create(3, 3)
r=20
display.fill((255,255,255))
color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

run=True

def disp(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))


while run:
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    p.draw.circle(display, (0,0,0), (int(object.getX()),int(object.getY())), r, r)
    
    mouse=p.mouse.get_pos()
    acc=vector_.vector_functions()
    acc.create(mouse[0]-object.getX(),mouse[1]-object.getY())
    acc.mul_to_xy(0.09)
    velocity.add_to_xy(acc)
    velocity.mul_to_xy(0.9)
    object.add_to_xy(velocity)

#     angle=math.atan2(mouse[1]-object.getY(), mouse[0]-object.getX())
#     velocity.set_angle(angle)
#     object.add_to_xy(velocity)
    
    p.display.flip()
    p.time.Clock().tick(60)
    
    
    