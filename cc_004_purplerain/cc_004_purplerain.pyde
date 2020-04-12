# purple rain
# (138, 43, 226)
# (230, 230, 250) BG

from Drop import *

drops = []

def setup():
    size(640,360)
    for i in range(1,600):
        drops.append(Drop())
    
    
    
def draw():
    background(230, 230, 250)
    for d in drops:
        d.fall()
        d.show()
