import math
import pygame as p
import particle
import random
import vector_
p.init()

width=640
height=400
screen = p.display.set_mode((width, height))

offset=0.99
r=25
run=True
n=5
particle_array=[]
particle_color=[]
g=0.3
for i in range(n):
    angle=random.random()*random.choice([1,-1,5,-5,10,-10,0])
    x=random.randint(10,width-10)
    y=random.randint(10,height-10)
    mass=random.randint(3,12)
    speed=random.randint(3,10)
    particle_=particle.particle()
    
    particle_.create(x, y, angle, speed, mass , g , 0.999)
    particle_array.append(particle_)
    
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    particle_color.append(color)
    
    
def calculate_velocity(v11,v22,m1,m2):
    
    v1x=((2*m2*v22.getX()) / (m1+m2)) + ((m1-m2)*v11.getX()) / (m1+m2)
    v1y=((2*m2*v22.getY()) / (m1+m2)) + ((m1-m2)*v11.getY()) / (m1+m2)
    
    v2x=((2*m1*v11.getX()) / (m1+m2)) + ((m2-m1)*v22.getX()) / (m1+m2)
    v2y=((2*m1*v11.getY()) / (m1+m2)) + ((m2-m1)*v22.getY()) / (m1+m2)
    
    v1=vector_.vector_functions()
    v1.create(v1x, v1y)
    
    v2=vector_.vector_functions()
    v2.create(v2x, v2y)
    return [v1,v2]    
    
while run:
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
    for i in range(0,n):
        
        p.draw.circle(screen, particle_color[i], ( int(particle_array[i].getX()) , int(particle_array[i].getY()) ), r, r)
        particle_array[i].update()
    
        if particle_array[i].getX()+r>=width:
            particle_array[i].velocity.setX(particle_array[i].velocity.getX()*-offset)
            particle_array[i].position.setX(width-r)
            
            
        if particle_array[i].getX()-r<=0:
            particle_array[i].velocity.setX(particle_array[i].velocity.getX()*-offset)
            particle_array[i].position.setX(r)
            
            
        if particle_array[i].getY()-r<=0:
            particle_array[i].velocity.setY(particle_array[i].velocity.getY()*-offset)
            particle_array[i].position.setY(r)
            
            
        if particle_array[i].getY()+r>=height and particle_array[i].gravity.get_length()!=0:
            
            particle_array[i].velocity.setY(particle_array[i].velocity.getY()*(-offset))
            particle_array[i].position.setY(height-r)
            
            if abs(particle_array[i].velocity.get_length())<=0.7 and particle_array[i].getY()+r>=width:
                
                particle_array[i].velocity.setY(0)
                particle_array[i].position.setY(height-r)
                particle_array[i].remove_gravity()
            else:
                particle_array[i].apply_gravity(g)
                
        if particle_array[i].getY()+r>=height and particle_array[i].drag.get_length()!=0:
            particle_array[i].drag_overall()
            if abs(particle_array[i].velocity.getX())<=0.1:
                
                particle_array[i].velocity.setX(0)
                particle_array[i].drag.set_length(0)
                
        if particle_array[i].velocity.get_length() > particle_array[i].drag.get_length() and particle_array[i].gravity.get_length()!=0:
            particle_array[i].drag_overall()
        else:
            particle_array[i].velocity.setY(0)
        if n>1:
            for j  in range(0,n):
                if j!=i:
                    d=particle_array[i].distance(particle_array[j])
                    if d<=2*r+1:
                        a=calculate_velocity(particle_array[i].velocity , particle_array[j].velocity,particle_array[i].mass,particle_array[j].mass)
                        
#                         x=particle_array[i].velocity.getX()
#                         y=particle_array[i].velocity.getY()
#                           
#                         x1=particle_array[j].velocity.getX()
#                         y1=particle_array[j].velocity.getY()
#                         a=vector_.vector_functions()
#                         a.create(x, y)
#                         b=vector_.vector_functions()
#                         b.create(x1, y1)
#                         particle_array[j].velocity.update_position(a)
#                         particle_array[i].velocity.update_position(b)
                        
                        
                        particle_array[i].velocity.setY(a[0].getY())
                        particle_array[i].velocity.setX(a[0].getX())
                        
                        particle_array[j].velocity.setY(a[1].getY())
                        particle_array[j].velocity.setX(a[1].getX())
        if abs(particle_array[i].velocity.getY())>0.7 and particle_array[i].gravity.get_length()==0:
                particle_array[i].apply_gravity(g)
#                 particle_array[i].gravity.set_angle(math.pi/2)
                
    p.display.flip()
    p.time.Clock().tick(80)