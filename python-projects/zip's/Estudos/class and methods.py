class book(object):
    def __init__(self, titulo, autor,estilo ,paginas ):
        print('um livro foi adicionado ao sistema . . .')
        self.titulo = titulo
        self.autor = autor
        self.estilo = estilo
        self.paginas = paginas

    def __str__(self):
        return 'titulo e o autor é: ' \
               '{}, o autor {}'.format(self.titulo, self.autor)

    def estilo_pag(self):
        print('o estilo do livro é de {}, ele tem {} paginas'.format(self.estilo, self.paginas))

livro1 = book('desing e cia', 'Pedro', 'estudo/apostila', 342)

print(livro1)
livro1.estilo_pag()
print(livro1.titulo)
print(livro1.autor)
print(livro1.paginas)