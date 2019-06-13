
from pymongo import MongoClient

def conexion():
    cliente = MongoClient(host='localhost', port=27017)
    db = cliente.get_database('db_prueba')
    return db


def guardar(documento):
    db = conexion()
    db.get_collection('lenguajes').insert(documento)

def guardar_pintura(museo, pintura):
    db = conexion()
    """
    db.get_collection('museos').find({'nombre': museo.nombre})
    db.get_collection('museos').update({'nombre': museo.nombre}, {'$push':
                                       {'muestras': {'artista': pintura.artista, 'anio': pintura.anio, 'titulo': pintura.titulo,
        'descripcion': pintura.descripcion, 'tipo': pintura.tipo, 'material': pintura.material,
        'estilo': pintura.estilo, 'tipo_muestra': 'Pintura'}}})
    """

def listar():
    db = conexion()
    documento = db.get_collection('lenguajes').find({'version':'2.7.9'})
    for dato in documento:
        print(dato)
        print(dato['nombre'])
        print(dato['frameworks'][0])

def lista():
    db = conexion()
    """
    documentos = db.get_collection('museos').find({})
    lista_museos = []
    for elemento in documentos:
        m = museo.Museo(elemento['nombre'], elemento['direccion'],
                        elemento['tipo'])
        lista_muestras(m)
        lista_museos.append(m)
    return lista_museos
    """
