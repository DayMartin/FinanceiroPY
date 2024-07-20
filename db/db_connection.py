import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='financeiro',
            user='dinahdoria',
            password='giovana0407',
            port=3306
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado ao MySQL Server versão {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"Conectado ao banco de dados {record}")

            return connection

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
