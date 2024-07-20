from db.db_connection import connect_to_database
import mysql.connector


def criar_usuario(nome_completo, cpf, celular, email, login, senha):
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO user (nome_completo, cpf, celular, email, login, senha)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (nome_completo, cpf, celular, email, login, senha))
        connection.commit()
        print("Usuário criado com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        cursor.close()
        connection.close()

def consultar_todos_clientes():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user;")
        user = cursor.fetchall()
        for cliente in user:
            print(cliente)
    except mysql.connector.Error as e:
        print(f"Erro ao consultar user: {e}")
    finally:
        cursor.close()
        connection.close()

def consultar_cliente_por_id(cliente_id):
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id = %s;", (cliente_id,))
        cliente = cursor.fetchone()
        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado.")
    except mysql.connector.Error as e:
        print(f"Erro ao consultar cliente por ID: {e}")
    finally:
        cursor.close()
        connection.close()

def verificar_usuario(login, senha):
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE login = %s AND senha = %s;", (login, senha))
        usuario = cursor.fetchone()
        if usuario:
            return 'Pass'
        else:
            print("Usuário não encontrado ou credenciais inválidas.")
    except mysql.connector.Error as e:
        print(f"Erro ao verificar usuário: {e}")
    finally:
        cursor.close()
        connection.close()
