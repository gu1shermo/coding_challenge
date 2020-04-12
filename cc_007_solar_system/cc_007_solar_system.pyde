from Planet import *

def setup():
    size(800, 800)
    sun = Planet(50,0)
    sun.spawnMoons(5)
    global sun

    
def draw():
    background(0)
    translate(width/2,height/2)
    sun.show()
