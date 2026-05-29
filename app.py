from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# ===== LOGIN =====

@app.route("/")
def home():
    return render_template("paginalogin.html")


# ===== RECEBE LOGIN =====

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("gmail")
    senha = request.form.get("senha")

    if len(senha) < 4:

        return render_template(
            "paginalogin.html",
            mensagem="A senha precisa ter pelo menos 4 caracteres."
        )

    conn = sqlite3.connect("primeiro_banco.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL

    )
    """)

    cursor.execute(
        """
        INSERT INTO usuarios (email, senha)
        VALUES (?, ?)
        """,
        (email, senha)
    )

    conn.commit()
    conn.close()

    return redirect("/index")


# ===== PÁGINAS =====

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/pagina.html")
def dashboard():
    return render_template("pagina.html")


@app.route("/matriculas.html")
def contato():
    return render_template("matriculas.html")


@app.route("/embreve.html")
def sobre():
    return render_template("embreve.html")

@app.route("/pagina.html")
def sobre():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)