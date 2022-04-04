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

 #==============================================================================================
 #Chris Williams 
 #4.3.2022

import os, random, time, pygame, math, datetime
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()
 

#Declare constants, variables, list, dictionaries, any object
#scree size
returnSquare=pygame.Rect(20,660,30,30)
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
#List f messages
ColorsList=['white', 'red', 'aqua','orange','purple','navy','pink']
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Square Colors','Backgrnd Color','Screen size','Other Options']
check=True #for the while loop
 
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')
 
#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
LEVIIBack= colors.get('aqua') 
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
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
def colorspage():
    text=TITLE_FNT.render('Square Colors', 1, (255,0,0))
    screen.fill((255,255,255))
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text, (xt,15))
    global MAIN
    global SETT
    global LEV_I
    global LEV_II
    global LEV_III
    global INST
    global colors
    global sq_color
    screen.fill(background)
    text=TITLE_FNT.render('Colors page', 1, (255,0,0))
    screen.fill((255,255,255))
    txty=243
    squareM.y=250
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        sq_color=colors.get('white')
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)):
        sq_color=colors.get('red')
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380)) :
        sq_color=colors.get('aqua')
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430)):
        sq_color=colors.get('orange')
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480)) :
        sq_color=colors.get('purple')
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530)):
        sq_color=colors.get('navy')
    for i in range(len(ColorsList)):
        message=ColorsList[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,'red', squareM )
        squareM.y +=50
        txty+=50

    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    screen.blit(text,(10,600))

    pygame.draw.rect(screen,'red',returnSquare)
    if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
        SETT=False
        LEV_I=False
        LEV_II=False
        LEV_III=False
        INST=False
        MAIN=True
    pygame.display.update()


def Settings():
    global sq_color
    global SETT
    global MAIN
    global INST
    global LEV_I
    global LEV_II
    global LEV_III
    screen.fill(background)
    text=TITLE_FNT.render('Settings', 1, (255,0,0))
    screen.fill((255,255,255))


    xt=WIDTH/2-text.get_width()/2
    screen.blit(text, (xt,15))

    text=MENU_FNT.render("CLICK HERE TO RETURN TO MENU", 1, (90,123,255))
    screen.blit(text,(10,600))
    pygame.draw.rect(screen,'red',returnSquare)
    if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
        SETT=False
        LEV_I=False
        LEV_II=False
        LEV_III=False
        INST=False
        MAIN=True
    # screen.blit(text, (20,20-10))
    txty=243
    squareM.y=250
    for i in range(len(SettingList)):
        message=SettingList[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,'red', squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        SETT=False
        MAIN=False
        colorspage()
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
            sq_color=colors.get('white')
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT :
            sq_color=colors.get('red')
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_I :
            sq_color=colors.get('aqua')
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_II :
            sq_color=colors.get('orange')
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
            sq_color=colors.get('purple')
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
            sq_color=colors.get('navy')

def instr():
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
    # if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
    #     INST=False
    #     MAIN=True


def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it
    # when y write it erases the prev
    myFile=open('CircleEatsSquareGame\FileForStuff.txt','a')
    myFile.write(scoreLine)
    myFile.close()
# def playGame2():
    # text=TITLE_FNT.render('LEVEL II', 1, (255,0,0))
    # screen.fill((255,255,255))
    # # screen.blit(text, (20,20-10))

    # xt=WIDTH/2-text.get_width()/2
    # screen.blit(text, (xt,15))
    # move=5 #pixels
    # #square variables
    # xs=20
    # ys=20
    # wbox=30
    # hbox=30
    # #circle variables
    # rad=15
    # xc=random.randint(rad, WIDTH-rad)
    # yc=random.randint(rad, HEIGHT-rad)
    # #inscribed Square:
    # ibox=int(rad*math.sqrt(2))
    # startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    # print(startpoint[0]-ibox,startpoint[1])
    # insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    # #creating the rect object
    # square=pygame.Rect(xs,ys,wbox,hbox)
    # global MAIN
    # global LEV_I
    # startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    # insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    # sq_color=colors.get(randColor)
    # MAX=10
    # jumpCount=MAX
    # JUMP=False
    # run=True
    # while run:
    #     screen.fill(background)
    #     keys=pygame.key.get_pressed()
    #     for event in pygame.event.get():
    #         if event.type==pygame.QUIT:
    #             run=False
    #             MAIN=True
    #             LEV_I=False
               
    #             print ("I want out", run)
               
    #     if keys[pygame.K_ESCAPE]:
    #         run=False        
    #     if keys[pygame.K_a] and square.x >=move:
    #             square.x -= move #substract 5 from the x value
    #     if keys[pygame.K_d] and square.x <WIDTH-wbox:
    #         square.x += move  
    #     #Jumping part
    #     if not JUMP:
    #         if keys[pygame.K_w]:
    #             square.y -= move
    #         if keys[pygame.K_s]:
    #             square.y += move  
    #         if keys[pygame.K_SPACE]:
    #             JUMP=True
    #     else:  
    #         if jumpCount >=-MAX:
    #             square.y -= jumpCount*abs(jumpCount)/2
    #             jumpCount-=1
    #         else:
    #             jumpCount=MAX
    #             JUMP=False
 
    # #Finish circle
    #     if keys[pygame.K_LEFT] and xc >=rad+move:
    #         xc -= move #substract 5 from the x value
    #         insSquare.x -= move
    #     if keys[pygame.K_RIGHT] and xc <=WIDTH -(rad+move):
    #         xc += move #substract 5 from the x value  
    #         insSquare.x += move
    #     if keys[pygame.K_DOWN] and yc <=HEIGHT-(rad+move):
    #         yc += move #substract 5 from the x value
    #         insSquare.y += move
    #     if keys[pygame.K_UP] and yc >=rad+move:
    #         yc -= move #substract 5 from the x value  
    #         insSquare.y -= move
           
    #     checkCollide = square.colliderect(insSquare)
    #     if checkCollide:
    #         square.x=random.randint(wbox, WIDTH-wbox)
    #         square.y=random.randint(hbox, HEIGHT-hbox)  
    #         changeColor()
    #         sq_color=colors.get(randColor)
    #         rad +=move
    #         ibox=int(rad*math.sqrt(2))
    #         startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    #         insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #     pygame.draw.rect(screen, sq_color, square)
    #     pygame.draw.rect(screen,cr_color, insSquare )
    #     pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    #     pygame.display.update()
    #     pygame.time.delay(10)
def playGame():
    global score
    score=0
    move=5 #pixels
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30
    #circle variables
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    #inscribed Square:
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    print(startpoint[0]-ibox,startpoint[1])
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    square=pygame.Rect(xs,ys,wbox,hbox)
    global MAIN
    global LEV_I
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    sq_color=colors.get('red')
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True

    while run:
        screen.fill(background)
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                MAIN=True
                LEV_I=False
               
                print ("I want out", run)
               
        if keys[pygame.K_ESCAPE]:
            run=False        
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
                JUMP=False
 
    #Finish circle
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
            sq_color=colors.get('red')
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
            score +=1
            print(score)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
    if int(score) >=10:
        print('game done')
        screen.fill('red')
def playGame2():
    global score
    score=0
    move=5 #pixels
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30
    #circle variables
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    #inscribed Square:
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    print(startpoint[0]-ibox,startpoint[1])
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    square=pygame.Rect(xs,ys,wbox,hbox)
    global MAIN
    global LEV_I
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    sq_color=colors.get('red')
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True

    while run:
        screen.fill('aqua')
        text=TITLE_FNT.render('LEVEL 2', 1, (255,0,0))
        # screen.fill((255,255,255))
        # screen.blit(text, (20,20-10))
        xt=WIDTH/2-text.get_width()/2
        screen.blit(text, (xt,15))
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                MAIN=True
                LEV_I=False
                print ("I want out", run)
               
        if keys[pygame.K_ESCAPE]:
            run=False        
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
                JUMP=False
 
    #Finish circle
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
            sq_color=colors.get('red')
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
            score +=1
            print(score)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
def playGame3():
    global score
    score=0
    move=5 #pixels
    #square variables
    xs=20
    ys=20
    wbox=30
    hbox=30
    #circle variables
    rad=15
    xc=random.randint(rad, WIDTH-rad)
    yc=random.randint(rad, HEIGHT-rad)
    #inscribed Square:
    ibox=int(rad*math.sqrt(2))
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    print(startpoint[0]-ibox,startpoint[1])
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    #creating the rect object
    square=pygame.Rect(xs,ys,wbox,hbox)
    global MAIN
    global LEV_I
    startpoint = (int(xc-ibox/2),int(yc-ibox/2))
    insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
    sq_color=colors.get('red')
    MAX=10
    jumpCount=MAX
    JUMP=False
    run=True

    while run:
        screen.fill('purple')
        text=TITLE_FNT.render('LEVEL 3', 1, (255,0,0))
        # screen.fill((255,255,255))
        # screen.blit(text, (20,20-10))
        xt=WIDTH/2-text.get_width()/2
        screen.blit(text, (xt,15))
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                MAIN=True
                LEV_I=False
                print ("I want out", run)
               
        if keys[pygame.K_ESCAPE]:
            run=False        
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
                JUMP=False
 
    #Finish circle
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
            sq_color=colors.get('red')
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
            score +=1
            print(score)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
# def Menupicking():
#     MAIN=True
#     INST=False
#     SETT=False
#     LEV_I=False
#     LEV_II=False
#     LEV_III=False
#     SCORE=False
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
#         MAIN=False
#         INST=True
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT :
#         MAIN=False
#         SETT=True  
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_I :
#         MAIN=False
#         LEV_I=True  
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_II :
#         MAIN=False
#         LEV_II=True  
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
#         MAIN=False
#         LEV_III=True  
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
#         MAIN=False
#         SCORE=True
#     if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
#         SETT=False
#         LEV_I=False
#         LEV_II=False
#         LEV_III=False
#         INST=False
#         MAIN=True
#sq_color=colors.get('navy')
#Making a rand c f the square
# changeColor()
# sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
first=True
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
        print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
        SETT=False
        LEV_I=False
        LEV_II=False
        LEV_III=False
        INST=False
        MAIN=True
    if MAIN:
        first=True
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
            MAIN=False
            INST=True
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT :
            MAIN=False
            SETT=True  
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_I :
            MAIN=False
            LEV_I=True  
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_II :
            MAIN=False
            LEV_II=True  
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
            MAIN=False
            LEV_III=True  
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
            MAIN=False
            SCORE=True
        if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
            SETT=False
            LEV_I=False
            LEV_II=False
            LEV_III=False
            INST=False
            MAIN=True
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
            SETT=False
            LEV_I=False
            LEV_II=False
            LEV_III=False
            INST=False
            MAIN=True
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
        if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
            SETT=False
            LEV_I=False
            LEV_II=False
            LEV_III=False
            INST=False
            MAIN=True
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        Settings()
        if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
            SETT=False
            LEV_I=False
            LEV_II=False
            LEV_III=False
            INST=False
            MAIN=True
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
    # if SETT: 
    #     if keys[pygame.K_ESCAPE]:
    #         INST=False
    #         MAIN=True
    #         first=True
    #     if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
    #         SETT=False
    #         LEV_I=False
    #         LEV_II=False
    #         LEV_III=False
    #         INST=False
    #         MAIN=True
    if LEV_I:
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        print("I shld be t")
        mouse_pos=(0,0)
    if LEV_II:
        screen.fill(LEVIIBack)
        # TitleMenu('LEVEL TWO')
        playGame2()
        LEV_II=False
        MAIN=True
        mouse_pos=(0,0)
        # if keys[pygame.K_ESCAPE]:
        #     LEV_II=False
        #     MAIN=True
    if LEV_III:
        TitleMenu("LEVEL III")
        playGame3()
        LEV_III=False
        MAIN=True
        mouse_pos=(0,0) 
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        SCORE=False
        MAIN=True
        text=MENU_FNT.render('your score is '+str(score), 1, (0,255,0))
        screen.blit(text,(20,260))
        #call funct t print scres
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or INST :
    #     MAIN=False
    #     INST=True
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT :
    #     MAIN=False
    #     SETT=True  
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_I :
    #     MAIN=False
    #     LEV_I=True  
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_II :
    #     MAIN=False
    #     LEV_II=True  
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
    #     MAIN=False
    #     LEV_III=True  
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
    #     MAIN=False
    #     SCORE=True
    # if ((mouse_pos[0] >20 and mouse_pos[0] <50) and (mouse_pos[1] >660 and mouse_pos[1] <690))or MAIN :
    #     SETT=False
    #     LEV_I=False
    #     LEV_II=False
    #     LEV_III=False
    #     INST=False
    #     MAIN=True
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580)):
        screen.fill(background)
        keepScore(score)
        text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you exit", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thank you for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)
 
os.system('cls')
pygame.quit()