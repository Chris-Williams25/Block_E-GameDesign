import os, time
from xml.dom import HierarchyRequestErr 
import pygame as p 

#intialize pygame
p.init() 

#define colors
white=[255,255,255] 
WIDTH=800
HEIGHT=800
red=[255,0,0] 
mag=[255,0,255] 
aqua=[51,153,255]
m=[47,234,232]
#create your window/screen
#putting it all in unpercase is a indicator that it should remain a constant, it doesn't affect the code, it is just a standard
# Thing=True
# while(Thing):
screen=p.display.set_mode((WIDTH,HEIGHT))
# screen.fill(m)
# p.display.update()
# p.time.delay(5000) 
# screen.fill(white) 
# p.display.update
# screen.fill(red)
# p.display.update
# p.display.set_caption("My Window") 

# ThisThing=True
# while(ThisThing):
#     screen
#     screen.fill(m)
#     p.display.update()
#     p.time.delay(1000)
#     screen.fill(red)
#     p.display.update()
#     p.time.delay(1000)
#     screen.blit


#define a rectangle
#position
x=20
y=30
#width and height of the rectangle
wbox=50
hbox=50
square=p.Rect(x,y,wbox,hbox)
square2=p.Rect(x+200,y+200,wbox,hbox)
run=True
while run:
    screen.fill(mag) 
    # p.display.update()
    for event in p.event.get():
        if event.type== p.QUIT:
            run =False
    square.x+=5
    square.y+=5
    p.draw.rect(screen,(white),square)
    p.draw.rect(screen,(red),square2) 
    p.display.update()
    p.time.delay(500)

#if you add to x it goes to the right, but if you add to y it goes down (which doesn't make sense but that's just how it is)













    
