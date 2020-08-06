'''
Created on May 31, 2020

@author: Sumit
'''
from PIL import ImageGrab as ig
import pyautogui as p
import time
import contextlib
from pynput.mouse import Controller,Button
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
mouse = Controller()
time.sleep(3)
#interval, button, duration, tween, pause, logScreenshot, _pause
count=0
xl=357
xr=616                                                                                                                                                
yt=100                                             
yb=507
# xl=750
# xr=756                                                                                                                                                
# yt=99                                             
# yb=404#475
                                 
box1=(xl,yt,xr,yb) 
ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
# p.doubleClick( button='left',interval=10)

run=True   
        
while run:
    pad=False
    stick_x_left=0
    d=21
    t=True
    xl=300
    xr=358                                                                                                                                                
    yt=469                                             
    yb=476
    box=(xl,yt,xr,yb) 
    while t:
#         print("dfsdf")
        img1=ig.grab(box).convert('L')
        px=img1.load()
#     print(px)
        with escapable() as a:
            for i in range(0,img1.size[0]):
                for j in range(0,img1.size[1]):
#                     print(px[i,j])
                    if px[i,j]<10:
                        stick_x_left=i
                        print(i)
                        t=False
                        pad=True
                        a.escape()
    stick_x_left+=d
    print(stick_x_left,"stick")
    stick=False
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------  
    while pad:
        distance=0
        xl=300+stick_x_left+10
        xr=616                                                                                                                                                
        yt=485                                             
        yb=500
        target_platform=(xl,yt,xr,yb)
        img2=ig.grab(target_platform).convert('L')
        px=img2.load()
        with escapable() as b:
            for i in range(0,img2.size[0]):
                for j in range(0,img2.size[1]):
                    if px[i,j]==32:
                        distance=i+3    
                        print(px[i,j])
                        pad=False
                        stick=True
                        b.escape()
    print(distance,"dis")
    length=0
    xl=300+stick_x_left-30
    xr=xl+50    
    yb=483-distance-2                                                                                                                                    
    yt=yb-4                                        
    box3=(xl,yt,xr,yb) 
    count=0
    ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
    while stick:
#         p.mouseDown(button='left')
        img3=ig.grab(box3).convert('L')
        px=img3.load()
        if count==0:
            mouse.press(Button.left)
            count=1
        with escapable() as c:
            for i in range(0,img3.size[0]):
                for j in range(0,img3.size[1]):
                    if px[i,j]<20 :
                        mouse.release(Button.left)
                        stick=False
                        c.escape()
         
               
    
    time.sleep(3)    
    #     break
    
