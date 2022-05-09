#Chris Williams
#4/24/2022

import os, random, time, pygame as p, math, datetime
from tkinter import Y
os.system('cls')

p.init() 
WIDTH=700
HEIGHT=700
win=p.display.set_mode((WIDTH,HEIGHT))
# walkRight = [p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R1.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R2.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R3.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R4.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R5.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R6.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R7.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R8.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R9.png')]
# walkLeft = [p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L1.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L2.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L3.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L4.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L5.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L6.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L7.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L8.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L9.png')]
Hero = p.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\standing.png')
vel = 5
Enemy= p.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R11E.png')
enemyvel=3
Arrow= p.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\\arrow.png')
class hero(object):
    def __init__(self,x,y,WIDTH,HEIGHT):
        self.x = x
        self.y = y
        self.vel = vel
        self.isright = False
        self.isleft = False
        self.isstanding = True
    def draw(self, win): #make s
        win.blit(Hero,self.x,self.y)

class enemy(object):
    # walkRight = [p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R1E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R2E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R3E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R4E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R5E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R6E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R7E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R8E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R9E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R10E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\R11E.png')]
    # walkLeft = [p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L1E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L2E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L3E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L4E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L5E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L6E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L7E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L8E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L9E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L10E.png'), p.image.load('ClassStuff\Images\Images\p-Tutorials-master\Game\L11E.png')]
    def __init__(self,x,y,WIDTH,HEIGHT,end):
        self.x = x
        self.y = y
        self.end = end
        self.enemyvel = enemyvel
        self.path = [self.x, self.end]
    def draw(self, win):
        win.blit(Enemy,self.x,self.y)
        
class arrow(object):
    def __init__(self,x,y,WIDTH,HEIGHT,vector):
        self.x = x
        self.y = y
        self.vector = vector
        self.vel = vel*vector
    def draw(self):
        win.blit(Arrow,self.x,self.y)

def drawgamewindow():
    player.draw(win) 
    goblin.draw(win) 

player = hero(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)

run=True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    drawgamewindow()