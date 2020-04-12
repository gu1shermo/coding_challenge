class Ship:
    
    def __init__(self):
        self.x = width/2
        self.xdir = 0
    
    def show(self):
        fill(255)
        rectMode(CENTER)
        rect(self.x,height-20,20,30)
    
    def move(self):
        self.x += self.xdir*5
    
    def setDir(self,dir):
        self.xdir = dir
        
