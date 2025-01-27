from tkinter import Tk, BOTH, Canvas
from window import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 6, 8, 50, 50, win)
    maze._break_entrance_and_exit()

    win.wait_for_close()


if __name__ == "__main__":
    main()
