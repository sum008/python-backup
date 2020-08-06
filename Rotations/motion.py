import pygame as p
import particle
import vector_
import math

p.init()
width=900
height=600
display = p.display.set_mode((width,height))
font=p.font.SysFont(None, 30)
print(math.atan2(10, 0))
#---------------------------------Platform creation-----------------------------------------------------

platform=p.Surface((width,100))
platform.fill((155,68,200))

#---------------------Player creation-------------------------------------------------------------------
player_box=p.Surface((50,50))
player_box.fill((255,255,255))

player_box1=p.Surface((50,50))
player_box1.fill((150,150,150))

platformx=0
platformy=500

x=200
y=450

fric_between_particles=0.3

particle_=particle.particle()
particle_.create(x, y, 50, 0, 10, 0, 0.90)

particle1=particle.particle()
particle1.create(x, 20, 50, 0, 10, 0.5, 0.90)

accelerateX=vector_.vector_functions()
accelerateX.create(0.5, 0)


jump_offset=-10
lastkey="null"
vel1=0

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


run=True
while run:
    
    display.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
        if event.type == p.KEYDOWN:
            if event.key==p.K_SPACE and particle_.getY()+50>=platformy:
                x=particle_.velocity.getX()
                y=jump_offset
                length=math.sqrt(x**2+y**2)
                angle=math.atan2(y, x)
                particle_.velocity.set_length(length)
                particle_.velocity.set_angle(angle)
                particle_.gravity.set_length(0.5)
                particle_.gravity.set_angle(math.pi/2)
                
    keys=p.key.get_pressed()
    if keys[p.K_RIGHT]:
        particle_.velocity.add_to_xy(accelerateX)
        lastkey="r"
    elif keys[p.K_LEFT] :
        particle_.velocity.subtract_from_xy(accelerateX)
        lastkey="l"
    else:
        particle_.drag_overall()  
        particle1.drag_overall()
        if abs(particle_.velocity.get_length())<0.3:
            particle_.velocity.set_length(0) 
        if abs(particle1.velocity.get_length())<0.3:
            particle1.velocity.set_length(0)
            
    if abs((particle1.getY()+50)-particle_.getY())<=10 and ((particle_.getX()>=particle1.getX() and particle_.getX()<=particle1.getX()+50) or (particle_.getX()+50<=particle1.getX()+50 and particle_.getX()+50>=particle1.getX())):
        
        if particle1.gravity.get_length()!=0:
            particle1.remove_gravity()
            particle1.velocity.setY(0)
            particle1.position.setY(particle_.getY()-50)
        else:
            if lastkey=="l":
                vel1=-fric_between_particles*particle_.velocity.get_length()
            elif lastkey=="r":
                vel1=fric_between_particles*particle_.velocity.get_length()

            particle1.velocity.setX(vel1)
#             particle1.velocity.set_angle(0)
#         print(particle1.getY()+50)       
    elif abs((particle1.getY()+50)-platformy)<=5 and particle1.gravity.get_length()!=0:
        particle1.remove_gravity()
        particle1.velocity.setY(0)
        particle1.position.setY(platformy-50)
    elif particle1.getY()+50<platformy :
        particle1.apply_gravity(1)
    
        
#     if not ((particle_.getX()>=particle1.getX() and particle_.getX()<=particle1.getX()+50) or (particle_.getX()+50<=particle1.getX()+50 and particle_.getX()+50>=particle1.getX())):
#         particle1.apply_gravity(1)
        
    if abs(particle1.getY()%height+50-platformy)<=5 and abs(particle_.getY()%height+50-platformy)<=5:
        if abs(particle_.getX()%width-(particle1.getX()%width+50))<=5 or abs((particle_.getX()%width+50)-particle1.getX()%width)<=5:
            print(particle1.mass)
            v=calculate_velocity(particle_.velocity, particle1.velocity, particle_.mass, particle1.mass)
            particle_.velocity.setX(v[0].getX())
            particle_.velocity.setY(v[0].getY())
             
            particle1.velocity.setX(v[1].getX())
#             particle1.velocity.setY(v[1].getY())
                
    
    display.blit(platform,(platformx,platformy))
    display.blit(player_box,(particle_.getX()%width,particle_.getY()%height))
    display.blit(player_box1,(particle1.getX()%width,particle1.getY()%height))
    particle_.update()
    particle1.update()
    p.display.update()

    if particle_.getY()+50 >= platformy:
        particle_.position.setY(platformy-50)
        particle_.remove_gravity()
    
    p.time.Clock().tick(100)