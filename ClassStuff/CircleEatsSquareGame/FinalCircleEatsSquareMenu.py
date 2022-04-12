import os, random, time, pygame, math, datetime
from turtle import screensize
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()
score=0
#Declare constants, variables, list, dictionaries, any object
#scree size
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
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')
squarecolors=('red','aqua',)
#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
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
def instr():
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
    # print("in instr")
    # myFile=open('ClassStuff\CircleEatsSquareGame\Instructions.txt', 'r')
    # yi=150
    # stuff= myFile.readlines()


    # print(stuff)
    # for line in stuff:
    #     print(line)
    #     text=INST_FNT.render(line, 1, BLACK)
    #     screen.blit(text, (40,yi))
    #     pygame.display.update()
    #     pygame.time.delay(50)
    #     yi+=50
    # myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquareGame\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('ClassStuff\CircleEatsSquareGame\sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        temp[j]=stuff[i]
        j +=1
        print(temp)
        for i in range(N):
            text=INST_FNT.render(temp[i], 1, BLACK)
            screen.blit(text, (40,yi))
            yi+=50
            pygame.display.update()
            pygame.time.delay(50)

def ChangeSquareColor(xm,ym):
    global colors
    global sq_color
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        sq_color=colors.get('red')
    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        sq_color=colors.get('aqua') 
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        sq_color=colors.get('purple')
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquareGame\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
 
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
    sq_color=colors.get(randColor)
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
            score +=1
            square.x=random.randint(wbox, WIDTH-wbox)
            square.y=random.randint(hbox, HEIGHT-hbox)   
            changeColor()
            sq_color=colors.get(randColor)
            rad +=move
            ibox=int(rad*math.sqrt(2))
            startpoint = (int(xc-ibox/2),int(yc-ibox/2))
            insSquare=pygame.Rect(startpoint[0],startpoint[1],ibox,ibox)
            print(score)
        pygame.draw.rect(screen, sq_color, square)
        pygame.draw.rect(screen,cr_color, insSquare )
        pygame.draw.circle(screen, cr_color, (xc,yc), rad)
        pygame.display.update()
        pygame.time.delay(10)
#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()

#==============================================
#
#Beginning  main prram
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
xm=0 
ym=0
f_SEET=True
sc_size=False
set_first=True
c_first=True
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
        print('main') 
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
        print('instructions')
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True   
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True       
    if SETT and f_SEET:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        f_SEET=False
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True   
    if SETT:
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
            f_SEET=True
    if LEV_I:
        screen.fill(background)
        playGame()
        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        keepScore(score)
        text=MENU_FNT.render(str(score), 1, (0,255,0)) 
        screen.blit(text,(20,130-30)) 
        # scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
        MAIN=False
        INST=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
        MAIN=False
        LEV_III=True   
    if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
        MAIN=False
        SCORE=True 
    if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        sc_size=True
        set_first=False
        f_SEET=True
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if sc_size and xm >0:
        changeScreenSize(xm,ym)
        screen.fill(background)
        TitleMenu("Screen Size")
        MainMenu(sizeList )
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    if ((xm >20 and xm <80) and (ym >300 and ym <330)) and SETT and c_first:
        screen.fill(background)
        TitleMenu("Background Color")
        ChangeSquareColor(xm,ym)
        MainMenu(squarecolors)
        c_first=False
        print('backgournd color')
        if keys[pygame.K_ESCAPE]:
            c_first=True
            set_first=True

    if ((xm >20 and xm <80) and (ym >550 and ym <580)):
        screen.fill(background)
        keepScore(121)
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