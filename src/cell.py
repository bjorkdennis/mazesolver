from line import *
from point import *

class Cell():

    def __init__(self, x0, y0, x1, y1, win):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1
        self._window = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def render(self):
        p0 = Point(self._x0, self._y0)
        p1 = Point(self._x1, self._y0)
        p2 = Point(self._x1, self._y1)
        p3 = Point(self._x0, self._y1)

        if self.has_top_wall:
            line = Line(p0, p1)
            self._window.draw_line(line, "gray4")
        else:
            line = Line(p0, p1)
            self._window.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(p1, p2)
            self._window.draw_line(line, "gray4")
        else:
            line = Line(p1, p2)
            self._window.draw_line(line, "white")
            
        if self.has_bottom_wall:
            line = Line(p2, p3)
            self._window.draw_line(line, "gray4")
        else:
            line = Line(p2, p3)
            self._window.draw_line(line, "white")

        if self.has_left_wall:
            line = Line(p3, p0)
            self._window.draw_line(line, "gray4")
        else:
            line = Line(p3, p0)
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        if to_cell is None:
            raise ValueError("to_cell cannot be None")
        
        x0, y0 = self.get_center()
        x1, y1 = to_cell.get_center()

        color = "gray8" if undo else "red"
        
        self._window.draw_line(Line(Point(x0, y0), Point(x1, y1)), color)

    def get_center(self):
        return (self._x0 + (self._x1 - self._x0)/2, self._y0 + (self._y1 - self._y0)/2)



