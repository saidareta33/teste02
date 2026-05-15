from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# ===== PÁGINA DE LOGIN =====
@app.route("/")
def home():
    return render_template("paginalogin.html")


# ===== LOGIN =====
@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("gmail")
    senha = request.form.get("senha")

    # CONECTA NO BANCO
    conn = sqlite3.connect("primeiro_banco.db")

    cursor = conn.cursor()

    # CRIA A TABELA
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL

    )
    """)

    # SALVA O LOGIN
    cursor.execute(
        """
        INSERT INTO usuarios (email, senha)
        VALUES (?, ?)
        """,
        (email, senha)
    )

    conn.commit()
    conn.close()

    # REDIRECIONA PARA O INDEX.HTML
    return redirect("/index")


# ===== INDEX.HTML =====
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)