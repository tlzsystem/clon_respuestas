from django.urls import path
from . import views

urlpatterns = [
    path('respuesta/add/<int:publicacion>', views.RespuestaCreate.as_view(), name= 'respuesta-create'),
]


