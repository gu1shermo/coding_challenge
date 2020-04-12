class Drop:
    def __init__(self):
        self.x = random(width)
        self.y = random(-500,-50)
        
        
        self.z = random(0,20)
        
        self.l = map(self.z,0,20,10,20)
        self.yspeed = map(self.z,0,20,1,20)
    
    def fall(self):
        self.y += self.yspeed
        grav = map(self.z,0,20,0.,0.2)
        self.yspeed += grav
        if self.y > height:
            self.y = random(-200,-100)
            self.yspeed = map(self.z,0,20,4,10)
        
    def show(self):
        thick = map(self.z,0,20,1,3)
        strokeWeight(thick)
        stroke(138,43,226)
        line(self.x,self.y,self.x,self.y + self.l)
