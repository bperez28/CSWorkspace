
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
    def pathFinder(self):
        #printing block down starting point
        found=0
        while found==0:
            print(self.startingPosition)
            j=self.startingPosition.get_x()
            i=self.startingPosition.get_y()+1
            if self.gameboard[i][j]==0:
                rec=Rectangle(Point(0+(self.block_size*j),0+(self.block_size*i)),Point(self.block_size+(self.block_size*j),self.block_size+(self.block_size*i)))
                rec.setFill('blue')
                rec.draw(self.win) 
            found=1
