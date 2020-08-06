import random,math,pygame as p
p.init()
display=p.display.set_mode((400,400))
platform=p.Surface((400,100))
platform.fill((155,68,200))
cx=200
cy=20
h=20
color=(255,1,26)
size=15
count=0
velocity=3
gravity=0.1
air_resistance=0.1
run=True
x=200
y=200
angle=30
while run:
    
    display.fill((255,255,255))
    for event in p.event.get(eventtype=None):
        if event.type==p.QUIT:
            run=False 
    count+=1
    if cy<20:
        velocity*=-1
            
    if cy>300-2*size:
        velocity=(velocity*90)/100
        velocity*=-1
        
    if velocity>0:
        air_resistance=-0.1
    if velocity<0:
        air_resistance=0.1
    velocity+=gravity+air_resistance 
    display.blit(platform,(0,300))
    a=p.draw.circle(display, color, (int(cx),int(cy)), size, 15)
    p.display.update()
    cy+=velocity
#     print(velocity)
    p.time.Clock().tick(60)
        