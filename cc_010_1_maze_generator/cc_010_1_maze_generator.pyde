from Cell import *

W = 10
COLS = -1
ROWS = -1
current = -1
stack = []



def setup():
    size(400, 400)
    COLS = floor(width  / W)
    ROWS = floor(height / W)
    grid = []
    # frameRate(1)
    
    # draw grid
    for i in range(ROWS):
        for j in range(COLS):
            grid.append(Cell(i,j))
    
    current = grid[0]
    global grid,current,COLS,ROWS,stack       
    
def draw():
    background(59)
    current.visited = True
    current.stucked = False
    
    # step 1
    next = current.checkNeighbors(grid,ROWS,COLS)
    if next:
        next.visited = True
        
        # step 2
        stack.append(current)
        # step 3
        
        Cell.removeWalls(current,next)
        
        # step 4
        current = next
        current.highlight(W)
    elif len(stack) > 0:
        
        current = stack.pop()
        current.stucked = True
        
        
    
    for cell in grid:
        cell.show(W)
        # print cell.walls
    
    global current
