def pn(x):
    #x = int(input('digite um numero :'))
    if x < 0 :
        print("o saldo e de {} Reais e é negtivo".format(x))
    else:
        print('o saldo e de {} Reais e é positivo'.format(x))

def depsac(saldoat):
    print('saldo inicial de {} Reais \n'
          'depositar ou sacar?\n [se for sacar escreva S, se for depositar escreva D ]'.format(saldoat))