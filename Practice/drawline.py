import sys, pygame
from pygame.locals import*
from pygame import gfxdraw
from random import randint
width=400
height=400
Color_screen=(49,150,100)

x=200
y=50
a=200
b=50
count=0
def main():
    global x,y,a,b,count
    Color_line=(255,0,0)
    screen=pygame.display.set_mode((width,height))
    
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)
#         screen.fill(Color_screen)
        gfxdraw.pixel(screen, x, y, Color_line)
        
        pygame.display.flip()
        if y!=b and count==0:
            x+=1
            y+=1
        elif count==1 and x==a:
            count=2
            x-=1
            y+=1
        elif count==1 and x!=a:
            y+=1
            x-=1
        elif y==b and count==0:
            count=1
        elif count==2:
            
            if y==b:
                count=3
                x+=1
                y-=1
            else:
                x-=1
                y-=1  
        elif count==3 and x!=a:
            x+=1
            y-=1
            
            if x==a:
                count=0
                #x+=5
                y-=1  
                Color_line=(randint(0,255),randint(0,255),randint(0,255))
        pygame.time.Clock().tick(20000)
        
main()