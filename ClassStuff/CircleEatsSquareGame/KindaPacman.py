#Chris WIlliams
#learning how to draw circles and rectangles
#use kets to move objects
#using Dictionaries

#the Bobjective of the game is for the rectanble to run away from the cirdcle, if they collide, the cthe circle es tthe square
#the cirscle witll get lardger, and a new rectangle shoudl appear somewhere on the screen.

import os, random, time, pygame
from shutil import move
#initialize pygame
pygame.init() 
#declare constants, variables, lists, dictionaries, any object
WIDTH=700
HEIGHT=700
move=5
check=True #for the while loop

#square variables
xs=20
xy=20
wbox=30
hbox=30
#circles variables
rad=15
#These two lines of code under this are to make sure the circle stays in the box, and not on the line.
xc=random.randint(rad, WIDTH-rad) 
yc=random.randint(rad, HEIGHT-rad) 
#creating the rectangle object
square=pygame.Rect(xs,xy,wbox,hbox)
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#now I will define my colors.
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'dark.purple':[48,25,52], 'mag':[203, 195, 227], 'violet':[238,130,238], 'pink':[200,3,75]}

#I want to use my colors now
backgrounds= colors.get('pink')
sq_colors=colors.get('aqua')
cr_colors=colors.get('orange')


# p.display.update()
while(check):
    screen.fill(backgrounds)
    for lol in pygame.event.get():
        if lol.type==pygame.QUIT:
            check=False

    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a]:
        square.x -= move #subtract
    if keys[pygame.K_d]:
        square.x += move
    if keys[pygame.K_w]:
        square.y -= move
    if keys[pygame.K_s]:
        square.y += move

#finish circle
    if keys[pygame.K_LEFT] and xc >=rad:
        xc -= move
    pygame.draw.rect(screen, sq_colors, square)
    pygame.draw.circle(screen, cr_colors, (xc,xy), rad) 
    pygame.display.update() 
    pygame.time.delay(10) 