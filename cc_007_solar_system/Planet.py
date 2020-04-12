class Planet:
    
    def __init__(self,r,d):
        self.radius = r
        self.angle = random(TWO_PI)
        self.distance = d
        self.children = []
    
    def show(self):
        pushMatrix()
        fill(255)
        rotate(self.angle)
        translate(self.distance,0)
        
        ellipse(0,0,self.radius*2,self.radius*2)
        if self.children:
            for child in self.children:
                child.show()
        popMatrix()
        
    def spawnMoons(self,n):
      for i in range(n):
            self.children.append(Planet(self.radius*(random(0.1,0.5)),random(75,300)))
            
    def orbit(self,):
        pass
        
