from django.views.generic.base import TemplateView
import pymongo

from portal.models import Despacho
# Create your views here.



def get_normas():
    MONGODB_URI = "mongodb+srv://lucas:bayout@cluster0.uqxmkzv.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(MONGODB_URI)
    db = client["complianceRAW"]
    collection_names = db.list_collection_names()
    normas = []
    for collection_name in collection_names:
        for norma in db[collection_name].find({}).limit(3):
            normas.append(norma)
    return normas


class IndexView(TemplateView):
    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['normas'] = get_normas()
        return context
