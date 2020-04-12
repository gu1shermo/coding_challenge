from Box import *

a = 0
b = Box(0,0,0,200)
boxes = []

def setup():
    size(400,400,P3D)
    boxes.append(b)
    

def mousePressed():
    global boxes
    next = []
    for box in boxes:
        newBoxes = box.generate()
        next += newBoxes
    boxes = next
    
def draw():
    global a,b
    background(51)
    lights()
    stroke(255)
    noFill()
    
    translate(width/2,height/2)
    rotateX(a)
    rotateY(a*0.5)
    rotateZ(a*0.3)
    for box in boxes:
        box.show()
    
    
    a += 0.01
    
    
