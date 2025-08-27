class Livro :
    def __init__(self, id, titulo, autor, ano, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

    def __repr__(self):
        return f"Livro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', ano={self.ano}, isbn='{self.isbn}')"