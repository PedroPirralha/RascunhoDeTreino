import func_
import pandas as pd 
func_.clear_t()
run = int(input('Digite qual numero voce quer que comece a contagem : '))
finish = int(input('Digite qual numero voce quer que termine a contagem : '))
func_.clear_t()
data_frame = {}
numeros = []
primos = []
cont_true = []
cont_false = []
for x in range(0, ((finish+1) - run)):
    pre_result = (run + x)
    result = func_.return_numPrimo(pre_result)
    numeros.append(pre_result)
    primos.append(result)
    if result == False:
        cont_false.append(1)
    else :
        cont_true.append(0)

data_frame['indice |'] = ' |'
data_frame['Numeros'] = numeros
data_frame['Primo?'] = primos
df_numprimos = pd.DataFrame(data_frame)
print(df_numprimos)
print('\nA quantidades de numeros primos é {}\n'
      'A quantidade de numeros NÂO primos é {}'.format(len(cont_true),len(cont_false)))

print(cont_true, cont_false) #registro de contagem
