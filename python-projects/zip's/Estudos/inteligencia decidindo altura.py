import inteligencia_decidindo_altura_func as idaf
import func_  as fn
import pandas as pd

limpar_terminal = fn.clear_t()
 #Variaveis 
openx = open('/home/pedro/Documentos/Projetos_Programação/Projetos Abertos/python-projects/Estudos/inteligencia_decidindo_altura.txt')
lenx = openx.readlines()
espaçamente = ('___'.center(38,'_'))
data_frame = {}
nome = []
tamanho = []
heigth_tf = []  # heigth true false
type_ = []

# func/def
def name_separation(num_name): # def que separa o nome da altura
    var_add = []
    for x in range( 0, len(lenx[num_name])+1  ):
        add_var = (lenx[num_name][0:x].replace('\n',' '))
        if ' ' in add_var:
            var_add = []
            var_add.append(add_var)
            break
        var_add.append(add_var)
        
    return(var_add[0].replace(' ',''))
def separiting_heigth(num_name): # def que separa a altura do nome
    var_add = []
    for x in range( 0, len(lenx[num_name])+1  ):
        add_var = (lenx[num_name][0:x].replace('\n',' '))
        if ' ' in add_var:
            var_add = []
            var_add.append(add_var)
            break
        var_add.append(add_var)

        add_varfinal = ( lenx[num_name][x:].replace('\n',' ').replace('/','').replace('+','').replace('-','').replace(' ',''))
    return(add_varfinal)
# laço de repeticao (for)
for i in range(0, len(lenx)):
    heigth = float(separiting_heigth(i))#
    lt = idaf.program_engine("AIwlm", heigth) 
    name = name_separation(i)

    if type(lt) == type("NULL"):
        print(lt)
        break  

    nome.append(name)
    tamanho.append(heigth)
    heigth_tf.append(lt[0])
    type_ = lt[1]

data_frame[' nomes '] = nome
data_frame[' altura '] = tamanho
data_frame[' é alto? '] = heigth_tf
dt = pd.DataFrame(data_frame)

print('\nAs considereações de alto e baixo são por uma perspectiva de visão ou talvez outra coisa\ntype: {}\n{}\n{}\n{}' 
''.format(type_,espaçamente,dt,espaçamente))
print(data_frame)

