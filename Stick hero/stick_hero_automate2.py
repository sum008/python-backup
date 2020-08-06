'''
Created on May 19, 2020

@author: Sumit
'''
from PIL import ImageGrab as ig
import pyautogui as p
import time
import contextlib
from pynput.mouse import Controller,Button

mouse = Controller()
time.sleep(3)
#interval, button, duration, tween, pause, logScreenshot, _pause
count=0
xl=751
xr=756                                                                                                                                                
yt=99                                             
yb=404                                      
# yb=404#475
                                 
# box1=(xl,yt,xr,yb) 
# ig.grab(box1).convert('L').save("screen_capture.jpg", "JPEG")
# p.doubleClick( button='left',interval=10)

count=0
xl=753
xr=755                                                                                                                                               
yt=105                                             
yb=404
box3=(xl,yt,xr,yb) 
mouse.press(Button.left)
while count<100000:
#             ig.grab(box3).convert('L').save("capture.jpg", "JPEG")
    count+=1
mouse.release(Button.left)
ig.grab(box3).save("capture.jpg", "JPEG")
print(count)

