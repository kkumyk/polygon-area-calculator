# Create a Rectangle object, initialized with width and height attributes.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            lines = ''
            line = "*" * self.width + "\n"
            for i in range(self.height):
                lines += line
            return lines

    def get_amount_inside(self, other_shape):
        max_width = self.width // other_shape.width
        max_height = self.height // other_shape.height
        return max_width * max_height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
    pass
