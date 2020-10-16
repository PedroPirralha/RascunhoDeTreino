import pygame
import time
import random 

heigth = 640
widht = 480

posCollY = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460]
posCollX = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620]

x_pos = int(heigth/2)
y_pos = int(widht/2)

x_coll = 100
y_coll = 100

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

tam_ = 33

tela = pygame.display.set_mode((heigth, widht))
pygame.display.set_caption('aula 5')

exit = True
while exit:
    time.sleep(0.05)
    tela.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    if pygame.key.get_pressed()[pygame.K_s]: #s
        if y_pos == 460:
            y_pos += -20
        y_pos += 20
        
    if pygame.key.get_pressed()[pygame.K_d]: #d
        if x_pos == 620:
            x_pos += -20
        x_pos += 20

    if pygame.key.get_pressed()[pygame.K_a]: #a
        if x_pos == 0:
            x_pos += 20
        x_pos += -20

    if pygame.key.get_pressed()[pygame.K_w]: #w
        if y_pos == 0:
            y_pos += 20
        y_pos += -20

   
    redSquare = pygame.draw.rect(tela, red, (x_coll,y_coll,20,20))
    blueSquare = pygame.draw.rect(tela, blue, (x_pos,y_pos,20,20))

    if redSquare.colliderect(blueSquare): #FUNÇÃO QUE DETECTA SE UIM OBJ ESTA SOBREPONDO O OUTRO, COLISÃO
        x_coll = random.choice(posCollX)
        y_coll = random.choice(posCollY)
        
    

    pygame.display.update()

