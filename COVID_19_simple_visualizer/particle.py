import vector_
import math

# v=vector_.vector_functions()
class particle:
    
    def create(self,x,y,direction,speed,mass,gravity,dragOrFriction): #velocity--length position--angle
        
        self.position=vector_.vector_functions()
        self.position.create(x, y)
        
        self.velocity=vector_.vector_functions()
        self.velocity.set_length(speed)
        self.velocity.set_angle(direction)
        
        self.gravity=vector_.vector_functions()
        self.gravity.set_length(gravity*mass)
        self.gravity.set_angle(math.pi/2)
        
        self.drag=vector_.vector_functions()
        self.drag.set_length(dragOrFriction)
        
        self.mass=mass
    def accelerate(self,accelerate_):
        self.velocity.add_to_xy(accelerate_)
        
    def deaccelerate(self,accelerate_):
        self.velocity.subtract_from_xy(accelerate_)
        
    def update(self):
        self.velocity.add_to_xy(self.gravity)
        self.position.add_to_xy(self.velocity)
        
    def angle(self,point2):
        return math.atan2(point2.getY()-self.position.getY(), point2.getX()-self.position.getX())
    
    def distance(self,point2):
        x=abs(point2.getX()-self.position.getX())
        y=abs(point2.getY()-self.position.getY())
        return math.sqrt(x**2+y**2)
    
    def gravitational_force(self,point2):
        g=vector_.vector_functions()
        g.create(0,0)
        d=self.distance(point2)
        g.set_length(point2.mass*self.mass/d**2)
        g.set_angle(self.angle(point2))
        self.velocity.add_to_xy(g)
    
    def dragX(self):
            angle=self.velocity.get_angle()
            self.drag.set_angle(angle)
            self.velocity.setX(self.velocity.getX()*self.drag.get_length())
     
    def dragY(self):
        angle=self.velocity.get_angle()
        self.drag.set_angle(angle)
        self.velocity.setY(self.velocity.getY()*self.drag.get_length())
        
    def drag_overall(self):
#         self.drag.set_angle(self.velocity.get_angle())
        angle=self.velocity.get_angle()
        self.drag.set_angle(angle)
        self.velocity.mul_to_xy(self.drag.get_length())
           
    def getX(self):
        return self.position.getX()
    
    def getY(self):
        return self.position.getY()
    
    def update_position(self,x,y):
        self.position.create(x, y)
        
    def apply_gravity(self,gravity):
        self.gravity.set_length(self.mass*gravity)
        self.gravity.set_angle(math.pi/2)
        
    def remove_gravity(self):
        self.gravity.set_length(0)
        
    
    