import pygame, time

screen = pygame.display.set_mode((500,500))
 
seqdraw = [[70,40],[60,40],[50,40]]


def drawSeq():
    for x in range(1, len(seqdraw)):
        seqdraw[x][0] = seqdraw[x-1][0]
        seqdraw[x][1] = seqdraw[x-1][1]



exit = True
while exit:
    time.sleep(0.09)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    

    seqdraw[0][0] += 10
    for x in range(1, len(seqdraw)):
        seqdraw[x][0] = seqdraw[x-1][0]
        seqdraw[x][1] = seqdraw[x-1][1]   
    print(seqdraw)
    

    for moveSnake in seqdraw:
        snake = pygame.draw.rect(screen, (255,255,255), (moveSnake[0],moveSnake[1],10,10))
    
    pygame.display.update()