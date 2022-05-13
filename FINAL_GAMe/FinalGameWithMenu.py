import os, random, time, pygame, math, datetime
from turtle import screensize
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()
score=0
#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=600
HEIGHT=600


Score=0
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
screen=pygame.display.set_mode((WIDTH,HEIGHT))

goblinspawn=random.randint(1,50)

#___________________________________________________________________________________________________________________________________


pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9.png')]
char = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\standing.png')
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
clock = pygame.time.Clock()
bg=pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\DungeonBackground.png')
BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT))  




class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 20
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('OW!!', 1, (255,0,0))
        screen.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,screen):
            fireball = pygame.image.load('FINAL_GAMe\Pictures for Final Game\\fireball-png-photos.png')
            FireBowl =pygame.transform.scale(fireball, (35,35))
            screen.blit(FireBowl,(self.x,self.y-10))


#This is the lvl 2 goblin

class enemylvltwo(object):
    walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R11E.png')]
    walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 30
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 4
        self.visible = True

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            # pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            # pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            goblins.pop(goblins.index(goblin))
            # self.visible = False
            # self.x = WIDTH+10
            # self.y = 410
            # self.visible= True
            # self.health= 2
            pygame.display.update()
            # i = 0
                # while i < 75:
            #     pygame.time.delay(10)
            #     i += 1
        print('hit')


class enemylvlthree(object):
    walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R11E.png')]
    walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 10
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 6
        self.visible = True

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            # pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            # pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            goblins.pop(goblins.index(goblin))
            print("Death")
            # self.visible = False
            # self.x = WIDTH+10
            # self.y = 410
            # self.visible= True
            # self.health= 2
            pygame.display.update()
            # i = 0
                # while i < 75:
            #     pygame.time.delay(10)
            #     i += 1
        print('hit')

class enemy(object):
    walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R11E.png')]
    walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L10E.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 2
        self.visible = True

    def draw(self,screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                screen.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            # pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            # pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            goblins.pop(goblins.index(goblin))
            # self.visible = False
            # self.x = WIDTH+10
            # self.y = 410
            # self.visible= True
            # self.health= 2
            pygame.display.update()
            # i = 0
                # while i < 75:
            #     pygame.time.delay(10)
            #     i += 1
        print('hit')



#mainloop
# font = pygame.font.SysFont('comicsans', 30, True)
# man = player(200, 410, 64,64)
# goblin = enemy(100, 410, 64, 64, 450)
# goblin2= enemy(100, 410, 64, 64, 450)
# goblin3 = enemy(100, 410, 64, 64, 450)
# goblin3= enemy(100, 410, 64, 64, 450)
# goblin4 = enemy(100, 410, 64, 64, 450)
# goblin5 = enemy(100, 410, 64, 64, 450)

# goblinlist = (goblin, goblin2, goblin3, goblin4, goblin5)
shootLoop = 0
goblinLoop = 0 
goblins =[]
bullets = []
#_______________________________________________________________________________________________________________________________________________
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')
squarecolors=('red','aqua','white')
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
    # screend.blit(text,(220,100)) 


    text=MENU_FNT.render("Player Controls:", 1, (0,255,0)) 
    screen.blit(text,(20,130-30))

    #I can take out the directions for the up and down controls because

    text=INST_FNT.render("Right Arrow is Right", 1, (0,255,0))
    screen.blit(text,(20,160-10)) 
    text=INST_FNT.render("Left Arrow is Left", 1, (0,255,0)) 
    screen.blit(text,(20,190-10))  
    text=INST_FNT.render("Space is Shooting Fireballs", 1, (0,255,0)) 
    screen.blit(text,(20,220-10)) 
    text=INST_FNT.render("They Spawn Naturally (the goblins I mean)" , 1, (0,255,0))
    screen.blit(text,(20,250-10))


    text=MENU_FNT.render("Oh Yeah! Up Arrow is jump", 1, (0,255,0))
    screen.blit(text,(20,260))
    text=INST_FNT.render("I forgot to tell you that", 1, (0,255,0))
    screen.blit(text,(20,260+30+10))
    # text=INST_FNT.render("DOWN ARROW is Down", 1, (0,255,0))
    # screen.blit(text,(20,260+60+10))
    # text=INST_FNT.render("LEFT ARROW is Left", 1, (0,255,0))
    # screen.blit(text,(20,260+90+10))
    # text=INST_FNT.render("RIGHT ARROW is Right", 1, (0,255,0))
    # screen.blit(text,(20,260+120+10))


    text=MENU_FNT.render("So this is how the game works:", 1, (90,123,255))
    screen.blit(text,(20,390+40))
    text=INST_FNT.render("Shoot fireballs and ", 1, (90,123,255))
    screen.blit(text,(20,480))
    text=INST_FNT.render("avoid goblins", 1, (90,123,255))
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
    myFile=open('FINAL_GAMe\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('FINAL_GAMe\sce.txt', 'r')
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

def ChangeSquareColor():
    global background
    global colors
    global sq_color
    if ((xm >80 and xm <140) and (ym >250 and ym <290)):
        background=colors.get('red')
        print('clciked')
    if ((xm >140 and xm <200) and (ym >300 and ym <330)):
        background=colors.get('aqua') 
        print('ouhoh')
    if ((xm >40 and xm <140) and (ym >350 and ym <380)):
        background=colors.get('white')
        print('aldsfie)')
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
 
    myFile=open('FINAL_GAMe\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen, BackGround
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000
        BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT))
    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT))
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
        BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT))
    screen=pygame.display.set_mode((WIDTH,HEIGHT))

 
#Here I actually start the game
#I had to put my redrawgame function down here becuase originally it was before i defined BackGround.

def redrawGamescreendow():
    global BackGround
    screen.blit(BackGround, (0,0))
    man.draw(screen)
    for goblin in goblins:
        goblin.draw(screen) 
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()


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
        LEV_II=False
        LEV_III=False
        LEV_I=False

        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
        # print('main') 
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
        # print('instructions')
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

        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        #Here i want the health to only be 3 

        screen.fill(background)
        man = player(200, 410, 64,64)
        goblin = enemy(100, 410, 64, 64, WIDTH-64)
        goblin2= enemy(100, 410, 64, 64, 450)
        goblin3 = enemy(100, 410, 64, 64, 450)
        goblin3= enemy(100, 410, 64, 64, 450)
        goblin4 = enemy(100, 410, 64, 64, 450)
        goblin5 = enemy(100, 410, 64, 64, 450)

        goblinlist = (goblin, goblin2, goblin3, goblin4, goblin5)
        shootLoop = 0
        goblinLoop = 0 
        goblins =[]
        bullets = []
        if len(goblins) == 0:
            checkgoblins=True
        run1 = True
        while run1:
            clock.tick(27)
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    run1 = False
                    print("quit level one") 
            for goblin in goblins:
                if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                        man.hit()
                        score=score//2
                        print(score)

            #creating the Goblin
            if goblinLoop > 0:
                goblinLoop += 1
            if goblinLoop > 30:
                goblinLoop = 0


            #creating the gun
            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 30:
                shootLoop = 0
            

                
            for bullet in bullets:
                if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                    if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        # hitSound.play()
                        goblin.hit()
                        score = score +1
                        print(score) 
                        bullets.pop(bullets.index(bullet))
                        
                if bullet.x < 600 and bullet.x > -30:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run1=False
                print('escape')
                LEV_I=False
                MAIN=True
            if goblinspawn==2 and goblinLoop == 0:
                if len(goblins) < 5:
                    goblins.append(enemy(goblin.x, goblin.y, goblin.width, goblin.height, goblin.end))
                goblinLoop = 1

            if keys[pygame.K_SPACE] and shootLoop == 0:
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 5:
                    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

                shootLoop = 1


            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                man.left = True
                man.right = False
                man.standing = False
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0
                
            if not(man.isJump):
                if keys[pygame.K_UP]:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10

            #winning portion of game

            # if goblin.x < 150:
            #     pointsforgoblin=True
            # while pointsforgoblin:
            #     print('goblin winning') 
            # 
            #    
            goblinspawn=random.randint(1,50)
            redrawGamescreendow()


        LEV_I=False
        MAIN=True
        xm=0
        ym=0
    if LEV_II:
        bg=pygame.image.load('FINAL_GAMe\Pictures for Final Game\istockphoto-1308121289-170667a.jpg')
        BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT)) 
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        # screen.fill(background)
        # TitleMenu("LEVEL II")

        #Here i want the health to only be 3 
        # if keys[pygame.K_ESCAPE]:
        #     LEV_I=False
        #     MAIN=True
        # if keys[pygame.K_ESCAPE]:
        #     LEV_III=False
        #     MAIN=True
        screen.fill(background)
        man = player(200, 410, 64,64)
        goblin = enemylvltwo(100, 410, 64, 64, WIDTH-64)
        goblin2= enemy(100, 410, 64, 64, 450)
        goblin3 = enemy(100, 410, 64, 64, 450)
        goblin3= enemy(100, 410, 64, 64, 450)
        goblin4 = enemy(100, 410, 64, 64, 450)
        goblin5 = enemy(100, 410, 64, 64, 450)

        goblinlist = (goblin, goblin2, goblin3, goblin4, goblin5)
        shootLoop = 0
        goblinLoop = 0 
        goblins =[]
        bullets = []
        run2 = True
        while run2:
            bg=pygame.image.load('FINAL_GAMe\Pictures for Final Game\istockphoto-1308121289-170667a.jpg')
            BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT)) 
            
            clock.tick(27)
            
            for event2 in pygame.event.get():
                if event2.type == pygame.QUIT:
                    run2 = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run2=False
                print('escape')
                LEV_II=False
                MAIN=True
            for goblin in goblins:
                if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                        man.hit()
                        score=score//3
                        print(score)

            #creating the Goblin
            if goblinLoop > 0:
                goblinLoop += 1
            if goblinLoop > 30:
                goblinLoop = 0


            #creating the gun
            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 30:
                shootLoop = 0

            
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         run = False
            # if keys[pygame.K_ESCAPE]:
            #     LEV_II=False
            #     MAIN=True
            for bullet in bullets:
                if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                    if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        # hitSound.play()
                        goblin.hit()
                        bullets.pop(bullets.index(bullet))
                        
                if bullet.x < 600 and bullet.x > -30:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))



            if goblinspawn == 2 and goblinLoop == 0:
                if len(goblins) < 5:
                    goblins.append(enemy(goblin.x, goblin.y, goblin.width, goblin.height, goblin.end))
                goblinLoop = 1

            if keys[pygame.K_SPACE] and shootLoop == 0:
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 5:
                    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

                shootLoop = 1
            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                man.left = True
                man.right = False
                man.standing = False
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0
                
            if not(man.isJump):
                if keys[pygame.K_UP]:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10

            #winning portion of game

            # if goblin.x < 150:
            #     pointsforgoblin=True
            # while pointsforgoblin:
            #     print('goblin winning') 
            # 
            #   
            goblinspawn=random.randint(1,50) 
            redrawGamescreendow()
        LEV_II=False
        MAIN=True
    
    if LEV_III:

        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        # screen.fill(background)
        # TitleMenu("LEVEL III")

        #Here i want the health to only be 3 
        # if keys[pygame.K_ESCAPE]:
        #     LEV_I=False
        #     MAIN=True
        # if keys[pygame.K_ESCAPE]:
        #     LEV_II=False
        #     MAIN=True
        screen.fill(background)
        man = player(200, 410, 64,64)
        goblin = enemylvlthree(100, 410, 64, 64, WIDTH-64)
        goblin2= enemy(100, 410, 64, 64, 450)
        goblin3 = enemy(100, 410, 64, 64, 450)
        goblin3= enemy(100, 410, 64, 64, 450)
        goblin4 = enemy(100, 410, 64, 64, 450)
        goblin5 = enemy(100, 410, 64, 64, 450)

        goblinlist = (goblin, goblin2, goblin3, goblin4, goblin5)
        shootLoop = 0
        goblinLoop = 0 
        goblins =[]
        bullets = []
        run3 = True
        while run3:
            bg=pygame.image.load('FINAL_GAMe\Pictures for Final Game\More-dungeon-background-variations-Crimson-Court-add-on-at-.png')
            BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT)) 
            clock.tick(27)

            for goblin in goblins:
                if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                        man.hit()
                        score=score//2

            #creating the Goblin
            if goblinLoop > 0:
                goblinLoop += 1
            if goblinLoop > 30:
                goblinLoop = 0


            #creating the gun
            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 30:
                shootLoop = 0
            
            for event3 in pygame.event.get():
                if event3.type == pygame.QUIT:
                    run = False
                
            for bullet in bullets:
                if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                    if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        # hitSound.play()
                        goblin.hit()
                        score=score//3
                        print(score)
                        bullets.pop(bullets.index(bullet))
                        
                if bullet.x < 600 and bullet.x > -30:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            keys = pygame.key.get_pressed()

            for event3 in pygame.event.get():
                if event3.type == pygame.QUIT:
                    run3 = False
            if keys[pygame.K_ESCAPE]:
                run3=False
                LEV_III=False
                MAIN=True

            if goblinspawn == 2 and goblinLoop == 0:
                if len(goblins) < 5:
                    goblins.append(enemy(goblin.x, goblin.y, goblin.width, goblin.height, goblin.end))
                goblinLoop = 1

            if keys[pygame.K_SPACE] and len(goblins) > 0 and shootLoop == 0:
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 5:
                    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

                shootLoop = 1


            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                man.left = True
                man.right = False
                man.standing = False
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0
                
            if not(man.isJump):
                if keys[pygame.K_UP]:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10

            #winning portion of game

            # if goblin.x < 150:
            #     pointsforgoblin=True
            # while pointsforgoblin:
            #     print('goblin winning') 
            # 
            #    
            goblinspawn=random.randint(1,50)
            redrawGamescreendow()
        LEV_III=False
        MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        keepScore(score)
        texty=250
        myFile=open('FINAL_GAMe\sce.txt', 'r')
        yi=150
        stuff= myFile.readlines()
        for i in range(len(stuff)):
            newscoreline=MENU_FNT.render(stuff[i],1,'green')
            textx=WIDTH/2-newscoreline.get_width()/2
            screen.blit(newscoreline,(textx,texty))
            texty+=50
        pygame.display.update()
        # myFile.close()
        # stuff.sort()
        # N=len(stuff)-1
        # temp=[]
        # j=0
        # for i in range(N, -1, -1):
        #     print(i,stuff[i])
        #     temp[j]=stuff[i]
        #     j +=1
        #     print(temp)
        #     for i in range(N):
        #         text=INST_FNT.render(temp[i], 1, BLACK)
        #         screen.blit(text, (40,yi))
        #         yi+=50
        #         pygame.display.update()
        #         pygame.time.delay(50)
        
        # text=MENU_FNT.render(str(score)+str(name), 1, (0,255,0)) 
        # screen.blit(text,(20,260+120+10))
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
        MainMenu(sizeList)
        if keys[pygame.K_ESCAPE]:
            sc_size=False
            set_first=True
    c_first = True
    if ((xm >80 and xm <140) and (ym >300 and ym <330)) and SETT:
        screen.fill(background)
        TitleMenu("Background Color")
        ChangeSquareColor()
        MainMenu(squarecolors)
        screen.fill(background)
        pygame.display.update()
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
    goblinspawn=random.randint(1,100)
    pygame.display.update()
    pygame.time.delay(10)
os.system('cls')
pygame.quit()
# https://docs.google.com/document/d/1MPhCOEWBFAyCdFYwEDHCUhnFk4VMdPeV-9zjy3ZTBW0/edit#heading=h.cpnqkbkruujo 