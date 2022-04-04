#copied and pasted from your "Code from class"


#Chris Williams
#3/28/2022


#MAria I SUarez
#learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

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
name=input('what is your name?  ') 
pygame.init()

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
SettList=['red','aqua','organge','purple']
MenuList=['Instructions','Settings', " Level One","Level Two",'Level Three','Score Board','asdasd']
SettingList=['Screen Size','Font Size','C','BC']
check=True #for the while loop
move=5 #pixels
#square variables
#inscribed Square:
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
def keepscore():
    score= 123
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+" "+name+" "+date.strftime('%m/%d/%Y'+'\n')
    print(scoreLine)
    #open a file and write in it
    myFile=open('ClassStuff\sce.txt','w')
    #if you have a specical text command thing such as \n or \t, you have to use \\ instead of just \ 
    #also, if it is in the same folder, you doing have to include the first part (ClassStuff) becuase it just assumes it us.
    myFile.write(scoreLine)
    myFile.close()
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))

#Create First button


#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def Instructions():
    global MAIN
    global INST
    text=TITLE_FNT.render('Instructions', 1, (255,0,0))
    screen.fill((255,255,255))
    # screen.blit(text, (20,20-10))

    xt=WIDTH/2-text.get_width()/2
    screen.blit(text, (xt,15))
    # text=INST_FNT.render("instructions", 1, (0,255,0)) 
    # wind.blit(text,(220,100)) 


    text=MENU_FNT.render("Circle Controls:", 1, (0,255,0)) 
    screen.blit(text,(20,130-30)) 
    text=INST_FNT.render("W is Up", 1, (0,255,0))
    screen.blit(text,(20,160-10)) 
    text=INST_FNT.render("S is Down", 1, (0,255,0)) 
    screen.blit(text,(20,190-10))  
    text=INST_FNT.render("A is Left", 1, (0,255,0)) 
    screen.blit(text,(20,220-10)) 
    text=INST_FNT.render("D is Right", 1, (0,255,0))
    screen.blit(text,(20,250-10))


    text=MENU_FNT.render("Square Controls:", 1, (0,255,0))
    screen.blit(text,(20,260))
    text=INST_FNT.render("UP ARROW is Up", 1, (0,255,0))
    screen.blit(text,(20,260+30+10))
    text=INST_FNT.render("DOWN ARROW is Down", 1, (0,255,0))
    screen.blit(text,(20,260+60+10))
    text=INST_FNT.render("LEFT ARROW is Left", 1, (0,255,0))
    screen.blit(text,(20,260+90+10))
    text=INST_FNT.render("RIGHT ARROW is Right", 1, (0,255,0))
    screen.blit(text,(20,260+120+10))


    text=MENU_FNT.render("So this is how the game works:", 1, (90,123,255))
    screen.blit(text,(20,390+40))
    text=INST_FNT.render("If you are a square, make it to the top blue circle things", 1, (90,123,255))
    screen.blit(text,(20,480))
    text=INST_FNT.render("If you are a circle, STOP THEM!!", 1, (90,123,255))
    screen.blit(text,(20,510))

    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    screen.blit(text,(10,600))
    pygame.draw.rect(screen,'red',returnSquare)
    pygame.display.update()
    if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or SETT :
        MAIN=True
        INST=False

#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
sq_color=colors.get(randColor)
def Settings():
    global MAIN
    global INST
    screen.fill(background)
    text=TITLE_FNT.render('Settings', 1, (255,0,0))
    screen.fill((255,255,255))


    xt=WIDTH/2-text.get_width()/2
    screen.blit(text, (xt,15))

    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    screen.blit(text,(10,600))
    pygame.draw.rect(screen,'red',returnSquare)
    if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690)):
        MAIN=True
        INST=False
    # screen.blit(text, (20,20-10))
    txty=243
    squareM.y=250
    for i in range(len(SettList)):
        message=SettList[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,'red', squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()

def Game():
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    move=5
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    print(startpoint[0]-ibox,startpoint[1])
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    xs=20
    ys=20
    wbox=30
    hbox=30
    square=pygame.Rect(xs,ys,wbox,hbox)
    #circle variables
    screen.fill('white')
    cr_color=colors.get('aqua')
    # sqM_color=colors.get('pink')
    sq_color=colors.get(randColor)
    while run:
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                run=False  
        keys=pygame.key.get_pressed() #this returns a list
        
        
        if keys[pygame.K_a] and square.x >=move:
            square.x -= move #substract 5 from the x value
        if keys[pygame.K_d] and square.x <WIDTH-wbox:
            square.x += move  
        #Jumping part
        if not JUMP:
            if keys[pygame.K_w]:
                square.y -= move
            if keys[pygame.K_s]:
                square.y += move   
            if keys[pygame.K_SPACE]:
                JUMP=True
        else:
            if jumpCount >=-MAX:
                square.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False#Finish circle
        if keys[pygame.K_LEFT] and xc >=rad+move:
            xc -= move #substract 5 from the x value
            insSquare.x -= move
        if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
            xc += move #substract 5 from the x value  
            insSquare.x += move
        if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
            yc += move #substract 5 from the x value
            insSquare.y += move
        if keys[pygame.K_UP] and yc >=rad+move:
            yc -= move #substract 5 from the x value  
            insSquare.y -= move
        checkCollide = square.colliderect(insSquare)
        if checkCollide:
            square.x=random.randint(wbox, WIDTH-wbox)
            square.y=random.randint(hbox, HEIGHT-hbox)   
            changeColor()
            sq_color=colors.get(randColor)
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
        screen.fill(background) 
        insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
        text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
        screen.blit(text,(10,600))
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        # pygame.draw.rect(screen,'red',returnSquare)
        pygame.display.update()
        pygame.time.delay(100)
        # if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or SETT :
        #     MAIN=True
        #     INST=False
        # pygame.display.update()
    



while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False    
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST:
        Instructions()
    if SETT:
        Settings()

    
    if case.type ==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <280))or INST :
            MAIN=False
            SETT=False
            INST=True
            # TitleMenu("INSTRUCTIONS")
            Instructions()
        if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690)):
            INST=False
            SETT=False
            MAIN=True
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT:
            MAIN=False
            SETT=True
            Settings()
        if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380)):
            MAIN=False
            SETT=False
            INST=False
            Game()
    pygame.display.update()
    pygame.time.delay(10)



# screen.fill('white')
# pygame.draw.rect(screen, sq_color, square)
# pygame.draw.rect(screen,cr_color, insSquare )
# pygame.draw.circle(screen, cr_color, (xc,yc), rad)
# if keys[pygame.K_a] and square.x >=move:
#     square.x -= move #substract 5 from the x value
# if keys[pygame.K_d] and square.x <WIDTH-wbox:
#     square.x += move  
# #Jumping part
# if not JUMP:
#     if keys[pygame.K_w]:
#         square.y -= move
#     if keys[pygame.K_s]:
#         square.y += move   
#     if keys[pygame.K_SPACE]:
#         JUMP=True
# else:
#     if jumpCount >=-MAX:
#         square.y -= jumpCount*abs(jumpCount)/2
#         jumpCount-=1
#     else:
#         jumpCount=MAX
#         JUMP=False#Finish circle
# if keys[pygame.K_LEFT] and xc >=rad+move:
#     xc -= move #substract 5 from the x value
#     insSquare.x -= move
# if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
#     xc += move #substract 5 from the x value  
#     insSquare.x += move
# if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
#     yc += move #substract 5 from the x value
#     insSquare.y += move
# if keys[pygame.K_UP] and yc >=rad+move:
#     yc -= move #substract 5 from the x value  
#     insSquare.y -= move
# checkCollide = square.colliderect(insSquare)
# if checkCollide:
#     square.x=random.randint(wbox, WIDTH-wbox)
#     square.y=random.randint(hbox, HEIGHT-hbox)   
#     changeColor()
#     sq_color=colors.get(randColor)
#     rad +=move
#     ibox=int(rad*math.sqrt(2))
#     startpoint = (int(xc-ibox/2),int(yc-ibox/2))
# insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
# text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
# screen.blit(text,(10,600))
# pygame.draw.rect(screen,'red',returnSquare)
# pygame.display.update()
# if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or SETT :
#     MAIN=True
#     INST=False
# pygame.display.update()
# pygame.time.delay(100)
        
    pygame.display.update()
    pygame.time.delay(10)