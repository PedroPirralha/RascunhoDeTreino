from tkinter import *

janela = Tk()

lb1 = Label(janela, text='espaço' , width=15, height=3 , bg='blue')

lbho = Label(janela, text='HORIZONTAL', bg='yellow')
lbver = Label(janela, text='vertical', bg='green')

lb1.grid(row=0 , column=0)
lbho.grid(row=1, column=0, sticky=E)
lbver.grid(row=0, column=1, sticky=S)
#propiedade sticky, permite realocar os elementos para uma posição em sua coluna ou linha, mesmos argumentos o anchor
janela.geometry('200x200')
janela.mainloop()