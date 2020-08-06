import math

class vector_functions:
    x=0
    y=0
    angle=0
    length=0 #magnitude
    def create(self,x,y):
        self.x=x
        self.y=y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x=x
    
    def setY(self,y):
        self.y=y
    
    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def set_length(self,length):
        a=self.get_angle()
        self.x=math.cos(a)*length
        self.y=math.sin(a)*length
    
    def set_angle(self,angle):
        l=self.get_length()
        self.x=math.cos(angle)*l
        self.y=math.sin(angle)*l
        
    def get_angle(self):
        return math.atan2(self.y, self.x)
    
    def add_to_xy(self,value):
#         return self.create(self.x+value.getX(), self.y+value.getY())
        self.x+=value.getX()
        self.y+=value.getY()
#         
    def subtract_from_xy(self,value):
#         return self.create(self.x-value.getX(), self.y-value.getY())

        self.x-=value.getX()
        self.y-=value.getY()
        
    
    def add_to_X(self,value):
        return self.x+value
    
    def add_to_Y(self,value):
        return self.y+value
    
    def sub_from_X(self,value):
        return self.x-value
    
    def sub_from_Y(self,value):
        return self.y-value
    
    def mul_to_X(self,value):
        return self.x*value
    
    def mul_to_Y(self,value):
        return self.y*value
    
    def mul_to_xy(self,value):
        self.x*=value
        self.y*=value
    
    def div_from_X(self,value):
        return self.x/value
    
    def div_from_Y(self,value):
        return self.y/value
    
    def div_from_xy(self,value):
        self.x=self.x/value
        self.y=self.y/value
        
    def update_position(self,value):
        self.x=value.getX()
        self.y=value.getY()
     
        
        
        