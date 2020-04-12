from Cell import *

def setup():
    size(400,400)
    
    cells = []
    for i in range(5):
        cells.append(Cell(PVector(random(width),random(height)), random(50,70), color(random(0,255),random(0,30),random(0,177))))
        
    global cells
    
def draw():
    background(15)
    for cell in cells:
        cell.move()
        cell.show()

def mousePressed():
    for cell in cells:
        if cell.clicked(mouseX,mouseY):
            cells.extend([cell.mitosis(),cell.mitosis()])
            cells.remove(cell)
    
