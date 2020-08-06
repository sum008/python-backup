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

k=0.05
f=0.989
vel=0.9
m=0
g=0.5
seperate=100
n=3
#f=k*position
particle_array=[]
for i in range(n):
    particle_=particle.particle()
    particle_.create(random.randint(0,width), random.randint(0,height), random.random()*math.pi*2, vel, m, g, f)
    particle_array.append(particle_)

screen.fill((255,255,255))

count=n

def particle_creat(springA,springB,seperate):
    
    x=springA.getX()
    y=springA.getY()
    
    v=vector_.vector_functions()
    v.create(x, y)
    v.subtract_from_xy(springB.position)  
    v.set_length(v.get_length()-seperate)     
    v.mul_to_xy(k)
    springB.velocity.add_to_xy(v)
    springA.velocity.subtract_from_xy(v)
    
    springA.drag_overall()
    springB.drag_overall()
last=0
while run:
    screen.fill((255,255,255))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
    for i in range(n):        
        p.draw.circle(screen, (0,0,0), (int(particle_array[i].getX()),int(particle_array[i].getY())), 15, 15)
        
    
    for i in range(n):
        j=(i+1)%n   
        p.draw.line(screen, (0,0,0), (particle_array[i].getX(), particle_array[i].getY()),(particle_array[j].getX(),particle_array[j].getY()), 1)
    
    for i in range(n):
        j=(i+1)%n
        particle_creat(particle_array[i], particle_array[j], seperate)
    
    for i in range(n):
        click=p.mouse.get_pressed()
        if click[0]==1 :
        
            pos=p.mouse.get_pos()
            particle_array[i].position.setX(pos[0])
            particle_array[i].position.setY(pos[1])
            
    for i in range(n):
        particle_array[i].update()
    
    
    for i in range(n):
        j=(i+1)%n
        if particle_array[i].getY()+15>=height and particle_array[j].getY()+15>=height:
            print("ggh")
            particle_array[i].position.setY(height-15)
            particle_array[j].position.setY(height-15)
            particle_array[(j+1)%n].gravity.set_length(0)
    for i in range(n):    
        
        if particle_array[i].getX()+15>=width:
            particle_array[i].velocity.setX(particle_array[i].velocity.getX()*-1)
            particle_array[i].position.setX(width-15)
                
                
        if particle_array[i].getX()-15<=0:
            particle_array[i].velocity.setX(particle_array[i].velocity.getX()*-1)
            particle_array[i].position.setX(15)
            
            
        if particle_array[i].getY()-15<=0:
            particle_array[i].velocity.setY(particle_array[i].velocity.getY()*-1)
            particle_array[i].position.setY(15)
            
            
        if particle_array[i].getY()+15>=height:
            
            particle_array[i].velocity.setY(particle_array[i].velocity.getY()*(-1))
            particle_array[i].position.setY(height-15)    
        
    
    p.display.flip()
    p.time.Clock().tick(25)