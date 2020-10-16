'''o func_ tem como ultilidade armazenar funções para uso pessoal, funções simples como achar o numero primo
    ativar um modo C.T.C (code the code,'codifique
    o codigo'), entre outros como gerador de numeros primos
    conversores de tempo, temperatura entre outros... '''
''' developer: Pedro Henrique Quadros Pirralha
    contato: pirralhapedro@gmail.com
    nivel de exp. : basico/Intermediario '''

import os
import time
import re

def clear_t():
    os.system('clear')
clear_t()
def loading():
    for x in range(1,4):
        print('loading ', end='')
        print('.'*x)
        time.sleep(0.09)
        os.system('clear')

def ctc_type_one(exibir_var):
    ''' o ctc ,code the code ou codifique o codigo foi desenvolvido para facilitar na
    vizualização e produção do codigo ele exibe listas tuples dicts str int float bool
    '''
    #tipo simples vizualização recomendado para caso se outras funções
    print('> {} <'.center(10,'-').format(exibir_var))

def ctc_type_two(exibir_var):
    #tipo mais chamativo para uma vizualização melhor recomendado para estetica de cod
    print('< C.T.C >'.center(40,'='))
    #print('_'.center(70,'_'))
    print('xupx'.center(40,'='))
    print('{}'.center(30,' ').format(exibir_var))
    print('xdonwx'.center(40,'='))

def verifc_numPrimo(num_prim_retornastr):
    #retorna uma str
    tot = 0
    for c in range(1, num_prim_retornastr+1):
        if num_prim_retornastr % c == 0:
            tot+=1
    if tot == 2:
        print('esse numero e primo')
    else:
        print('esse numero não e primo')

def return_numPrimo(num_prim_retornabool):
    #retorna um valor bool
    tot = 0
    for c in range(1, num_prim_retornabool+1):
        if num_prim_retornabool % c == 0:
            tot+=1
    if tot == 2:
        return True
    else:
        return False

def terminal_dimensions(terminalsize): #retorna as dimensões do terminal
    getsize_terminal= os.get_terminal_size()
    getcollum = getsize_terminal[0]
    getline = getsize_terminal[1]
    if terminalsize == 'collum':
        return print( getcollum )
    elif terminalsize == 'line':
        return print( getline )
    else:
        return print( getsize_terminal )

def fibonacci (start, end):
    x1 = start
    x2 = start
    fibb = []
    print(start, start, end=" ")
    for x in range(0, end):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
        fibb.append(x3)
    return fibb



def hipotenusa(a , b):
    hip = a**2 + b**2
    result = hip ** (1/2)
    return result

hipp = hipotenusa(3,4)
print(hipp)
