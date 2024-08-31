class Circle:
    pi=3.142
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return  f"area of circle is {self.radius**2*self.pi}"
    
    def area(self,pi):
        return  self.radius**2*pi
    
    def perimeter(self):
        return f"perimeter of circle is {self.radius *2 *self.pi}"

class Shape(Circle): #inheritance
    # overiding
    def __init__(self,radius,border_colors):
        Circle.__init__(self,radius,)
        self.radius=radius
        self.border_colors=border_colors
        
    def shapeName(self):
        if self.radius<=0:
            return f"this is square with{self.border_colors} color"
        elif self.area(3.142) < 50:
            return f"this is big circle with {self.border_colors} color"
        else:
            return f"this is circle with {self.border_colors} color"
        
x=Shape(radius=1,border_colors="red")

print (x.area(3.142))
print (x.perimeter())
print (x.shapeName())
        
x=Circle(radius=4)
# print(x.perimeter())