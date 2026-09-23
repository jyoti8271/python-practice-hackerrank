from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
    
class rectange(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
    
shape1=[circle(6),rectange(8,9)]

for shape in shape1:
    print(shape.area())
        
        
        
        
        
