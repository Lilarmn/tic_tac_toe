from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
# ---------
main=tk.Tk()
main.config(background='black')
main.title('Dooz')
main.geometry("600x678")
main.resizable(False,False)
# ----
main.columnconfigure(0,weight=3)
main.columnconfigure(1,weight=5)

header=ttk.Label(main,
                 text='tictoe Game'.title(),
                 background='white',
                 foreground='black',
                 font=(None,15),
                 anchor=tk.CENTER)
header.grid(column=1,row=0,sticky=tk.N,pady=5,ipady=20,ipadx=20)

a=0

def Message(butt):
    showinfo(
        title='game is end',
        message=f'{butt.cget("bg")} is win'
    )

def EndLogic():
    if (b1.cget('bg')==b2.cget('bg')==b3.cget('bg')) and b1.cget('bg')!='white':
        Message(b1)
    elif (b4.cget('bg')==b5.cget('bg')==b6.cget('bg')) and b4.cget('bg')!='white':
        Message(b4)
    elif (b7.cget('bg')==b8.cget('bg')==b9.cget('bg')) and b7.cget('bg')!='white':
        Message(b7)
    elif (b1.cget('bg')==b4.cget('bg')==b7.cget('bg')) and b1.cget('bg')!='white':
        Message(b1)
    elif (b2.cget('bg')==b5.cget('bg')==b8.cget('bg')) and b2.cget('bg')!='white':
        Message(b7)
    elif (b3.cget('bg')==b6.cget('bg')==b9.cget('bg')) and b3.cget('bg')!='white':
        Message(b7)
    elif (b1.cget('bg')==b5.cget('bg')==b9.cget('bg')) and b1.cget('bg')!='white':
        Message(b7)
    elif (b3.cget('bg')==b5.cget('bg')==b7.cget('bg')) and b3.cget('bg')!='white':
        Message(b7)

def buttonLogic(name):
    global a
    if name.cget('bg')=='white':
        if a%2==0:
            name.config(background='black')
            a+=1
            EndLogic()
        else:
            name.config(background='gold')
            a+=1
            EndLogic()

Padds={'ipadx':100, 'ipady':70}

b1=tk.Button(main, text="_",background='white')
b1.configure(command=lambda :buttonLogic(b1))
b1.grid(column=0,row=1,sticky=tk.NW,**Padds)

b2=tk.Button(main, text="_",command=lambda :buttonLogic(b2),background='white')
b2.grid(column=1,row=1,sticky=tk.N,**Padds)

b3=tk.Button(main, text="_",command=lambda :buttonLogic(b3),background='white')
b3.grid(column=2,row=1,sticky=tk.NE,**Padds)


b4=tk.Button(main, text="_",command=lambda :buttonLogic(b4),background='white')
b4.grid(column=0,row=2,sticky=tk.W,**Padds)

b5=tk.Button(main, text="_",command=lambda :buttonLogic(b5),background='white')
b5.grid(column=1,row=2,**Padds)

b6=tk.Button(main, text="_",command=lambda :buttonLogic(b6),background='white')
# b6.configure(com)
b6.grid(column=2,row=2,sticky=tk.E,**Padds)

b7=tk.Button(main, text="_",command=lambda :buttonLogic(b7),background='white')
b7.grid(column=0,row=3,sticky=tk.SW,**Padds)

b8=tk.Button(main, text="_",command=lambda :buttonLogic(b8),background='white')
b8.grid(column=1,row=3,sticky=tk.S,**Padds)

b9=tk.Button(main, text="_",command=lambda :buttonLogic(b9),background='white')
b9.grid(column=2,row=3,sticky=tk.SE,**Padds)

def resetFunc():
    grids=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in grids:
        i.config(background='white')

resetButton=tk.Button(main,
                      text='Reset',
                      command=lambda : resetFunc(),
                      foreground='black',
                      background='white')
# resetButton.pack(expand=True)
resetButton.grid(row=0,column=0,)

message_color=tk.Label(
    main,
    text='color background',
    background='white',
    foreground='black',
    font=(None,12)
)
message_color.grid(row=4,column=0,sticky=tk.N,pady=50)

colorBack=tk.StringVar()
color_input=tk.Entry(
    main,
    textvariable=colorBack,
    background='white',foreground='black'
)
color_input.grid(row=4,column=1,pady=50)

def Color_changer(C):
    try:
        main.config(background=C.get())
    except NameError:
        pass
colorChanger=tk.Button(

    main,
    text='color change',
    command=lambda : Color_changer(colorBack),
    foreground='black',
    background='white'
)
colorChanger.grid(row=4,column=2,pady=50)
# ----
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    main.mainloop()

