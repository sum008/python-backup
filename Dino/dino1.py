'''
Created on May 5, 2020

@author: Sumit
'''
from PIL import ImageGrab as ig
import pyautogui as p
import time
import contextlib

@contextlib.contextmanager
def escapable():
    class Escape(RuntimeError): pass
    class Unblock(object):
        def escape(self):
            raise Escape()

    try:
        yield Unblock()
    except Escape:
        pass

xl=495
xr=575                                                                                                                                                         
yt=376                                               
yb=414 #475

time.sleep(2)                                  
box=(xl,yt,xr,yb) 
# ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
score=0       
x=0.1
while True:
    img1=ig.grab(box).convert('L')
    px=img1.load()
    with escapable() as a:
        for i in range(0,img1.size[0]):
            for j in range(0,img1.size[1]):
                if 80<px[i,j]<90:
#                 if 170<px[i,j]<180:
                    p.keyDown("up", pause=x)
#                     p.press("up", pause=x) #,pause=0.07
                    a.escape()           
        
    if score<1401:
        score+=1
        
    if score==800:
        box=(xl-10,yt,xr+65,yb)
#         x=0.09
    elif score==1000:
#         box=(xl,yt,xr+90,yb)
        box=(xl-50,yt,xr+90,yb)
#         x=0.06
#         print("c")
#     elif score==1400:
#         box=(xl+25,yt,xr+25,yb)
        
        