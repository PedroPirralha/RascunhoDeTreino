from tkinter import *
 
janela = Tk()
janela['bg'] = 'black'
lb1 = Label(janela, text='side1', bg='white')
lb2 = Label(janela, text='side2', bg='blue')
lb3 = Label(janela, text='side3', bg='green')
lb4 = Label(janela, text='side4', bg='red')

lb1.pack(anchor=CENTER , side=RIGHT, fill=Y) # nova propiedade "fill" faz com que crie uma barra na direção escolhida (x, y)
lb2.pack(anchor=N , side=TOP, fill=X)
lb3.pack(anchor=S , side=BOTTOM, fill=Y)
lb4.pack(anchor=CENTER , side=LEFT, fill=X)

janela.geometry('300x350+200+200')

janela.mainloop()