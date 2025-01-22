from tkinter import Tk, BOTH, Canvas
from Window import *
from Point import *
from Line import *

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(400, 300)
    p3 = Point(400, 0)
    p4 = Point(0, 300)
    p5 = Point(400, 0)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p2, p4)
    l4 = Line(p2, p5)
    win.draw_line(l1, "black")
    win.draw_line(l2, "black")
    win.draw_line(l3, "black")
    win.draw_line(l4, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
