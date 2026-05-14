import sqlite3
from datetime import datetime
import os

# =========================
# CONECTANDO AO BANCO
# =========================

# pega a pasta do projeto automaticamente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# cria o caminho do banco
db_path = os.path.join(BASE_DIR, 'primeiro_banco.db')

# conecta ao banco
banco = sqlite3.connect(db_path)

# cria o cursor
cursor = banco.cursor()

print('Banco conectado com sucesso.')

# =========================
# CRIANDO A TABELA
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT NOT NULL,

    idade INTEGER NOT NULL,

    email TEXT NOT NULL UNIQUE,

    senha TEXT NOT NULL,

    data_criacao TEXT, 

    codigo_cripto TEXT,

)
""")

print('Tabela verificada/criada.')

# =========================
# LISTA DE USUÁRIOS
# =========================

usuarios = [

    ('Arthur', 20, 'arthur@gmail.com', '2905', '2905'),

    ('Yasmin', 19, 'yasmin@gmail.com', '2905', '1605'),

    ('Antonia', 25, 'antonia@gmail.com', '2905', '0510'),

    ('Douglas', 30, 'douglas@gmail.com', '2905', '2511'),

]

# =========================
# ADICIONANDO USUÁRIOS
# =========================

for usuario in usuarios:

    try:

        cursor.execute("""

        INSERT INTO pessoas
        (nome, idade, email, senha, codigo_cripto, data_criacao)

        VALUES (?, ?, ?, ?, ?, ?)

        """, (

            usuario[0],
            usuario[1],
            usuario[2],
            usuario[3],

            datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        ))

        print(f'Usuário {usuario[0]} cadastrado com sucesso.')

    except sqlite3.IntegrityError:

        print(f'O email {usuario[2]} já existe no banco.')

# =========================
# SALVANDO ALTERAÇÕES
# =========================

banco.commit()

print('Dados salvos.')

# =========================
# MOSTRANDO USUÁRIOS
# =========================

cursor.execute("SELECT * FROM pessoas")

usuarios_salvos = cursor.fetchall()

print('\nUSUÁRIOS CADASTRADOS:\n')

for usuario in usuarios_salvos:

    print(usuario)

# =========================
# FECHANDO O BANCO
# =========================

banco.close()

print('\nBanco encerrado.')