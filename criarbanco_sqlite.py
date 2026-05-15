import sqlite3

# CONECTA NO BANCO
conn = sqlite3.connect('primeiro_banco.db')

# CRIA O CURSOR
cursor = conn.cursor()

# CRIA A TABELA
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    senha TEXT NOT NULL

)
''')

print("Tabela criada com sucesso!")

conn.commit()
conn.close()