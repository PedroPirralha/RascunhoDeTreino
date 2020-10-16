import random

#Variaveis
result_true = []
result_false = []
lens_TX = []
lens_FY = []

#laços
for xx in range(1,6):
    result_true = []
    result_false = []
    for x in range(1,12):
        neuronio = random.randint(0,1)
        if neuronio == 1:
            result_true.append(neuronio)
        else:
            result_false.append(neuronio)
    
    lens_TX.append(len(result_true))
    lens_FY.append(len(result_false))


def MostResult():
    max_true = len(result_true)
    max_false = len(result_false)
    if max_true > max_false:
        return(True)
    else:
        return(False)

print('os neuronios responderam como {} a resposta'.format(MostResult()))

print('lens t = {} , soma {}\nlens f = {} , soma {} '.format( lens_TX,sum(lens_TX), lens_FY, sum(lens_FY) ) )
