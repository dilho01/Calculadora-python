from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    expressao = request.form['expressao']
    
    try:
        resultado = str(eval(expressao))
        return render_template('index.html', resultado=resultado)
    except:
        return render_template('index.html', resultado='Erro')

if __name__ == '__main__':
    app.run(debug=True)
