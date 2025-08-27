from database.db import Database
from models.livro import Livro
class LivroController:
    def __init__(self, db_config):
        self.db = Database(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        self.criar_tabela_se_nao_existir()
    
    def criar_tabela_se_nao_existir(self):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS livros (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    ano INTEGER,
                    isbn VARCHAR(20)    
                ) 
            """)
            conn.commit()
            cur.close()
            conn.close()
    
    def adicionar_livro(self, id, titulo, autor, ano, isbn):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO livros (id, titulo, autor, ano, isbn) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;",
                (id, titulo, autor, ano, isbn)
            )
            conn.commit()
            cur.close()
            conn.close()
            print("Livro adicionado com sucesso!")
        else:
            print("Erro ao conectar ao banco de dados.")
            
    def listar_livros(self):
        conn = self.db.connect()
        livros = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT id, titulo, autor, ano, isbn FROM livros ORDER BY id;")
            for linha in cur.fetchall():
                livros.append(Livro(*linha))
                cur.close()
                conn.close()
        return livros