import math
import pygame as p
import vector_
import particle
p.init()

screen = p.display.set_mode((1080, 640))
screen.fill((0,0,0))
run=True

moonmass=50
earthmass=1985

earthx=500
earthy=300

moonx=800
moony=100

moon=p.Vector2(moonx, moony)
earth=p.Vector2(earthx,earthy)

while run:
    screen.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
    
    direction=earth-moon
    direction=direction
    d=math.sqrt((moonx-earthx)**2+(moony-earthy)**2)
    print(direction,"sdfsfsd")
    direction=direction.normalize()*1.5
    print(direction)
    force=moonmass*earthmass/(d*d)
    direction=direction*force
    moon+=direction
   
    p.draw.circle(screen, (123,123,123), ( int(earth[0]) , int(earth[1]) ), 30, 1)
    p.draw.circle(screen, (123,123,123), ( int(moon[0]) , int(moon[1]) ), 15, 1)
    p.display.flip()
    p.time.Clock().tick(30)
    