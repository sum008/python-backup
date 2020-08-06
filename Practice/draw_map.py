import pygame as p

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
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
     [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],]#12x11

row=11
col=18
display=p.display.set_mode((tile_height*col,tile_width*row))

run=True
while run:
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
            
    for r in range(row):
        for c in range(col):
            
            p.draw.rect(display, tile_color[map_[r][c]]  , (c*tile_height,r*tile_width,tile_width,tile_height),0)
    
            
    p.display.flip()
    p.time.Clock().tick(60)
