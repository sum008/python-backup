'''
Created on Jun 17, 2020

@author: Sumit
'''
import pygame as p
import math

p.init()
window=(600,600)
display=p.display.set_mode(window)

points=[[300,300],[350,300],[400,300],[450,300]]

fps=30
run=True
length=50
fix=(300,300)
count=0
while run:
    
    display.fill((255,255,255))
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    
    mouse=p.mouse.get_pos()
    
    t=math.atan2(mouse[1]-fix[1],mouse[0]-fix[0])
    print(t)
    if fix[0]-3*length>mouse[0] or fix[1]-3*length>mouse[1] or fix[0]+3*length<mouse[0]  or fix[1]+3*length<mouse[1]:
        
        angle2=0
        angle1=t
        angle3=0
    
    else:
        l=math.sqrt((mouse[0]-fix[0])**2+(mouse[1]-fix[1])**2)
        c=math.sqrt((fix[0]-points[2][0])**2+(fix[1]-points[2][1])**2)
        ct=math.atan2(fix[1]-points[2][1], fix[0]-points[2][0])
        
        if l!=0 and c!=0 :
            x=(c**2+l**2-length**2)/(2*c*l)
            try:
                t1=math.acos(x)
            except:
                print(x,"ee")
                t1=math.acos(x%0.017428)
            
            y=(c**2+length**2-l**2)/(2*c*length)
            
            try:
                t2=math.acos(y)
            except:
                print(y,"sfs")
                t2=math.acos(y%0.017428)
            
            x1=(length**2+c**2-length**2)/(2*c*length)
            try:
                alpha=math.acos(x1)
            except:
                alpha=math.acos(int(x1))
            
            y1=(length**2+c**2-length**2)/(2*length*c)
            
            try:
                gama=math.acos(y1)
            except:
                gama=math.acos(int(y1))
            
            beta=(2*length**2-c**2)/(2*length**2)
            
            try:
                angle2=3.14-math.acos(beta)
            except:
                pass
            
            angle1=t-(alpha+t1)
            
            angle3=3.14-(gama+t2)
        
        
        
    points[1][0]=fix[0]+int(length*math.cos(angle1))
    points[1][1]=fix[1]+int(length*math.sin(angle1))

    points[2][0]=points[1][0]+int(length*math.cos(angle2+angle1))
    points[2][1]=points[1][1]+int(length*math.sin(angle2+angle1))
    
    points[3][0]=points[2][0]+int(length*math.cos(angle3+angle2+angle1))
    points[3][1]=points[2][1]+int(length*math.sin(angle3+angle2+angle1))
    
    
    p.draw.line(display, (0,0,0),fix,(int(points[1][0]),int(points[1][1])), 1)
    p.draw.circle(display, (0,0,0), (points[1][0],points[1][1]), 4, 4  )
    p.draw.line(display, (0,0,0),(int(points[1][0]),int(points[1][1])),(int(points[2][0]),int(points[2][1])), 1)
    p.draw.line(display, (0,0,0),(int(points[2][0]),int(points[2][1])),(int(points[3][0]),int(points[3][1])), 1)
        
    p.display.flip()
        
    p.time.Clock().tick(fps)
