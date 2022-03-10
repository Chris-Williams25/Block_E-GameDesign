#I copied and pasted this, and then I added the parameters to keep the sqaure in the box frame thing
#chris Williams
#3/9/2022
import os, random, time, pygame
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
check=True #for the while loop
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
#creating the rect object
square=pygame.Rect(xs,ys,wbox,hbox)
square2=pygame.Rect(xc,yc,wbox,hbox)
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}

#Get colors
background= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')
while check:
    screen.fill(background)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    

    keys=pygame.key.get_pressed() #this returns a list
    if keys[pygame.K_a] and square.x >=move:
        square.x -= move #substract 5 from the x value
    if keys[pygame.K_d] and square.x <WIDTH-wbox:
        square.x += move
    if keys[pygame.K_w] and square.y >=move:
        square.y -= move
    if keys[pygame.K_s] and square.y <HEIGHT-hbox:
        square.y += move   
#Finish circle
    if keys[pygame.K_LEFT] and xc >=rad:
        xc -= move #substract 5 from the x value
    if keys[pygame.K_RIGHT] and xc <=WIDTH-rad:
        xc += move
    if keys[pygame.K_UP] and yc>=rad:
        yc -= move
    if keys[pygame.K_DOWN] and yc<=HEIGHT-rad:
        yc += move

    # if keys[pygame.K_LEFT] and square2.x >=move:
    #     square2.x -= move #substract 5 from the x value
    # if keys[pygame.K_RIGHT] and square2.x <WIDTH-wbox:
    #     square2.x += move
    # if keys[pygame.K_UP] and square2.y >=move:
    #     square2.y -= move
    # if keys[pygame.K_DOWN] and square2.y <HEIGHT-hbox:
    #     square.y += move
    pygame.draw.rect(screen, sq_color, square)
    # pygame.draw.rect(screen, cr_color, square2)
    pygame.draw.circle(screen, cr_color, (xc,yc), rad)
    pygame.display.update()
    pygame.time.delay(10)


# square.colliderect(square2)


    