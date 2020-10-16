#   ' transformadno sequencia de numero em str
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n'
      'TODO(A) VALOR OU SEQUENCIA EXIBIDA SERA PARA CONTRUÇÃO DO CODIGO E\n'
      'DEVERA SER EXPECIFICADA PARA A FACILITAÇÃO DA CONSTRUÇÃO DO PROPIO \n'
      '=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n')
numx = input('digite um numero ')
def TransformandoEmStr(x):
    xx = str(x)
    return str(xx)

NumStr = TransformandoEmStr(numx)
list_num_str = list()
for x in NumStr:
    list_num_str.append(x)
num_and_cript = {}
#capturando a sequencia de numeros
cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = cont7 = cont8 = cont9 = cont0 = 0

for x in range(0, len(list_num_str)):
    x2 = x+1
    if list_num_str[x] == '1' :
        cont1 += 1
        num_and_cript['1'] = cont1
    if list_num_str[x] == '2' :
        cont2 += 1
        num_and_cript['2'] = cont2
    if list_num_str[x] == '3' :
        cont3 += 1
        num_and_cript['3'] = cont3
    if list_num_str[x] == '4' :
        cont4 += 1
        num_and_cript['4'] = cont4
    if list_num_str[x] == '5' :
        cont5 += 1
        num_and_cript['5'] = cont5
    if list_num_str[x] == '6' :
        cont6 += 1
        num_and_cript['6'] = cont6
    if list_num_str[x] == '7' :
        cont7 += 1
        num_and_cript['7'] = cont7
    if list_num_str[x] == '8' :
        cont8 += 1
        num_and_cript['8'] = cont8
    if list_num_str[x] == '9' :
        cont9 += 1
        num_and_cript['9'] = cont9
    if list_num_str[x] == '0' :
        cont0 += 1
        num_and_cript['0'] = cont0

print('valor de cada numero ',num_and_cript,'\n')
lista_cript = list(num_and_cript.values())
soma = sum(lista_cript)
print('--> listacript ',lista_cript,'\n')
# Deslocação da numeração

inc_sequence = [] #sequencia inicial para a deslocação
for k in range(soma+1):
    if k == 0:
        pass
    else:
        inc_sequence.append(k)
print(inc_sequence,'< inc sequence (sequencia inicial para a deslocação, \n'
    'e feito a adição de totodos os item da var soma)\n')
# novo dicionario com a numeraçãao nova
new_digit = {'0': 1, '1': 1, 
             '2': 1, '3': 1,
             '4': 1, '5': 1, 
             '6': 1, '7': 1, 
             '8': 1, '9': 1}
print('--> {}\n'.format(new_digit))

#criando a deslocação com novos algarismos



'''
0123456789
7890123456
cada valor novo deslocado recebera seu
novo valor na dict com seu valor original,
sendo assim apenas fazer essa mutação
apenas fazer um dicionario com o seu valor
original recebendo seu novo valo de deslocação
'''
