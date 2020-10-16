from tkinter import *

janela = Tk()

lb1 = Label(janela, text='label 1')
lb2 = Label(janela, text='label 2')
lb3 = Label(janela, text='label 3')
lb4 = Label(janela, text='label 4')

lb1.grid(row=1 , column=1) # grid funciona como pack e place, o grid posiciona os objetos como linhas e colunas, todas as linha e coluna é colocada de acordo com a anterior
lb2.grid(row=4 , column=4)
lb3.grid(row=3 , column=7)
lb4.grid(row=10 , column=10)



janela.geometry('400x450')

janela.mainloop()