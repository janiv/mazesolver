from cell import *
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = random.seed()
        self._cells = self._create_cells()
        self._draw_cell()


    def _create_cells(self):
        cells = []
        for i in range(0, self.num_cols):
            temp = []
            for j in range(0, self.num_rows):
                x1 = self._x1 + (i) * self.cell_size_x
                x2 = self._x1 + (i+1) * self.cell_size_x
                y1 = self._y1 + (j) * self.cell_size_y
                y2 = self._x1 + (j+1) * self.cell_size_y
                cell = Cell(True, True, True, True, x1, y1, x2, y2, self._win)
                temp.append(cell)
            cells.append(temp)
        return cells
    
    def _draw_cell(self):
        if(self._win):
            for col in self._cells:
                for c in col:
                    c.draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[-1][-1]
        top_val = random.randint(0,1)
        bot_val = random.randint(0,1)
        if top_val == 1:
            top_left_cell.has_left = False
        else:
            top_left_cell.has_top = False
        if bot_val == 1:
            bottom_right_cell.has_bot = False
        else:
            bottom_right_cell.has_right = False
        self._draw_cell()

    def _break_walls_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        going = True
        while(going):
            to_visit = []


    def isVisitable(self, i, j):
        if i<0 or j<0:
            return False
        if i>= self.num_rows or j>=self.num_cols:
            return False
        if self._cells[i][j].visited:
            return False
        return True



