class Snake:
    def __init__(self, scl):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.scl = scl
        
    def eat(self):
        pass
    
    def update(self):
        self.x += self.xspeed*self.scl
        self.y += self.yspeed*self.scl
        
        self.x = constrain(self.x,0,width-self.scl)
        self.y = constrain(self.y,0,height-self.scl)
    
    def show(self):
        fill(255)
        rect(self.x,self.y,self.scl,self.scl)
        
    def dir(self,x,y):
        self.xspeed = x
        self.yspeed = y
        
    
def keyPressed():
    if(keyCode == UP):
        s.dir(0,-1)
    elif keyCode == DOWN:
        s.dir(0,1)
    elif keyCode == RIGHT:
        s.dir(1,0)
    elif keyCode == LEFT:
        s.dir(-1,0)

def pickLocation():
    cols = width //  s.scl
    rows = height // s.scl
    food = PVector(floor(random(cols)),floor(random(rows)))
    food.mult(s.scl)
    return food

s = Snake(scl=10)
food = pickLocation()

def setup():
    size(400,400)
    frameRate(10)
    

    
def draw():
    background(127)
    s.update()
    s.show()
    fill(255,0,0)
    rect(food.x,food.y,s.scl,s.scl)
    

    
