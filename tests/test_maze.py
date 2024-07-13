import unittest

import src

import window
import maze

class TestMaze(unittest.TestCase):

    def test_cells_visited_reset(self):
        print("running tests")
        win = window.Window(640, 480) 
        test_maze = maze.Maze(10, 10, 40, 40, win, 123)

        for cell in test_maze._cells:
            self.assertEqual(cell.visited, False)