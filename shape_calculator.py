# Create a Rectangle object, initialized with width and height attributes.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

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


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_height(self, side_length):
        self.width = side_length
        self.height = side_length



