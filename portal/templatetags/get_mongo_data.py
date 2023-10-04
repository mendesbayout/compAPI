# from django import template
# from django.template.loader import get_template
# import pymongo



# register = template.Library()


# @register.inclusion_tag("portal/show_data.html")
# def get_data():
#     client = pymongo.MongoClient("mongo", 27017)

#     db = client["mydb"]
#     despachos = db.despachos

#     return {'despachos': despachos.find({})}
