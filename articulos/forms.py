from django.forms import ModelForm, Textarea, TextInput, URLInput
from . import models



class crea_articulo(ModelForm):
    class Meta:
        model = models.Articulos
        fields=['titulo','slug','cuerpo', 'thumb']