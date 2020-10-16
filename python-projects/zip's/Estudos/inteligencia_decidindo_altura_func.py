# motor principal da logica

import random
#passe o metodo de logica bool, ou AI without learning memory AIwlm(IA sem memoria de aprendizagem)

def program_engine (logictype, heigth):
    if logictype == "Bool":
        if heigth > 1.66:
            return ['Alto', logictype]
        else:
            return ['Baixo', logictype]
    
    elif logictype == "AIwlm":
        heigths = [1.62,1.63,1.64,1.65,1.66,1.67,1.68,1.69]
        if heigth in heigths:
            x = random.randint(0,1)
            if x == 0:
                return ['Alto', logictype]
            else:
                return ['Baixo', logictype]
        elif heigth > 1.69:
            return ['Alto', logictype]
        elif heigth < 1.62:
            return ['Baixo', logictype]
    else:
        return("Digite um tipo de logica valida")