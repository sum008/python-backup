'''
Created on May 17, 2020

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
xl=751
xr=756                                                                                                                                                
yt=99                                             
yb=404
# xl=750
# xr=756                                                                                                                                                
# yt=99                                             
# yb=404#475
                                 
box1=(xl,yt,xr,yb) 
ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
# p.doubleClick( button='left',interval=10)
pxl=703
pxr=869                                                                                                                                                
pyt=350                                             
pyb=492
box=(pxl,pyt,pxr,pyb)
run=False
stick=False
while True:
    img1=ig.grab(box).convert('L')
    px=img1.load()
#     print(px)
    with escapable() as a:
        for i in range(0,img1.size[0]):
            for j in range(0,img1.size[1]):
                if px[i,j]==0:
                    run=True
#                     print(run)
                    a.escape()
    xvalue=0           
    while run:
         
        xl=763
        xr=982                                                                                                                                              
        yt=404                                             
        yb=408
        box2=(xl,yt,xr,yb)
        img2=ig.grab(box2).convert('L')
        px=img2.load()
        with escapable() as b:
            for i in range(0,img2.size[0]):
                for j in range(0,img2.size[1]):
#                     if px[i,j]==0 and black==False:
#                         black=True
#                         print("Sdfsdfsds")
                    if 70<= px[i,j]<=82:
                        xvalue=i
                        print(i,j)
                        stick=True
                        b.escape()
        length=0
        xl=754
        xr=755                                                                                                                                               
        yt=106                                             
        yb=404
        box3=(xl,yt,xr,yb) 
        count=0
        while stick:
#                 length+=33
#                 print("sdfsd")
#             ig.grab(box3).convert('L').save("capture.jpg", "JPEG")
            img3=ig.grab(box3).convert('L')
            px=img3.load()
            if count==0:
                mouse.press(Button.left)
                count=1
#             p.mouseDown(button='left')
            with escapable() as c:
                for i in range(img3.size[0]-1,-1,-1):
                    for j in range(img3.size[1]-1,-1,-1):
                        print(j,xvalue,(yb-(j+106)), px[i,j])
                        if abs((yb-(j+106))-xvalue)<10:
                            if px[i,j]<40:
                                mouse.release(Button.left)
                                print(j)
                                stick=False
                                c.escape()
                            else:
                                c.escape()
            
                  
        run=False
    time.sleep(3)    
#     break

