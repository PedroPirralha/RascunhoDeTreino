import pygame 

heigth = 640
widht = 480

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

tela = pygame.display.set_mode((heigth, widht))
pygame.display.set_caption('aula-3')

x=40
y=40

fps = pygame.time.Clock() # define a variavel que sera usado pra definir o tempo de cada loop por second

exit=True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    tela.fill(white)

    pygame.draw.circle(tela, blue, (x,y), 40)
    y+=1
    x+=1
    if y == widht:
        y=0
        x=0
    
    pygame.display.update()
    fps.tick(30) #define o tempo do jogo, quantas mudanças fara por second

