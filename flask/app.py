from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato', methods=['GET'])
def contato():
    return render_template('contato.html')

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('perfil.html', nome_usuario=nome, idade=25, cidade='São Paulo')