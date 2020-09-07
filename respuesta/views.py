from django.views.generic.edit import CreateView
from .models import Respuesta
from publicacion.models import Publicacion
from django.urls import reverse_lazy, reverse

class RespuestaCreate(CreateView):
    model = Respuesta
    fields = ['respuesta', 'publicacion']

    def get_success_url(self):
        return reverse('publicaciones-detail', kwargs={'pk':self.object.publicacion.id} )

    def get_context_data(self, **kwargs):
        context = super(RespuestaCreate, self).get_context_data(**kwargs)
        context['publicacion'] =Publicacion.objects.get(id=self.kwargs['publicacion'])
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


