1
import sqlite3 as sql
from tabelaDeCores2 import color
import os,time

green = color['green']
yellow = color['yellow']
cyan = color['cyan']
clear = color['clear']
red = color['red']
bold = color['bold']
years = []

data_frame = {'nome':[],'idade':[]}

def acessBanc():
    try:
        banc = sql.connect('sistemCad.db')
        sisBanc = banc.cursor()
        sisBanc.execute("SELECT * FROM sistemcad")
    except:
        sisBanc.execute("CREATE TABLE sistemcad (name text, year integer)")

def AddRegister(name, year):
    banc = sql.connect('sistemCad.db')
    sisBanc = banc.cursor()
    sisBanc.execute("SELECT * FROM sistemcad")
    sisBanc.execute(f"INSERT INTO sistemcad VALUES ('{name}', '{year}')")
    banc.commit()
    banc.close()

def pressEnter():
    input(f'{red}pressEnter{clear}')

exit = True
while exit:
    acessBanc()
    os.system('cls')
    menu = input(f'{green}\n-------------------------------------{clear}\n\n'
                 f'{cyan}1 - Consultar pessoas cadastradas\n'
                 f'2 - Para cadastrar\n'
                 f'3 - Sair do sistema de cadastro\n'
                 f'4 - Excluir banco de dados\n'
                 f'5 - Exibir informações do banco de dados{clear}\n'
                 f'\n{green}-----------------------------------{clear}> ')
    print('\n')

    if menu == '3':
        break

    elif menu == '2':
        name = input(f'{yellow}Digite o nome da pessoa a ser cadastrada .:{clear}')
        year = input(f'{yellow}Digite a idade da pessoa a ser cadastrada .:{clear}')
        AddRegister(name,year)

    elif menu == '1':
        print(f'\n<{green}-------------------------------------{clear}')
        banc = sql.connect('sistemCad.db')
        sisBanc = banc.cursor()
        sisBanc.execute("SELECT* FROM sistemcad")
        mostRegister = sisBanc.fetchall()
        banc.commit()
        banc.close()

        for most in mostRegister:
            print(most[0],end=' <nome - idade> ')
            print(most[1])


        pressEnter()

    elif menu == '4':
        verify = input('o banco será deletado pressione S para confirmar').upper()
        if verify =='S':
            os.remove('sistemCad.db')
            years = []
            print('banco de dados foi removido !!')
        else:
            print('o banco de dados não foi removido')


    elif menu == '5':
        banc = sql.connect('sistemCad.db')
        sisBanc = banc.cursor()
        sisBanc.execute("SELECT* FROM sistemcad")
        mostRegister = sisBanc.fetchall()
        banc.commit()
        banc.close()
        for mostYear in mostRegister:
            years.append(mostYear[1])


        sumResult = sum(years)
        if sumResult == 0:
            print(f'{bold}{red} Reinicie o programa e registre alguem no sistema !!{clear}')
            break
        result =int(sumResult/len(years))
        print('numero de cadastros ->{}\nidade media -> {}'.format(len(mostRegister),result))

 
        pressEnter()


    else:
        print(f'{bold}{red}digite apenas opções validas !!{clear}')
        time.sleep(1.5)



