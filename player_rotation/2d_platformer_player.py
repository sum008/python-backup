import pygame as p
import particle
import vector_
import math

p.init()

class platform:
    
    def __init__(self,width,height,x,y):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    def create(self):
        platform_=p.Surface((self.width,self.height))
        platform_.fill((0,0,0))
        return platform_
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y


width=900

green=(50, 168, 82)
blue=(79, 179, 196)
brown=(97, 81, 41)

tile_color={1:green,
            2:blue,
            3:brown}

tile_width=20
tile_height=20



map_=[[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]#12x11

row=11
col=18
display=p.display.set_mode((tile_width*col,tile_height*row))



font=p.font.SysFont(None, 30)
#---------------------------------Platform creation-----------------------------------------------------

# platform=p.Surface((width,100))
# platform.fill((155,68,200))

#---------------------Player creation-------------------------------------------------------------------
player_box=p.Surface((10,10))
player_box.fill((255,255,255))

x=100
y=(row-1)*tile_height-10

player=particle.particle()
player.create(x, y, 0, 0, 0, 0.7, 0.9)

accelerateX=vector_.vector_functions()
accelerateX.create(0.4, 0)

platform_list=[]



platform_=platform(50,10,150,130)
plat=platform_.create()
platform_list.append([platform_,plat])

platform_=platform(50,10,100,150)
plat=platform_.create()
platform_list.append([platform_,plat])

platform_=platform(50,10,200,100)
plat=platform_.create()
platform_list.append([platform_,plat])

platform_=platform(50,10,300,100)
plat=platform_.create()
platform_list.append([platform_,plat])

jump_offset=-15
lastkey="null"
current=None
run=True
hit_=False
def hit(player,platform):
    
    if (player.position.getX()>=platform.getX()) and (player.position.getX()<=platform.getX()+platform.width) and abs((player.position.getY()+10)-platform.getY())<=3:
        return True
    elif (player.position.getX()+10>=platform.getX()) and (player.position.getX()+10<=platform.getX()+platform.width) and abs((player.position.getY()+10)-platform.getY())<=3:
        return True
    else:
        return False

while run:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            run=False
        if event.type == p.KEYDOWN:
            if event.key==p.K_SPACE and player.gravity.get_length()==0:
                x_=player.velocity.getX()
                y_=jump_offset
                length=math.sqrt(x_**2+y_**2)
                angle=math.atan2(y_, x_)
                player.velocity.set_length(length)
                player.velocity.set_angle(angle)
                player.apply_gravity(0.7)
                print("sdfsd")
    keys=p.key.get_pressed()
    if keys[p.K_RIGHT]:
        player.accelerate(accelerateX)
    elif keys[p.K_LEFT] :
        player.deaccelerate(accelerateX)
         
#     else:  
#         if abs(player.velocity.get_length())<0.1:
#             player.velocity.set_length(0) 
            
    player.drag_overall()
    player.update()
    for r in range(row):
        for c in range(col):
            
            p.draw.rect(display, tile_color[map_[r][c]]  , (c*tile_width,r*tile_height,tile_width,tile_height),0)
    
    for i in platform_list:        
        
        hit_=hit(player,i[0])
        if hit_==True:
            current=i[0]
        display.blit(i[1],(i[0].getX(),i[0].getY()))
        
#         print(player.getX(),(i[0].getX()+i[0].width))
        if hit_  and  player.velocity.get_length()!=0 and player.gravity.get_length()!=0 :
#             print(player.getX(),i[0].getX()+i[0].width)
#             print(player.getX(),(i[0].getX()+i[0].width),"fgdfgdfgd")
            player.velocity.set_length(0)
            player.remove_gravity()
            player.position.setY(current.getY()-10)
            
        if current !=None and player.gravity.get_length()==0 and (player.position.getX()+10)<current.getX() and (player.position.getY()+10<current.getY() or abs(player.position.getY()+10-current.getY())<=3):
#             print("jhj")
            player.apply_gravity(0.7)
        elif current!=None and player.gravity.get_length()==0 and player.position.getX()>(current.getX()+current.width) and (player.position.getY()+10<current.getY() or abs(player.position.getY()+10-current.getY())<=3):
#             print("22")
            player.apply_gravity(0.7)
    
    display.blit(player_box,(player.getX(),player.getY()))
    
    p.display.update()
    
    if player.getY()+10 >= (row-1)*tile_height and player.velocity.get_length()!=0 and player.gravity.get_length()!=0:
        player.velocity.set_length(0)
        player.remove_gravity()
        player.position.setY((row-1)*tile_height-10)
        print("hhhh")
    
    p.time.Clock().tick(100)