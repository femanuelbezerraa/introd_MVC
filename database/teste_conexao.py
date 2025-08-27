import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mvc_3a",
<<<<<<< HEAD
        user="postgres",
        password="wcc@2023",
        host="127.0.0.1",
        port="5433"
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:\n")
    print(e)
        
            
=======
        user="postgres",    
        password="wcc@2023",
        host="127.0.0.1",
        port="5433",
        )
    print("Conexão bem sucedida")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
    print(e)
        
>>>>>>> bea0971b3dccec7864bdd88f472c5d3b38640a1b
