from tkinter import *



janela = Tk()
janela['bg'] = 'black'



lb1 = Label(janela, text=' ', bg='pink')
lb2 = Label(janela, text=' ', bg='purple')
lb3 = Label(janela, text=' ', bg='red')
lb4 = Label(janela, text=' ', bg='purple')
lb5 = Label(janela, text=' ', bg='pink')

lb1.pack(side=LEFT, fill=BOTH, expand=1) #complemento do fill, e expando, possiveis atribuições 1,0; TRUE , FALSE
lb2.pack(side=LEFT, fill=BOTH, expand=1)
lb3.pack(side=LEFT, fill=BOTH, expand=1)
lb4.pack(side=LEFT, fill=BOTH, expand=1)
lb5.pack(side=LEFT, fill=BOTH, expand=1)


janela.geometry('750x500+200+200')

janela.mainloop()