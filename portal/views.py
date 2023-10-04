from django.views.generic.base import TemplateView
import pymongo

# Create your views here.


class IndexView(TemplateView):
    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = pymongo.MongoClient("mongo", 27017)
        db = client["mydb"]
        despachos = db.despachos
        context['despachos'] = despachos.find({})
        return context
