
from tkinter import Canvas

class Line():

    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
    
    def render(self, canvas, color):
        canvas.create_line(self.p0.x, self.p0.y, self.p1.x, self.p1.y, fill=color, width=2)

