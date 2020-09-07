from categoria.models import Categoria

def obtener_categorias(request):
    return {'categorias': Categoria.objects.all()}