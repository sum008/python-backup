'''
Created on May 3, 2020

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

# xl=360
# xr=475                                                                                                                                                     
# yt=460                                               
# yb=475 #475
xl=360
xr=455                                                                                                                                                
yt=390                                             
yb=450 #475

time.sleep(2)                                  
box=(xl,yt,xr,yb) 
# ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
score=0       
x=0.1
# if j<=27:
#                         p.keyDown("down", pause=x)
#                     else:
#                         p.keyDown("up", pause=x)
while True:
    img1=ig.grab(box).convert('L')
    px=img1.load()
    with escapable() as a:
        for i in range(0,img1.size[0]):
            for j in range(0,img1.size[1]):
                if 171<px[i,j]<=174:
                    p.keyDown("up", pause=x) 
                    a.escape()
#                     if j<=18:
#                         p.press("down", pause=x)
#                         a.escape()
#                     else:

    if score<1601:
        score+=1
        
    if score==750:
        box=(xl-50,yt,xr+140,yb)
        x=0.07
#         print("d")
    elif score==1100:
#         box=(xl-20,yt,xr+160,yb)
        box=(xl-85,yt,xr+150,yb)
        x=0.05
#         print("e")
    elif score==1600:
        box=(xl,yt,xr+100,yb)
#         print("s")
#     elif score==1400:
#         box=(xl+25,yt,xr+25,yb)
        
        