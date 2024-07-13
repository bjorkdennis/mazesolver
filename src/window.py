import tkinter

class Window():

    def __init__(self, width, height):
        self.__root_widget = tkinter.Tk()
        self.__root_widget.title = "JAg e titel"
        self.canvas = tkinter.Canvas()
        self.canvas.pack()
        self.running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def render(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.render()

    def draw_line(self, line):
        line.render(self.canvas, "gray4")

    def close(self):
        self.running = False
