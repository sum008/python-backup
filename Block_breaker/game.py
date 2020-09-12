'''
Created on 29 Aug, 2020

@author: sumit
'''
import pygame as p
from paddle import paddle
from ball import ball
from random import randint

fps=50
p.init()
window=(600,600)
display=p.display.set_mode(window)
run=True

x=300
y=590

pd_speed=15
pd=paddle()
pd.create(x, y)

l=100
b=10
platform=p.image.load("tile/56-Breakout-Tiles.png")
platform=p.transform.scale(platform, (l,b))

r=10
length=10
a=randint(20,170)
angle=-0.0174533*a
bl=ball()
bl.create(x+l//2, y-r, length, angle)
start=False
angle_offset=1.4
bal=p.image.load("tile/58-Breakout-Tiles.png")
bal=p.transform.scale(bal, (15, 15))

tiles_={1:"tile/01-Breakout-Tiles.png",2:"tile/03-Breakout-Tiles.png",
        3:"tile/05-Breakout-Tiles.png",4:"tile/07-Breakout-Tiles.png",5:"tile/09-Breakout-Tiles.png",
        6:"tile/11-Breakout-Tiles.png",7:"tile/13-Breakout-Tiles.png",8:"tile/15-Breakout-Tiles.png",
        9:"tile/17-Breakout-Tiles.png"}

m=3
n=11
tiles=[[0 for i in range(n)] for j in range(m)] 
t_l=50
t_b=30

t_x=10
t_y=20
t_offset_x=t_l+2
t_offset_y=t_b+2


def draw_ball(radius,color):
    
    s=p.Surface((radius*2,radius*2))
    p.draw.circle(s, color, (radius,radius), radius)
    s.set_colorkey((0,0,0))
    return s

for j in range(0,m):
#     t_y=20
    for i in range(0,n):
        t=randint(1,8)
        t=p.image.load(tiles_[t])
        t=p.transform.scale(t, (t_l, t_b))
        tiles[j][i]=[t,(t_x,t_y)]
        t_x+=t_offset_x
#     print(t_y)
    t_y+=t_offset_y
    t_x=10
t_offset_x=t_l+2
t_offset_y=t_b+2
t_x=10
t_y=20

while run:
    
    display.fill((91,81,79))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    #-----------Update Paddle Position-----------------------------
    mouse=p.mouse.get_pos()
    keys=p.mouse.get_pressed()
    
    if keys[0]==1:
        start=True
    if mouse[0]>=0 and mouse[0]+l<=600:
        pd.x=mouse[0]
    
    if start==False:
        bl.x=pd.x+l//2
        bl.y=pd.y-r-10
    
    if start==True:
        bl.update()
        
    if bl.x+r>=600 and start==True:
        bl.x=600-r
        bl.angle=3.14-bl.angle
    if bl.x-r<=0 and start==True:
        bl.x=r
        bl.angle=3.14-bl.angle
    if bl.y-r<=0 and start==True:
        bl.y=r
        bl.angle=-bl.angle
#     if bl.y+r>=600 and start==True:
#         bl.y=600-r
#         bl.angle=-bl.angle
    if bl.y+r>=pd.y and bl.y-r<pd.y and bl.x+r>=pd.x and bl.x-r<=pd.x+l and start==True:
        bl.y=pd.y-r-10
        length=bl.x-pd.x
#         print("len",length)
        if length>l//2:
            if length>l:
                length=l
            ang=90-(length-l//2)*angle_offset
            bl.angle=-0.0174533*ang
        else:
            if length<0:
                length=0
            ang=90+(l//2-length)*angle_offset
            bl.angle=-0.0174533*ang
            
    #---------------------Tile work-----------------------------------------------
    
    index_y=int(bl.x//t_l)
    index_x=int(bl.y//t_b)
#     print(index)
    if bl.y-r<90:
#         print("row : ",index_x,"col : ",index_y)
        if index_x==m:
            index_x-=1
        if index_y==n:
            index_y-=1
#         if index_x!=0:
#             index_x-=1
#         if index_y!=0:
#             index_y-=1
            
#         print("row :",index_x,"column :",index_y)
        if bl.y-r-20<=tiles[index_x][index_y][1][1]+t_b and bl.x+r+20>=tiles[index_x][index_y][1][0] and bl.x-r-20<=tiles[index_x][index_y][1][0]+t_offset_x-2 and tiles[index_x][index_y][0]!="null":
            bl.y=tiles[index_x][index_y][1][1]+t_b+r
            bl.angle=-bl.angle
            tiles[index_x][index_y][0]="null"
            print("bottom")
            
        if bl.y+r+10>=tiles[index_x][index_y][1][1] and bl.x+r>=tiles[index_x][index_y][1][0] and bl.x-r<=tiles[index_x][index_y][1][0]+t_l and tiles[index_x][index_y][0]!="null":
            bl.y=tiles[index_x][index_y][1][1]-r
            bl.angle=-bl.angle
            tiles[index_x][index_y][0]="null"
            print("top")
            
        if bl.x+r>=tiles[index_x][index_y][1][0] and bl.y+r>=tiles[index_x][index_y][1][1] and bl.y-r<=tiles[index_x][index_y][1][1]+t_b and tiles[index_x][index_y][0]!="null":
            bl.x=tiles[index_x][index_y][1][0]-r
            bl.angle=3.14-bl.angle
            tiles[index_x][index_y][0]="null"
            print("left")
            
        if bl.x-r<=tiles[index_x][index_y][1][0]+t_l and bl.y+r>=tiles[index_x][index_y][1][1] and bl.y-r<=tiles[index_x][index_y][1][1]+t_b and tiles[index_x][index_y][0]!="null":
            bl.x=tiles[index_x][index_y][1][0]+t_offset_x-2+r
            bl.angle=3.14-bl.angle
            tiles[index_x][index_y][0]="null"
            print("right")
    
    #----------------Displaying---------------------------------------------------------------------
    
    for i in range(m):
        for j in range(n):
            if tiles[i][j][0]!="null":
                display.blit(tiles[i][j][0],tiles[i][j][1])
        
#     p.draw.circle(display, (0,0,0), bl.pos(), r, 1)
    display.blit(platform,pd.pos())
    display.blit(draw_ball(r, (190,190,190)),(bl.x,bl.y))
    display.blit(platform,(pd.x,pd.y))
    p.display.flip()
    p.time.Clock().tick(fps)
    