'''
Created on 7 Sep, 2020

@author: sumit
'''

import pygame as p
import ball
import math
import time
import threading

fps=150
p.init()
window=(600,600)
display=p.display.set_mode(window)
run=True

particles=[]
n=30
x=300
y=300
length=5
radius=6
mass=2
g=0.4
f=0.95
w=0.5

for i in range(n):
    particle=ball.ball()
    particle.create(x,y,x,y,mass,g,f,w)
    particles.append(particle)
    y+=length
    
particles[0].pinned=True

def reposition(particles,count):
    
    for _ in range(count):
        for i in range(0,n-1):
            dx=particles[i].x-particles[i+1].x
            dy=particles[i].y-particles[i+1].y
            
            l=math.sqrt(dx**2+dy**2)
            d=l-length
    #         print(d)
            if l!=0:
                percent=d/l*2.5
                offsetx=dx*percent*0.5
                offsety=dy*percent*0.5
                m=particles[i].mass+particles[i+1].mass
                m1=particles[i].mass/m
                m2=particles[i+1].mass/m
                
                if particles[i].pinned==False:
                    
                    particles[i].x-=offsetx*m1
                    particles[i].y-=offsety*m1
                    
                    particles[i+1].x+=offsetx*m2
                    particles[i+1].y+=offsety*m2
                else:
                    particles[i+1].x+=offsetx*m2
                    particles[i+1].y+=offsety*m2
            
prev=int(time.clock())
count=0
while run:
    
    count+=1
    cl=int(time.clock())
    
    if prev!=cl:
        print("FPS : "+ str(count//abs(prev-cl)))
        count=0
        prev=int(time.clock())
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            
    for i in range(0,n-1):
        p.draw.line(display, (0,0,0), (int(particles[i].x),int(particles[i].y)), (int(particles[i+1].x),int(particles[i+1].y)),1)
        
    
#     keys=p.mouse.get_pressed()
#     if keys[0]==1:
    mouse=p.mouse.get_pos()
    particles[0].x=mouse[0]
    particles[0].y=mouse[1]
#         particles[0].pinned=True
#     else:
#         particles[0].pinned=False
            
    for particle in particles:
        
        if particle.pinned==False:
            vx=particle.get_x()-particle.get_ox()
            vy=particle.get_y()-particle.get_oy()
#             print(vx,vy)
            particle.set_ox(particle.get_x())
            particle.set_oy(particle.get_y())
              
            particle.set_x(particle.get_x()+vx)
            particle.set_y(particle.get_y()+vy)
#             particle.apply_friction()
            particle.apply_g()
            
#     t1=threading.Thread(target=reposition,args=(particles,150))
#     for _ in range(50):
#     t1.start()
    reposition(particles,150)
        
    p.display.flip()
    p.time.Clock().tick(fps)
    