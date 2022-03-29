#Chris Williams
#Mrs. Suarez
#here is the main menu for the game
from pickle import FALSE
from sys import maxsize
from xml.dom import XMLNS_NAMESPACE
import pygame, os, time, random
pygame.init() 

WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=40
hb=40
mxs=50
mys=250
MAIN=True
INST=False
SETT=False
GAME=False
check=True #for the while loop
move=5 #pixels
screen=pygame.display.set_mode((WIDTH,HEIGHT))
MAX=10
rad=15
xs=random.randint(30,670)
ys=670
wbox=30
hbox=30
#circle variables
rad=15
# xc=random.randint(rad, WIDTH-rad)
# yc=685
xc=350
yc=350
endingthing=False

#these are the colors:
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
thingtoendgame=pygame.Rect(0,0,700,40)
square=pygame.Rect(xs,ys,wbox,hbox)
# randColors=random.choice(list(colors))
background=colors.get('pink')
# sq_color=colors.get('navy')
#making a rand c f the square

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')
square2=pygame.Rect(mxs,mys,wb,hb)
wind=pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Cirle Eats Square") 
#create different types of fonts
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153,255], 'orange':[255,85,0], 'dark.purple':[48,25,52], 'mag':[203, 195, 227], 'violet':[238,130,238], 'pink':[200,3,75]}
MenuList=['Instructions','Level 1','Level 2','Level 3','Settings','Score Board','Return']
SettingsList=['Screen settings','Font size','Circle Color','Sensitivity'] 
# wind.fill((255,255,255))

background= colors.get('aqua') 
TITLE_FNT=pygame.font.SysFont('arial', 80)
MENU_FNT=pygame.font.SysFont('arial', 40) 
INST_FNT=pygame.font.SysFont('arial', 30)

def TitleFunction():
    text=TITLE_FNT.render('MENU', 1, (255,0,0))
    #get the width of the text
    #x-value should be equal to half the width minus half the width of the the text (WIDTH/2 -wText/2)
    xt=WIDTH/2-text.get_width()/2
    wind.blit(text, (xt,50)) 
    
    wind.blit(text,(10,600))
    text=TITLE_FNT.render('MENU', 1, (255,0,0))
    wind.fill((200,200,200))
    #get the width of the text
    #x-value should be equal to half the width minus half the width of the the text (WIDTH/2 -wText/2)
    xt=WIDTH/2-text.get_width()/2
    wind.blit(text, (xt,50))
    pygame.time.delay(1000)
    pygame.display.update()

def changecolor():
    global randColors
    colorCheck=True
    while(colorCheck): 
        randColors=random.choice(list(colors))
        if colors.get(randColors)==background:
            randColors=random.choice(list(colors))
        else:
            colorCheck=False
#this is a function that uses a parameter.
def Menu():
    txty=100
    for i in range(7):
        pygame.draw.rect(wind,(0,255,0),square2)
        message=MenuList[i]
        text=INST_FNT.render(message, 1, (0,255,0)) 
        wind.blit(text,(100,square2.y))
        pygame.draw.rect(wind,(102,153,255),square2)
        txty +=50
        square2.y +=50
    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    pygame.time.delay(1000)
    pygame.display.update()
    
def Instructions():
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
    pygame.time.delay(1000)



changecolor()
sq_color=colors.get(randColors)
cr_color=colors.get('white')
MAX=10
jumpcount=MAX
JUMP=False 

gaming=True
while(gaming):
    wind.fill(background)
    TitleFunction()
    Menu()
    pygame.display.update()
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            gaming=False


    keys=pygame.key.get_pressed() #this returns a list
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos) 
        if ((mouse_pos[0] >20 and mouse_pos[0] <60) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
            MAIN=False
            INST=True
            screen.fill(background) 
            TitleFunction("INSTRUCTIONS")
# while(check):
#     screen.fill(background)
#     for case in pygame.event.get():
#         if case.type==pygame.QUIT:
#             check=False
#     keys=pygame.key.get_pressed() #this returns a list
#     if keys[pygame.K_a] and square.x >=move:
#         square.x -= move #substract 5 from the x value
#     if keys[pygame.K_d] and square.x <WIDTH-(wbox+move):
#         square.x += move
#     # if keys[pygame.K_s] and square.x >=move:
#     #     square.y += move #substract 5 from the x value
#     # if keys[pygame.K_w] and square.x <WIDTH-(hbox+move):
#     #     square.y -= move
#     #here we jump
#     if not JUMP:
#         if keys[pygame.K_w] and square.y >=move:
#             square.y -= move
#         if keys[pygame.K_s] and square.y <HEIGHT-(hbox+move):
#             square.y += move   
#         if keys[pygame.K_SPACE]: 
#             JUMP=True 
#     else:
#         if jumpcount >=-MAX:
#             square.y -= (jumpcount*abs(jumpcount))/2 #abs is absolute value
#             jumpcount -=1
#         else:
#             jumpcount=MAX 
#             JUMP=False
# #Finish circle
#     if keys[pygame.K_LEFT] and xc >=rad+move:
#         xc -= move #substract 5 from the x value
#     if keys[pygame.K_RIGHT] and xc <=WIDTH-(rad+move):
#         xc += move
#     if keys[pygame.K_UP] and yc>=rad+move:
#         yc -= move
#     if keys[pygame.K_DOWN] and yc<=HEIGHT-(rad+move):
#         yc += move

#     checkCollide=square.collidepoint(xc,yc) 
#     if checkCollide:
#         # xc=random.randint(wbox, WIDTH-wbox)
#         # yc=700-rad-5
#         xc=350
#         yc=350
#         changecolor()
#         sq_color=colors.get(randColors) 
#         rad+=move
#         xs=random.randint(30,670)
#         ys=670
#         square=pygame.Rect(xs,ys,wbox,hbox)
        
#     checkEndgame=square.collidepoint(40,40)
#     checkEndgame2=square.collidepoint(350,40)
#     checkEndgame3=square.collidepoint(660,40)

#     if checkEndgame:
#         background=colors.get('navy')
#         endingthing=True
#     if checkEndgame2:
#         background=colors.get('navy')
#         endingthing=True
#     if checkEndgame3:
#         background=colors.get('navy')
#         endingthing=True
#     # while(endingthing):
#     #     pygame.time.delay(50)
#     #     pygame.QUIT
#     # if keys[pygame.K_LEFT] and square2.x >=move:
#     #     square2.x -= move #substract 5 from the x value
#     # if keys[pygame.K_RIGHT] and square2.x <WIDTH-wbox:
#     #     square2.x += move
#     # if keys[pygame.K_UP] and square2.y >=move:
#     #     square2.y -= moves
#     # if keys[pygame.K_DOWN] and square2.y <HEIGHT-hbox:
#     #     square.y += move
#     pygame.draw.rect(screen, sq_color, square)
    
#     # pygame.draw.rect(screen, cr_color, square2)
#     pygame.draw.circle(screen, ((255,255,255)), (xc,yc), rad)
#     pygame.draw.rect(screen,'aqua',thingtoendgame)
#     pygame.draw.circle(screen, 'red', (40,40), 15)
#     pygame.draw.circle(screen, 'red', (350,40), 15)
#     pygame.draw.circle(screen, 'red', (640,40), 15)


# while(check):
#     wind.fill(background)
#     for lol in pygame.event.get():
#         if lol.type==pygame.QUIT:
#             check=False

#     TITLE_FNT=pygame.font.SysFont('arial', 80)
#     MENU_FNT=pygame.font.SysFont('arial', 40) 
#     INST_FNT=pygame.font.SysFont('arial', 30) 


#     text=TITLE_FNT.render('MENU', 1, (255,0,0))
#     wind.fill((255,255,255))
#     #get the width of the text
#     #x-value should be equal to half the width minus half the width of the the text (WIDTH/2 -wText/2)
#     xt=WIDTH/2-text.get_width()/2
#     wind.blit(text, (xt,50)) 

#     # text=INST_FNT.render("instructions", 1, (0,255,0)) 
#     # wind.blit(text,(220,100)) 


#     text=MENU_FNT.render("Instructions", 1, (0,255,0)) 
#     wind.blit(text,(90,243)) 

#     #creating a square:


    
#     ##useless junk:
#     # text=INST_FNT.render("W is Up", 1, (0,255,0))
#     # wind.blit(text,(20,160-10)) 
#     # text=INST_FNT.render("S is Down", 1, (0,255,0)) 
#     # wind.blit(text,(20,190-10))  
#     # text=INST_FNT.render("A is Left", 1, (0,255,0)) 
#     # wind.blit(text,(20,220-10)) 
#     # text=INST_FNT.render("D is Right", 1, (0,255,0))
#     # wind.blit(text,(20,250-10))


#     # text=MENU_FNT.render("Square Controls:", 1, (0,255,0))
#     # wind.blit(text,(20,260))
#     # text=INST_FNT.render("UP ARROW is Up", 1, (0,255,0))
#     # wind.blit(text,(20,260+30+10))
#     # text=INST_FNT.render("DOWN ARROW is Down", 1, (0,255,0))
#     # wind.blit(text,(20,260+60+10))
#     # text=INST_FNT.render("LEFT ARROW is Left", 1, (0,255,0))
#     # wind.blit(text,(20,260+90+10))
#     # text=INST_FNT.render("RIGHT ARROW is Right", 1, (0,255,0))
#     # wind.blit(text,(20,260+120+10))


#     # text=MENU_FNT.render("So this is how the game works:", 1, (90,123,255))
#     # wind.blit(text,(20,390+40))
#     # text=INST_FNT.render("If you are a square, make it to the top blue circle things", 1, (90,123,255))
#     # wind.blit(text,(20,480))
#     # text=INST_FNT.render("If you are a circle, STOP THEM!!", 1, (90,123,255))
#     # wind.blit(text,(20,510))

#     text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
#     wind.blit(text,(10,600))
#     pygame.display.update()
#     pygame.time.delay(100)