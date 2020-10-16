#definindo Classes, um glossario de funçoes, chato de entender mas muito bom e divertido
class Pessoas:
    #fumção __init__ ela sempre sera executada
    def __init__(self, nome, idade, sexo, comendo=False, ):
        #self.algo, tudo que vc atribuir a self.algo podera ser chamado depois que for atribuido uma variavel na class
        self.nome = nome  #variavel-self
        self.idade = idade
        self.comendo = comendo 
        self.secret = 'isso é segredo'
        if sexo == "m":
            sexo = 'Masculino'
            self.sexo = sexo
            return
        elif sexo == "f":
            sexo = 'Feminino'
            self.sexo = sexo 
            return
    #funçoes que podem ser adicionada, ela pode ou não ser execuatada podendo ter ou não um valor a ser adicionado
    def comer(self,comida):
        self.comida = comida
        self.secretfood = 'almondega?'
        if self.comendo == True:
            return (f'{self.nome} ja esta comendo')
           

        self.comendo = True
        return (f'{self.nome} esta comendo {self.comida}')

    def getInfo(self):
        # quando a função getInfo for chamada ela retornará os seguintes self's, esses self's podem ser chamados individualmente
        return self.nome, self.idade,self.sexo



#uma def que vai chamar todas as variaveis-self em uma ordem desiginada para facilitar a chamada delas
def returnClass():
    #pessoa é a variavel no qual a class esta sendo atribuida, para chamar uma variavel-self especifica de dentro da class, basta colocar a variavel pessoa e a variavel-self 
    pessoa = Pessoas('Bianca',15,'f')
    print(
        pessoa.getInfo(),
        pessoa.nome, #para chamar as variavel-self, não pode conter parenteses 
        pessoa.idade,
        pessoa.sexo,
        pessoa.comer('abacaxi'),
        ',coma pera',
        pessoa.comer('pera')
    )

pessoa = Pessoas('Bianca',15,'f')
print()
