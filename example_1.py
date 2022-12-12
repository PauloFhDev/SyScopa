# Construindo nossa 1ª janela
from tkinter import *
import mysql.connector

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)
print(db_connection)



window = Tk()

txt = Label(window, text='Hello world')
txt.pack()

btn = Button(
    text='Clica aqui!',
    width=10,
    height=10,
    border=5,
    fg='#FFFFFF',
    bg='#0D0052'
)
btn.pack(fill = BOTH, expand=True, side=LEFT)


btn2 = Button(
  text='Clica aqui!',
  width=10,
  height=10,
  border=5,
  fg='#FAFA0D',
  bg='#E6B540'
)
btn2.pack(fill = BOTH, expand=True, side=RIGHT)
window.mainloop()


# from tkinter import *
# from tkinter import messagebox
# top = Tk()

# C = Canvas(top, bg="blue", height=250, width=300)
# filename = PhotoImage(file = "D:\Paulinho\ESTUDOS\SENAI\3_semestre\Desenvolvimento 2\10.12.2022_sabado\download.jpeg")
# background_label = Label(top, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# C.pack()
# top.mainloop
