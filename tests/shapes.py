import math

class Shape:
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        return self.width == other.width and self.lenght == other.lenght
    
    def area(self):
        return self.lenght * self.width
    
    def perimeter(self):
        return 2 * (self.lenght + self.width)


class Square(Rectangle):
    def __init__(self, side_lenght):
        super().__init__(side_lenght, side_lenght)
