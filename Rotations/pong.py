import pygame as p
import vector_
import particle
import random
p.init()

width=640
height=500

display = p.display.set_mode((width, height))
display.fill((0,0,0))
run=True

left_=p.Surface((5,80))
left_.fill((255,255,255))

right_=p.Surface((5,80))
right_.fill((255,255,255))

left=particle.particle()
left.create(20, 300, 0, 0, 0, 0, 0)

right=particle.particle()
right.create(610, 300, 0, 0, 0, 0, 0)


velocity=vector_.vector_functions()
velocity.create(0, 2.5)


x=random.randint(150,600)
y=random.randint(50,490)
direction=random.random()*random.choice([1,-1,5,-5,10,-10,0])
ball=particle.particle()
ball.create(x, y, 0, 2, 0, 0, 0)


while run:
    display.fill((0,0,0))
    for event in p.event.get():
        if event.type == p.QUIT:
            run= False
            
            
    keys=p.key.get_pressed()
    
    if keys[p.K_s]:
        left.position.add_to_xy(velocity)
        if ball.velocity.getY()==0 and (abs((ball.getX()+10)-left.getX())<=2 or abs((ball.getX()-10)-(left.getX()+5))<=2) and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):
            ball.velocity.set_angle(random.random())
#             ball.velocity.setX(ball.velocity.getX()*-1) 
            
#         elif ball.velocity.getY()!=0 and (abs((ball.getX()+10)-left.getX())<=2 or  abs((ball.getX()-10)-(left.getX()+5))<=2) and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):
#             ball.velocity.set_angle(velocity.get_angle()+0.01)
#             ball.velocity.setX(ball.velocity.getX()*-1)
          
    if keys[p.K_w] :  
        left.position.subtract_from_xy(velocity)
        if ball.velocity.getY()==0 and (abs((ball.getX()+10)-left.getX())<=2 or  abs((ball.getX()-10)-(left.getX()+5))<=2) and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):
            ball.velocity.set_angle(-random.random())
#             ball.velocity.setX(ball.velocity.getX()*-1) 
#         elif ball.velocity.getY()!=0 and (abs((ball.getX()+10)-left.getX())<=2 or  abs((ball.getX()-10)-(left.getX()+5))<=2) and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):
#             ball.velocity.set_angle(velocity.get_angle()+0.01)
#             ball.velocity.setX(ball.velocity.getX()*-1)
            
        
    if keys[p.K_DOWN]:
         
        right.position.add_to_xy(velocity) 
        
        if ball.velocity.getY()==0 and (abs((ball.getX()+10)-right.getX()-5)<=2 or  abs((ball.getX()-10)-(right.getX()))<=2) and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):
            ball.velocity.set_angle(random.random())
#             ball.velocity.setX(ball.velocity.getX()*-1) 
        elif ball.velocity.getY()!=0 and (abs((ball.getX()+10)-right.getX()-5)<=2 or  abs((ball.getX()-10)-(right.getX()))<=2) and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):
            ball.velocity.set_length(velocity.get_length()+0.01)
             
    if keys[p.K_UP] :  
         
        right.position.subtract_from_xy(velocity)
        if ball.velocity.getY()==0 and (abs((ball.getX()+10)-right.getX()-5)<=2 or  abs((ball.getX()-10)-(right.getX()))<=2) and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):
            ball.velocity.set_angle(-random.random())
#             ball.velocity.setX(ball.velocity.getX()*-1) 
       
             
        elif ball.velocity.getY()!=0 and (abs((ball.getX()+10)-right.getX())<=2 or  abs((ball.getX()-10)-(right.getX()+5))<=2) and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):
            ball.velocity.set_length(velocity.get_length()+0.01)
        
    #------------------------------------WALLS-----------------------------------------------------------------------------------------
        
    if ball.getX()+10>=width:    
        ball.position.setX(width-10)
        ball.velocity.setX(ball.velocity.getX()*-1)       
        
    elif ball.getX()-10<=1:    
        ball.position.setX(10)
        ball.velocity.setX(ball.velocity.getX()*-1)
        
    elif ball.getY()+10>=height:    
        ball.position.setY(height-10)
        ball.velocity.setY(ball.velocity.getY()*-1)
        
    elif ball.getY()-10<=1:    
        ball.position.setY(11)
        ball.velocity.setY(ball.velocity.getY()*-1)
    
    #-----------------------------------------------LEFT PADDLE--------------------------------------------------------------------------    
        
    if abs((ball.getX()+10)-left.getX())<=2 and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):
            
        ball.position.setX(left.getX()-11)
        ball.velocity.setX(ball.velocity.getX()*-1) 
               
          
    if abs((ball.getX()-10)-(left.getX()+5))<=2 and (((ball.getY()+10)>=(left.getY()) and ball.getY()+10<=left.getY()+80) or (ball.getY()-10<=left.getY()+80 and ball.getY()-10>=left.getY())):    
        ball.position.setX(left.getX()+16)
        ball.velocity.setX(ball.velocity.getX()*-1)
        
    #-------------------------------------------------RIGHT PADDLE----------------------------------------------------------------------    
        
    if abs((ball.getX()+10)-right.getX()-5)<=2 and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):
            
        ball.position.setX(right.getX()-6)
        ball.velocity.setX(ball.velocity.getX()*-1) 
               
          
    if abs((ball.getX()-10)-(right.getX()))<=2 and (((ball.getY()+10)>=(right.getY()) and ball.getY()+10<=right.getY()+80) or (ball.getY()-10<=right.getY()+80 and ball.getY()-10>=right.getY())):    
        ball.position.setX(right.getX()-16)
        ball.velocity.setX(ball.velocity.getX()*-1)    
        
            
            
    p.draw.circle(display, (255,255,255), ( int(ball.getX()), int(ball.getY()) ), 10, 10)
    display.blit(left_,(left.getX(),left.getY()))
    display.blit(right_,(right.getX(),right.getY()))

    ball.update()
    p.display.flip()
    p.time.Clock().tick(180)