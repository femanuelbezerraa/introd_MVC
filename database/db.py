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
            # conecta ao BD
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port 
            )
            conn.autocommit = True
            cur = conn.cursor()
            # Verificar se o banco de dados existe
            cur.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s", (self.dbname,)
            )
            exists = cur.fetchone()
            if not exists:
                cur.execute(
                    (sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
                )
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao criar o banco de dados: {e}")
    
    def connect(self):
        self.criar_database_se_nao_existir()
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
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None