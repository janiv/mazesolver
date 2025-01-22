from Line import *
from Point import *
from Window import *

class Cell:
    def __init__(self, has_left, has_right, has_top, has_bottom, x1, y1, x2, y2, win):
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        top_l = Point(self._x1, self._y1)
        top_r = Point(self._x2, self._y1)
        bot_l = Point(self._x1, self._y2)
        bot_r = Point(self._x2, self._y2)
        top = Line(top_l, top_r)
        left = Line(top_l, bot_l)
        right = Line(top_r, bot_r)
        bottom = Line(bot_l, bot_r)
        if self.has_left:
            self._win.draw_line(left, "black")
        if self.has_right:
            self._win.draw_line(right, "black")
        if self.has_top:
            self._win.draw_line(top, "black")
        if self.has_bottom:
            self._win.draw_line(bottom, "black")
