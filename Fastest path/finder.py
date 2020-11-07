
# this class will get input of position and finish line 
# to get fastest path
#by Bryan Perez


from objectsPosition import Position
from graphics import *

class path(object):
    steps=[]
    def __init__(self,win,gameboard,startingPosition,endPosition):
        self.win=win
        self.gameboard=gameboard
        self.startingPosition=startingPosition
        self.endPosition=endPosition
        self.block_size=20
    def getStartpoint(self):
        return self.startpoint
    def getEndpoint(self):
        return self.endpoint
    def pathFinder(self,tempPosition):
        print("pathFinder")
        print(tempPosition)
        i=tempPosition.get_x()
        j=tempPosition.get_y()
        if(tempPosition.get_x==self.endPosition.get_x and tempPosition.get_y==self.endPosition.get_y):
            return 
        if i+1<20 :
            rightBlockValue=self.gameboard[i+1][j]
            if rightBlockValue==0:
                print("right")
                i=tempPosition.get_x()+1
                rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                rec.setFill('blue')
                rec.draw(self.win)
                tempPosition.right()
                self.pathFinder(tempPosition)
        if i-1>0:
            leftBlockValue=self.gameboard[i-1][j]
            if leftBlockValue==0:
                print("left")
                j=tempPosition.get_x()-1
                rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                rec.setFill('blue')
                rec.draw(self.win)
            tempPosition.left()
            self.pathFinder(tempPosition)
        if j+1<20:
            upBlockValue=self.gameboard[i][j+1]
            if upBlockValue==0:
                print("up")
                j=tempPosition.get_y()+1
                rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                rec.setFill('blue')
                rec.draw(self.win)
            tempPosition.up()
            self.pathFinder(tempPosition)
        if j-1>0:
            downBlockValue=self.gameboard[i][j-1]
            if downBlockValue==0:
                print("down")
                j=tempPosition.get_y()-1
                if self.gameboard[i][j]==0:
                    rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                    rec.setFill('blue')
                    rec.draw(self.win)
                tempPosition.down()
                self.pathFinder(tempPosition)

    def test(self):
        #printing block down starting point
        found=0
        while found==0:
            print(self.startingPosition)
            j=self.startingPosition.get_x()
            i=self.startingPosition.get_y()
            if self.gameboard[i][j]==0:
                rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                rec.setFill('blue')
                rec.draw(self.win) 
            found=1
