import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L1.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L2.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L3.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L4.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L5.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L6.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L7.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L8.png'), pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\L9.png')]
bg = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\\157-1573121_telephone-lines-png-power-lines-silhouette.png')
char = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\standing.png')
# rip=pygame
# rip=pygame.transform.scale(rip,(50,50)) 
clock = pygame.time.Clock()


x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
deathsquare=pygame.Rect(250,240,40,40)
manSquare=pygame.Rect(x,y,20,20)


def redrawGameWindow():
    global walkCount
    win.fill((255,255,255))
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    pygame.draw.rect(win,(255,0,0), deathsquare)
    pygame.draw.rect(win,(255,0,0), manSquare)
    pygame.display.update()


#mainloop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x >400:
        print('castle') 
        bg = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\png_castle_2_by_moonglowlilly_d5tk46h-fullview.png')
        check=False
    # elif x <400:
    #     print('not castle')
    #     bg = pygame.image.load('ClassStuff\Images\Images\Pygame-Tutorials-master\Game\\157-1573121_telephone-lines-png-power-lines-silhouette.png')
    clock.tick(27)



    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
    
pygame.quit()