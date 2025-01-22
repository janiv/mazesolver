from tkinter import Tk, BOTH, Canvas
from Window import *
from Cell import *

def main():
    win = Window(800, 600)

    cell1 = Cell(True, True, False, True, 100, 100, 200, 200, win)
    cell2 = Cell(True, True, True, True, 200, 100, 300, 200, win)
    cell3 = Cell(True, False, True, True, 300, 100, 400, 200, win)
    cell4 = Cell(True, True, True, False, 300, 300, 400, 400, win)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
