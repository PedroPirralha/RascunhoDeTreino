from tkinter import *
'''            top - north
     

left - W-west     center         rigth - E-east


                bottom - S-south
'''
janela = Tk()
janela['bg'] = 'black'
lb1 = Label(janela, text='side1', bg='white')
lb2 = Label(janela, text='side2', bg='blue')
lb3 = Label(janela, text='side3', bg='green')
lb4 = Label(janela, text='side4', bg='red')

# por padrão o side vem setado no top
# side e anchor ocupam todo o espaço seja top ou north, west ou left
# propiedades do anchor= N , W , S , E ; NW , SW , SE , NE ; são oito possiveis direções para se aplicar
lb1.pack(anchor=CENTER , side=RIGHT)
lb2.pack(anchor=N , side=TOP)
lb3.pack(anchor=S , side=BOTTOM)
lb4.pack(anchor=CENTER , side=LEFT)

janela.geometry('300x350+200+200')

janela.mainloop()