from django.urls import path, re_path
from . import views

app_name = 'articulos'

urlpatterns = [

    re_path(r'^$',views.lista_art, name='lista'),
    re_path(r'^crear/$', views.crear_art, name='crear'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detalles_art,name ='detalle'),

]
