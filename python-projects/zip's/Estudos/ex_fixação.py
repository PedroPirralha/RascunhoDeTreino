import time
def time_():
    time.sleep(0.50)

titulo_livro1 = 'magic'#input(str('digite o nome do livro'))
criador_livro1 = 'pedro'#input(str('digite o nome do criador do livro'))
dt_criacao_livro1 = '10/10'#input(str('digite a data de criação do livro'))
paginas_livro1 = '142'#input(str('digite quantas paginas há no livro'))
class libraly(object):
    def __init__(self, titulo, criador, dt_criacao, paginas):
        print('livro esta sendo digitalizado\n.')
        for c in range(1, 3):
            time_()
            print('. ')
        print('concluido')

        self.titulo = titulo
        self.criador = criador
        self.dt_criacao = dt_criacao
        self.paginas = paginas

livro1 = libraly(titulo_livro1,criador_livro1,dt_criacao_livro1,paginas_livro1)
print('o titulo do livro é {}\n'
               ' o criador é {}\n'
               'data de criação {} \n'
               'quantas paginas ha no livro {}'.format(livro1.titulo ,livro1.criador , livro1.dt_criacao , livro1.paginas))