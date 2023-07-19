from flask import Flask, render_template, request, redirect, session, flash, url_for


class Usuario:
    def __init__(self, nome, nickName, senha):
        self.nome = nome
        self.nickName = nickName
        self.senha = senha

usuario = Usuario('Eduardo', 'Eduzao', 'senha')
usuario2 = Usuario('Camila', 'Camilinha', 'teste')
usuario3 = Usuario('Gustavo', 'Gugu', 'tester')

usuarios = {usuario.nickName : usuario,
            usuario2.nickName : usuario2,
            usuario3.nickName : usuario3
            }


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
    if 'usuarioLogado' not in session or 'usuarioLogado' == None:
        redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html',  titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',  proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuarioLogado'] = usuario.nickName
            flash(usuario.nickName + ', seja Bem vindo!')
            prxoima_pagina = request.form['proxima']
            return redirect(prxoima_pagina)
    else:
        flash('usuario não logado! por favor tente novamente')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuarioLogado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)