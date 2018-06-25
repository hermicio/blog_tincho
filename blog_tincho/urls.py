from django.contrib import admin
from django.urls import path, include, re_path
#from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articulos import views as art_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^about/', views.about),
    re_path(r'^$',art_views.lista_art, name="home"),
    re_path(r'^articulos/',include('articulos.urls')),
    re_path(r'^cuentas/',include('cuentas.urls'))
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
