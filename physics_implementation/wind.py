import pygame as p
import particle
import vector_
p.init()

width=640
height=400
display=p.display.set_mode((width,height))

r=20
x=320
y=400-r

mass=20
direction=0
speed=0
gravity=0.1
dragOrFriction=0.99
ball=particle.particle()
ball.create(x, y, direction, speed, mass, gravity, dragOrFriction)

def calculate_wind(ball):
    acc=vector_.vector_functions()
    f=25
    a=f/ball.mass
    angle=-20
    
    acc.set_length(a)
    acc.set_angle(angle*(0.01745))
    return acc
toggle=0
run=True
while run:
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
            
    p.draw.circle(display, (0,0,0), (int(ball.getX())%width,int(ball.getY())%height), r, r)
    
    keys=p.key.get_pressed()
    if keys[p.K_SPACE] :
        f=calculate_wind(ball)
        ball.accelerate(f)
        toggle=1
        
    if (ball.getY()%height)+r>=height:
        print("dssds")
        if ball.gravity!=0:
            ball.remove_gravity()
            toggle=0
            ball.position.setY(height-r)
    if toggle==1:
        ball.apply_gravity(gravity)
    print((ball.getY()%height)+r)
    ball.update()
    ball.drag_overall()
    p.display.update()
    p.time.Clock().tick(100)
        
        
        