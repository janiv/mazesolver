from Cell import *
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = self._create_cells()

    def _create_cells(self):
        cells = []
        for i in range(0, self.num_cols):
            temp = []
            for j in range(0, self.num_rows):
                c = self._draw_cell(i, j)
                temp.append(c)
            cells.append(temp)
        return cells
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + (i) * self.cell_size_x
        x2 = self._x1 + (i+1) * self.cell_size_x
        y1 = self._y1 + (j) * self.cell_size_y
        y2 = self._x1 + (j+1) * self.cell_size_y
        cell = Cell(True, True, True, True, x1, y1, x2, y2, self._win)
        cell.draw()
        self._animate()
        return cell

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)