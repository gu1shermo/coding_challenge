class Flower:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 60
        self.xdir = 1
        self.ydir = 0
        
    
    def show(self):
        fill(255,0,200)
        rectMode(CENTER)
        ellipse(self.x,self.y, self.r, self.r)
    
    def move(self):
        self.x += self.xdir
        self.y += self.ydir
    
    def shiftDown(self):
        self.xdir *= -1.5
        self.y += self.r / 2
        
    def grow(self):
        self.r += 2
