'''
Created on May 1, 2020

@author: Sumit
'''

class ball:
    
    def create(self,x,y,ox,oy,mass,g,friction,wind):
        self.x=x
        self.y=y
        self.ox=ox
        self.oy=oy
        self.g=g
        self.friction=friction
        self.wind=wind
        self.mass=mass
        self.pinned=False
        
    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def get_ox(self):
        return self.ox


    def get_oy(self):
        return self.oy


    def set_x(self, value):
        self.x = value


    def set_y(self, value):
        self.y = value


    def set_ox(self, value):
        self.ox = value


    def set_oy(self, value):
        self.oy = value
        
    def apply_g(self):
#         self.oy+=self.g*self.mass
        self.y+=self.g*self.mass
        
    def remove_g(self):
        self.g=0
        
    def apply_friction(self):
        self.x=self.x*self.friction
        self.y=self.y*self.friction
#         self.ox*=self.friction
#         self.oy*=self.friction
        
    def remove_friction(self):
        self.friction=1
        
    def apply_wind(self):
        self.x=self.x+self.wind
        
    def remove_wind(self):
        self.wind=0

    def set_mass(self,mass):
        self.mass=mass

    def get_mass(self):
        return self.mass
    
    def update(self):
        self.x+=(self.x-self.ox)
        self.y+=(self.y-self.oy)
        
        
        