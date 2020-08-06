import pygame as p
import math
p.init()
width=900
heigth=600
display = p.display.set_mode((width,heigth))
font=p.font.SysFont(None, 30)

#---------------------------------Platform creation-----------------------------------------------------

platform=p.Surface((width,100))
platform.fill((155,68,200))

#---------------------Player creation-------------------------------------------------------------------
player_box=p.Surface((50,50))
player_box.fill((255,255,255))
m1=10


#----------------------Ground movement variables--------------------------------------------------
bx=50
velocity1=0
acceleration1=0
friction=0.03   #0.03

#----------------------Air movement variables--------------------------------------------------
groundy=0
gravity=10
g=gravity
air_resistance=0.01  #0.01
jump_offset=20

count1=1

def disp(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))
    
 
# def calcl_vel(v1,v2,m1,m2):
#      
#     v=(m1/m2)*(v1+v2)
#     return v
c=0   
count=0
run=True
while run:
    
    display.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
            
#---------------------Display Stats------------------------------------------------------------------------------------------
            
    disp("Position (white box) : "+str(int(bx))+" "+str(int(groundy)),(255,255,255),5,10)
    disp("velocity1 : "+str(velocity1)+" km/h",(255,255,255),5,40)
    disp("acceleration1 : "+str(acceleration1),(255,255,255),5,70)
    disp("Friction : "+str(friction),(255,255,255),5,110)
    disp("Air resistance : "+str(air_resistance),(255,255,255),5,140)
    disp("Gravity : "+str(gravity),(255,255,255),5,180)
    disp("mass 1(White) : "+str(m1),(255,255,255),5,250)
    disp("Momentum 1(white) : "+str(m1*velocity1),(255,255,255),5,350)
#---------------acceleration1, velocity1 and deacceleration1--------------------------------------------------------------------

    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and groundy>=500:
        acceleration1=-0.1
        velocity1+=acceleration1
        c=-1
    if keys[p.K_RIGHT] and groundy>=500:
        acceleration1=0.1
        velocity1+=acceleration1
        c=1
#-----------------------Jump and gravity-----------------------------------------------------------------------------------------

    if keys[p.K_SPACE] and groundy-jump_offset>=0 and count==0:
        groundy=groundy-(jump_offset-gravity-air_resistance/groundy+0.00001)
#         print(jump_offset-gravity)
    else:
        if groundy<500:
            groundy=groundy+gravity-air_resistance
#             print(groundy,gravity)   
        if groundy>=500:
            gravity=g
            groundy=500
#             print(gravity)  
        count=1
        
    if groundy>=500:
        count=0  
    
#---------------velocity1 at ground in air(Inertia)----------------------------------------------------------------------------

    if round(velocity1,4)>0.00000:
        if velocity1>0 and groundy>=500:
            velocity1-=friction-air_resistance//2
            
            
        elif groundy< 500 and velocity1>0 :
            velocity1-=air_resistance
            
        if velocity1<=0.01: #velocity1 is zero-->Stop now
            velocity1=0
            acceleration1=0
            
            
        
    elif round(velocity1,4)<0.00000:
        if velocity1<0 and groundy>=500: #At ground-->friction and little air resistance
            velocity1+=friction+air_resistance//2
        elif groundy< 500 and velocity1<0 : #In air--> air resistance
            velocity1+=air_resistance
            
        if velocity1>=0.01: #velocity1 is zero-->Stop now
            velocity1=0
            acceleration1=0  
            
    if bx<=2:
        velocity1=-velocity1
    elif bx>=843:
        velocity1=-velocity1
    
                
    bx=bx+math.cos(c*(0.01745))*velocity1 #+math.sin(c*(0.01745))*velocity1
    print(velocity1,"bxbxbxbxbbxbxbbxb")
    display.blit(platform,(0,550))
    display.blit(player_box,(bx,groundy))
    
#     bx=(bx+velocity1)%width #Directional movement negative or positive
    
    p.display.update()
    p.time.Clock().tick(100)    
        
        