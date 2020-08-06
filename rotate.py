import pygame as p
import math
p.init()

display=p.display.set_mode((400,400))
# point=p.Surface((50,50))
# point.set_colorkey((0,0,0))
# point.fill((255,255,255))
point=p.image.load("Spaceship (4).png")
run=True
angle=1
display.fill((0,0,0))

while run:
    display.fill((0,0,0))
    point_=p.transform.rotate(point, angle)
    getrect=point_.get_rect()
    print(getrect)
    getrect.center=(200,200)
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
#     p.draw.rect(display, (120,88,19), getrect, 1)
    display.blit(point_,getrect)
    
    
    keys=p.key.get_pressed()
            
    if keys[p.K_LEFT]:
        angle=(angle+1)%360
        
    if keys[p.K_RIGHT]:
        angle=(angle-1)%360
    
    p.display.flip()
    p.time.Clock().tick(120)
    
    