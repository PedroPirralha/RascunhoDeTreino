from tkinter import *
#gerenciador de leiaute pack

janela = Tk()

lb1 = Label(janela, text='label 1', bg='green')
lb2 = Label(janela, text='label 2', bg='blue')
lb3 = Label(janela, text='label 3', bg='yellow')
lb4 = Label(janela, text='label 4', bg='red')

lb1.pack(side=RIGHT)
lb2.pack(side=LEFT)
lb3.pack(side=TOP)
lb4.pack(side=BOTTOM)

janela.geometry('400x300+200+200')
janela.mainloop()