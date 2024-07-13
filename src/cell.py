from line import *
from point import *

class Cell():

    def __init__(self, x0, y0, x1, y1):
        self.__x0 = x0
        self.__y0 = y0
        self.__x1 = x1
        self.__y1 = y1
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def render(self, canvas):
        p0 = Point(self.__x0, self.__y0)
        p1 = Point(self.__x1, self.__y0)
        p2 = Point(self.__x1, self.__y1)
        p3 = Point(self.__x0, self.__y1)

        if self.has_top_wall:
            line = Line(p0, p1)
            line.render(canvas, "gray4")

        if self.has_right_wall:
            line = Line(p1, p2)
            line.render(canvas, "gray4")
            
        if self.has_bottom_wall:
            line = Line(p2, p3)
            line.render(canvas, "gray4")

        if self.has_left_wall:
            line = Line(p3, p0)
            line.render(canvas, "gray4")



