import pygame,time,random

screen = pygame.display.set_mode((500,500))

DOWN = False
UP = False
RIGHT = False
LEFT = False


pos_snakeb = [[50,40]]
applePosX = 60
applePosY = 40

exit = True
while exit:

    time.sleep(0.09)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    snake = pygame.draw.rect(screen, (0,255,0),(pos_snakeb[0][0], pos_snakeb[0][1], 10,10))
    apple = pygame.draw.rect(screen,(255,0,0), (applePosX,applePosY,10,10))
    
#------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_s]:
        LEFT = False
        RIGHT = False
        UP = False
        DOWN = True
       
    if DOWN == True:
        pos_snakeb[0][1] += 10

#------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_w]:
        RIGHT = False
        LEFT = False
        DOWN = False
        UP = True

    if UP == True:
 
        pos_snakeb[0][1] += -10
#------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_a]:
        UP = False
        DOWN = False
        RIGHT = False
        LEFT = True

    if LEFT == True:
  
        pos_snakeb[0][0] += -10
#------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_d]:
        UP = False
        DOWN = False
        LEFT = False
        RIGHT = True

    if RIGHT == True:

        pos_snakeb[0][0] += 10
#------------------------------------------------

    if snake.colliderect(apple):
        applePosX = random.randint(10, 490)
        applePosY = random.randint(10, 490)
        addX = pos_snakeb[0][0]+10
        addY = pos_snakeb[0][1]+10
        add = [addX,addY]

        pos_snakeb.append(add)
        print(pos_snakeb)





    pygame.display.update()                         
