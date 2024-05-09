from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado= '')
@app.route('/verificar')
def verificar():
    x = 1
    resultado = ''
    while x <= 100:
        if ((x % 7 == 0) and (x % 5 != 0)):
            resultado += str(x) + ", "
        x = x + 1

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)