import mysql.connector

def conectar():
    #informas os dados necessários para acessa o banco.#
    conexao = mysql.connector.connect(
        #servidor on esta o mysql
        host="localhost",
        #usuario
        user="root",
        #senha
        password = "",
        #nome do banco
        database = "loja"
    )
    
    return conexao