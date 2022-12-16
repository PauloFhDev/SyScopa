import mysql.connector

def criar_conexao():
    return mysql.connector.connect(host="localhost",user="root",password="",database="syscopa")
    
def fechar_conexao(con):
    return con.close()