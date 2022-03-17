#chris Williams
#3/16/2022

import os, random, time, pygame
pygame.init()
WIDTH=700
HEIGHT=700
check=True #for the while loop
move=5 #pixels



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

thingtoendgame=pygame.Rect(0,0,700,40)
square=pygame.Rect(xs,ys,wbox,hbox)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#these are the colors:
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}

background= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')

MAX=10
jumpcount=MAX
JUMP=False

while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #substract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-(wbox+move):
        square.x += move
    # if keys[pygame.K_s] and square.x >=move:
    #     square.y += move #substract 5 from the x value
    # if keys[pygame.K_w] and square.x <WIDTH-(hbox+move):
    #     square.y -= move
    #here we jump
    if not JUMP:
        if keys[pygame.K_w] and square.y >=move:
            square.y -= move
        if keys[pygame.K_s] and square.y <HEIGHT-(hbox+move):
            square.y += move   
        if keys[pygame.K_SPACE]:
            JUMP=True 
    else:
        if jumpcount >=-MAX:
            square.y -= (jumpcount*abs(jumpcount))/2 #abs is absolute value
            jumpcount -=1
        else:
            jumpcount=MAX 
            JUMP=False
#Finish circle
    if keys[pygame.K_LEFT] and xc >=rad+move:
        xc -= move #substract 5 from the x value
    if keys[pygame.K_RIGHT] and xc <=WIDTH-(rad+move):
        xc += move
    if keys[pygame.K_UP] and yc>=rad+move:
        yc -= move
    if keys[pygame.K_DOWN] and yc<=HEIGHT-(rad+move):
        yc += move

    checkCollide=square.collidepoint(xc,yc) 
    if checkCollide:
        # xc=random.randint(wbox, WIDTH-wbox)
        # yc=700-rad-5
        xc=350
        yc=350
        rad+=move
        xs=random.randint(30,670)
        ys=670
        square=pygame.Rect(xs,ys,wbox,hbox)
        
    checkEndgame=square.collidepoint(40,40)
    checkEndgame2=square.collidepoint(350,40)
    checkEndgame3=square.collidepoint(660,40)

    if checkEndgame:
        background=colors.get('navy')
        endingthing=True
    if checkEndgame2:
        background=colors.get('navy')
        endingthing=True
    if checkEndgame3:
        background=colors.get('navy')
        endingthing=True
    # while(endingthing):
    #     pygame.time.delay(50)
    #     pygame.QUIT
    # if keys[pygame.K_LEFT] and square2.x >=move:
    #     square2.x -= move #substract 5 from the x value
    # if keys[pygame.K_RIGHT] and square2.x <WIDTH-wbox:
    #     square2.x += move
    # if keys[pygame.K_UP] and square2.y >=move:
    #     square2.y -= moves
    # if keys[pygame.K_DOWN] and square2.y <HEIGHT-hbox:
    #     square.y += move
    pygame.draw.rect(screen, sq_color, square)
    
    # pygame.draw.rect(screen, cr_color, square2)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    pygame.draw.rect(screen,'aqua',thingtoendgame)
    pygame.draw.circle(screen, 'red', (40,40), 15)
    pygame.draw.circle(screen, 'red', (350,40), 15)
    pygame.draw.circle(screen, 'red', (640,40), 15)
    
    pygame.display.update()
    pygame.time.delay(50)