import pygame

print('\n\n'*500)

pygame.font.init()

getFont = pygame.font.get_fonts()
for f in getFont:
    print(f)

print(f'lista de fontes instaladas em ordem alfabetica, numero de fontes encontrada {len(getFont)}')