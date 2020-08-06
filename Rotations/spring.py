import math
import pygame as p
import particle
import random
import vector_
p.init()

width=640
height=400
screen = p.display.set_mode((width, height))
run=True

k=0.2
f=0.97
vel=50
m=0
g=0.3
#f=k*position

spring_point=vector_.vector_functions()
spring_point.create((width/2), height/2)

spring=particle.particle()
spring.create(random.random()*width, random.random()*height, random.random()*math.pi*2, vel, m, g, f)

screen.fill((255,255,255))
seperate=100
while run:
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
            
    p.draw.circle(screen, (0,0,0), ( int(spring_point.getX()),int(spring_point.getY())), 3, 3)
    
    p.draw.circle(screen, (0,0,0), (int(spring.getX()),int(spring.getY())), 15, 15)
    
    p.draw.line(screen, (0,0,0), (spring_point.getX(),spring_point.getY()),(spring.getX(),spring.getY()), 1)
    
    click=p.mouse.get_pressed()

    pos=p.mouse.get_pos()
    if click[0]==1 :#and abs(pos[0]-spring.getX())<5 and abs(pos[1]-spring.getY())<5:
        
        pos=p.mouse.get_pos()
        spring.position.setX(pos[0])
        spring.position.setY(pos[1])
        
    x=spring_point.getX()
    y=spring_point.getY()
    v=vector_.vector_functions()
    v.create(x, y)
    v.subtract_from_xy(spring.position)  
    v.set_length(v.get_length()-seperate)     
    v.mul_to_xy(k)
    spring.velocity.add_to_xy(v)
    spring.drag_overall()
    
    print(spring.velocity.get_length(),spring.gravity.get_length())
    spring.update()
    p.display.flip()
    p.time.Clock().tick(25)