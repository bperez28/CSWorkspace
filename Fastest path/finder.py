
# this class will get input of position and finish line 
# to get fastest path
#by Bryan Perez


from objectsPosition import Position
from graphics import *

class path(object):
    steps=[]
    def __init__(self,win,gameboard,startpoint,endpoint):
        self.win=win
        self.gameboard=gameboard
        self.startpoint=startpoint
        self.endpoint=endpoint
    def setGameboard(self,array):
        self.gameboard=array
    def getGameboard(self):
        return self.gameboard
    def setStartpoint(self,x,y):
        self.startpoint=Position(x,y)
    def getStartpoint(self):
        return self.startpoint
    def setEndpoint(self,x,y):
        self.endpoint=Position(x,y)
    def getEndpoint(self):
        return self.endpoint 


       
     
