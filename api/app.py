from flask import Flask
from flask import render_template, jsonify, request, redirect, url_for
from funciones_mongo import get_all, guardar_doc, actualizar_doc, get_one
import json

app = Flask(__name__)



"""
titulo = "mi app"
lista = [['walter', 'bel'], ['Juan', 'redis'], ['python', 'guido']]
return render_template('/index.html', t=titulo, datos=lista)

"""
@app.route('/')
def index():
    """Retorna la pagina index."""
    lista = get_all()
    #return jsonify(lista)
    return render_template('/index.html', valor_h1="App de Superheroes",
                           datos=lista)

@app.route('/cargar')
def cargar():
    return render_template('/cargar.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    dic = {}
    dic['nombre'] = request.form['valor1']
    dic['personaje'] = request.form['valor2']
    dic['biografia'] = request.form['valor3']
    guardar_doc(dic)
    return render_template('/index.html')

@app.route('/update', methods=['POST'])
def update():
    if(request.method == 'POST'):
        if(request.form['action'] == 'update'):
            print("actualizar")
            dic = {}
            dic['_id'] = request.form['valor0']
            dic['nombre'] = request.form['valor1']
            dic['personaje'] = request.form['valor2']
            dic['biografia'] = request.form['valor3']
            actualizar_doc(dic)
    return redirect(url_for('index'))

@app.route('/detalle', methods=['GET'])
def detalle():
    id = request.args.get('id')
    nombre = request.args.get('nombre')
    print(nombre)
    documento = get_one(id)
    #documento['biografia'] = "el increible hombre verde...."
    #actualizar(documento)
    return render_template('/detalle.html', documento=documento)

@app.route('/about')
def about():
    """Retorna la pagina about."""
    return render_template('/about.html', valor_h1="About")


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
