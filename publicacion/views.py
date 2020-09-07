from django.views.generic import ListView, DetailView
from .models import Publicacion
from categoria.models import Categoria
from respuesta.models import Respuesta
from django.http import Http404


class PublicacionListByCategoria(ListView):
    def get_queryset(self):

        try:
            self.categoria = Categoria.objects.get(id=self.kwargs['categoria'])
            return Publicacion.objects.filter(categoria=self.categoria).order_by('-fecha_publicacion')
        except:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(PublicacionListByCategoria, self).get_context_data(**kwargs)
        context['categoria'] = self.categoria
        return context

class PublicacionDetail(DetailView):
    model = Publicacion

    def get_context_data(self, **kwargs):
        context = super(PublicacionDetail, self).get_context_data(**kwargs)
        respuestas = Respuesta.objects.filter(publicacion= self.object.id).order_by('-created')
        context['respuestas'] = respuestas
        return context

