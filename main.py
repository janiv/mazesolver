from tkinter import Tk, BOTH, Canvas
from window import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 6, 8, 100, 100, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
