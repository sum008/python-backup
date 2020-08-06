import pygame as p
import vector_
import particle
import math

p.init()

green=(50, 168, 82)
blue=(79, 179, 196)
brown=(97, 81, 41)

tile_color={1:green,
            2:blue,
            3:brown}

tile_width=30
tile_height=30



map_=[[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,3],
     [3,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]#12x11

row=11
col=18
display=p.display.set_mode((tile_height*col,tile_width*row))

# player_=p.Surface((20,20))
# player_.set_colorkey((255,255,255))
# player_.fill((0,0,0))

player_=p.image.load("player.png")
player_=p.transform.scale(player_, (50, 50))

player=vector_.vector_functions()
player.create(50,50)

player_velocity=vector_.vector_functions()
player_velocity.set_length(1.5)
player_velocity.set_angle(0.0174)

angle=0
player1=p.transform.rotate(player_, -90)

bullet1=p.Surface((2,2))
bullet1.fill((255,255,255)) 

list_bullet=[]

run=True
while run:
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            
    for r in range(row):
        for c in range(col):
            
            p.draw.rect(display, tile_color[map_[r][c]]  , (c*tile_width,r*tile_height,tile_width,tile_height),0)

            
    player1=p.transform.rotate(player_, angle)
    getrect=player1.get_rect()
    getrect.center=(player.getX(),player.getY())
            
    keys=p.key.get_pressed()
           
    if keys[p.K_LEFT]:
        angle=(angle+3)%360
        
    if keys[p.K_RIGHT]:
        angle=(angle-3)%360
        
    if keys[p.K_UP]:
        player_velocity.set_angle(-(angle)*0.01745)
        player.add_to_xy(player_velocity)
        
    if keys[p.K_DOWN]:
        player_velocity.set_angle(-(angle)*0.01745)
        player.subtract_from_xy(player_velocity)
        
    if keys[p.K_SPACE]:    
        bullet=particle.particle()
        bullet.create(player.getX() , player.getY(), -(angle)*0.01745, player_velocity.get_length()*2+6, 0, 0, 0)
        list_bullet.append(bullet)
                
    for cur_bullet in list_bullet:
        
        if cur_bullet.getX()>tile_height*col or cur_bullet.getX()<0 or cur_bullet.getY()>tile_width*row or cur_bullet.getY()<0:
            list_bullet.remove(cur_bullet)
                      
        display.blit(bullet1,(cur_bullet.getX(),cur_bullet.getY()))
        cur_bullet.update()
        
        
#     print(len(list_bullet),math.sin(-(angle)*0.01745))    
    display.blit(player1,getrect)
    
            
    p.display.flip()
    p.time.Clock().tick(60)
