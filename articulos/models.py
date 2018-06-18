from django.db import models

# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=60)
    slug = models.SlugField()
    cuerpo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=60)
    thumb = models.ImageField(default='default.png', blank=True)


    def __str__(self):
        return self.titulo

    def creado_por(self):
        return self.autor

    def snippet(self):
        return self.cuerpo[:100] + '....'