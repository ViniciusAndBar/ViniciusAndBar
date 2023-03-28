from flask import app, Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sobre_mim.html', tittle='sobre mim')

@app.route('/Interesses')
def interesses():
    return render_template('interesses.html', tittle='interesses')

@app.route('/Trabalhos')
def trabalhos():
    return render_template('trabalhos_desenvolvidos.html', tittle='trabalhos desenvolvidos')

if __name__ == '__main__':
    app.run()