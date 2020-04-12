class Drop:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 15
    
    def show(self):
        noStroke()
        fill(0,150,220)
        ellipse(self.x,self.y, self.r, self.r)
    
    def move(self):
        self.y -= 10
    
    def hits(self,flower):
        distance = dist(self.x,self.y,flower.x,flower.y)
        if distance  < self.r + flower.r:
            return True
        else: return False 
