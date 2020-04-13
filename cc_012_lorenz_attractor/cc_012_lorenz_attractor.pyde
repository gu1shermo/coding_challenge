# from peasy import PeasyCam

x = 0.01
y = 0.
z = 0.

a = 10
b = 28
c = 8./3.

angle = 0
points = []

def setup():
    size(800,600, P3D)
    colorMode(HSB)
    # cam = PeasyCam(this, 100)

def draw():
    global x,y,z,a,b,c,points,angle
    
    background(0)


    dt = 0.01
    
    dx = (a * (y - x))    * dt
    dy = (x * (b-z) - y)  * dt
    dz = (x * y - c * z)  * dt
    
    x = x + dx
    y = y + dy
    z = z + dz
    
    points.append(PVector(x,y,z))
    
    translate(width/2,height/2)
    scale(5)
    
    
    noFill()
    rotateY(angle)
    rotateX(angle)
    angle += 0.01
    beginShape()
    hu = 0
    for v in points:
        stroke(hu,255,255)
        vertex(v.x, v.y, v.z)
        
        # offset = PVector.random3D()
        # offset.mult(0.05)
        # v.add(offset)
        
        hu += 1
        if hu > 30:
            hu = 0
    endShape()
    
    
    print x, y, z
