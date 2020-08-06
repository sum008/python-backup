import pygame as p

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

#----------------------Ground movement variables--------------------------------------------------
bx=50
velocity=0
acceleration=0.3
a=acceleration
friction=0.03
time=0.5
#----------------------Air movement variables--------------------------------------------------
groundy=0
gravity=3
g=gravity
air_resistance=0.01
jump_offset=20
vely=velocity
def disp(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))
    
count=0
run=True
while run:
    
    display.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
            
#---------------------Display Stats------------------------------------------------------------------------------------------
            
    disp("Position : "+str(int(bx%width))+" "+str(int(groundy%heigth)),(255,255,255),5,10)
    disp("Velocity : "+str(velocity)+" km/h",(255,255,255),5,40)
    disp("Acceleration : "+str(acceleration),(255,255,255),5,70)
    disp("Friction : "+str(friction),(255,255,255),5,110)
    disp("Air resistance : "+str(air_resistance),(255,255,255),5,140)
    disp("Gravity : "+str(gravity),(255,255,255),5,180)
    
#---------------Acceleration, velocity and deacceleration--------------------------------------------------------------------

    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and groundy>=500:
        acceleration=-a
        velocity+=acceleration*time
        vely=velocity
    if keys[p.K_RIGHT] and groundy>=500:
        acceleration=a
        velocity+=acceleration*time
        vely=velocity
#-----------------------Jump and gravity--------------------------------------------------------------------------------------

    if keys[p.K_SPACE] and groundy-jump_offset>=0 and count==0:
        
        vely=vely+time*gravity
        groundy=groundy+vely*time-jump_offset
#         print(jump_offset-gravity)
    else:
        if groundy<500:
            vely=vely+time*gravity
            groundy=groundy+vely*time
#             gravity+=gravity/(gravity+5)
#             print(groundy,gravity)   
        if groundy>=500:
            gravity=g
            groundy=500
            vely=0
#             print(gravity)  
        count=1
        
    if groundy>=500:
        count=0  
    
#---------------Velocity at ground in air(Inertia)----------------------------------------------------------------------------

    if round(velocity,4)!=0.00000:
        
        if velocity<0 and groundy>=500: #At ground-->friction and little air resistance
            velocity+=friction+air_resistance//2
            
        elif velocity>0 and groundy>=500:
            velocity-=friction-air_resistance//2
            
        elif groundy< 500 and velocity<0 : #In air--> air resistance
            velocity+=air_resistance
            
        elif groundy<500 and velocity>0 :
            velocity-=air_resistance
            
    elif velocity<=0.01: #Velocity is zero-->Stop now
        velocity=0
        acceleration=0
        
    print(vely)
    display.blit(platform,(0,550))
    display.blit(player_box,(bx,groundy))
    bx=(bx+velocity*time)%width #Directional movement negative or positive
    p.display.update()
    p.time.Clock().tick(100)    
        
        