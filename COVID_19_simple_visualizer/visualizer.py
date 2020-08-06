# xi=particle_array[i].velocity.getX()
#                     yi=particle_array[i].velocity.getY()
#                     xj=j.velocity.getX()
#                     yj=j.velocity.getY()
#                     particle_array[i].velocity.setX(xj)
#                     particle_array[i].velocity.setY(yj)
#                     j.velocity.setX(xi)
#                     j.velocity.setY(yi)

import pygame as p
import particle
import random
import vector_
import math

p.init()
def distance(x1,x2,y1,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    return math.sqrt(x**2+y**2)
width=840
height=650
screen = p.display.set_mode((width, height))
font=p.font.SysFont(None, 30)
offset=0.99
r=25
run=True
n=1
particle_array=[]
particle_color=[]
g=0
infected=0
remaining=0

x1=2*r
y1=2*r
for i in range(n):
    angle=random.random()*random.choice([1,-1,5,-5,10,-10,0])
    x=random.randint(2*r+10,width-2*r)
    y=random.randint(2*r+10,height-2*r)
#     t=True
#    
#     while t:
#         for j in range(0,len(particle_array)):
# #             print(distance(particle_array[j].getX(),x,particle_array[j].getY(),y),j)
#             if distance(particle_array[j].getX(),x,particle_array[j].getY(),y)<=300:
#                 x=random.randint(2*r+10,width-2*r)
#                 y=random.randint(2*r+10,height-2*r)
#                 print(j,"DFgd")
#                 continue
#         t=False
            
    mass=random.randint(2,12)
    speed=random.randint(3,10)
    particle_=particle.particle()
    
    particle_.create(x, y, angle, 0, mass , g , 0.99)
    particle_array.append(particle_)
    color=(0,0,0)
    particle_color.append(color)
    
    
#     color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     particle_color.append(color

def calculate_velocity(v11,v22,m1,m2): ## Will return magnitude of velocity in x and y direction
    
    v1x=((2*m2*v22.getX()) / (m1+m2)) + ((m1-m2)*v11.getX()) / (m1+m2)
    v1y=((2*m2*v22.getY()) / (m1+m2)) + ((m1-m2)*v11.getY()) / (m1+m2)
    
    v2x=((2*m1*v11.getX()) / (m1+m2)) + ((m2-m1)*v22.getX()) / (m1+m2)
    v2y=((2*m1*v11.getY()) / (m1+m2)) + ((m2-m1)*v22.getY()) / (m1+m2)
    
    v1=vector_.vector_functions()
    v1.create(v1x, v1y)
    
    v2=vector_.vector_functions()
    v2.create(v2x, v2y)
    return [v1,v2]

def calculate_wind(ball):
    acc=vector_.vector_functions()
    f=25
    a=f/ball.mass
    angle=-30
    
    acc.set_length(a)
    acc.set_angle(angle*(0.01745))
    return acc

def disp(text,color,x,y):
    text=font.render(text,True,color)
    screen.blit(text,(x,y))
    
count=0
run=True
while run:
    
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
            
    disp("Total Population : "+str(n),(0,0,0),5,10)
    disp("Infected Population : "+str(infected),(0,0,0),5,40)
    disp("Healthy Population : "+str(remaining),(0,0,0),5,70)
 
    for i in range(0,n):
        keys=p.key.get_pressed()
        if keys[p.K_SPACE] :
            force=calculate_wind(particle_array[i])
            particle_array[i].accelerate(force)
            disp("Wind Applied",(0,0,0),650,10)
        else:
            disp("No wind",(0,0,0),700,10)
        if keys[p.K_DOWN]:
            disp("Gravity Applied",(0,0,0),650,30)
            particle_array[i].apply_gravity(0.9)
        else:
            disp("No gravity",(0,0,0),700,30)
            particle_array[i].remove_gravity()
        p.draw.circle(screen, particle_color[i], ( int(particle_array[i].getX()) , int(particle_array[i].getY()) ), r, 1)
        particle_array[i].update()
        
        if particle_array[i].getY()+r>=height-5 : 
#             particle_array[i].position.setY(height-r)
            particle_array[i].velocity.set_angle(particle_array[i].velocity.get_angle()*-1)   
            
        if particle_array[i].getY()-r<=5:
#             particle_array[i].position.setY(r)
            particle_array[i].velocity.set_angle(particle_array[i].velocity.get_angle()*-1)   
            
        if particle_array[i].getX()-r<=5 : 
#             particle_array[i].position.setX(r)
            particle_array[i].velocity.setX((particle_array[i].velocity.getX())*-1)
            
            
        if particle_array[i].getX()+r>=width-5:
#             particle_array[i].position.setX(width-r-2)
            particle_array[i].velocity.setX((particle_array[i].velocity.getX())*-1)
            
            
        if n>1:
            for j in range(0,n):
                d=particle_array[i].distance(particle_array[j])
                if j!=i and d<2*r+15:
#                     ai=particle_array[i].velocity.get_angle()
#                     aj=j.velocity.get_angle()
#                     particle_array[i].velocity.set_angle(aj)
#                     j.velocity.set_angle(ai)
                    
                    a=calculate_velocity(particle_array[i].velocity , particle_array[j].velocity,particle_array[i].mass,particle_array[j].mass)
                        
                    particle_array[i].velocity.setY(a[0].getY())
                    particle_array[i].velocity.setX(a[0].getX())
                    
                    particle_array[j].velocity.setY(a[1].getY())
                    particle_array[j].velocity.setX(a[1].getX())
                    
                    if infected<=n and particle_color[j]==(0,0,0):
                        infected+=1
                        remaining=n-infected
                        particle_color[j]=(242,12,12)
                    elif infected<=n and particle_color[i]==(0,0,0):
                        infected+=1
                        remaining=n-infected
                        particle_color[i]=(242,12,12)
                    elif infected<=n and (particle_color[j]==(0,0,0) and particle_color[i]==(0,0,0)):
                        infected+=2
                        remaining=n-infected
                        particle_color[i]=(242,12,12)
                        particle_color[j]=(242,12,12)
                        
        if particle_array[i].getY()>height//2:          
            particle_array[i].drag_overall()               
                    
    p.display.flip()
    p.time.Clock().tick(60)
        
        
        
        
        
        
        
        
        
        
