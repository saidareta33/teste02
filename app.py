from flask import Flask, render_template, request, redirect
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

            # REDIRECIONA PARA O PAINEL
            return redirect('/painel')

        else:
            mensagem = 'E-mail ou senha incorretos.'

    return render_template(
        'paginalogin.html',
        mensagem=mensagem
    )


# NOVA ROTA
@app.route('/painel')
def painel():
    return '<h1>Bem-vindo ao painel!</h1>'


if __name__ == '__main__':
    app.run(debug=True)