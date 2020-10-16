from tkinter import *

janela = Tk()
janela.title('LOGIN')
janela['bg'] = 'lightgray'

lb1 = Label(janela, text='Login')
lb2 = Label(janela, text='Senha')

inp1 = Entry(janela)
inp2 = Entry(janela, show='*')

btLogin = Button(janela,width=5 ,text='Ok')
btSenha = Button(janela,width=5 ,text='Ok')

espace1 = Label(janela,text='', bg='lightgray')
veri = Label(janela,text='', bg='lightgray')


espace1.grid(row=0, column=1)
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
inp1.grid(row=1 , column=1)
inp2.grid(row=2, column=1)
veri.grid(row=3,column=1)
btLogin.grid(row=1, column=2)


janela.geometry('200x120')
janela.mainloop()

