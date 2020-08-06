import math
import pygame as p
import vector_
import particle
p.init()

width=600
height=600
screen = p.display.set_mode((width, height))

fixed_point=(300,100)

ball=vector_.vector_functions()
ball.create(300, 300)

g=1
m=60
force=0
velocity=0
force=1
angle=1
direction=vector_.vector_functions()
velocity=vector_.vector_functions()
velocity.create(0, 0)
run=True
while run:
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
        
    p.draw.circle(screen, (0,0,0), fixed_point, 3, 3)
    
    p.draw.circle(screen, (0,0,0), (int(ball.getX()),int(ball.getY())), 15, 15)
    
    p.draw.line(screen, (0,0,0), fixed_point,(ball.getX(),ball.getY()), 1)
    click=p.mouse.get_pressed()        
    
    if click[0]==1:
        mouse=p.mouse.get_pos()
        ball.setX(mouse[0])
        ball.setY(mouse[1])
    x=fixed_point[0]
    y=fixed_point[1]
    
    direction.create(x, y)
    lenght=ball.distance(direction)
    print(lenght)
    if lenght<30:
        velocity.setY(velocity.getY()+g)
    
    direction.subtract_from_xy(ball)
    r=direction.normalize()
#     print(r)
#     direction.set_length(direction.get_length()-100)
    direction.mul_to_xy(force)
    velocity.add_to_xy(direction)
    ball.add_to_xy(velocity)
#     print(x,y)
#     ball.setX(ball.getX())
#     ball.setY(ball.getY())
#     angle+=1
    p.display.flip()
    p.time.Clock().tick(30)
    
    