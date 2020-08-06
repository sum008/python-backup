import pygame as p
import math
p.init()

display=p.display.set_mode((1080,400))
point=p.Surface((50,50))
point.fill((205,25,111))

bullet=p.Surface((2,2))
bullet.fill((42,193,198))
px=500
py=350

wallhit=False
groundhit=False

cx=px
cy=py
drag=0
x=cx+50
y=cy
angle=0
bx=x
by=y
count=0
velocity=0
gravity=0
time=0
air_res=0
curangle=0
vx=0
vy=0
q=0.1
run=True
display.fill((0,0,0))
while run:
#     display.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
            
            
    keys=p.key.get_pressed()
              
    if keys[p.K_LEFT]:
        display.fill((0,0,0))
        angle=(angle-1)%360
        x=cx+math.cos(angle*(0.01745))*(x-cx)-math.sin(angle*(0.01745))*(y-cy)
        y=cy+math.sin(angle*(0.01745))*(x-cx)+math.cos(angle*(0.01745))*(y-cy)
        bx=x
        by=y
        velocity=0
        gravity=0
        time=0
        air_res=0
        drag=0
        vx=0
        count=0
        vy=0
        pe=400-50-y
        b=x-500
        curangle=math.atan2(pe, b)
        q=0.1
        vx=velocity*math.cos(curangle)
        vy=velocity*math.sin(curangle)
    if keys[p.K_RIGHT]:
        display.fill((0,0,0))
        angle=(angle+1)%360
        x=cx+math.cos(angle*(0.01745))*(x-cx)-math.sin(angle*(0.01745))*(y-cy)
        y=cy+math.sin(angle*(0.01745))*(x-cx)+math.cos(angle*(0.01745))*(y-cy)
        bx=x
        by=y
        velocity=0
        gravity=0
        time=0
        air_res=0
        drag=0
        vx=0
        vy=0
        pe=400-50-y
        b=x-500
        count=0
        curangle=math.atan2(pe, b)
        vx=velocity*math.cos(curangle)
        vy=velocity*math.sin(curangle)

        
    if keys[p.K_SPACE]:
        wallhit=False
        groundhit=False
        velocity=4.5
        gravity=9.8
        time=0.1
        drag=0.1
        air_res=0.5
        vx=0
        vy=0
        pe=400-50-y
        b=x-500
        curangle=math.atan2(pe, b)
        
        vx=velocity*math.cos(curangle)-0.1
        vy=velocity*math.sin(curangle)+drag
    
    bx=bx+vx*time
    by=by-vy*time+((gravity*time*time)/2)
    time+=0.01
#     count=0
    
    if by>=395 and count==0:
        
        time=0.1
        velocity=velocity*0.9
        if wallhit==True:
            if vx<0:
                vx=-velocity*math.cos(curangle)
            elif velocity*math.cos(curangle) < 0 :
                vx=velocity*math.cos(math.pi-curangle)
    
        else:
            vx=velocity*math.cos(curangle)
            
#         vx=velocity*math.cos(curangle)
        vy=velocity*math.sin(curangle)
        count=1
        
    if by<395:
        count=0   
    if bx>=1050 and count==0:
        wallhit=True
        time=0.1
        velocity=velocity*0.9
        vx=velocity*math.cos(math.pi-curangle)
        vy=velocity*math.sin(0)
        count=1
    elif abs(bx)<=10 and count==0:
        wallhit=True
        time=0.1
        velocity=velocity*0.9
#         curangle=math.pi-curangle
        vx=velocity*math.cos(math.pi-curangle)
        vy=velocity*math.sin(0)
        count=1
        
        
    print(vx,"      ", curangle)
    display.blit(point,(px,py))
    display.blit(bullet,(bx,by))
    
    p.draw.line(display, (203,25,14), (cx,cy), (x,y), 4)
    p.display.flip()
    angle=0
    p.time.Clock().tick(120)
    
    