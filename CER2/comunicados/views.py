from django.shortcuts import render, get_object_or_404
from .models import Comunicado

def lista_comunicados(request):
    comunicados = Comunicado.objects.all().order_by('-fecha_envio')
    return render(request, 'comunicados/lista_comunicados.html', {'comunicados': comunicados})

def detalle_comunicado(request, pk):
    comunicado = get_object_or_404(Comunicado, pk=pk)
    return render(request, 'comunicados/detalle_comunicado.html', {'comunicado': comunicado})
