from django.db import models
import pymongo

class Despacho(models.Model):
    _id = models.CharField(max_length=24, unique=True)
    url = models.URLField()
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    date = models.CharField(max_length=64)
    tipo = models.CharField(max_length=64)



def add_despacho(d):
    despacho = Despacho(
        _id = str(d['_id']),
        url = d['url'],
        title = d['title'],
        text = d['text'],
        date = d['date'],
        tipo = d['tipo']
    )
    despacho.save()
    return despacho


def get_despachos():
    client = pymongo.MongoClient("mongo", 27017)
    db = client["mydb"]
    despachos = db.despachos
    d = despachos.find({})
    return d


def update_all():
    added = 0
    error = 0
    for despacho in get_despachos():
        try:
            add_despacho(despacho)
            # print('Despacho added! ')
        except:
            error += 1
            # print('########## ERRO #########')
        else:
            added += 1

    return {
        'added': added,
        'error': error
    }