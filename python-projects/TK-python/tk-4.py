from tkinter import *

janela = Tk()
janela.geometry('300x350+300+150')
janela['bg'] = 'blue'

def bt_onclick():
    lb['text']  = en.get()

en = Entry(janela)
en.place(x=90, y=100)
en['bg'] = 'cyan'

bt = Button(janela, width=19, text='OK', command=bt_onclick)
bt.place(x=81, y=140)

lb = Label(janela, text='caixa de texto - Label')
lb.place(x=91, y=180)


janela.mainloop()