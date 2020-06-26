import objectsPosition
import finder
from graphics import *

def main():
    block_size=20
    screen_width=500
    screen_height=500
    w, h = screen_width/block_size, screen_height/block_size
    gameboard = [[0 for x in range(w)] for y in range(h)] 
    win = GraphWin("Path Finder",screen_width,screen_height)
    win.setBackground('white')
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][j]==0:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.draw(win)

    win.getMouse()

    win.close()
main()