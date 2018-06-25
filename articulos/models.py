from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=60)
    slug = models.SlugField()
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    thumb = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.titulo

    def snippet(self):
        return self.cuerpo[:100] + '....'