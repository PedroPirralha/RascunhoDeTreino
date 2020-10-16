from tkinter import Tk, Button, Label, mainloop

def BtClic():
    print('button_1_click')


janela = Tk()

janela.geometry('300x350+550+200')
janela['bg'] = 'blue'

lb = Label(janela,text='None')
lb.place(x=120, y=75)

#adiciona botões a janela
bt1 = Button(janela,width=10 ,text='bt1' ,command=BtClic)
bt1.place(x=110, y=100)

bt2 = Button(janela, width=10, text='bt2', command=BtClic)
bt2.place(x=110,y= 130)


janela.mainloop()