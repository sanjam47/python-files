class Circle:

    pi=3.14

    def __init__(self,radius):
        self.radius=radius
    
    def getPerimeter(self):
        return 2*self.pi*self.radius
    
    def getArea(self):
        return self.pi*(self.radius**2)

C1=Circle(25)

print(f'Area is {C1.getArea()} unit.')
print(f'Perimeter is {C1.getPerimeter()}.')