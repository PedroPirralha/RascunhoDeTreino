import pygame

pygame.font.init() #!!
tela = pygame.display.set_mode((600,400))
varpy = 'pygame'
fonte = pygame.font.SysFont('schadow', 25, Bold=False,italic=False)#!! 'nome da fonte, tamanho, negrito, italico'
white = (255,255,255)
exit = True
while exit:
    msg = f'isso e uma frase no {varpy}'#!!
    msgCall = fonte.render(msg, False, white)#!! 'texto que sera exibido, se o texto sera serrilhado ou não, cor do texto'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    tela.blit(msgCall,(100, 200) )#!!
    pygame.display.update()

#este codigo mostra como é feito para se escrever algo na tela

#mostFont = pygame.font.get_fonts() #isso mostra as fontes instaladas no computador
#print(mostFont)