'''
Created on 29 Aug, 2020

@author: sumit
'''

import math

class ball:
   
    def create(self,x,y,length,angle):
        self.x=x
        self.y=y
        self.length=length
        self.angle=angle
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x=x
    
    def setY(self,y):
        self.y=y
    
    def set_length(self,length):
        self.x=math.cos(self.angle)*length
        self.y=math.sin(self.angle)*length
    
    def set_angle(self,angle):
        self.x=math.cos(angle)*self.lenght
        self.y=math.sin(angle)*self.length
        
    def get_angle(self):
        return math.atan2(self.y, self.x)
    
    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def update(self):
        self.x+=math.cos(self.angle)*self.length
        self.y+=math.sin(self.angle)*self.length
        
    def pos(self):
        return (int(self.x),int(self.y))
    

    

        
        
        