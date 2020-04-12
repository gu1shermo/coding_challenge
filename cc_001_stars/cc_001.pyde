from Star import *
 
stars = []
speed = 0
def setup():
    size(800,800)
    for i in range(0,800):
        print i
        stars.append(Star())
         
    
def draw():
    background(0)
    translate(width/2,height/2)
    speed = map(mouseX,0,width, 0, 50)
    
    
    for star in stars:
        star.update(speed)
        star.show()
