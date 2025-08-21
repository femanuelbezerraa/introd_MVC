from database.db import Database
from models.livro import Livro

class LivroController: 
    def __init__(self, db_config):
        self.db = Database(
            db_config["dbname"],
            db_config["user"],
            db_config["password"],
            db_config["host"],
            db_config["port"]
        )
        self.criar_tabela_se_nao_existir()
        #self.view = LivroView()
        
    def criar_tabela_se_nao_existir(self):
        conn = self.db.connect()

        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS livros(
                    id_livro SERIAL PRIMARY KEY,
                    titulo VARCHAR(225) NOT NULL,
                    autor VARCHAR(225) NOT NULL,
                    ano_publicacao INT NOT NULL,
                    isbn VARCHAR(20) NOT NULL UNIQUE
                );
            """)

            conn.commit()
            cursor.close()
            conn.close()

    def adicionar_livro(self, titulo, autor, ano_publicacao, isbn):
        conn = self.db.connect()

        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO livros (titulo, autor, ano_publicacao, isbn) VALUES (%s, %s, %s, %s) ON CONFLICT (isbn) DO NOTHING;""",
                (titulo, autor, ano_publicacao, isbn))
            
            conn.commit()
            cursor.close()
            conn.close()

            print("Livro adicionado com sucesso!")
        else:
            print("Falha ao conectar ao banco de dados. Livro não adicionado.")

    def listar_livros(self):
        #self.view.mostrar_livros(livros)
        conn = self.db.connect()
        livros = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_livro, titulo, autor, ano_publicacao, isbn FROM livros ORDER BY id_livro;")
            for linha in cursor.fetchall():
                livros.append(Livro(*linha))
            cursor.close()
            conn.close()
        return livros
    
