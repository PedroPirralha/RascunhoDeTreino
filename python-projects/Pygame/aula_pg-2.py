import pygame

heigth = 640
widht = 480

black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

tela = pygame.display.set_mode((heigth, widht))
pygame.display.set_caption('aula-2')


exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    
    tela.fill(white)

    pygame.draw.rect(tela, red, (5,5,15,430))
    pygame.draw.rect(tela, green, (25,25,15,430))
    pygame.draw.rect(tela, blue, (45,45,15,430))
#                              cordenadas, tamanhox, tamanhoy
    pygame.draw.circle(tela, black, (320, 215), 40)
#             onde sera exib., cor , cordenada do centro do circ., tamanho do circ
    pygame.draw.line(tela, black,(12,7), (50,50), 5 )
    pygame.draw.line(tela, black,(270,480), (270,0),2 )
#                       cordenada 1(x,y)cord.2(x,y) espessura
    pygame.display.update()


#ultilizando objetos do tipo rect, circle, line