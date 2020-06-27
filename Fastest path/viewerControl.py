import objectsPosition
import finder
from graphics import *


def main():
    loop=0
    block_size=20
    screen_width=500
    screen_height=500
    w, h = screen_width/block_size, screen_height/block_size
    gameboard = [[0 for x in range(w)] for y in range(h)] 
    win = GraphWin("Path Finder",screen_width,screen_height)
    win.setBackground('white')

    #game inti print 
    for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                if gameboard[i][j]==0:
                    rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                    rec.draw(win)
                    
                if gameboard[i][j]==1:
                    # start printed
                    rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                    rec.setFill('green')
                    rec.draw(win)
                    
                if gameboard[i][j]==2:
                    #  end printed
                    rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                    rec.setFill('red')
                    rec.draw(win)
                if gameboard[i][j]==3:
                    #  wall printed
                    rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                    rec.setFill('black')
                    rec.draw(win)


    # while loop to keep program running
    while win.isOpen():
        print("runnning game") 
        '''mouse clicks on the screen give back coordinates used
        for making walls,start and end point'''        
        coordinate = win.checkMouse()
        while coordinate == None:
            coordinate = win.checkMouse()
        print(coordinate)
        j=int(round((coordinate.getX() / block_size)-0.3))
        i=int(round((coordinate.getY() / block_size)-0.3))
        print(j)
        print(i)
        if coordinate != None:
            '''making wall'''
            if gameboard[i][j]>3:
                gameboard[i][j]=0
            gameboard[i][j]+=1
            if gameboard[i][j]==1:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('green')
                rec.draw(win)
            if gameboard[i][j]==2:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('red')
                rec.draw(win)
            if gameboard[i][j]==3:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('black')
                rec.draw(win)
        
        

    # win.close()
main()