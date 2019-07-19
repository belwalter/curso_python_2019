
from pymongo import MongoClient
from bson.objectid import ObjectId

def connection():
    cliente = MongoClient(host='localhost', port=27017)
    db = cliente.get_database('curso_python')
    return db


def save_doc(documento):
    control = False
    try:
        db = connection()
        db.superheroes.insert(documento)
        control = True
    except:
        pass
    return control


def update_doc(documento):
    db = connection()
    id = ObjectId(documento['_id'])
    documento.pop('_id', None)
    db.superheroes.update_one({'_id': id}, {'$set': documento}, upsert=False)


def delete_doc(id):
    db = connection()
    id = ObjectId(id)
    db.superheroes.remove({'_id': ObjectId(id)})


def get_all():
    db = connection()
    documento = db.get_collection('superheroes').find({})
    lista = []
    for dato in documento:
        datos = dato
        datos['_id'] = str(datos['_id'])
        lista.append(datos)
    return lista


def get_one(id):
    db = connection()
    documento = db.get_collection('superheroes').find_one({'_id': ObjectId(id)})
    documento['_id'] = str(documento['_id'])
    return documento
