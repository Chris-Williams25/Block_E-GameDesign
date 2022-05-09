import pygame
pygame.init()
WIDTH=600
HEIGHT=600
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9.png')]
char = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\standing.png')
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
clock = pygame.time.Clock()
bg=colors.get('white')



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

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 20
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
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

    def draw(self,win):
            fireball = pygame.image.load('FINAL_GAMe\Pictures for Final Game\\fireball-png-photos.png')
            FireBowl =pygame.transform.scale(fireball, (35,35))
            win.blit(FireBowl,(self.x,self.y-10))



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

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            # pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            # pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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

        

def redrawGameWindow():
    win.fill(bg)
    man.draw(win)
    for goblin in goblins:
        goblin.draw(win) 
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
goblinLoop = 0 
goblins =[]
bullets = []
pointsforgoblin=False
run = True
while run:
    clock.tick(27)

    for goblin in goblins:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_g] and goblinLoop == 0:
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
            
    redrawGameWindow()

pygame.quit()


