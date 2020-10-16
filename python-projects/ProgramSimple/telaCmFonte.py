import pygame

#VAR
altura = 125
largura = 200
tamanho = (largura,altura)
line1 ="ola meu"
line2 ="nome é"
line3 ="Pedro "
white = (255,255,255)

#VAR IN PYGAME
pygame.font.init()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('hii')
fonte = pygame.font.SysFont('schadow', 25, False, False)


#CODE MECHANICS
exit = True
while exit:
    render1 = fonte.render(line1, True, white)
    render2 = fonte.render(line2, True, white)
    render3 = fonte.render(line3, True  , white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False


    tela.blit(render1, (20, 20))
    tela.blit(render2, (20, 45))
    tela.blit(render3, (20, 70))
    pygame.display.update()

# eu não achei outros modos de manipular textos com o pygame, o modo que achei foi esse,
# armazenas os textos linha por variavel, dps rederiza eles em cada posição, por exemplo como linhas