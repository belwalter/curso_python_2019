from flask import Flask
from flask import render_template, jsonify, request, redirect, url_for
from funciones_mongo import get_all, save_doc, update_doc, get_one, delete_doc
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Retorna la pagina index."""
    op_alta = False
    res_alta = True
    lista = get_all()
    lista.sort(key=orden)
    if(request.method == 'POST'):
        filtro = request.form['filtro']
        criterio = request.form['selection']
        laux = []
        for documento in lista:
            if(criterio == "Nombre" and documento['nombre'][0:len(filtro)].lower() == filtro.lower()):
                laux.append(documento)
            elif (criterio == "Personaje" and documento['personaje'][0:len(filtro)].lower() == filtro.lower()):
                laux.append(documento)
            elif (criterio == "Biografía" and documento['biografia'].find(filtro) > -1):
                laux.append(documento)
        lista = laux
    return render_template('/index.html', datos=lista, op_alta=op_alta, res_alta=res_alta)

@app.route('/cargar')
def cargar():
    dic = {'nombre': '', 'aparicion': '', 'biografia': '', 'personaje': ''}
    return render_template('/cargar.html', documento=dic)

@app.route('/guardar', methods=['POST'])
def guardar():
    dic = {}
    dic['nombre'] = request.form['valor1']
    dic['personaje'] = request.form['valor2']
    dic['biografia'] = request.form['valor3']
    if(len(request.form['valor4']) > 0):
        dic['aparicion'] = int(request.form['valor4'])
    resultado = save_doc(dic)
    lista = get_all()
    return redirect(url_for('index', ))

@app.route('/update', methods=['POST'])
def update():
    if(request.method == 'POST'):
        if(request.form['boton'] == 'update'):
            dic = {}
            dic['_id'] = request.form['valor0']
            dic['nombre'] = request.form['valor1']
            dic['personaje'] = request.form['valor2']
            if(len(request.form['valor4']) > 0):
                dic['aparicion'] = int(request.form['valor4'])
            dic['biografia'] = request.form['valor3']
            print(dic)
            update_doc(dic)
        if(request.form['boton'] == 'delete'):
            id = request.form['valor0']
            delete_doc(id)
    return redirect(url_for('index'))

@app.route('/detalle', methods=['GET'])
def detalle():
    id = request.args.get('id')
    documento = get_one(id)
    return render_template('/detalle.html', documento=documento)

@app.route('/about')
def about():
    """Retorna la pagina about."""
    return render_template('/about.html', valor_h1="About")


def orden(documento):
    return documento['nombre']


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
