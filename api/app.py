from flask import Flask
from flask import render_template, jsonify
from funciones_mongo import listar, guardar

app = Flask(__name__)



"""
titulo = "mi app"
lista = [['walter', 'bel'], ['Juan', 'redis'], ['python', 'guido']]
return render_template('/index.html', t=titulo, datos=lista)

"""
@app.route('/')
def index():
    """Retorna la pagina index."""
    lista = listar()
    # print(lista)
    #return jsonify(lista)
    return render_template('/index.html', valor_h1="App de Superheroes",
                           datos=lista)

@app.route('/cargar')
def cargar():
    dic = {'nombre': 'ant-man', 'personaje': 'Bruce Scott Lang'}
    guardar(dic)
    return "ok"

@app.route('/about')
def about():
    """Retorna la pagina about."""
    return render_template('/about.html', valor_h1="About")


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=False)
