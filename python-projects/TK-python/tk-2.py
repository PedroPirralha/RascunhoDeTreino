from tkinter import *


janela = Tk() #<---

#definindo tamanho da janela
janela.geometry('350x350+200+200') #<--

#define oque será escrito na janela
lb = Label(janela,text='Hello Word')
lb.place(x=148 ,y=160)

janela.mainloop() #<---