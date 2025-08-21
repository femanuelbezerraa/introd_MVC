class Livro:
    def __init__(self, id_livro, titulo, autor, ano_publicacao, isbn):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao}) - ISBN: {self.isbn}"