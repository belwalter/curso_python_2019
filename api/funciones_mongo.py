
from pymongo import MongoClient
from bson.objectid import ObjectId

def conexion():
    cliente = MongoClient(host='localhost', port=27017)
    db = cliente.get_database('curso_python')
    return db


def guardar_doc(documento):
    db = conexion()
    db.superheroes.insert(documento)


def actualizar_doc(documento):
    db = conexion()
    id = ObjectId(documento['_id'])
    documento.pop('_id', None)
    db.superheroes.update_one({'_id': id}, {'$set': documento}, upsert=False)


def get_all():
    db = conexion()
    documento = db.get_collection('superheroes').find({})
    lista = []
    for dato in documento:
        datos = dato
        datos['_id'] = str(datos['_id'])
        lista.append(datos)
    return lista


def get_one(id):
    db = conexion()
    documento = db.get_collection('superheroes').find_one({'_id': ObjectId(id)})
    documento['_id'] = str(documento['_id'])
    return documento
