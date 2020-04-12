class Box:
    def __init__(self,x,y,z,size):
        self.pos = PVector(x,y,z)
        self.size = size
        
    def show(self):
        pushMatrix()
        noStroke()
        translate(self.pos.x,self.pos.y,self.pos.z)
        fill(255)
        box(self.size)
        popMatrix()
        
    def generate(self):
        boxes = []
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    sum = abs(x) + abs(y) + abs(z)
                    if sum > 1:
                        new_size = self.size/3
                        b = Box(self.pos.x + x*new_size,self.pos.y + y*new_size,self.pos.z + z*new_size,new_size)
                    boxes.append(b)
        return boxes
    
