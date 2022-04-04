#Chris Williams
#2/24/2022

import pygame, os, time 

#Chris Williams
#Mrs. Suarez
#here is the main menu for the game
import pygame, os, time 
pygame.init() 

WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30

square=pygame.Rect(xs,ys,wb,hb)
wind=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cirle Eats Square") 
#create different types of fonts
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'dark.purple':[48,25,52], 'mag':[203, 195, 227], 'violet':[238,130,238], 'pink':[200,3,75]}
MenuList=['Instructions','h','g','r','w','e','p']
# wind.fill((255,255,255))
background= colors.get('aqua') 
TITLE_FNT=pygame.font.SysFont('arial', 80)
MENU_FNT=pygame.font.SysFont('arial', 40) 
INST_FNT=pygame.font.SysFont('arial', 30) 
text=TITLE_FNT.render('MENU', 1, (255,0,0))
wind.fill((255,255,255))
#get the width of the text
#x-value should be equal to half the width minus half the width of the the text (WIDTH/2 -wText/2)
xt=WIDTH/2-text.get_width()/2
wind.blit(text, (xt,50)) 
txty=100
for i in range(7):
    pygame.draw.rect(wind,(0,255,0),square)
    message=MenuList[i]
    text=INST_FNT.render(message, 1, (0,255,0)) 
    wind.blit(text,(220,100))
    pygame.draw.rect(wind,(102,153,255),square)
    txty +=50
    square.y +=50
text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
pygame.time.delay(1000)