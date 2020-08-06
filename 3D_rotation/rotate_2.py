'''
Created on Jun 26, 2020

@author: Sumit
'''
import pygame as p
import math as m

p.init()
width=600
height=600
display=p.display.set_mode((width,height))

angle=0.01
scale=5
points=[0]*8
points[0]=[200,200,-50]
points[1]=[300,200,-50]
points[2]=[300,300,-50]
points[3]=[200,300,-50]
points[4]=[200,200,50]
points[5]=[300,200,50]
points[6]=[300,300,50]
points[7]=[200,300,50]
distance=2



def mat_mul1(mat,pdt):
    x=mat[0][0]*pdt[0]+mat[0][1]*pdt[1]+mat[0][2]*pdt[2]
    y=mat[1][0]*pdt[0]+mat[1][1]*pdt[1]+mat[1][2]*pdt[2]
    
    return [x,y]

def mat_mul(mat,pdt):
    x=mat[0][0]*pdt[0]+mat[0][1]*pdt[1]+mat[0][2]*pdt[2]
    y=mat[1][0]*pdt[0]+mat[1][1]*pdt[1]+mat[1][2]*pdt[2]
    z=mat[2][0]*pdt[0]+mat[2][1]*pdt[1]+mat[2][2]*pdt[2]
    return [x,y,z]

def rotate_X(x,y,z,angle):
    mat=[
        [1,0,0],
        [0,m.cos(angle),-m.sin(angle)],
        [0,m.sin(angle),m.cos(angle)]
         ]
    pdt=[x,y,z]
    p1=mat_mul(mat,pdt)
    return p1

def rotate_Y(x,y,z,angle):
    mat=[
        [m.cos(angle),0,m.sin(angle)],
        [0,1,0],
        [-m.sin(angle),0,m.cos(angle)]
         ]
    pdt=[x,y,z]
    p1=mat_mul(mat,pdt)
    return p1

def rotate_Z(x,y,z,angle):
    mat=[
        [m.cos(angle),-m.sin(angle),0],
        [m.sin(angle),m.cos(angle),0],
        [0,0,1]
         ]
    pdt=[x,y,z]
    p1=mat_mul(mat,pdt)
    return p1

def rotate_XYZ(x,y,z,angle):
    mat=[
        [m.cos(angle)*m.sin(angle),m.cos(angle)*m.sin(angle)**2-m.sin(angle)*m.cos(angle),m.cos(angle)**2*m.sin(angle)+m.sin(angle)**2],
        [m.cos(angle)*m.sin(angle),m.sin(angle)**3+m.cos(angle)**2,m.cos(angle)*m.sin(angle)**2-m.sin(angle)*m.cos(angle)],
        [-m.sin(angle),m.cos(angle)*m.sin(angle),m.cos(angle)*m.sin(angle)]
         ]
    pdt=[x,y,z]
    p1=mat_mul(mat,pdt)
    return p1

run=True

while run:
    
    display.fill((0,0,0))
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run=False
    pt=[]    
    for point in points:
        p1=rotate_X(point[0],point[1],point[2],angle)
        point[0]=p1[0]
        point[1]=p1[1]
        point[2]=p1[2]
        
        p1=rotate_Y(point[0],point[1],point[2],angle)
        point[0]=p1[0]
        point[1]=p1[1]
        point[2]=p1[2]
        
        p1=rotate_Z(point[0],point[1],point[2],0.002)
        point[0]=p1[0]
        point[1]=p1[1]
        point[2]=p1[2]
        
        z=50/abs(200-point[2])
        print(z)
        projection_to_2d=[[z,0,0],
                          [0,z,0]]
        
        pr=mat_mul1(projection_to_2d,[point[0],point[1],point[2]])
        pt.append(pr)
        
    for i in range(0,4):
        p.draw.line(display, (255,255,255),(int(pt[i%4][0]),int(pt[i%4][1])) ,(int(pt[i+4][0]),int(pt[i+4][1])), 2)
        p.draw.line(display, (255,255,255),(int(pt[i][0]),int(pt[i][1])) ,(int(pt[(i+1)%4][0]),int(pt[(i+1)%4][1])), 2)
        if i+5==8:
            p.draw.line(display, (255,255,255),(int(pt[i+4][0]),int(pt[i+4][1])) ,(int(pt[4][0]),int(pt[4][1])), 2)
        else:
            p.draw.line(display, (255,255,255),(int(pt[i+4][0]),int(pt[i+4][1])) ,(int(pt[(i+5)][0]),int(pt[(i+5)][1])), 2)
#     angle+=0.01
    p.display.flip()
    p.time.Clock().tick(60)