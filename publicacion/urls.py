from django.urls import path
from . import views

urlpatterns = [
    path('publicaciones/categoria/<int:categoria>', views.PublicacionListByCategoria.as_view(),
         name='publicaciones-by-categoria'),
    path('publicaciones/<int:pk>', views.PublicacionDetail.as_view(), name= 'publicaciones-detail'),
]