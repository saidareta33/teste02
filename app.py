from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():

    mensagem = ''

    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        conn = sqlite3.connect('primeiro_banco.db')
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM usuarios WHERE email=? AND senha=?',
            (email, senha)
        )

        usuario = cursor.fetchone()

        conn.close()

        if usuario:
            mensagem = 'Login realizado com sucesso!'
        else:
            mensagem = 'E-mail ou senha incorretos.'

    return render_template(
        'paginalogin.html',
        mensagem=mensagem
    )


if __name__ == '__main__':
    app.run(debug=True)