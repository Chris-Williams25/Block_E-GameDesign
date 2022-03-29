#Chris Williams
#Mrs. Suarez
#here is the main menu for the game

WIDTH=700
HEIGHT=700

wb=30
hb=30


import pygame, os, time 
pygame.init() 
wind=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cirle Eats Square") 
#create different types of fonts
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'dark.purple':[48,25,52], 'mag':[203, 195, 227], 'violet':[238,130,238], 'pink':[200,3,75]}
check=True
background= colors.get('aqua') 
while(check):
    wind.fill(background)
    for lol in pygame.event.get():
        if lol.type==pygame.QUIT:
            check=False

    TITLE_FNT=pygame.font.SysFont('arial', 80)
    MENU_FNT=pygame.font.SysFont('arial', 40) 
    INST_FNT=pygame.font.SysFont('arial', 25) 

    
    

    text=TITLE_FNT.render('Instructions', 1, (255,0,0))
    wind.fill((255,255,255))
    # wind.blit(text, (20,20-10))

    xt=WIDTH/2-text.get_width()/2
    wind.blit(text, (xt,15))
    # text=INST_FNT.render("instructions", 1, (0,255,0)) 
    # wind.blit(text,(220,100)) 


    text=MENU_FNT.render("Circle Controls:", 1, (0,255,0)) 
    wind.blit(text,(20,130-30)) 
    text=INST_FNT.render("W is Up", 1, (0,255,0))
    wind.blit(text,(20,160-10)) 
    text=INST_FNT.render("S is Down", 1, (0,255,0)) 
    wind.blit(text,(20,190-10))  
    text=INST_FNT.render("A is Left", 1, (0,255,0)) 
    wind.blit(text,(20,220-10)) 
    text=INST_FNT.render("D is Right", 1, (0,255,0))
    wind.blit(text,(20,250-10))


    text=MENU_FNT.render("Square Controls:", 1, (0,255,0))
    wind.blit(text,(20,260))
    text=INST_FNT.render("UP ARROW is Up", 1, (0,255,0))
    wind.blit(text,(20,260+30+10))
    text=INST_FNT.render("DOWN ARROW is Down", 1, (0,255,0))
    wind.blit(text,(20,260+60+10))
    text=INST_FNT.render("LEFT ARROW is Left", 1, (0,255,0))
    wind.blit(text,(20,260+90+10))
    text=INST_FNT.render("RIGHT ARROW is Right", 1, (0,255,0))
    wind.blit(text,(20,260+120+10))


    text=MENU_FNT.render("So this is how the game works:", 1, (90,123,255))
    wind.blit(text,(20,390+40))
    text=INST_FNT.render("If you are a square, make it to the top blue circle things", 1, (90,123,255))
    wind.blit(text,(20,480))
    text=INST_FNT.render("If you are a circle, STOP THEM!!", 1, (90,123,255))
    wind.blit(text,(20,510))

    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    wind.blit(text,(10,600))
    pygame.display.update()
    pygame.time.delay(100)