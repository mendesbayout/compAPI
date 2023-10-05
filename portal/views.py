from django.views.generic.base import TemplateView
import pymongo

from portal.models import Despacho
# Create your views here.


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
    d = despachos.find_one()
    return d

class IndexView(TemplateView):
    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = pymongo.MongoClient("mongo", 27017)
        db = client["mydb"]
        despachos = db.despachos
        context['despachos'] = despachos.find({})
        return context
