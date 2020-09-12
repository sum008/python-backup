'''
Created on 29 Aug, 2020

@author: sumit
'''
class paddle:
    
    def create(self,x,y):
        self.x=x
        self.y=y
        
    def pos(self):
        return (self.x,self.y)
        
    def update_pos(self,speed):
        self.x+=speed
        
    
        