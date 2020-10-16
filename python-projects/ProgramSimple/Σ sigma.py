#somatoria / sigma
print('Sigma\n___\n\ \n/__, \n ')

inicialN = int(input('digite o valor para começo de n, N = '))

endN = int(input('digite o valor para fim N, N = '))
expression = input('digite como sera feito a somatoria\n'
                   'para expoentes use "*" \n'
                   'para usar adição "+" \n'
                   'para usar subtração "-" \n'
                   'para usar divisão "/" \n'
                   'para usar mulplicação "x" \n'
                    '.......................: ')

def ContSigma(inicialN,endN,expression):
    if expression == '*':
        valorElevado = int(input('digite o valor da potencia .:'))
        soma = []
        for n in range(inicialN,endN+1):
            soma.append(int(n)**valorElevado)
            print(int(n)**valorElevado, end='')
            if n == endN:
                print(' =',sum(soma))
                break
            print(' + ',end='')

    elif expression == '+':
        valorAdicionado = int(input('digite o valor da adição .:'))
        soma = []
        for n in range(inicialN,endN+1):
            soma.append(int(n)+valorAdicionado)
            print(int(n)+valorAdicionado, end='')
            if n == endN:
                print(' =',sum(soma))
                break
            print(' + ',end='')
    elif expression == '-':
        valorSubtraido = int(input('digite o valor da subtração .:'))
        soma = []
        for n in range(inicialN,endN+1):
            soma.append(int(n)-valorSubtraido)
            print(int(n)-valorSubtraido, end='')
            if n == endN:
                print(' =',sum(soma))
                break
            print(' + ',end='')
    elif expression == '/':
        valorDividido = int(input('digite o valor da divisão .:'))
        soma = []
        for n in range(inicialN,endN+1):
            soma.append(int(n)/valorDividido)
            print(int(n)/valorDividido, end='')
            if n == endN:
                print(' =',sum(soma))
                break
            print(' + ',end='')
    elif expression == 'x':
        valorMultiplicado = int(input('digite o valor da multiplicação .:'))
        soma = []
        for n in range(inicialN,endN+1):
            soma.append(int(n)*valorMultiplicado)
            print(int(n)*valorMultiplicado, end='')
            if n == endN:
                print(' =',sum(soma))
                break
            print(' + ',end='')


ContSigma(inicialN,endN,expression)

