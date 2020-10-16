import pygame
import pygame.locals

pygame.init()

heigth = 640 #altura
width = 480 #largura

tela = pygame.display.set_mode((heigth, width)) #definindo a janela e passando tamanho
pygame.display.set_caption('pg-1') #nome a janela

exit = True
while exit:
    for event in pygame.event.get(): #captura o evento e atribui a event
        if event.type == pygame.QUIT: #compara o event com o evento de sair
            exit = False 



    pygame.display.update() #para que a tela possa ser modifcada em execução tem de que ficar se atualizando

#aula 1, criando uma janela