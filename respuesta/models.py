from django.db import models
from django.contrib.auth.models import User
from publicacion.models import Publicacion


class Respuesta(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_respuesta=models.DateField(auto_now_add=True)
    respuesta=models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural="Respuestas"
