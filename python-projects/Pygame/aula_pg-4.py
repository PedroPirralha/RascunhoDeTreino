import pygame

heigth = 640
widht = 480

x_pos = int(heigth/2)
y_pos = int(widht/2)
tam_ = 33

white = (255,255,255)
black = (0,0,0)

tela = pygame.display.set_mode((heigth, widht))
pygame.display.set_caption('aula4')

exit = True
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    if pygame.key.get_pressed()[pygame.K_s]: #s
        y_pos += 2
    if pygame.key.get_pressed()[pygame.K_d]: #d
        x_pos += 2
    if pygame.key.get_pressed()[pygame.K_a]: #a
        x_pos += -2
    if pygame.key.get_pressed()[pygame.K_w]: #w
        y_pos += -2

    print(event)

    tela.fill(white)

    pygame.draw.circle(tela, black, (x_pos,y_pos),tam_)

    pygame.display.update()


