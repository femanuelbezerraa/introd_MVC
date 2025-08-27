import tkinter as tk
from tkinter import ttk, messagebox
from controller.livro_controller import LivroController

class LivroView:
    def __init__(self, controller):
        self.controller = controller
        self._show_livros_tela()

    @staticmethod
    def iniciar_login_banco():
        def conectar():
            db_config = {
                "dbname": db_name_entry.get(),
                "user": db_user_entry.get(),
                "password": db_password_entry.get(),
                "host": db_host_entry.get(),
                "port": db_port_entry.get()
            }
            try:
                controller = LivroController(db_config)
                login_win.destroy()
                LivroView(controller)
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao conectar ao banco de dados: {e}")
        login_win = tk.Tk()
        login_win.title("Login Banco de Dados")
        login_win.geometry("350x300")

        # Titulo " Banco de dados" no centro da tela
        tk.Label(login_win, text="Banco de Dados", font=("Arial", 16)).pack(pady=10)
        #o "login_win" é a janela principal
        
        tk.Label(login_win, text="Nome:").pack(pady=5) # o "text" é o texto que aparece na tela, o "pack" é o método que organiza os elementos na tela
        db_name_entry = tk.Entry(login_win) # o "Entry" é o campo de texto
        db_name_entry.pack(pady=5)  
        # o "pady" é o espaçamento vertical

        tk.Label(login_win, text="Usuário:").pack(pady=5)
        db_user_entry = tk.Entry(login_win)
        db_user_entry.pack(pady=5)

        tk.Label(login_win, text="Senha:").pack(pady=5)
        db_password_entry = tk.Entry(login_win, show="*") #o "show" é o caractere que aparece no lugar da senha
        db_password_entry.pack(pady=5)

        tk.Label(login_win, text="Host:").pack(pady=5)
        db_host_entry = tk.Entry(login_win)
        db_host_entry.pack(pady=5)

        tk.Label(login_win, text="Porta:").pack(pady=5)
        db_port_entry = tk.Entry(login_win)
        db_port_entry.pack(pady=5)

        #botão conectar areedondado no canto inferior direito da tela abaixo dos campos de texto
        conectar_button = tk.Button(login_win, text="Conectar", command=conectar) # o "command" é o método que é chamado quando o botão é clicado
        conectar_button.pack(pady=10, side=tk.BOTTOM, anchor=tk.E) # o "side" é o lado onde o botão fica, o "anchor" é a âncora do botão
        # "ancora" é a posição do botão em relação ao lado

    def _show_livros_tela(self):
        livros = self.controller.listar_livros()
        win = tk.Tk()
        win.title("Livros Cadastrados")
        win.geometry("700x400")

        columns = ("id", "título", "autor", "ano de publicação", "isbn")
        tabela = ttk.Treeview(win, columns=columns, show="headings")
        for col in columns:
            tabela.heading(col, text=col.capitalize())
            tabela.column(col, width=150)
        for livro in livros:
            tabela.insert("", "end", values=(livro.id_livro, livro.titulo, livro.autor, livro.ano_publicacao, livro.isbn))

        tabela.pack(expand=True, fill="both")

        win.mainloop()

