from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Olá Mundo</h1>"

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

if __name__ == "__main__":
    app.run()  