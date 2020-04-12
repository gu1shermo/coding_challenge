from Ship import *
from Flower import *
from Drop import *

def setup():
    size(800, 900)
    
    ship = Ship()
    drops = []
    flowers = []
    for i in range(0,6):
        flowers.append(Flower(i*80+60,60))
    global ship,flowers,drops
    
    
def draw():
    background(51)
    ship.show()
    ship.move()
    borders = False
    for flower in flowers:
        flower.show()
        flower.move()
        if(flower.x + flower.r > width or flower.x - flower.r < 0):
            borders = True
    
    if borders:
        for flower in flowers:
            flower.shiftDown()
    
    
            
        
    for drop in drops:
        drop.show()
        drop.move()
        for flower in flowers:
            if drop.hits(flower):
                flower.grow()
                drops.remove(drop)
                break
 
                
def keyReleased():
    if keyCode is not 32:
        ship.setDir(0)

def keyPressed():
    if keyCode == 32:
        drops.append(Drop(ship.x,height))
    if keyCode == RIGHT:
        ship.setDir(1)
    elif keyCode == LEFT:
        ship.setDir(-1)
    
    
    
