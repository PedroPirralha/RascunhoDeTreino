
try: #trecho de codigo supostamente errado
    for i in ['a','b','c']:
        print(i**2)
except:                                                                                 #se estiver errado pode definir qual tipo de erro esperado ou
    print('não se pode multiplicar letras troque as letras por numeros ou troqe o cod.')  # deixar generico para que receba todos os erros

finally: # esse cod. ira rodar independentemente se ta ou não errado
    print('RESPOSTA SUPOSTAMENTE ESPERADA\n'
          'a\n'
          'b b b b\n'
          'c c c c c c c c c')
y = 5
x = 0
try:
    z = y/x
except:
    print('não se pode dividir o numero 0 pois ele e um valor inrredutivel')
finally:
    print('All done')

def aoquadrado():
    s = input('escreva um numero inteiro :')
    print('quadrado desse numero e')
