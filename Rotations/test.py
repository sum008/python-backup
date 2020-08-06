import pygame as p
import vector_
import random
import math
p.init()
width=600
height=600
display=p.display.set_mode((width,height))

run=True
angle=0
print(math.atan2(10,0))
display.fill((0,0,0))

# velocity=vector_.vector_functions()

x=width/2
y=height/2

# velocity.create(0, 0)
# velocity.set_length(3) #magnitude
# velocity.set_angle(1.5708) #1.5708 radians or 90 degree = y-axis , 0 degree or radians = x-axis
                       
# print(velocity.getX(), velocity.getY(), velocity.get_length() ,velocity.get_angle())
accelerate=vector_.vector_functions()
accelerate.create(0, 0)
a=[]
b=[]
c=[]

r=100
g=0.5
h=0.5
for i in range(r):
    
    position=vector_.vector_functions()
    position.create(x, y)
    a.append(position)
    
    velocity=vector_.vector_functions()
    velocity.set_length(random.randint(1,5))
    velocity.set_angle(random.random()*random.choice([-1,1,5,-5,10,-10]))
    b.append(velocity)
    
    point=p.Surface((g,h))
    g+=0.5
    h+=0.5
    point.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    c.append(point)
    
    
print(math.atan2(0, 3))
while run:
#     display.fill((0,0,0))
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            
    for i in range(r):
        display.blit(c[i],(a[i].getX() , a[i].getY()))
    
        a[i].add_to_xy(b[i])
        
        b[i].add_to_xy(accelerate)
    
        a[i].create(a[i].getX()%width , a[i].getY()%height)
    
#     print(position.getX() , position.getY(),position.get_length(),position.get_angle())
    
    p.display.flip()
    p.time.Clock().tick(30)
    
    