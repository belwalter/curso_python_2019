from pymongo import MongoClient

def conexion():
    cliente = MongoClient(host='localhost', port=27017)
    db = cliente.get_database('curso_python')
    return db


def guardar(documento):
    db = conexion()
    db.superheroes.insert(documento)


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
    documento = db.get_collection('superheroes').find({})
    lista = []
    for dato in documento:
        lista.append({'nombre': dato['nombre'], 'personaje': dato['personaje']})
    return lista
