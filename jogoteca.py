from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Aventura', 'PS5')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS5')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = "EduardoSocratesAlura"

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html',  titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html',  titulo = 'Login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'senha123' == request.form['senha']:
        session['usuarioLogado'] = request.form['usuario']
        flash(session['usuarioLogado']+ ', seja Bem vindo!')
        return redirect('/')
    else:
        flash('usuario não logado! por favor tente novamente')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuarioLogado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(debug=True)