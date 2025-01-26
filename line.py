from Point import *

class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def draw(self, canvas, fill_color):
        canvas.create_line(self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y, fill=fill_color, width=2)