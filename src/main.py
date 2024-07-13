
from window import *
from point import *
from line import *
from cell import *


def render(window):

    cell.render(window.canvas)


def main():
    
    print("Hello ponuts")

    win = Window(300, 200)
    render(win)
    win.wait_for_close()






if __name__ == "__main__":
    main()