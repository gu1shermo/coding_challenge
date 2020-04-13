rows = 10
cols = 10
scl  = 20
w = 1600
h = 1600
terrain = []






def setup():
    size(600,600,P3D)
    
    cols = w / scl
    rows = h / scl
    
    flying = 0.
    
    global rows,cols,scl,w,h,terrain,flying
    
def draw():
    global flying
    terrain = []
    flying -= 0.05
    print flying
    
     
    # fill terrain with random Perlin values
    xoff = 0  
    for x in range(rows):
        yoff = flying
        for y in range(cols):
            terrain.append(map(noise(xoff,yoff),0,1,-150,150))
            # print('terrain[{}][{}]: '.format(x,y,str(terrain[x*cols+y])))
            yoff += 0.15
        xoff += 0.13
    
    
    
    
    background(0)
    stroke(255,100,7,100)
    noFill()
    
    translate(width/2,height/2)
    rotateX(PI/3)
    translate(-w/2.5,-h/2)
    for x in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for y in range(cols):
            vertex(x*scl,y*scl,terrain[x*cols+y])
            vertex((x+1)*scl,y*scl,terrain[(x+1)*cols+y])
        endShape()
    
    
