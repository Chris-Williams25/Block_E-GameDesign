def playGame():
    global BackGround
    BackGround =pygame.transform.scale(bg, (WIDTH,HEIGHT))
    man = player(200, 410, 64,64)
    goblin = enemy(100, 410, 64, 64, 450)
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
                
        redrawGamescreendow()