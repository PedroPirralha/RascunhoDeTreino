from tkinter import *

janela = Tk()

lb1 = Label(janela, width=15, height=6, bg="black")
lb2 = Label(janela, width=15, height=6, bg="blue")
lb3 = Label(janela, width=15, height=6, bg="blue")
lb4 = Label(janela, width=15, height=6, bg="black")

lb5 = Label(janela, bg='red', height=3) 
lb6 = Label(janela, bg='red', width=5)

lb1.grid(row=0 ,column=0)
lb2.grid(row=0 ,column=1)
lb3.grid(row=1 ,column=0)
lb4.grid(row=1 ,column=1)

lb5.grid(row=2 , column=0, columnspan=2, stick=W+E)
lb6.grid(row=0 , column=2, rowspan=2, stick=N+S)
janela.mainloop()
