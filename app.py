from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Olá Mundo</h1>"

@app.route('/contato')
def contato():
    return render_template('contato.html', tel='(84) 988796655', email='alba.lopes@ifrn.edu.br')

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/perfil', defaults={'nome':'fulano'})

@app.route('/perfil/<nome>')
def usuario (nome):
    return render_template('perfil.html', nome = nome)

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x + 1
    return render_template('semestre.html', x = x, y = y)

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return str(n1+n2)

if __name__ == "__main__":
    app.run()  