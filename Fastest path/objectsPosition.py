#this class will hold position of object
# By Bryan Perez

print("position")

class Position(object):
    def __init__(self,x,y):
        self.x = x
        self.y=y
    def __repr__(self):
        return "<Test a:%s b:%s>" % (self.x, self.y)

    def __str__(self):
        return "From str method of Test: x is %s, y is %s" % (self.x, self.y)
        
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y 
    def set_x(self,x):
        self.x= x
    def set_y(self,y):
        self.y=y
    def up(self):
        self.y+=1
    def down(self):
        self.y-=1
    def right(self):
        self.x+=1
    def left(self):
        self.x-=1
    

