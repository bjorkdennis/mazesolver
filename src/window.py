import tkinter

class Window():

    def __init__(self, width, height):
        self._root_widget = tkinter.Tk()
        self._root_widget.title = "JAg e titel"
        self._root_widget.geometry(f"{width}x{height}")
        self.canvas = tkinter.Canvas()
        self.canvas.pack(expand=1, fill="both")
        self.running = False
        self._root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def render(self):
        self._root_widget.update_idletasks()
        self._root_widget.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.render()

    def draw_line(self, line, color):
        line.render(self.canvas, color)


    def close(self):
        self.running = False

