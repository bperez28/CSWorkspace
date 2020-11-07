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

    #increment is to make sure there is only one start and end point
    increment=1 
    startingPosition=objectsPosition.Position(0,0)
    endPosition=objectsPosition.Position(0,0)
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
            #if starting point is clicked finder will start to find fastest path
            if gameboard[i][j]==1 and increment>2:
                path=finder.path(win,gameboard,startingPosition,endPosition)
                path.pathFinder(startingPosition)
                # path.pathFinder(startingPosition)
                print("find end")
                
            #if start and end point havent been click 
            if increment<3:
                if gameboard[i][j]!=1:
                    gameboard[i][j]=increment
                    endPosition.set_x(j)
                    endPosition.set_y(i)
                    if increment==1:
                        startingPosition.set_x(j)
                        startingPosition.set_y(i)
                    increment+=1
                    
            else:
                #create wall if wall clicked than make it empty
                if gameboard[i][j]==3:
                    gameboard[i][j]=0
                else:
                    if gameboard[i][j]==0:
                        gameboard[i][j]=3
            #fill in boxes dependent on array value empty(0), start(1),end(2),wall(3)
            if gameboard[i][j]==0:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('white')
                rec.draw(win)
            if gameboard[i][j]==1:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('green')
                rec.draw(win)
            if gameboard[i][j]==2:
                endPostion=objectsPosition.Position(i,j)
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('red')
                rec.draw(win)
            if gameboard[i][j]==3:
                rec=Rectangle(Point(0+(block_size*j),0+(block_size*i)),Point(block_size+(block_size*j),block_size+(block_size*i)))
                rec.setFill('black')
                rec.draw(win)
        
        

    # win.close()
main()