import func_do_caixa
import time
import os
saldoatual  = cont1= 0
print('bom dia')
time.sleep(0.60)
while True :
    if cont1 == 2:
        os.system('cls')
    func_do_caixa.depsac(saldoatual)
    sd = input('...\n ').upper()
    for c in range(3):
        print('.')
        time.sleep(0.55)
    if sd == 'D':
        depositar = int(input('digite quanto quer depositar :'))
        saldoatual = saldoatual + depositar
        func_do_caixa.pn(saldoatual)
    else:
        sacar = int(input('digite quanto quer sacar :'))
        saldoatual = saldoatual - sacar
        func_do_caixa.pn(saldoatual)
    cont1 =+ 1

