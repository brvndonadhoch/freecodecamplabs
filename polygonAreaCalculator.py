import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height    
    
    def set_width(self, width: float):
        self._width = width
        return width

    def set_height(self, height: float):
        self._height = height
        return height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return math.sqrt((self.width ** 2) + (self.height ** 2))

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return("Too big for picture")
        
        picture = ''
        for height in range(self.height):
            picture +='*' * self.width + '\n'
        return picture

    def get_amount_inside(self):
        ...

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side,side)