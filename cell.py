from line import *
from point import *
from window import *

class Cell:
    def __init__(self, has_left, has_right, has_top, has_bottom, x1, y1, x2, y2, win=None, visited=False):
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = visited

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
        if not self.has_left:
            self._win.draw_line(left, "white")
        if not self.has_right:
            self._win.draw_line(right, "white")
        if not self.has_top:
            self._win.draw_line(top, "white")
        if not self.has_bottom:
            self._win.draw_line(bottom, "white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        
        center_self_x = (self._x1 + self._x2)/2
        center_self_y = (self._y1 + self._y2)/2
        to_cell_x = (to_cell._x1 + to_cell._x2)/2
        to_cell_y = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(center_self_x, center_self_y), Point(to_cell_x, to_cell_y))
        self._win.draw_line(line, color)
