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
        for i in range(0, self.num_rows):
            temp = []
            for j in range(0, self.num_cols):
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
        bottom_right_cell = self._cells[self.num_rows-1][self.num_cols-1]
        top_val = random.randint(0,1)
        bot_val = random.randint(0,1)
        if top_val == 1:
            top_left_cell.has_left = False
        else:
            top_left_cell.has_top = False
        if bot_val == 1:
            bottom_right_cell.has_bottom = False
        else:
            bottom_right_cell.has_right = False
        self._draw_cell()

    def _break_walls_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        going = True
        while(going):
            to_visit = []
            left = (i-1,j)
            right = (i+1,j)
            up = (i,j-1)
            down= (i,j+1)
            # Check which directions are visitable
            if self.isVisitable(left[0], left[1]):
                to_visit.append(left)
            if self.isVisitable(right[0], right[1]):
                to_visit.append(right)
            if self.isVisitable(up[0], up[1]):
                to_visit.append(up)
            if self.isVisitable(down[0], down[1]):
                to_visit.append(down)
            if len(to_visit) == 0:
                return
            # Pick random direction
            dir = random.randint(0, len(to_visit)-1)
            choice = to_visit[dir]
            next_cell = self._cells[choice[0]][choice[1]]
            # Knock down walls
            if choice == left:
                curr_cell.has_left = False
                next_cell.has_right = False
            if choice == right:
                curr_cell.has_right = False
                next_cell.has_left = False
            if choice == up:
                curr_cell.has_top = False
                next_cell.has_bottom = False
            if choice == down:
                curr_cell.has_bottom = False
                next_cell.has_top = False
            self._break_walls_r(choice[0], choice[1])

    def _reset_cells_visited(self):
        for cl in self._cells:
            for c in cl:
                c.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        if(i == self.num_rows-1 and j == self.num_cols-1):
            return True
        left = (i-1, j)
        right = (i+1, j)
        up = (i, j-1)
        down = (i, j+1)

        # handle left
        if self.isVisitable(left[0], left[1]):
            left_cell = self._cells[left[0]][left[1]]
            if not left_cell.has_right:
                curr_cell.draw_move(left_cell, False)
                if self._solve_r(left[0], left[1]):
                    return True
                else:
                    curr_cell.draw_move(left_cell, True)
        
        # handle right
        if self.isVisitable(right[0], right[1]):
            right_cell = self._cells[right[0]][right[1]]
            if not right_cell.has_left:
                curr_cell.draw_move(right_cell, False)
                if self._solve_r(right[0], right[1]):
                    return True
                else:
                    curr_cell.draw_move(right_cell, True)

        # handle up
        if self.isVisitable(up[0], up[1]):
            up_cell = self._cells[up[0]][up[1]]
            if not up_cell.has_bottom:
                curr_cell.draw_move(up_cell, False)
                if self._solve_r(up[0], up[1]):
                    return True
                else:
                    curr_cell.draw_move(up_cell, True)

        #handle down
        if self.isVisitable(down[0], down[1]):
            down_cell = self._cells[down[0]][down[1]]
            if not down_cell.has_top:
                curr_cell.draw_move(down_cell, False)
                if self._solve_r(down[0], down[1]):
                    return True
                else:
                    curr_cell.draw_move(down_cell, True)
        return False
            
            
            



    def isVisitable(self, i, j):
        if i<0 or j<0:
            return False
        if i>= self.num_rows or j>=self.num_cols:
            return False
        if self._cells[i][j].visited:
            return False
        return True



