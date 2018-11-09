from django.shortcuts import render
from django.utils import timezone
from .models import Publicar
from django.shortcuts import render, get_object_or_404


def listar(request):
    articulos = Publicar.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'articulos':articulos})

def post_detail(request, pk):
    post = get_object_or_404(Publicar, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})