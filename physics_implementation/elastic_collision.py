import pygame as p

p.init()
p.mixer.init()
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
m1=100

#---------------------------------------------------------------------------------------------------------

object2=p.Surface((50,50))
object2.fill((219,55,89))

ox=50
oy=500
m2=1
velocity2=0
acceleration2=0

#----------------------Ground movement variables--------------------------------------------------
bx=150
velocity1=0
acceleration1=0.5
a=0.5
friction=0   #0.03

#----------------------Air movement variables--------------------------------------------------
groundy=0
gravity=3
g=gravity
air_resistance=0 #0.01
jump_offset=20
vely=0
time=0.5
count1=0
collisions=0
def disp(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))
    
    
    
def calculate_velocity(v11,v22,m1,m2):
    
#     v2=(m1/m2)*v1
#     return v2
    v1=((2*m2*v22)/(m1+m2))+((m1-m2)*v11)/(m1+m2)
    
    v2=((2*m1*v11)/(m1+m2))+((m2-m1)*v22)/(m1+m2)
    
    return [v1,v2]
 
# def calcl_vel(v1,v2,m1,m2):
#      
#     v=(m1/m2)*(v1+v2)
#     return v
    
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
    disp("velocity2 : "+str(velocity2)+" km/h",(255,255,255),5,210)
    disp("mass 1(White) : "+str(m1),(255,255,255),5,250)
    disp("mass 2(pink) : "+str(m2),(255,255,255),5,300)
    disp("Momentum 1(white) : "+str(m1*velocity1),(255,255,255),5,350)
    disp("Momentum 2(pink) : "+str(m2*velocity2),(255,255,255),5,400)
    disp("Position (pink box) : "+str(int(ox))+" "+str(int(oy)),(255,255,255),600,10)
#---------------acceleration1, velocity1 and deacceleration1--------------------------------------------------------------------

    keys=p.key.get_pressed()
    if keys[p.K_LEFT] and groundy>=500:
        print(acceleration1)
        acceleration1=-a
        print(acceleration1,time)
        velocity1+=acceleration1*time
        vely=velocity1
    if keys[p.K_RIGHT] and groundy>=500:
        print(acceleration1)
        acceleration1=a
        velocity1=velocity1+acceleration1*time
        vely=velocity1
    
#-----------------------Jump and gravity-----------------------------------------------------------------------------------------

    if keys[p.K_SPACE] and groundy-jump_offset>=0 and count==0:
        groundy=groundy-(jump_offset-gravity-air_resistance/groundy+0.00001)
#         print(jump_offset-gravity)
    else:
        if groundy<500:
            vely=vely+gravity*time
            groundy=groundy+vely*time-air_resistance
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
            
    if bx<=5:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        velocity1=-velocity1
        collisions+=1
    elif bx>=845:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        velocity1=-velocity1
        collisions+=1
    
    if ox<=5:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        velocity2=-velocity2
        collisions+=1
    elif ox>=845:
        collisions+=1
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        velocity2=-velocity2  
        
    if abs(int(bx+50)-int(ox))<=7  and groundy==oy:# and  velocity1!=0 and velocity2==0:
        p.mixer.music.load("click.mp3")
        p.mixer.music.play()
        collisions+=1
        a=calculate_velocity(velocity1,velocity2, m1, m2)
        velocity1=a[0]
        velocity2=a[1]
        
    elif abs(int(bx)-int(ox+50))<=7  and groundy==oy: #and  velocity1!=0 and velocity2==0:
        p.mixer.music.load("click.mp3")
        collisions+=1
        p.mixer.music.play()
        a=calculate_velocity(velocity1,velocity2, m1, m2)
        velocity1=a[0]
        velocity2=a[1]
                
    if velocity2>0:
            
        if (velocity2-friction-air_resistance//2)>0 :
            velocity2-=(friction-air_resistance//2)
#             print("vel2",velocity2)
            
#         elif oy<500 and velocity2>0 :
#             velocity2-=air_resistance
            
        if velocity2<=0.1: #velocity1 is zero-->Stop now
            velocity2=0

            acceleration2=0   
            
    elif velocity2<0:
        if velocity2<0 and oy>=500: #At ground-->friction and little air resistance
            velocity2+=(friction+air_resistance//2)
#         elif oy< 500 and velocity2<0 : #In air--> air resistance
#             velocity2+=air_resistance
            
        if velocity2>=0.01: #velocity1 is zero-->Stop now
            velocity2=0
            acceleration2=0    
    
#     print(velocity1,velocity2,"bxbxbxbxbbxbxbbxb")
    display.blit(platform,(0,550))
    display.blit(player_box,(bx,groundy))
    display.blit(object2,(ox,oy))
    
    bx=(bx+velocity1*time)%width #Directional movement negative or positive
    ox=(ox+velocity2*time)%width
    
    if abs((ox-25)-(bx-25))<=5 :
        ox-=100
    print(collisions)
    p.display.update()
    p.time.Clock().tick(100)    
        
        