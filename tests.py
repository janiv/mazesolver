import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells[0]), num_cols)
        self.assertEqual(len(m1._cells), num_rows)
    
    
    def test_maze_create_cells2(self):
        num_cols = 6
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells[0]), num_cols)
        self.assertEqual(len(m1._cells), num_rows)

    def test_break_down_walls_top(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        tl = m1._cells[0][0]
        tl_count = 0
        if tl.has_left:
            tl_count+= 1
        if tl.has_right:
            tl_count+=1
        if tl.has_top:
            tl_count+=1
        if tl.has_bottom:
            tl_count+=1
        self.assertEqual(tl_count, 3)
    
    
    def test_break_down_walls_bottom(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        tl = m1._cells[-1][-1]
        tl_count = 0
        if tl.has_left:
            tl_count+= 1
        if tl.has_right:
            tl_count+=1
        if tl.has_top:
            tl_count+=1
        if tl.has_bottom:
            tl_count+=1
        self.assertEqual(tl_count, 3)

    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1=Maze(0,0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        c = m1._cells
        visited_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if c[i][j].visited:
                    visited_count += 1
        self.assertEqual(visited_count, 0)

    def test_dfs_break_walls_r(self):
        num_cols = 5
        num_rows = 5
        m1=Maze(0,0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        c = m1._cells
        visited_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if c[i][j].visited:
                    visited_count += 1
        self.assertEqual(visited_count, num_cols*num_rows)

if __name__ == "__main__":
    unittest.main()