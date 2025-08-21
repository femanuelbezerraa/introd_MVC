import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def criar_database_se_nao_existir(self):
        try:
            # conecta ao banco 'postgres' para criar/verificar outros bancos
            conn = psycopg2.connect(
                dbname='postgres',
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            conn.autocommit = True  # Necessário para criar banco de dados
            cursor = conn.cursor()
            # verifica se o banco de dados já existe
            cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [self.dbname])
            exists = cursor.fetchone()
            if not exists:
                # cria o banco de dados se não existir
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao criar ao banco de dados: {e}")
    
    def conectar(self):
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except Exception as e:
            print("Erro ao conectar ao banco de dados:", e)
            return None
        