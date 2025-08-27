import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mvc_3a",
        user="postgres",
        password="wcc@2023",
        host="127.0.0.1",
        port="5433"
    )
    print("Conexão bem-sucedida!")
except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados:\n")
    print(e)
        
            