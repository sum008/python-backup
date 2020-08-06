import pygame as p
import math
p.init()
width=900
height=600
display = p.display.set_mode((width,height))

w=50
h=10
# paddle=p.Surface((100,10))
# paddle.set_colorkey((255,255,255))
# paddle.fill((0,0,0))

angle=0.1
lis=[]
x=width//2
y=height//2
count=55
angle=0.1
for i in range(0,5):
    
    lis.append((x,y,angle))
    x+=count
run=True

display.fill((255,255,255))
while run:
    
#     display.fill((255,255,255))
#     paddle_=p.transform.rotate(paddle, angle)
#     getrect=paddle_.get_rect()
#    
#     getrect.center=(width/2,height/2)
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
#     print(paddle_.get_rect())        
#     display.blit(paddle_,getrect)
#     angle-=0.5
    for i in range(0,5):
        x=lis[i][0]
        y=lis[i][1]
        angle=lis[i][2]
        p.draw.circle(display, (0,0,0), (int(x),int(y)), 3, 3)
        if i>len(lis)//2:
#             x=lis[i][0]
#             y=lis[i][1]
#             angle=lis[i][2]
#             p.draw.circle(display, (0,0,0), (int(x),int(y)), 3, 3)
            x=x-math.sin(angle)
            y=y+math.cos(angle)
#             angle+=(180/10*(len(lis)-5%(i+1)))*0.0174533
            angle+=0.0174/(5-i)
#             angle+=0.1/(len(lis)+i+1)
            lis[i]=(x,y,angle)
             
        elif i<len(lis)//2:
#             x=lis[i][0]
#             y=lis[i][1]
#             angle=lis[i][2]
#             p.draw.circle(display, (0,0,0), (int(x),int(y)), 3, 3)
            x=x+math.sin(angle)
            y=y-math.cos(angle)
            angle+=(180/(len(lis)-(i+1)))*0.01745
#             angle+=0.1/(len(lis)+i)
            lis[i]=(x,y,angle)
            
            
    p.display.flip()
    p.time.Clock().tick(50)
            