class Cell:
    
    
    
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False
        self.stucked = False
    
    
        
    
    def show(self,w):
        x = self.i * w
        y = self.j * w
        stroke(250)
        if self.walls[0]:
            line(x    , y    , x + w, y    )
        if self.walls[1]:
            line(x + w, y    , x + w, y + w)
        if self.walls[2]:
            line(x + w, y + w, x    , y + w)
        if self.walls[3]:
            line(x    , y + w, x    , y    )
        
        
        if self.visited:
            noStroke()
            fill(0,77,250,100)
            rect(x,y,w,w)
        
        if self.stucked:
            noStroke()
            fill(255,0,66,100)
            rect(x,y,w,w)
    
    @staticmethod
    def removeWalls(a,b):
        print 'enter removewalls'
        print a,b
        x = a.i - b.i
        print x
        if x == 1:
            a.walls[3] = False
            b.walls[1] = False
        if x == -1:
            a.walls[1] = False
            b.walls[3] = False
        y = a.j - b.j
        print y
        if y == 1:
            a.walls[0] = False
            b.walls[2] = False
        if y == -1:
            a.walls[2] = False
            b.walls[0] = False
        
       
    
    def highlight(self,w):
        print 'hlight'
        x = self.i * w
        y = self.j * w
        noStroke()
        fill(0,250,250,100)
        rect(x,y,w,w)
    
    def index(self,i,j,rows,cols):
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return 0
        return i * cols  + j
    
    def checkNeighbors(self,grid,rows,cols):
        neighbors = []
        top_index = self.index(self.i  , self.j-1, rows, cols)
        right_index = self.index(self.i+1, self.j  , rows, cols)
        bottom_index = self.index(self.i  , self.j+1, rows, cols)
        left_index = self.index(self.i-1, self.j  , rows, cols)
        
        top    = None
        right  = None
        bottom = None
        left   = None
        if top_index > 0:
            top    = grid[top_index]
        if right_index > 0:
            right    = grid[right_index]
        if bottom_index > 0:
            bottom    = grid[bottom_index]
        if left_index > 0:
            left    = grid[left_index]
        
 
        
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        

        
        if len(neighbors) > 0:
            r = floor(random(0,len(neighbors)))
            return neighbors[r]
        else:
            return None
            
     
