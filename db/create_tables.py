from db.db_connection import connect_to_database
import mysql.connector


def create_table():
    
    create_cliente(),
    create_user(),
    create_fornecedor(),
    create_produto(),
    create_categoria(),
    create_marca(),
    create_compra(),
    create_produto_compra(),
    create_venda(),
    create_produto_venda(),
    create_parcela(),
    create_logs(),
    create_historico_estoque()


# Função para criar tabela cliente
def create_cliente():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_completo VARCHAR(255) NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                rg VARCHAR(20),
                celular VARCHAR(20),
                telefone VARCHAR(20),
                email VARCHAR(255),
                cep VARCHAR(10),
                logradouro VARCHAR(255),
                numero VARCHAR(10),
                bairro VARCHAR(255),
                cidade VARCHAR(255),
                estado VARCHAR(2),
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connection.commit()
        print("Tabela 'Cliente' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_user():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_completo VARCHAR(255) NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                celular VARCHAR(20),
                email VARCHAR(255),
                login VARCHAR(255),
                senha VARCHAR(255),
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connection.commit()
        print("Tabela 'User' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_fornecedor():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return
    
    try: 
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedor (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_fantasia VARCHAR(255) NOT NULL,
                razao_social VARCHAR(255) NOT NULL,
                cnpj VARCHAR(14) NOT NULL,
                ie VARCHAR(20),
                telefone VARCHAR(20),
                site VARCHAR(255),
                email VARCHAR(255),
                observacao TEXT,
                cep VARCHAR(10),
                logradouro VARCHAR(255),
                numero VARCHAR(10),
                bairro VARCHAR(255),
                cidade VARCHAR(255),
                estado VARCHAR(2),
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connection.commit()
        print("Tabela 'Fornecedor' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_produto():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INT AUTO_INCREMENT PRIMARY KEY,
                descricao VARCHAR(255) NOT NULL,
                categoria VARCHAR(255),
                marca VARCHAR(255),
                estoque INT,
                observacao TEXT,
                custo DECIMAL(10,2),
                venda_varejo DECIMAL(10,2),
                venda_atacado DECIMAL(10,2),
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP


            );
        """)
        connection.commit()
        print("Tabela 'Produto' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_categoria():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categoria (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            );
        """)
        connection.commit()
        print("Tabela 'Categoria' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_marca():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS marca (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            );
        """)
        connection.commit()
        print("Tabela 'Marca' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_compra():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS compra (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fornecedor_id INT,
            cliente_id INT,
            valor_total DECIMAL(10,2),
            desconto DECIMAL(10,2),
            frete DECIMAL(10,2),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id),
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
            );
        """)
        connection.commit()
        print("Tabela 'Compra' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_produto_compra():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto_compra (
            id INT AUTO_INCREMENT PRIMARY KEY,
            compra_id INT,
            produto_id INT,
            quantidade INT,
            valor_unitario DECIMAL(10,2),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (compra_id) REFERENCES compra(id),
            FOREIGN KEY (produto_id) REFERENCES produto(id)
            );
        """)
        connection.commit()
        print("Tabela 'produto_compra' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_venda():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS venda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT,
            valor_total DECIMAL(10,2),
            desconto DECIMAL(10,2),
            frete DECIMAL(10,2),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
            );
        """)
        connection.commit()
        print("Tabela 'Venda' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_produto_venda():
    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto_venda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            venda_id INT,
            produto_id INT,
            quantidade INT,
            valor_unitario DECIMAL(10,2),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (venda_id) REFERENCES venda(id),
            FOREIGN KEY (produto_id) REFERENCES produto(id)
            );
        """)
        connection.commit()
        print("Tabela 'produto_venda' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_parcela():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS parcela (
            id INT AUTO_INCREMENT PRIMARY KEY,
            conta_id INT,
            tipo_conta ENUM('compra', 'venda') NOT NULL,
            forma_pagamento VARCHAR(255),
            parcela INT,
            vencimento DATE,
            valor DECIMAL(10,2),
            ja_pago BOOLEAN,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (conta_id) REFERENCES compra(id) ON DELETE CASCADE,
            FOREIGN KEY (conta_id) REFERENCES venda(id) ON DELETE CASCADE
            );
        """)
        connection.commit()
        print("Tabela 'Parcela' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_logs():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            acao VARCHAR(255),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user(id)
            );
        """)
        connection.commit()
        print("Tabela 'Logs' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()

def create_historico_estoque():

    # Conectar ao banco de dados
    connection = connect_to_database()
    if connection is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico_estoque (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produto_id INT,
            quantidade INT,
            tipo VARCHAR(255),
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES produto(id)
            );
        """)
        connection.commit()
        print("Tabela 'historico_estoque' criada com sucesso.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        # Fechar a conexão e o cursor
        cursor.close()
        connection.close()       