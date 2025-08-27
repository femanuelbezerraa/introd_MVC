'''class LivroView:
    def mostrar_livro(self, livro):
        print (livro)
        
        def mostrar_livros(self, livros):
            for livro in livros:
                self.mostrar_livro(livro)'''
                
import tkinter as tk
from tkinter import ttk, messagebox
from controller.livro_controller import LivroController

class LivroView:
    def __init__(self, controller):
        self.controller = controller
        self._show_livros_tela()
    
    @staticmethod   
    def iniciar_Login_banco():
        
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
<<<<<<< HEAD
                messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados:\n {e}")
        
        login_win = tk.Tk()
        login_win.title("Conectar ao Banco de Dados")
        login_win.geometry("300x250")
=======
                messagebox.showerror("Erro", f"Falha ao conectar ao banco de dados: {e}")
        login_win = tk.Tk()
        login_win.title("Login Banco de Dados")
        login_win.geometry("350x300")

        # Titulo " Banco de dados" no centro da tela
        tk.Label(login_win, text="Banco de Dados", font=("Arial", 16)).pack(pady=10)
        #o "login_win" é a janela principal
>>>>>>> bea0971b3dccec7864bdd88f472c5d3b38640a1b
        
        tk.Label(login_win, text="Dbname:").pack(pady=2)
        db_name_entry = tk.Entry(login_win)
        db_name_entry.pack()
        
        tk.Label(login_win, text="User:").pack(pady=2)
        db_user_entry = tk.Entry(login_win)
        db_user_entry.pack()
        
        tk.Label(login_win, text="Password:").pack(pady=2)
        db_password_entry = tk.Entry(login_win)
        db_password_entry.pack()
        
        tk.Label(login_win, text="Host:").pack(pady=2)
        db_host_entry = tk.Entry(login_win)
        db_host_entry.pack()

        tk.Label(login_win, text="Port:").pack(pady=2)
        db_port_entry = tk.Entry(login_win)
        db_port_entry.pack()
        
        tk.Button(login_win, text="Conectar", command=conectar).pack(pady=15)
        login_win.mainloop()
        
    def _show_livros_tela(self):
        livros = self.controller.listar_livros()
        win = tk.Tk()
        win.title("Livros cadastrados")
        win.geometry("700x400")
        
        columns = ("ID", "Título", "Autor", "Ano", "ISBN")
        tree = ttk.Treeview(win, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=120)
        for livro in livros:
            tree.insert("", tk.END, values=(livro.id, livro.titulo, livro.autor, livro.ano, livro.isbn))
        tree.pack(expand=True, fill="both")
        
        win.mainloop()
              
 