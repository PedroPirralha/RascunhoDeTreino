from tkinter import *

jn = Tk()
jn.geometry('210x270+200+150')
jn.title('soma')
jn['bg'] = 'grey'

def soma():
    try:
        var1 = float(vl1.get())
        var2 = float(vl2.get())
        lbresp['text'] = var1+var2
    except:

        lbresp['text'] = 'somente numeros'



lb1 = Label(jn, text='digite o primeiro valor .: ')
lb1.place(x=30, y=50)

vl1 = Entry(jn)
vl1.place(x=40,y=80)

lb2 = Label(jn, text='digite o segundo valor .: ')
lb2.place(x=30, y=115)

vl2 = Entry(jn)
vl2.place(x=40,y=145)

bt = Button(jn, text='somar', width=16, command=soma)
bt.place(x=35, y=170)
 
lbresp = Label(jn, text=' ')
lbresp.place(x=36, y=200)


jn.mainloop()
