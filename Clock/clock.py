import math
import pygame
from datetime import datetime
import random
pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode((500, 500))
font=pygame.font.SysFont(None, 30)

FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
BLUE = pygame.Color("blue")
green=pygame.Color("green")
angle = 1.5708
done = False

offset=100

cx=250
cy=250
x1=cx
y1=cy-160

x2=cx
y2=cy-150

x3=cx
y3=cy-130
ax=cx
ay=cy-offset

bx=cx
by=cy+50

dx=cx
dy=cy+50
def rot(cx,cy,oldx,oldy,angle):
    
    x=cx+math.cos(angle)*(oldx-cx)-math.sin(angle)*(oldy-cy)
    y=cy+math.sin(angle)*(oldx-cx)+math.cos(angle)*(oldy-cy)
    return [x,y]

def disp(text,color,x,y):
    score=font.render(text,True,color)
    display.blit(score,(x,y))

display.fill((0,0,0))
color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
toggle=True
prev=1
second=1
count=1
hour_ang=0.00872665
while not done:
    
    display.fill((0,0,0))
    for i in range(1,61):
        r=rot(cx, cy, x1, y1-40, (6*(i)%360)*0.0174533)
        if i%5==0:
            pygame.draw.circle(display, color, (int(r[0]),int(r[1])), 5, 5)
        else:
            pygame.draw.circle(display, green, (int(r[0]),int(r[1])), 2, 2)
    
    prev=second
    time=datetime.now()
    second=time.second
    minute=time.minute
    hour=time.hour
    
    if prev!=second:
        pygame.mixer.music.load("Clock-sound-tick-tock.mp3")
        pygame.mixer.music.play()
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
        
    pygame.draw.circle(display, (123,123,123), (cx,cy), 220, 2)
    pygame.draw.circle(display, color, (cx,cy), 3, 3)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    angle_sec = second*6
    angle_min = minute*6
    angle_hour = hour*60*0.5+minute*(0.5)
    
    d=rot(cx, cy, x3, y3, (angle_hour%360)*0.0174533)
    pygame.draw.line(display, green, (cx,cy), (dx,dy), 7)
    dx=d[0]
    dy=d[1]
    
    b=rot(cx, cy, x2, y2, angle_min*0.0174533)
    pygame.draw.line(display, BLUE, (cx,cy), (bx,by), 5)
    bx=b[0]
    by=b[1]
    
    a=rot(cx, cy, x1, y1, angle_sec*0.0174533)
    pygame.draw.line(display, RED, (cx,cy), (ax,ay), 2)
    ax=a[0]
    ay=a[1]
    
    pygame.draw.circle(display, color, (cx,cy), 8,8)
    disp(str(hour)+" : "+str(minute)+" : "+str(second),color,200,200)
    pygame.display.flip()
    FPSCLOCK.tick(60)
