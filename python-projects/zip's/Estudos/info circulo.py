class circ(object):

    def __init__(self, diametro):

        self.diametro = diametro

    def mostrar_raio(self):
        return self.diametro / 2

    def mostrar_area(self):
        return (self.diametro / 2) ** 2 * 3.14
diametro_ = 133		
'''float(input("digite o diametro \n"
                      "(caso não seje um diametro coloque o dobro do raio) \n"
                      "de um circulo :"))'''

circulo_x = circ(diametro_)
print('o diametro do circulo e {}, o raio desse circulo é {}, e sua area e {} cm²'.
      format(circulo_x.diametro, circulo_x.mostrar_raio(), circulo_x.mostrar_area()))