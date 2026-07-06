import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height    
    
    def set_width(self, width: float):
        self.width = width
        return width

    def set_height(self, height: float):
        self.height = height
        return height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        
        picture = ''
        for height in range(self.height):
            picture +='*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):         
        return (self.width // shape.width) * (self.height // shape.height)
    
    def __str__(self):
        return (f'Rectangle(width={self.width}, height={self.height})')

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)
    
    def set_width(self, width: float):
        self.height = width
        self.width = width
        return width

    def set_height(self, height: float):
        self.height = height
        self.width = height
        return height

    def set_side(self, side):
        self.height = side
        self.width = side
        return side
    
    def __str__(self):
        return (f'Square(side={self.width})')

""" USAGE
rect = Rectangle(51, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))"""