class Cell:
    
    def __init__(self,pos,r,c):
        self.pos = pos or PVector(random(width),random(height))
        self.r = r or 60
        self.c = c  or color(random(100,255),0,random(100,255))
        
    def move(self):
        velocity = PVector.random2D()
        self.pos.add(velocity)
        
    def show(self):
        noStroke()
        fill(self.c)
        ellipse(self.pos.x,self.pos.y,self.r,self.r)
        
    def clicked(self,x,y):
        distance = dist(self.pos.x,self.pos.y,x,y)
        if distance < self.r:
            return True
        else:
            return False
    
    def mitosis(self):
        cell = Cell(PVector(
                            random(self.pos.x - self.r, self.pos.x + self.r),
                            random(self.pos.y - self.r, self.pos.y + self.r)),
                    self.r * 0.8,
                    self.c)
        return cell
