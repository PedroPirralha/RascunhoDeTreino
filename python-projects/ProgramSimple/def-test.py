#rtornar uma função de dentro de outra função, não é necessario, pois seria mais facil ultilizar classes

def defOne():

    def defTwo():
        print('cheguei no defTwo')

    return defTwo()


defOne() 