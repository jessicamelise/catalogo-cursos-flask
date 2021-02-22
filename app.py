from flask import Flask, render_template

app = Flask('teste')

lista = [
    'item1',
    'item2',
    'item3'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ola')
def ola():
    resposta = '<h1>Olá mundo no Flask!</h1>'
    resposta += '<ul>'
    for item in lista:
        resposta += '<li>' + item + '</li>'
    resposta += '</ul>'

    return resposta


app.run(debug=True)