class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius*3.14*self.radius
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
odj=circle(78.5)
print("radius of the Cicle :",odj.radius)
print("Area of the Cicle :",odj.area())
odj=rectangle(5,4)
print("Area of the Rectangle :",odj.area())
        
