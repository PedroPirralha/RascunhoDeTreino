from tkinter import *

janela = Tk()
janela.title('LOGIN')


lb1 = Label(janela, text='Login')
lb2 = Label(janela, text='Senha')

inp1 = Entry(janela)
inp2 = Entry(janela, show='*')

bt = Button(janela,width=15 ,text='Enviar')

espace1 = Label(janela,text='')
veri = Label(janela,text='')

espace1.grid(row=0, column=1)
lb1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
inp1.grid(row=1 , column=1)
inp2.grid(row=2, column=1)
veri.grid(row=3,column=1)
bt.grid(row=4, column=1)


janela.geometry('200x120')
janela.mainloop()