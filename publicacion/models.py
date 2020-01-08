from django.db import models
from categoria.models import Categoria
from django.contrib.auth.models import User

class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural="Publicaciones"
