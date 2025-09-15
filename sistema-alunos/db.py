import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",       
        password="senha",
        database="nome_db"   
    )
