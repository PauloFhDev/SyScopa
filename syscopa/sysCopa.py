from syscopa.conect import criar_conexao,fechar_conexao
con = criar_conexao()
from tkinter import *
import tkinter as tk
from tkinter import messagebox


def insere_tecnico():
    nomearbi=codigoValue.get()
    cursor = con.cursor()
    sql = "INSERT INTO arbitro (nome_arbitro) values (%s)"
    valores = (nomearbi)
    cursor.execute(sql,[valores])
    cursor.close()
    con.commit()

"""insere_tecnico(con,"marcos")"""

def insere_equipe(con, nome_equipe,tecnico_id):
    cursor = con.cursor()
    sql = "INSERT INTO equipe (nome_equipe,tecnico_id) values (%s,%s)"
    valores = (nome_equipe,tecnico_id)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()


# def insere_arbitro(con):
"""def insere_arbitro(arbi):
    teste = con.criar_conexao()
    cursor = teste.cursor()
    #arbi = codigoValue.get()
    print("ARBI: ", arbi)
    sql = "INSERT INTO arbitro (nome_arbitro) values (%s)"
    valores = (arbi)
    cursor.execute(sql,[valores])
insere_arbitro("felps")"""

    

win = Tk()


texto = Label(win, text="insira seu arbitro aqui")
texto.grid(column=0, row=0)

codigoValue = StringVar()
codigoEntry = Entry(win, textvariable = codigoValue)
codigoEntry.grid(row=0, column=1)
btn1 = Button(win, text="insere_arbitro",command = insere_tecnico).grid(column=0, row=2)

texto1 = Label(win, text="insira seu arbitro aqui")
texto1.grid(column=0, row=10)



# botao = Button(win, text="insere_arbitro",command= insere_arbitro(con))
# botao.grid(column=0, row=2)
btn3 = Button(win, text="insere_arbitro2",command = insere_tecnico).grid(column=0, row=20)

win.mainloop()



