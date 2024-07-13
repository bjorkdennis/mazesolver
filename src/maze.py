import random
import time
from cell import *
import window

class Maze():

    def __init__(self, num_rows, num_cols, cell_width, cell_height, window, seed=None):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_width = cell_width
        self.cell_height = cell_height
        self._window = window
        self._cells = []
        self._debug_path = []

        self.seed = seed
        if self.seed is not None:
            random.seed(self.seed)

        self._create_cells()
        self._create_entrance_and_exit()
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            self._cells[i].visited = False

    def _create_cells(self):
        offset_x = 10
        offset_y = 10

        for y in range(0, self.num_rows):
            for x in range(0, self.num_cols):
                cell = Cell((x * self.cell_width) + offset_x,
                             (y * self.cell_height) + offset_y,
                             ((x * self.cell_width) + self.cell_width) + offset_x,
                               ((y * self.cell_height) + self.cell_height) + offset_y,
                                 self._window)
                self._cells.append(cell)
                self._draw_cell(x, y)
        

    def _draw_cell(self, col, row):
        self._cells[row * self.num_cols + col].render()
        self._animate()

    def _animate(self):
        self._window.render()
        time.sleep(0.05)

    def _get_cell(self, x, y):
        return self._cells[y * self.num_cols + x]
    
    def _create_entrance_and_exit(self):
        entrance = self._get_cell(0, 0)    
        exit = self._get_cell(self.num_cols-1, self.num_rows-1)

        entrance.has_top_wall = False
        exit.has_bottom_wall = False
        self._animate()

    def _break_walls_r(self, x, y):

        cell = self._get_cell(x, y)
        cell.visited = True

        while True:
            cell_coords = []

            if y > 0:
                cell_coords.append((x, y - 1))
            if x > 0:
                cell_coords.append((x - 1, y))
            if x < (self.num_cols - 1):
                cell_coords.append((x + 1, y))
            if y < (self.num_rows - 1):
                cell_coords.append((x, y + 1))



            possible_cells = []


            for i in range(0, len(cell_coords)):
                cell_coord = cell_coords[i]

                c = self._get_cell(cell_coord[0], cell_coord[1])
                if c.visited is False:
                    possible_cells.append((c, cell_coord))
            
            if len(possible_cells) == 0:
                self._draw_cell(x, y)
                return
            
            rand_index = random.randrange(0, len(possible_cells))
            next_cell, next_coord = possible_cells[rand_index]

            print(f"From X:{x}, Y:{y} to X:{cell_coord[0]}, Y:{cell_coord[1]}")

            if x < next_coord[0]:
                next_cell.has_left_wall = False
                cell.has_right_wall = False
            elif x > next_coord[0]:
                next_cell.has_right_wall = False
                cell.has_left_wall = False
            elif y < next_coord[1]:
                next_cell.has_top_wall = False
                cell.has_bottom_wall = False
            elif y > next_coord[1]:
                cell.has_top_wall = False
                next_cell.has_bottom_wall = False

            self._break_walls_r(next_coord[0], next_coord[1])
            


            
            

        

        


