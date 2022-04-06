#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame
import os, random, time, pygame, math, datetime
from pickle import TRUE
#initialize pygame
# name=input('what is your name?  ') 
pygame.init()
check=True
returnSquare=pygame.Rect(20,660,30,30)
#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=TRUE
INST=False
SETT=False
LEV_I=False
#List f messages
# SettList=['red','aqua','organge','purple']
# MenuList=['Instructions','Settings', " Level One","Level Two",'Level Three','Score Board','asdasd']
# SettingList=['Screen Size','Font Size','C','BC']
# check=True #for the while loop
move=5 #pixels
#square variables
#inscribed Square:
rad=15
ox=20
oy=20
#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
rad=15

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')

#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

bg=pygame.image.load('ClassStuff\CircleEatsSquareGame\Images\\bg.jpg')

otherthing=pygame.image.load('ClassStuff\CircleEatsSquareGame\Images\Images\Pygame-Tutorials-master\Game\R4E.png')

while(check):
    for lol in pygame.event.get():
        screen.blit(bg,(0,0))
        screen.blit(otherthing,(ox,oy))
        if lol.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a]:
        ox -= move #subtract
    if keys[pygame.K_d]:
        ox += move
    if keys[pygame.K_w]:
        oy -= move
    if keys[pygame.K_s]:
        oy += move
pygame.display.update()
pygame.time.delay(10)

