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

k=0.02
f=0.97
vel=50
m=0
g=0.5
#f=k*position
spring_pivot_point=[]
n=1
position=[]
for i in range(n):
    spring_pivot_point_=vector_.vector_functions()
    x=random.randint(10,width)
    y=random.randint(10,height)
    
    while [x,y] in position:
        x=random.randint(10,width)
        y=random.randint(10,height)
    position.append([x,y])
    spring_pivot_point_.create(x, y)
    spring_pivot_point.append(spring_pivot_point_)
    
spring_weight=particle.particle()
spring_weight.create(random.random()*width, random.random()*height, random.random()*math.pi*2, vel, m, g, f)

screen.fill((255,255,255))
seperate=100
while run:
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
            
    p.draw.circle(screen, (0,0,0), (int(spring_weight.getX()),int(spring_weight.getY())), 15, 15)
    for i in range(n):
        p.draw.circle(screen, (0,0,0), ( int(spring_pivot_point[i].getX()),int(spring_pivot_point[i].getY())), 3, 3)
    
    for i in range(n):
        p.draw.line(screen, (0,0,0), (spring_pivot_point[i].getX(),spring_pivot_point[i].getY()),(spring_weight.getX(),spring_weight.getY()), 1)
    
    click=p.mouse.get_pressed()
    if click[0]==1 :
        pos=p.mouse.get_pos()
        spring_weight.position.setX(pos[0])
        spring_weight.position.setY(pos[1])
    
    for i in range(n):
        
        x=spring_pivot_point[i].getX()
        y=spring_pivot_point[i].getY()
        v=vector_.vector_functions()
        v.create(x, y)
        v.subtract_from_xy(spring_weight.position)  
        v.set_length(v.get_length()-seperate)     
        v.mul_to_xy(k)
        spring_weight.velocity.add_to_xy(v)
        spring_weight.drag_overall()
        spring_weight.update()
        
    p.display.flip()
    p.time.Clock().tick(25)