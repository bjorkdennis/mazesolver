
from window import *
from point import *
from line import *
from cell import *
from maze import *




def main():

    

    win = Window(640, 480)
    maze = Maze(8, 8, 40, 40, win, 123)
    
    
    
    win.wait_for_close()






if __name__ == "__main__":
    main()