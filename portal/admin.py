from django import forms
from django.contrib import admin
from django.forms import Textarea
from .models import Despacho


class DespachoAdminForm(forms.ModelForm):
  class Meta:
    model = Despacho
    widgets = {
      'text': Textarea(),
    }
    fields = '__all__'



class DespachoAdmin(admin.ModelAdmin):
    form = DespachoAdminForm
    list_display = ('_id', 'url', 'title', 'text', 'date', 'tipo')


admin.site.register(Despacho, DespachoAdmin)